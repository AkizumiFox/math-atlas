"""math-atlas: check, measure and draw the chapter-level dependency graph.

  python3 tools/atlas.py check    # hard errors -> exit 1
  python3 tools/atlas.py stats    # generated/report.md
  python3 tools/atlas.py render   # generated/*.mmd, generated/README.md, generated/atlas.html
  python3 tools/atlas.py diff     # plan vs computed vs statement-level edges
  python3 tools/atlas.py all      # check, stats, render, diff
"""
import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
import graph as G  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
REG = ROOT / "registry"
OUT = ROOT / "generated"

HARD = ("s", "b")
SOFT = ("see", "revisits")
STRENGTH = {"s": 3, "b": 2, "revisits": 1, "see": 0}
INDEGREE_WARN = 6
FIELD_STATUS = {"core": "已涵蓋", "partial": "部分", "branch": "支線候選", "out": "範圍外"}
BRANCH_COLOUR = {"found": "#e8e2f4", "analysis": "#dcebf7", "linalg": "#dff2e1",
                 "algebra": "#fbe6d4", "side": "#eeeeee"}
BRANCH_NAME = {"found": "基礎", "analysis": "分析", "linalg": "線代", "algebra": "代數", "side": "支線"}


# ───────────────────────── loading ─────────────────────────

class Atlas:
    def __init__(self, reg=REG):
        self.volumes = yaml.safe_load((reg / "volumes.yaml").read_text())
        self.vol = {v["id"]: v for v in self.volumes}
        raw = yaml.safe_load((reg / "chapters.yaml").read_text())
        self.errors, self.warnings, self.notes = [], [], []
        self.chapters, self.order = {}, []
        for vid, chs in raw.items():
            if vid not in self.vol:
                self.errors.append(f"chapters.yaml: volume {vid} is not in volumes.yaml")
            for i, ch in enumerate(chs):
                ch = dict(ch, vol=vid, idx=i, opt=bool(ch.get("opt")))
                src = ch.get("src")
                ch["src"] = src if isinstance(src, list) else [src]
                if ch["id"] in self.chapters:
                    self.errors.append(f"chapters.yaml: duplicate id {ch['id']}")
                if not ch["id"].startswith(vid + "."):
                    self.errors.append(f"chapters.yaml: {ch['id']} is listed under {vid}")
                self.chapters[ch["id"]] = ch
                self.order.append(ch["id"])
        for v in self.volumes:
            if v["id"] not in raw:
                self.errors.append(f"volumes.yaml: {v['id']} has no chapters")

        self.plan = self._load_plan(reg / "plan-edges.yaml")
        self.computed, self.witnesses = self._load_computed(reg / "computed")
        self.edges = self._merge()
        self.statements = self._load_statements(reg / "statements.yaml")
        self.targets = yaml.safe_load((reg / "exam-targets.yaml").read_text())
        moves = reg / "moves.yaml"
        self.moves = (yaml.safe_load(moves.read_text()) or []) if moves.exists() else []
        for m in self.moves:
            for c in [m["from"], m["to"], *m.get("borrowed_by", []), *m.get("scope", [])]:
                self._known(c, f"moves.yaml[{m['label']}]")
            for user in m.get("borrowed_by", []):
                self.scope[(user, m["to"])] = m.get("scope", [])
        fields = reg / "fields.yaml"
        self.fields = yaml.safe_load(fields.read_text()) if fields.exists() else {}
        self.subject = {f["id"]: f for fs in self.fields.values() for f in fs if "id" in f}
        ext = reg / "external" / "subject-dag.yaml"
        self.external = yaml.safe_load(ext.read_text()) if ext.exists() else None
        terms = reg / "terms.yaml"
        self.terms = (yaml.safe_load(terms.read_text()) or []) if terms.exists() else []
        triage = reg / "label-triage.yaml"
        rows = (yaml.safe_load(triage.read_text()) or []) if triage.exists() else []
        self.label_triage = {lbl: row for row in rows for lbl in row["labels"]}
        cons = reg / "chapter-constraints.yaml"
        self.constraints = (yaml.safe_load(cons.read_text()) or []) if cons.exists() else []
        dev = reg / "field-deviations.yaml"
        self.deviations = (yaml.safe_load(dev.read_text()) or []) if dev.exists() else []

    def _known(self, cid, where):
        if cid not in self.chapters:
            self.errors.append(f"{where}: unknown chapter {cid}")
            return False
        return True

    def _load_plan(self, path):
        data = yaml.safe_load(path.read_text()) or {}
        out = {}
        self.scope = {}  # (to, from) -> chapters whose vocabulary the borrowed statement needs
        for to, spec in data.items():
            if not self._known(to, "plan-edges.yaml"):
                continue
            why = spec.get("why") or {}
            for typ in ("s", "b", "see", "revisits"):
                for frm in spec.get(typ) or ():
                    if not self._known(frm, f"plan-edges.yaml[{to}]"):
                        continue
                    if frm == to:
                        self.errors.append(f"plan-edges.yaml: {to} depends on itself")
                    if typ == "b" and frm not in why:
                        self.errors.append(f"plan-edges.yaml: b edge {to} <- {frm} has no `why`")
                    prev = out.get((to, frm))
                    if prev:
                        self.errors.append(f"plan-edges.yaml: {to} <- {frm} listed as both {prev[0]} and {typ}")
                    out[(to, frm)] = (typ, why.get(frm))
            for frm in why:
                if (to, frm) not in out:
                    self.warnings.append(f"plan-edges.yaml: {to} has a `why` for {frm} but no edge")
            for frm, chs in (spec.get("scope") or {}).items():
                if out.get((to, frm), (None,))[0] != "b":
                    self.errors.append(f"plan-edges.yaml: {to} has a `scope` for {frm}, which is not a b edge")
                self.scope[(to, frm)] = [c for c in chs if self._known(c, f"plan-edges.yaml[{to}].scope")]
        return out

    def _load_computed(self, folder):
        out, wit = {}, {}
        self.overrides = []
        self.vocab_terms = {}  # (to, from) -> term ids behind a term edge, most used first
        self.vocab = {"all": {}, "stmt": {}, "term": {}}  # statement reader: definitions needed (import_la.vocabulary, term_edges)
        labels = folder / "labels.yaml"
        self.labels = (yaml.safe_load(labels.read_text()) or {}) if labels.exists() else {}
        for path in sorted(folder.glob("*-edges.yaml")):
            data = yaml.safe_load(path.read_text())
            for to, frm, typ, hard, soft in data["edges"]:
                if self._known(to, path.name) and self._known(frm, path.name):
                    out[(to, frm)] = (typ, hard, soft, path.name)
            wit.update(data.get("witnesses") or {})
            self.overrides += [tuple(o) for o in data.get("overrides") or ()]
            for to, frm, kind, _n, *which in data.get("vocab") or ():
                if self._known(to, path.name) and self._known(frm, path.name):
                    self.vocab[kind].setdefault(to, set()).add(frm)
                    if which:
                        self.vocab_terms[(to, frm)] = which[0]
        return out, wit

    def _merge(self):
        """Effective edge type per (to, from).

        Where both chapters have a manuscript with computed edges, the computed type replaces the plan: a planned
        hard edge the proofs never use is dropped (diff lists it), and a planned soft edge survives only when the
        proofs have no edge at all. Elsewhere the plan fills in what is not written yet, and the stronger type wins.
        """
        eff = {}
        for key, (typ, _) in self.plan.items():
            if self.written(*key) and typ in HARD:
                continue
            eff[key] = typ
        for key, (typ, *_rest) in self.computed.items():
            if self.written(*key) or key not in eff or STRENGTH[typ] > STRENGTH[eff[key]]:
                eff[key] = typ
        return eff

    def written(self, to, frm):
        """Both chapters come from a manuscript whose citation graph is imported (today: the linear-algebra book)."""
        return all(all(str(s).startswith("la:") for s in self.chapters[c]["src"]) for c in (to, frm))

    def _load_statements(self, path):
        if not path.exists():
            return {"nodes": [], "edges": []}
        data = yaml.safe_load(path.read_text())
        ids = set()
        for n in data["nodes"]:
            ids.add(n[0])
            self._known(n[1], f"statements.yaml[{n[0]}]")
        for frm_to in data["edges"]:
            for x in frm_to[:2]:
                if x not in ids:
                    self.errors.append(f"statements.yaml: edge mentions unknown statement {x}")
        return data

    # graphs: node -> set(preds)
    def preds(self, types):
        out = {c: set() for c in self.chapters}
        for (to, frm), typ in self.edges.items():
            if typ in types:
                out[to].add(frm)
        return out

    def label(self, cid):
        return f"{cid} {self.chapters[cid]['title']}"


# ───────────────────────── check ─────────────────────────

def check(at):
    sb = at.preds(HARD)
    cyc = G.find_cycle(sb)
    if cyc:
        at.errors.append("s ∪ b has a cycle: " + " -> ".join(reversed(cyc)))
    for (to, frm), typ in sorted(at.edges.items()):
        a, b = at.chapters[to], at.chapters[frm]
        if typ in HARD and a["vol"] == b["vol"] and b["idx"] >= a["idx"]:
            at.errors.append(f"{a['vol']}: chapter order puts {frm} after {to}, but {to} <-{typ}- {frm}")
        if typ == "s" and b["opt"] and not a["opt"]:
            at.errors.append(f"optional {frm} is an s-prerequisite of non-optional {to}")
    # A/R: on a uses edge, what the user needs must not exceed what the used statement teaches
    teach = {n[0]: (n[4], n[5]) for n in at.statements["nodes"]}
    for user, used, typ, *rest in at.statements["edges"]:
        if not rest:
            continue
        need = parse_ar(rest[0], f"statements.yaml edge {user} -> {used}", at)
        if len(rest) > 1 and rest[1] not in ("yes", "no", True, False):  # YAML reads bare yes/no as booleans
            at.errors.append(f"statements.yaml edge {user} -> {used}: assessed must be yes or no")
        if need and typ == "borrows" and need[1] > 1:
            at.errors.append(f"A/R lint: {user} borrows {used} but needs {rest[0]}; a borrow needs at most R1, "
                             "otherwise it is a uses edge")
        if need and typ == "uses":
            have = parse_ar(f"{teach[used][0]}/{teach[used][1]}", f"statements.yaml node {used}", at)
            if have and (need[0] > have[0] or need[1] > have[1]):
                at.errors.append(f"A/R lint: {user} needs {rest[0]} of {used}, which only teaches "
                                 f"{teach[used][0]}/{teach[used][1]}")
    sonly = at.preds(("s",))
    # a generalization must be linked to its special case at chapter level, so neither is written in isolation
    stmt_ch = {n[0]: n[1] for n in at.statements["nodes"]}
    for user, used, typ, *_ in at.statements["edges"]:
        a, b = stmt_ch[user], stmt_ch[used]
        if typ == "generalizes" and a != b and not ((a, b) in at.edges or (b, a) in at.edges
                                                     or b in G.ancestors(sonly, [a])):
            at.errors.append(f"{user} ({a}) generalizes {used} ({b}), but the chapters are not linked; "
                             f"add a revisits or see edge {a} <- {b}")
    local = check_terms(at)
    # notation scope (chapter-level proxy): what a borrowed statement is written in must already be in scope
    for (to, frm), chs in sorted(at.scope.items()):
        if at.edges.get((to, frm)) != "b":
            at.errors.append(f"scope declared for {to} <- {frm}, but the effective edge is {at.edges.get((to, frm))}")
            continue
        anc = G.ancestors(sonly, [to])
        if to in chs and not local.get(to):
            at.errors.append(f"scope lint: {to} <- {frm} lists {to} itself, but {to} registers no local definition "
                             "(a def node that specializes the canonical one)")
        for c in chs:
            if c not in anc:
                at.errors.append(f"scope lint: {to} borrows from {frm} a statement written in the vocabulary of {c}, "
                                 f"which is not an s-ancestor of {to}")
    check_overrides(at)
    # volume level
    vpreds = volume_preds(at, HARD, main=True)
    vcyc = G.find_cycle(vpreds)
    if vcyc:
        at.warnings.append("volume-level cycle (chapters are fine, but no volume order works): "
                           + " -> ".join(reversed(vcyc)))
    pos = {v["id"]: i for i, v in enumerate(at.volumes)}
    for v, ps in volume_preds(at, ("s",), main=True).items():
        for p in ps:
            if pos[p] > pos[v]:
                at.warnings.append(f"volumes.yaml lists {v} before {p}, which it s-depends on")
    # congestion: count prerequisites after transitive reduction, so shortcuts in computed edges don't inflate it
    for c, ps in G.transitive_reduction(at.preds(("s",))).items():
        if len(ps) > INDEGREE_WARN:
            at.warnings.append(f"{c} has {len(ps)} irreducible s-prerequisites (> {INDEGREE_WARN}): "
                               + ", ".join(sorted(ps, key=at.order.index)))
    roots = [c for c, ps in sb.items() if not ps and c != at.order[0]]
    for c in roots:
        at.warnings.append(f"{c} has no prerequisites at all")
    for t in at.targets:
        for c in t["chapters"]:
            at._known(c, f"exam-targets.yaml[{t['id']}]")
        for it in t.get("items") or ():
            for c in it.get("ch") or ():
                at._known(c, f"exam-targets.yaml[{t['id']}].items")
    check_fields(at)
    check_ids(at)
    import sync_constraints
    reason = sync_constraints.drift(at.constraints)
    if reason:
        at.errors.append(reason)
    written = at.labels.get("written") or {}
    for k in at.constraints:
        book = str(k.get("book", "")).split(":")[0]
        done = {c for b, cs in written.items() if book in (b, "new") for c in cs}  # a new chapter: no book may have it
        if at._known(k["chapter"], "chapter-constraints.yaml") and k["chapter"] in done:
            at.errors.append(f"chapter-constraints.yaml: {k['chapter']} is already written in {k.get('book')}; "
                             "a change to it is a rewrite and belongs in spec/06")
        if not k.get("rule") or not k.get("decided"):
            at.errors.append(f"chapter-constraints.yaml: {k['chapter']} needs `rule` and `decided`")
    return not at.errors


STATEMENT_PREFIX = {"def": "def", "thm": "thm", "prp": "prp", "cor": "cor", "lem": "lem", "concept": "cpt"}


def check_ids(at):
    """Statement ids use the books' label format `kind-slug` (spec/01); labels must be unique across books."""
    for n in at.statements["nodes"]:
        pre = STATEMENT_PREFIX.get(n[2])
        if not pre or not re.fullmatch(rf"{pre}-[a-z0-9]+(-[a-z0-9]+)*", n[0]):
            at.errors.append(f"statements.yaml: {n[0]} ({n[2]}) is not a `{pre or n[2]}-slug` id")
    dup = {lbl for lbl, _ in at.labels.get("duplicates") or []}
    open_ = sorted(dup - set(at.label_triage))
    if open_:
        at.warnings.append(f"{len(open_)} labels defined in more than one book are not triaged in "
                           f"registry/label-triage.yaml: {', '.join(open_)}")
    for lbl in sorted(set(at.label_triage) - dup):
        at.warnings.append(f"label-triage.yaml: {lbl} is no longer defined in two books; delete it")
    for row in {id(r): r for r in at.label_triage.values()}.values():
        if row.get("kind") not in ("same", "special", "clash") or not row.get("why"):
            at.errors.append(f"label-triage.yaml: {row['labels'][0]} needs kind same|special|clash and a why")
    if dup:
        kinds = Counter(at.label_triage[lbl]["kind"] for lbl in dup if lbl in at.label_triage)
        at.notes.append(f"{len(dup)} labels defined in two books: " + ", ".join(f"{k} {n}" for k, n in sorted(kinds.items()))
                        + (f", untriaged {len(open_)}" if open_ else ""))


def check_fields(at):
    """Subject ids, the subject-level `after` graph (must be acyclic), the external comparison and its accepted deviations."""
    ids = Counter(f.get("id") for fs in at.fields.values() for f in fs)
    for group, subjects in at.fields.items():
        for f in subjects:
            if not f.get("id"):
                at.errors.append(f"fields.yaml: {f['name']} has no id")
            elif ids[f["id"]] > 1:
                at.errors.append(f"fields.yaml: duplicate subject id {f['id']}")
            if f.get("status") not in FIELD_STATUS:
                at.errors.append(f"fields.yaml: {f['name']} has unknown status {f.get('status')}")
            for c in (f.get("ch") or []) + (f.get("hook") or []):
                at._known(c, f"fields.yaml[{f['name']}]")
            for a in f.get("after") or ():
                if a not in at.subject:
                    at.errors.append(f"fields.yaml[{f.get('id')}]: after names unknown subject {a}")
    cyc = G.find_cycle(after_preds(at))
    if cyc:
        at.errors.append("fields.yaml: subject-level after cycle: " + " -> ".join(cyc))
    if not at.external:
        return
    ext_ids = {x["id"] for x in at.external["subjects"]}
    for x in at.external["subjects"]:
        for a in x.get("fields") or ():
            if a not in at.subject:
                at.errors.append(f"external/subject-dag.yaml[{x['id']}]: unknown fields subject {a}")
        for c in x.get("ch") or ():
            at._known(c, f"external/subject-dag.yaml[{x['id']}]")
        for d in (x.get("deps") or []) + (x.get("soft") or []):
            if d not in ext_ids:
                at.errors.append(f"external/subject-dag.yaml[{x['id']}]: unknown dependency {d}")
    if at.errors:
        return
    found = dict(field_deviations(at))
    accepted = set()
    for d in at.deviations:
        keys = d["key"] if isinstance(d["key"], list) else [d["key"]]
        if not d.get("why"):
            at.errors.append(f"field-deviations.yaml: {keys[0]} has no `why`")
        for k in keys:
            accepted.add(k)
            if k not in found:
                at.warnings.append(f"field-deviations.yaml: {k} no longer occurs; delete it")
    new = [k for k in found if k not in accepted]
    if new:
        at.warnings.append(f"{len(new)} new deviations from external/subject-dag.yaml (generated/diff.md): " + ", ".join(new))
    at.notes.append(f"external subject DAG: {len(found)} deviations, {len(found) - len(new)} accepted in field-deviations.yaml")


def after_preds(at):
    return {i: set(f.get("after") or ()) & set(at.subject) for i, f in at.subject.items()}


def subject_entry(at, ids, s_only):
    """Entry reading for subjects `ids`: their ch and hook plus those of every `after` subject (transitively), closed under s."""
    subj = G.ancestors(after_preds(at), ids)
    start = {c for i in subj for c in (at.subject[i].get("ch") or []) + (at.subject[i].get("hook") or [])}
    return subj, G.ancestors(s_only, start)


def field_deviations(at):
    """(key, message) for each disagreement between registry/external/subject-dag.yaml and the atlas.

    edge     the external graph has hard prerequisite A of B, but B's entry reading (subject_entry)
             contains none of A's chapters and B's after-closure does not contain A's subjects
    after    fields.yaml says B after C, both are on the map, but no chapter of C is an s-ancestor of B's chapters
    scope    the external graph puts the subject in layer 0-1 (undergraduate), fields.yaml marks it out
    unmatched  a fields.yaml subject that no external subject maps to
    """
    s_only = at.preds({"s"})
    X = {x["id"]: x for x in at.external["subjects"]}
    out = []

    def chapters(x):
        return {c for i in x.get("fields") or () for c in (at.subject[i].get("ch") or []) + (at.subject[i].get("hook") or [])} \
            | set(x.get("ch") or ())

    for b in X.values():
        subj, entry = subject_entry(at, b.get("fields") or (), s_only)
        entry |= G.ancestors(s_only, b.get("ch") or ())
        for dep in b.get("deps") or ():
            a = X[dep]
            if set(a.get("fields") or ()) & subj or chapters(a) & entry:
                continue
            out.append((f"{b['id']} <- {dep}", f"{b['name']} ← {a['name']}：入口必讀不含 {'、'.join(sorted(chapters(a))) or '（無章）'}"))
        if b["layer"] <= 1 and any(at.subject[i]["status"] == "out" for i in b.get("fields") or ()):
            out.append((f"scope {b['id']}", f"{b['name']}：外部圖為第 {b['layer']} 層（大學部），fields.yaml 標為範圍外"))
    for i, f in at.subject.items():
        for c in f.get("after") or ():
            mine, theirs = set(f.get("ch") or ()), set(at.subject[c].get("ch") or ())
            if mine and theirs and not (G.ancestors(s_only, mine) & theirs):
                out.append((f"after {i} <- {c}", f"{f['name']} after {at.subject[c]['name']}：兩科都已在地圖上，但章層級沒有對應的 s 路徑"))
    mapped = {i for x in X.values() for i in x.get("fields") or ()}
    out += [(f"unmatched {i}", f"{f['name']}：外部圖沒有對應科目") for i, f in at.subject.items() if i not in mapped]
    return out


LOCAL_DEF_MAX = 3


def check_terms(at):
    """One canonical definition per term; every other definition of it is a local special case that
    specializes it. A local definition (one that specializes a def in another chapter) is how a borrowing
    chapter brings vocabulary into scope: definitions only, at most three per chapter, read at R0-R1.
    Returns {chapter: [local def ids]}."""
    nodes = {n[0]: n for n in at.statements["nodes"]}
    term = {n[0]: n[6] for n in at.statements["nodes"] if len(n) > 6}
    spec = defaultdict(list)
    for user, used, typ, *_ in at.statements["edges"]:
        if typ == "specializes":
            spec[user].append(used)
            if term.get(user) != term.get(used):
                at.errors.append(f"statements.yaml: {user} specializes {used}, but their terms differ "
                                 f"({term.get(user)} vs {term.get(used)})")
    by_term = defaultdict(list)
    for nid, t in term.items():
        if nodes[nid][2] == "def":
            by_term[t].append(nid)
    for t, ids in sorted(by_term.items()):
        canonical = [i for i in ids if not spec[i]]
        if len(canonical) != 1:
            at.errors.append(f"term `{t}` has {len(canonical)} definitions not linked by specializes: "
                             + ", ".join(canonical) + " (exactly one may be canonical)")
    if at.terms:
        registry = {t["id"]: t for t in at.terms}
        for t, ids in sorted(by_term.items()):
            canonical = [i for i in ids if not spec[i]]
            if t not in registry:
                at.errors.append(f"statements.yaml: term `{t}` is not in registry/terms.yaml")
            elif canonical and registry[t]["def"] != canonical[0]:
                at.errors.append(f"terms.yaml: `{t}` names {registry[t]['def']} as its definition, "
                                 f"but statements.yaml's canonical node is {canonical[0]}")
        pending = [t["id"] for t in at.terms if t.get("also")]
        if pending:
            at.warnings.append(f"{len(pending)} terms in registry/terms.yaml have more than one definition (`also`); "
                               "triage each into a local definition, a homonym, or a duplicate to merge")
        status = Counter(t.get("naer") for t in at.terms)
        at.notes.append(f"terms.yaml: {len(at.terms)} terms; Chinese names: " + ", ".join(
            f"{k} {status[k]}" for k in ("univ", "hs", "hand", "choose", "missing") if status[k])
            + " (choose and missing are the author's to decide)")
    local = defaultdict(list)
    for nid, targets in spec.items():
        n = nodes[nid]
        if any(nodes[t][1] != n[1] for t in targets):
            if n[2] != "def":
                at.errors.append(f"local definition {nid} must be a def, not {n[2]} (theorems cannot be defined in place)")
            ar = parse_ar(f"{n[4]}/{n[5]}", f"statements.yaml node {nid}", at)
            if ar and ar[1] > 1:
                at.errors.append(f"local definition {nid} is taught at {n[5]}; in-place definitions are read at R0-R1, "
                                 "otherwise make the edge s")
            local[n[1]].append(nid)
    for ch, ids in sorted(local.items()):
        if len(ids) > LOCAL_DEF_MAX:
            at.errors.append(f"{ch} defines {len(ids)} terms in place (> {LOCAL_DEF_MAX}): {', '.join(ids)}; "
                             "make the borrow an s edge instead")
    return local


def check_overrides(at):
    """moves.yaml makes the map say what the book will say after a rewrite. Each row must point at an open
    spec/06 TODO, and must go once the book has caught up (import_la.py records a 0 effect)."""
    spec = (ROOT / "spec" / "06-migration.md").read_text()
    open_todo = set(re.findall(r"^(?:\d+\.\s+)?- \[ \].*?`todo:([a-z0-9-]+)`", spec, re.M))
    done_todo = set(re.findall(r"^(?:\d+\.\s+)?- \[x\].*?`todo:([a-z0-9-]+)`", spec, re.M))
    for m in at.moves:
        t = m.get("todo")
        if not t:
            at.errors.append(f"moves.yaml[{m['label']}]: no `todo` linking it to spec/06")
        elif t in done_todo:
            at.errors.append(f"moves.yaml[{m['label']}]: spec/06 todo:{t} is ticked; delete the row")
        elif t not in open_todo:
            at.errors.append(f"moves.yaml[{m['label']}]: todo:{t} is not an open item in spec/06")
    seen = {(o[0], o[1], o[2]) for o in at.overrides}
    for m in at.moves:
        want = [(m["label"], "move", m["to"])] + [(m["label"], k, c) for k in ("softened_for", "borrowed_by")
                                                  for c in m.get(k, ())]
        for w in want:
            if w not in seen:
                at.warnings.append(f"moves.yaml[{m['label']}]: {w[1]} {w[2]} not in the computed edges; rerun import_la.py")
    for label, kind, ch, n in at.overrides:
        if n == 0:
            what = "the label is already there" if kind == "move" else "no citation is affected any more"
            at.errors.append(f"stale override in moves.yaml[{label}]: {kind} {ch} — {what}; the book has caught up, "
                             "delete it (and tick the spec/06 todo)")
    at.notes.append(f"{sum(1 for o in at.overrides if o[3])} active rewrite overrides from moves.yaml "
                    f"({len(at.moves)} rows)")


def parse_ar(text, where, at):
    """'A2/R3' -> (2, 3)."""
    try:
        a, r = str(text).split("/")
        assert a[0] == "A" and r[0] == "R"
        return int(a[1:]), int(r[1:])
    except (ValueError, AssertionError, IndexError):
        at.errors.append(f"{where}: bad A/R value {text!r}")
        return None


def volume_preds(at, types, main=False):
    """main=True ignores optional chapters: a crossing chapter sits downstream of two branches by design."""
    out = {v["id"]: set() for v in at.volumes}
    for (to, frm), typ in at.edges.items():
        if main and (at.chapters[to]["opt"] or at.chapters[frm]["opt"]):
            continue
        a, b = at.chapters[to]["vol"], at.chapters[frm]["vol"]
        if typ in types and a != b:
            out[a].add(b)
    return out


def volume_edge_type(at, main=False):
    """(to_vol, from_vol) -> 's' if any chapter s-edge, else 'b'. main=True ignores optional chapters."""
    out = {}
    for (to, frm), typ in at.edges.items():
        if main and (at.chapters[to]["opt"] or at.chapters[frm]["opt"]):
            continue
        a, b = at.chapters[to]["vol"], at.chapters[frm]["vol"]
        if typ in HARD and a != b:
            if out.get((a, b)) != "s":
                out[(a, b)] = typ
    return out


# ───────────────────────── stats ─────────────────────────

def main_only(preds, at):
    """Drop optional chapters: the statistics describe the main line unless a column says otherwise."""
    return {c: {p for p in ps if not at.chapters[p]["opt"]}
            for c, ps in preds.items() if not at.chapters[c]["opt"]}


def stats(at):
    s_all = at.preds(("s",))
    sb_all = at.preds(HARD)
    s_only = main_only(s_all, at)
    sb = main_only(sb_all, at)
    height, back = G.longest_paths(s_only)
    longest = max(height, key=lambda c: (height[c], -at.order.index(c)))
    height_all, back_all = G.longest_paths(s_all)
    longest_all = max(height_all, key=lambda c: (height_all[c], -at.order.index(c)))
    lines = ["# 地圖統計（由 `tools/atlas.py stats` 產生，勿手改）", ""]
    n_s = sum(1 for t in at.edges.values() if t == "s")
    n_b = sum(1 for t in at.edges.values() if t == "b")
    n_soft = sum(1 for t in at.edges.values() if t in SOFT)
    computed_s = sum(1 for k, v in at.computed.items() if v[0] == "s")
    lines += [f"- 冊：{len(at.volumes)}；章：{len(at.chapters)}（選讀 {sum(c['opt'] for c in at.chapters.values())}）",
              f"- 章層級邊：s {n_s}、b {n_b}、軟邊 {n_soft}；其中 {computed_s} 條 s 邊是從線代書的證明計算出來的，其餘是計畫值",
              ""]

    lines += ["除非欄位註明「含選讀」，以下統計都排除選讀章（opt）。", ""]
    lines += ["## 最長硬依賴鏈（只計 s）", ""]
    chain = G.path_to(back, longest)
    lines += [f"**{len(chain)} 章**，終點 {at.label(longest)}：", "",
              " → ".join(chain), ""]
    if height_all[longest_all] > height[longest]:
        lines += [f"含選讀：{height_all[longest_all]} 章，終點 {at.label(longest_all)}。", ""]
    top = sorted(height, key=lambda c: -height[c])
    seen_vol, others = set(), []
    for c in top:
        v = at.chapters[c]["vol"]
        if v not in seen_vol:
            seen_vol.add(v)
            others.append(f"{v} {height[c]}（{c}）")
    lines += ["各冊最高的章（高度＝從零讀到該章至少要依序讀的章數）：" + "、".join(others), ""]

    hist = Counter(height.values())
    lines += ["### 章高度直方圖", "", "| 高度 | 章數 |", "|---:|---:|"]
    lines += [f"| {h} | {hist[h]} |" for h in sorted(hist)]
    tall = [c for c in at.order if height.get(c, 0) > 20]
    lines += ["", f"高度超過 20 的章（{len(tall)} 個，逐一檢查能否把 s 降成 b）：" + "、".join(tall), ""]

    lines += ["## 資格考目標的最短必讀集合", "",
              "必讀＝目標章在 s 圖上的祖先閉包（含目標本身）；b 的來源不計入。", "",
              "| 目標 | 目標章數 | 必讀章數 | 對話報告手算值 | 涉及的冊 |", "|---|---:|---:|---:|---|"]
    details = []
    for t in at.targets:
        req = G.ancestors(s_only, t["chapters"])
        vols = Counter(at.chapters[c]["vol"] for c in req)
        vol_ids = [x["id"] for x in at.volumes]
        vol_txt = "、".join(f"{v} {n}" for v, n in sorted(vols.items(), key=lambda kv: vol_ids.index(kv[0])))
        lines.append(f"| {t['name']} | {len(t['chapters'])} | **{len(req)}** | {t.get('reported', '—')} | {vol_txt} |")
        borrowed = sorted({p for c in req for p in sb[c] - s_only[c]} - req, key=at.order.index)
        details.append((t, req, borrowed))
    lines.append("")
    for t, req, borrowed in details:
        lines += [f"### {t['name']}", "", t.get("note", ""), "",
                  "必讀：" + "、".join(sorted(req, key=at.order.index)), ""]
        if borrowed:
            lines += ["只借用（不必讀）：" + "、".join(borrowed), ""]

    desc = {c: len(G.descendants(sb, [c])) - 1 for c in sb}
    s_red = G.transitive_reduction(s_only)
    lines += ["## 瓶頸：後代最多的章（s ∪ b）", "", "| 章 | 後代章數 | 約簡後 s 入度 | 後代涉及冊數 |", "|---|---:|---:|---:|"]
    for c in sorted(desc, key=lambda c: (-desc[c], at.order.index(c)))[:20]:
        vols = {at.chapters[d]["vol"] for d in G.descendants(sb, [c])} - {at.chapters[c]["vol"]}
        lines.append(f"| {at.label(c)} | {desc[c]} | {len(s_red[c])} | {len(vols)} |")
    lines.append("")

    lines += ["## 每冊的外部必讀量", "",
              "讀完該冊主幹章之前，冊外至少要讀的章數（s 祖先閉包，扣掉本冊）。上游冊只計本冊非選讀章的邊。", "",
              "| 冊 | 本冊章數（選讀） | 冊外必讀章數 | 含選讀 | 直接上游冊（s） | 只借用的冊（b） |", "|---|---:|---:|---:|---|---|"]
    vt = volume_edge_type(at, main=True)
    for v in at.volumes:
        mine_all = [c for c in at.order if at.chapters[c]["vol"] == v["id"]]
        mine = [c for c in mine_all if not at.chapters[c]["opt"]]
        req = G.ancestors(s_only, mine) - set(mine_all)
        req_all = G.ancestors(s_all, mine_all) - set(mine_all)
        up_s = sorted(b for (a, b), t in vt.items() if a == v["id"] and t == "s")
        up_b = sorted(b for (a, b), t in vt.items() if a == v["id"] and t == "b")
        n_opt = len(mine_all) - len(mine)
        lines.append(f"| {v['id']} {v['title']} | {len(mine_all)}" + (f"（{n_opt}）" if n_opt else "")
                     + f" | {len(req)} | {len(req_all)} | {'、'.join(up_s) or '—'} | {'、'.join(up_b) or '—'} |")
    lines.append("")

    if at.fields:
        lines += ["## 領域覆蓋", "", "依 `registry/fields.yaml`。「入口必讀」＝支線候選的入口先修（hook）在 s 圖上的祖先閉包章數。", "",
                  "| 領域 | 科目數 | 已涵蓋 | 部分 | 支線候選 | 範圍外 |", "|---|---:|---:|---:|---:|---:|"]
        for group, subjects in at.fields.items():
            cnt = Counter(f["status"] for f in subjects)
            lines.append(f"| {group} | {len(subjects)} | " + " | ".join(str(cnt[k]) for k in FIELD_STATUS) + " |")
        lines += ["", "### 支線候選（未涵蓋，但先修已在地圖上）", "",
                  "入口必讀＝自己的入口先修，加上 `after` 科目（遞移）的章與入口先修，再取 s 祖先閉包。", "",
                  "| 科目 | 入口先修 | 先讀科目（after） | 入口必讀章數 | 備註 |", "|---|---|---|---:|---|"]
        for group, subjects in at.fields.items():
            for f in subjects:
                if f["status"] == "branch":
                    hook = f.get("hook") or []
                    n = len(subject_entry(at, [f["id"]], s_only)[1])
                    after = "、".join(at.subject[a]["name"] for a in f.get("after") or ())
                    lines.append(f"| {f['name']}（{f['en']}） | {'、'.join(hook)} | {after} | {n} | {f.get('note', '')} |")
        lines.append("")

    lines += ["## 陳述讀者必讀集（spec/03 §6.2）", "",
              "陳述讀者只讀定義與陳述、會套用定理，不讀證明（對應 b 邊的 R ≤ R1 門檻，不是 R1 程度的讀者）。要讀的是：目標章引用到的定義、借用的定理陳述所用的定義，"
              "以及這些章的定義與陳述再引用到的定義（遞移）。這個集合只能由書稿的 crossref 算出，目前只有純線代章有資料。"
              "書稿沒有明寫引用的隱含語彙（例如定義裡直接使用「矩陣」而不引用）看不到，所以「下界」偏低。"
              "「術語比對」再加上 `registry/terms.yaml` 的術語在定義與陳述文字裡出現、卻沒有引用的情形，"
              "常用詞會造成假陽性，所以偏高。比對只在該章的 s 閉包裡走（完整讀者讀得到的語彙，陳述讀者不會需要更多），"
              "所以估計不超過上界。真實值夾在下界與估計值之間。", "",
              "結構性的章（例如 AL4.8：結合代數、自由向量空間、群作用、張量積）以定義為主，"
              "幾乎沒有「只需套用、可以跳過證明」的定理，陳述讀者必讀量本來就接近 s 閉包；"
              "這是指標在區分兩種讀者，不是計算出錯。", "",
              "| 章 | 下界 | 術語比對估計 | s 閉包（上界） | 估計比下界多出的章 |", "|---|---:|---:|---:|---|"]
    outside, rows = [], []
    for c in at.order:
        if la_only(at, c) and not at.chapters[c]["opt"] and at.chapters[c]["vol"] in ("MA", "GEO", "NLA", "AL4"):
            low, (est, out, via) = stmt_reader_lower(at, c), stmt_reader_estimate(at, c, s_only)
            rows.append((c, low, est))

            def why(x):
                frm, terms = via[x]
                if terms:
                    return f"{x}（{'、'.join(terms[:2])}{'' if frm == c else '，經 ' + frm}）"
                return f"{x}（經 {frm}）"
            lines.append(f"| {at.label(c)} | {len(low)} | {len(est | low)} | {len(G.ancestors(s_only, [c])) - 1} | "
                         + "、".join(why(x) for x in sorted(est - low, key=at.order.index)) + " |")
            if out:
                outside.append(f"- {c}：" + "、".join(sorted(out, key=at.order.index)))
    support, sole = Counter(), Counter()  # term -> chapter entries it supports / that vanish without it
    for c, low, est in rows:
        closure = G.ancestors(s_only, [c])
        for x in est - low:
            support.update({t for (to, frm), ts in at.vocab_terms.items()
                            if frm == x and to in closure | {c} for t in ts})
    for t in [t for t, _ in support.most_common(15)]:
        for c, low, est in rows:
            sole[t] += len(est | low) - len(stmt_reader_estimate(at, c, s_only, frozenset([t]))[0] | low)
    term_ch = {t["id"]: t["ch"] for t in at.terms}
    lines += ["", "影響最大的術語：「支撐」＝上表多出的章裡，有幾章（各列合計）是經由這個詞的比對進來的；"
              "「唯一」＝只拿掉這個詞，估計合計會少幾章（多數章同時被好幾個詞拉進來，所以通常很小）。"
              "分流 terms.yaml 的 `also` 時從上面幾個詞開始：常用詞（even、over 之類）多半是假陽性，"
              "可以加進 seed_terms.py 的 STOP 或標成 meta。F1 的邏輯用語已標為 `meta`，不參與比對。", "",
              "| 術語 | 正式定義所在 | 支撐 | 唯一 |", "|---|---|---:|---:|"]
    lines += [f"| {t} | {term_ch.get(t, '')} | {n} | {sole[t]} |" for t, n in support.most_common(15)] or ["| （無） | | | |"]
    lines += ["", "術語比對找到、但不在該章 s 閉包裡的章（同形異義、前向提及，或地圖漏了一條邊；分流 terms.yaml 的 also 之後會減少）：", ""]
    lines += outside or ["（無）"]
    lines.append("")

    lines += ["## 線代書計算邊的抽查：LA3 能否跳過 LA2 第 10 章", ""]
    la3 = [c for c in at.order if at.chapters[c]["vol"] == "LA3"]
    needs = "LA2.10" in G.ancestors(s_only, la3)
    for (to, frm), (typ, h, s, _) in sorted((k, v) for k, v in at.computed.items()
                                             if k[0] in la3 and k[1] == "LA2.10"):
        w = at.witnesses.get(f"{to}<-{frm}") or []
        lines.append(f"- {to} ← {frm}：{typ}，硬引用 {h}、軟引用 {s}。" +
                     (" 硬引用來自 " + "；".join(f"`{a}` 引用 `{b}`" for a, b in w) if w else ""))
    lines += ["", ("結論：LA3 仍然需要 LA2 第 10 章。" if needs else
                   "結論：LA3 的 s 祖先閉包不含 LA2.10，可以跳過第 10 章"
                   + ("（已套用 registry/moves.yaml 的計畫搬家，書稿尚未改）" if at.moves else "") + "。"), ""]
    (OUT / "report.md").write_text("\n".join(lines) + "\n")
    migration(at)
    return lines


def migration(at):
    """generated/migration.md: manuscript chapter -> atlas chapters, from the src column of chapters.yaml."""
    by_src = defaultdict(list)
    for c in at.order:
        for src in at.chapters[c]["src"]:
            by_src[str(src)].append(c)

    def key(src):
        return [int(x) if x.isdigit() else x for x in re.split(r"(\d+)", src)]

    def name(c):
        ch = at.chapters[c]
        return f"{c} {ch['title']}" + ("（選讀）" if ch["opt"] else "")
    lines = ["# 書稿 → 冊的對照（由 `tools/atlas.py stats` 從 `registry/chapters.yaml` 的 `src` 欄產生）", "",
             "對照的理由與決策記在 spec/06。", ""]
    for book, title in (("ab", "analysis-book（`ab:N` ＝ blueprint/book.yaml 第 N 章）"),
                        ("la", "linear-algebra（`la:chNN` ＝ 第 NN 章；`la:ch00/NN` ＝ 第 0 章第 NN 節）")):
        lines += [f"## {title}", "", "| 書稿 | 冊的章 |", "|---|---|"]
        for src in sorted((k for k in by_src if k.startswith(book + ":")), key=key):
            lines.append(f"| {src} | {'；'.join(name(c) for c in by_src[src])} |")
        lines.append("")
    new = [c for c in at.order if "new" in at.chapters[c]["src"]]
    lines += ["## 尚無書稿（`new`）", ""]
    for vid in dict.fromkeys(at.chapters[c]["vol"] for c in new):
        lines.append(f"- **{vid}**：" + "、".join(name(c) for c in new if at.chapters[c]["vol"] == vid))
    (OUT / "migration.md").write_text("\n".join(lines) + "\n")


# ───────────────────────── diff ─────────────────────────

def stmt_reader_lower(at, cid):
    """Chapters a statement reader of `cid` must read (definitions and statements only), from the computed vocab edges."""
    return G.ancestors(at.vocab["stmt"], at.vocab["all"].get(cid, ())) - {cid}


def stmt_reader_estimate(at, cid, s_only, skip=frozenset()):
    """(estimate, outside, via): the lower bound plus the vocabulary found by matching registered terms
    (import_la.term_edges), traversed only inside cid's s closure. Whatever cid needs is read by the full reader too,
    so a term hit outside the closure is a homonym, a forward mention, or a missing map edge: it goes to `outside`.
    via[chapter] = (chapter it was reached from, term ids if through a term edge) for the first path found.
    Terms in `skip` are ignored (to measure how much each term pulls in)."""
    closure = G.ancestors(s_only, [cid])

    def term_preds(c):
        return {f for f in at.vocab["term"].get(c, ()) if set(at.vocab_terms.get((c, f), ())) - skip}
    via, todo = {}, [cid]
    for f in at.vocab["all"].get(cid, ()):
        via.setdefault(f, (cid, None))
    for f in term_preds(cid):
        via.setdefault(f, (cid, [t for t in at.vocab_terms[(cid, f)] if t not in skip]))
    outside = set(via) - closure
    todo = [c for c in via if c in closure]
    seen = set(todo)
    while todo:
        c = todo.pop(0)
        for f in at.vocab["stmt"].get(c, ()):
            if f in closure and f not in seen:
                seen.add(f)
                via[f] = (c, None)
                todo.append(f)
        for f in term_preds(c):
            if f in closure and f not in seen:
                seen.add(f)
                via[f] = (c, [t for t in at.vocab_terms[(c, f)] if t not in skip])
                todo.append(f)
    return seen - {cid}, outside, via


def la_only(at, cid):
    return all(str(s).startswith("la:") for s in at.chapters[cid]["src"])


def diff(at):
    lines = ["# 計畫 vs 計算 vs 陳述層（由 `tools/atlas.py diff` 產生）", ""]
    b_as_s, plan_unused, added = [], [], []
    for key, (ptyp, why) in sorted(at.plan.items()):
        ctyp = at.computed.get(key, (None,))[0]
        if ptyp == "b" and ctyp == "s":
            b_as_s.append(f"- {key[0]} ← {key[1]}：計畫為 b，證明裡是 s（{why}）")
        if ptyp == "s" and la_only(at, key[0]) and la_only(at, key[1]) and ctyp != "s":
            plan_unused.append(f"- {key[0]} ← {key[1]}：計畫為 s，計算值為 {ctyp or '無'}")
    moved = [f"- `{m['label']}`：{m['from']} → {m['to']}（{m.get('decided', '')}）"
             + (f"；改以 b 借用的章：{'、'.join(m['borrowed_by'])}" if m.get("borrowed_by") else "")
             for m in at.moves]
    lines += ["## 計畫中的搬家（registry/moves.yaml，已套用在計算邊上，書稿尚未改）", ""] + (moved or ["（無）"]) + [""]
    for key, (ctyp, h, s, _) in sorted(at.computed.items()):
        if ctyp == "s" and not la_only(at, key[0]) and at.plan.get(key, (None,))[0] != "s":
            added.append(f"- {key[0]} ← {key[1]}：計算為 s（硬引用 {h}），計畫為 {at.plan.get(key, ('無',))[0]}")
    lines += ["## b 被當成 s 使用", ""] + (b_as_s or ["（無）"]) + [""]
    lines += ["## 計畫中有、證明沒用（兩端都有書稿：已由計算值取代，不進入圖）", ""] + (plan_unused or ["（無）"]) + [""]
    lines += ["## 證明有用、計畫中沒有（只列混合來源的章；純線代章本來就以計算值為準）", ""] + (added or ["（無）"]) + [""]

    stmt_ch = {n[0]: n[1] for n in at.statements["nodes"]}
    sb = at.preds(HARD)
    missing = []
    for user, used, typ, *_ in at.statements["edges"]:  # [user, used, type, need?, assessed?]
        if typ not in ("uses", "borrows"):
            continue
        user_ch, used_ch = stmt_ch[user], stmt_ch[used]
        if user_ch != used_ch and used_ch not in G.ancestors(sb, [user_ch]):
            missing.append(f"- `{user}`（{user_ch}）{typ} `{used}`（{used_ch}）：章層級沒有 {used_ch} ⇒ {user_ch} 的硬路徑")
    lines += ["## 陳述層的 uses／borrows 在章層級找不到路徑", ""] + (missing or ["（無）"]) + [""]
    noscope = [f"- {to} ← {frm}" for (to, frm), typ in sorted(at.edges.items(), key=lambda kv: at.order.index(kv[0][0]))
               if typ == "b" and (to, frm) not in at.scope]
    lines += ["## b 邊尚未宣告記號作用域（`scope`，spec/03 §6.1）", ""] + (noscope or ["（無）"]) + [""]
    kind_name = {"same": "同一內容，遷移時合併", "special": "特例，改名並以 specializes 指回", "clash": "撞名，改名"}
    dup = [f"- `{lbl}`：" + "、".join(f"{b} {c or '（無對應章）'}" for b, c in where) + "　"
           + (kind_name[at.label_triage[lbl]["kind"]] if lbl in at.label_triage else "**未分流**")
           for lbl, where in at.labels.get("duplicates") or ()]
    lines += ["## 跨書重複的 label（registry/computed/labels.yaml，分流見 registry/label-triage.yaml）", ""] \
        + (dup or ["（無）"]) + [""]
    stmt_ch = {n[0]: n[1] for n in at.statements["nodes"]}
    takes = {lbl: k["chapter"] for k in at.constraints for lbl in k.get("takes") or ()}
    off = [f"- `{sid}`：地圖放在 {stmt_ch[sid]}，書稿目前在 " + "、".join(f"{b} {c}" for b, c in where)
           + (f"　已知：{takes[sid]} 寫好後接手（chapter-constraints.yaml）" if takes.get(sid) == stmt_ch[sid] else "")
           for sid, where in sorted((at.labels.get("statements") or {}).items())
           if all(c != stmt_ch.get(sid) for _, c in where)]
    lines += ["## 陳述 ID 對到的書稿 label 不在同一章", ""] + (off or ["（無）"]) + [""]
    if at.external:
        accepted = {k for d in at.deviations for k in (d["key"] if isinstance(d["key"], list) else [d["key"]])}
        found = field_deviations(at)
        new = [f"- `{k}` {msg}" for k, msg in found if k not in accepted]
        lines += ["## 外部科目圖的對照（registry/external/subject-dag.yaml）", "",
                  f"共 {len(found)} 項差異，其中 {len(found) - len(new)} 項已記在 `registry/field-deviations.yaml`。以下只列新出現的：", ""] \
            + (new or ["（無）"]) + [""]
    (OUT / "diff.md").write_text("\n".join(lines) + "\n")
    return lines


# ───────────────────────── render ─────────────────────────

def mid(cid):
    return cid.replace(".", "_")


def esc(s):
    return s.replace('"', "#quot;")


def render(at):
    OUT.mkdir(exist_ok=True)
    (OUT / "chapters").mkdir(exist_ok=True)
    md = ["# 教材地圖（由 `tools/atlas.py render` 產生，勿手改）", "",
          "實線＝s（需讀），虛線＝b（借用具名結果）。see／revisits 不畫。圖已做傳遞約簡，只為了好讀；",
          "完整的直接邊在 registry 與 `atlas.html`。互動版：用瀏覽器開 `atlas.html`。", ""]

    # volume level
    vt = volume_edge_type(at)
    vpre = defaultdict(set)
    for (a, b) in vt:
        vpre[a].add(b)
    vred = G.transitive_reduction({v["id"]: vpre[v["id"]] for v in at.volumes})
    vm = ["flowchart TD"]
    for v in at.volumes:
        vm.append(f'  {v["id"]}["{v["id"]} {esc(v["title"])}"]:::{v["branch"]}')
    for v in at.volumes:
        for p in sorted(vred[v["id"]]):
            arrow = "-->" if vt[(v["id"], p)] == "s" else "-.->"
            vm.append(f"  {p} {arrow} {v['id']}")
    vm += [f"  classDef {k} fill:{c},stroke:#888,color:#222" for k, c in BRANCH_COLOUR.items()]
    (OUT / "volumes.mmd").write_text("\n".join(vm) + "\n")
    md += ["## 冊層級", "", "```mermaid", *vm, "```", ""]

    # chapter level, one diagram per volume
    sb = at.preds(HARD)
    red = G.transitive_reduction(sb)
    for v in at.volumes:
        mine = [c for c in at.order if at.chapters[c]["vol"] == v["id"]]
        lines = ["flowchart LR"]
        ports = set()
        body = []
        for c in mine:
            ch = at.chapters[c]
            cls = ":::opt" if ch["opt"] else (":::segb" if ch.get("seg") == "B" else "")
            body.append(f'  {mid(c)}["{c.split(".", 1)[1]} {esc(ch["title"])}"]{cls}')
        for c in mine:
            for p in sorted(red[c], key=at.order.index):
                arrow = "-->" if at.edges[(c, p)] == "s" else "-.->"
                if at.chapters[p]["vol"] != v["id"]:
                    ports.add(p)
                body.append(f"  {mid(p)} {arrow} {mid(c)}")
        for p in sorted(ports, key=at.order.index):
            lines.append(f'  {mid(p)}["{p} {esc(at.chapters[p]["title"])}"]:::ext')
        lines += body
        lines += ["  classDef ext fill:#e6e6e6,stroke:#999,color:#555",
                  "  classDef opt fill:#fff,stroke:#999,stroke-dasharray:4 3,color:#555",
                  "  classDef segb fill:#f6f6fb,stroke:#99a,color:#333"]
        (OUT / "chapters" / f"{v['id']}.mmd").write_text("\n".join(lines) + "\n")
        md += [f"## {v['id']} {v['title']}", "", "```mermaid", *lines, "```", ""]
    md += ["圖例：灰底＝冊外來源；虛框＝選讀章；淡紫＝B 段。", ""]
    (OUT / "README.md").write_text("\n".join(md))

    # interactive html
    data = {
        "volumes": [{k: v[k] for k in ("id", "title", "en", "branch", "tier", "status")} for v in at.volumes],
        "chapters": [{"id": c, "vol": at.chapters[c]["vol"], "title": at.chapters[c]["title"],
                      "src": at.chapters[c]["src"], "opt": at.chapters[c]["opt"],
                      "seg": at.chapters[c].get("seg")} for c in at.order],
        "edges": [{"to": a, "from": b, "type": t, "reduced": b in red.get(a, ()) if t in HARD else False,
                   "origin": "computed" if (a, b) in at.computed else "plan",
                   "why": (at.plan.get((a, b)) or (None, None))[1]}
                  for (a, b), t in sorted(at.edges.items())],
        "branches": {k: {"name": BRANCH_NAME[k], "colour": BRANCH_COLOUR[k]} for k in BRANCH_COLOUR},
        "targets": [{k: t.get(k) for k in ("id", "name", "note", "chapters")} for t in at.targets],
    }
    tpl = (ROOT / "tools" / "atlas_template.html").read_text()
    (OUT / "atlas.html").write_text(tpl.replace("/*__DATA__*/null", json.dumps(data, ensure_ascii=False)))


# ───────────────────────── main ─────────────────────────

def main(argv=None):
    ap = argparse.ArgumentParser(description="math-atlas graph tools")
    ap.add_argument("cmd", choices=["check", "stats", "render", "diff", "all"])
    args = ap.parse_args(argv)
    at = Atlas()
    ok = check(at)
    for w in at.warnings:
        print("warning:", w)
    for e in at.errors:
        print("error:", e)
    if not ok:
        sys.exit(1)
    OUT.mkdir(exist_ok=True)
    if args.cmd in ("stats", "all"):
        stats(at)
        print("wrote generated/report.md")
    if args.cmd in ("diff", "all"):
        diff(at)
        print("wrote generated/diff.md")
    if args.cmd in ("render", "all"):
        render(at)
        print("wrote generated/README.md, volumes.mmd, chapters/*.mmd, atlas.html")
    if args.cmd == "check":
        print(f"ok: {len(at.volumes)} volumes, {len(at.chapters)} chapters, {len(at.edges)} edges")
    for n in at.notes:
        print("note:", n)


if __name__ == "__main__":
    main()
