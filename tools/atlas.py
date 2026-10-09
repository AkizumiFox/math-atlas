"""math-atlas: check, measure and draw the chapter-level dependency graph.

  python3 tools/atlas.py check    # hard errors -> exit 1
  python3 tools/atlas.py stats    # generated/report.md
  python3 tools/atlas.py render   # generated/*.mmd, generated/README.md, generated/atlas.html
  python3 tools/atlas.py diff     # plan vs computed vs statement-level edges
  python3 tools/atlas.py all      # check, stats, render, diff
"""
import argparse
import json
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
        fields = reg / "fields.yaml"
        self.fields = yaml.safe_load(fields.read_text()) if fields.exists() else {}

    def _known(self, cid, where):
        if cid not in self.chapters:
            self.errors.append(f"{where}: unknown chapter {cid}")
            return False
        return True

    def _load_plan(self, path):
        data = yaml.safe_load(path.read_text()) or {}
        out = {}
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
        return out

    def _load_computed(self, folder):
        out, wit = {}, {}
        for path in sorted(folder.glob("*-edges.yaml")):
            data = yaml.safe_load(path.read_text())
            for to, frm, typ, hard, soft in data["edges"]:
                if self._known(to, path.name) and self._known(frm, path.name):
                    out[(to, frm)] = (typ, hard, soft, path.name)
            wit.update(data.get("witnesses") or {})
        return out, wit

    def _merge(self):
        """Effective edge type per (to, from): the strongest of plan and computed."""
        eff = {}
        for key, (typ, _) in self.plan.items():
            eff[key] = typ
        for key, (typ, *_rest) in self.computed.items():
            if key not in eff or STRENGTH[typ] > STRENGTH[eff[key]]:
                eff[key] = typ
        return eff

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
    # volume level
    vpreds = volume_preds(at, HARD)
    vcyc = G.find_cycle(vpreds)
    if vcyc:
        at.warnings.append("volume-level cycle (chapters are fine, but no volume order works): "
                           + " -> ".join(reversed(vcyc)))
    pos = {v["id"]: i for i, v in enumerate(at.volumes)}
    for v, ps in volume_preds(at, ("s",)).items():
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
    for group, subjects in at.fields.items():
        for f in subjects:
            if f.get("status") not in FIELD_STATUS:
                at.errors.append(f"fields.yaml: {f['name']} has unknown status {f.get('status')}")
            for c in (f.get("ch") or []) + (f.get("hook") or []):
                at._known(c, f"fields.yaml[{f['name']}]")
    return not at.errors


def volume_preds(at, types):
    out = {v["id"]: set() for v in at.volumes}
    for (to, frm), typ in at.edges.items():
        a, b = at.chapters[to]["vol"], at.chapters[frm]["vol"]
        if typ in types and a != b:
            out[a].add(b)
    return out


def volume_edge_type(at):
    """(to_vol, from_vol) -> 's' if any chapter s-edge, else 'b'."""
    out = {}
    for (to, frm), typ in at.edges.items():
        a, b = at.chapters[to]["vol"], at.chapters[frm]["vol"]
        if typ in HARD and a != b:
            if out.get((a, b)) != "s":
                out[(a, b)] = typ
    return out


# ───────────────────────── stats ─────────────────────────

def stats(at):
    s_only = at.preds(("s",))
    sb = at.preds(HARD)
    height, back = G.longest_paths(s_only)
    longest = max(height, key=lambda c: (height[c], -at.order.index(c)))
    lines = ["# 地圖統計（由 `tools/atlas.py stats` 產生，勿手改）", ""]
    n_s = sum(1 for t in at.edges.values() if t == "s")
    n_b = sum(1 for t in at.edges.values() if t == "b")
    n_soft = sum(1 for t in at.edges.values() if t in SOFT)
    computed_s = sum(1 for k, v in at.computed.items() if v[0] == "s")
    lines += [f"- 冊：{len(at.volumes)}；章：{len(at.chapters)}（選讀 {sum(c['opt'] for c in at.chapters.values())}）",
              f"- 章層級邊：s {n_s}、b {n_b}、軟邊 {n_soft}；其中 {computed_s} 條 s 邊是從線代書的證明計算出來的，其餘是計畫值",
              ""]

    lines += ["## 最長硬依賴鏈（只計 s）", ""]
    chain = G.path_to(back, longest)
    lines += [f"**{len(chain)} 章**，終點 {at.label(longest)}：", "",
              " → ".join(chain), ""]
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
    tall = [c for c in at.order if height[c] > 20]
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

    desc = {c: len(G.descendants(sb, [c])) - 1 for c in at.chapters}
    s_red = G.transitive_reduction(s_only)
    lines += ["## 瓶頸：後代最多的章（s ∪ b）", "", "| 章 | 後代章數 | 約簡後 s 入度 | 後代涉及冊數 |", "|---|---:|---:|---:|"]
    for c in sorted(desc, key=lambda c: (-desc[c], at.order.index(c)))[:20]:
        vols = {at.chapters[d]["vol"] for d in G.descendants(sb, [c])} - {at.chapters[c]["vol"]}
        lines.append(f"| {at.label(c)} | {desc[c]} | {len(s_red[c])} | {len(vols)} |")
    lines.append("")

    lines += ["## 每冊的外部必讀量", "",
              "開始讀該冊（整冊）之前，冊外至少要讀的章數（s 祖先閉包，扣掉本冊）。", "",
              "| 冊 | 本冊章數 | 冊外必讀章數 | 直接上游冊（s） | 只借用的冊（b） |", "|---|---:|---:|---|---|"]
    vt = volume_edge_type(at)
    for v in at.volumes:
        mine = [c for c in at.order if at.chapters[c]["vol"] == v["id"]]
        req = G.ancestors(s_only, mine) - set(mine)
        up_s = sorted(b for (a, b), t in vt.items() if a == v["id"] and t == "s")
        up_b = sorted(b for (a, b), t in vt.items() if a == v["id"] and t == "b")
        lines.append(f"| {v['id']} {v['title']} | {len(mine)} | {len(req)} | {'、'.join(up_s) or '—'} | {'、'.join(up_b) or '—'} |")
    lines.append("")

    if at.fields:
        lines += ["## 領域覆蓋", "", "依 `registry/fields.yaml`。「入口必讀」＝支線候選的入口先修（hook）在 s 圖上的祖先閉包章數。", "",
                  "| 領域 | 科目數 | 已涵蓋 | 部分 | 支線候選 | 範圍外 |", "|---|---:|---:|---:|---:|---:|"]
        for group, subjects in at.fields.items():
            cnt = Counter(f["status"] for f in subjects)
            lines.append(f"| {group} | {len(subjects)} | " + " | ".join(str(cnt[k]) for k in FIELD_STATUS) + " |")
        lines += ["", "### 支線候選（未涵蓋，但先修已在地圖上）", "", "| 科目 | 入口先修 | 入口必讀章數 | 備註 |", "|---|---|---:|---|"]
        for group, subjects in at.fields.items():
            for f in subjects:
                if f["status"] == "branch":
                    hook = f.get("hook") or []
                    n = len(G.ancestors(s_only, hook)) if hook else 0
                    lines.append(f"| {f['name']}（{f['en']}） | {'、'.join(hook)} | {n} | {f.get('note', '')} |")
        lines.append("")

    lines += ["## 線代書計算邊的抽查", ""]
    la3 = [(k, v) for k, v in at.computed.items() if k[0].startswith("LA3") and k[1] == "LA2.10"]
    if la3:
        for (to, frm), (typ, h, s, _) in sorted(la3):
            w = at.witnesses.get(f"{to}<-{frm}") or []
            lines.append(f"- {to} ← {frm}：{typ}，硬引用 {h}、軟引用 {s}。" +
                         (" 硬引用來自 " + "；".join(f"`{a}` 引用 `{b}`" for a, b in w) if w else ""))
        lines += ["", "結論：LA3 對 LA2 第 10 章的硬依賴只來自上列引用。只要把這幾個結果改成 b（借用矩陣指數的性質）"
                  "或移到 LA2 第 10 章之後，LA3 就可以跳過第 10 章。", ""]
    (OUT / "report.md").write_text("\n".join(lines) + "\n")
    return lines


# ───────────────────────── diff ─────────────────────────

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
    for key, (ctyp, h, s, _) in sorted(at.computed.items()):
        if ctyp == "s" and not la_only(at, key[0]) and at.plan.get(key, (None,))[0] != "s":
            added.append(f"- {key[0]} ← {key[1]}：計算為 s（硬引用 {h}），計畫為 {at.plan.get(key, ('無',))[0]}")
    lines += ["## b 被當成 s 使用", ""] + (b_as_s or ["（無）"]) + [""]
    lines += ["## 計畫中有、證明沒用", ""] + (plan_unused or ["（無）"]) + [""]
    lines += ["## 證明有用、計畫中沒有（只列混合來源的章；純線代章本來就以計算值為準）", ""] + (added or ["（無）"]) + [""]

    stmt_ch = {n[0]: n[1] for n in at.statements["nodes"]}
    sb = at.preds(HARD)
    missing = []
    for user, used, typ in at.statements["edges"]:  # [user, used, type]
        if typ not in ("uses", "borrows"):
            continue
        user_ch, used_ch = stmt_ch[user], stmt_ch[used]
        if user_ch != used_ch and used_ch not in G.ancestors(sb, [user_ch]):
            missing.append(f"- `{user}`（{user_ch}）{typ} `{used}`（{used_ch}）：章層級沒有 {used_ch} ⇒ {user_ch} 的硬路徑")
    lines += ["## 陳述層的 uses／borrows 在章層級找不到路徑", ""] + (missing or ["（無）"]) + [""]
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


if __name__ == "__main__":
    main()
