"""Import the computed citation graph of the linear-algebra book into atlas chapters.

Reads linear-algebra/_build/crossref_labels.json (written by its build) and maps
each section to an atlas chapter. The edge policy is the book's own
(tools/reading_path.py): a citation is hard when it is made from a proof-like
block of a non-optional result; everything else is soft.

Writes registry/computed/la-edges.yaml:
  edges: [[to, from, s|b|see, hard_count, soft_count], ...]
  (b only for citations that registry/moves.yaml reclassifies as borrows; its softened_for turns citations soft)
  witnesses: {"to<-from": [[citing_label, cited_label], ...]}  (hard, cross-volume, first few)
  vocab: [[to, from, all|stmt|term, count], ...]  (definitions a statement reader needs; see vocabulary(), term_edges())
"""
import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

import yaml

from lexicon import Matcher

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_LA = ROOT / "books" / "linear-algebra"
OUT = ROOT / "registry" / "computed" / "la-edges.yaml"
MOVES = ROOT / "registry" / "moves.yaml"

HARD_KINDS = {"proof", "proofofclaim", "claim", "idea"}
STATEMENT_KINDS = {"definition", "theorem", "proposition", "corollary", "lemma"}
STATEMENT_PREFIXES = {"def", "thm", "prp", "cor", "lem"}
SECTION = re.compile(r"^(ch\d+[a-z]*)[^/]*/(\d+|index)")

CH00 = {"01": "F1.5", "02": "F1.5", "03": "F2.1", "04": "F2.1", "05": "F2.5",
        "06": "F4.1", "07": "F5.2", "08": "F5.4", "09": "LA1.0", "10": "F5.3"}
CHAPTER = {**{f"ch{n:02d}": f"LA1.{n}" for n in range(1, 6)},
           **{f"ch{n:02d}": f"LA2.{n}" for n in range(6, 11)},
           **{f"ch{n:02d}": f"LA3.{n}" for n in range(11, 14)},
           **{f"ch{n:02d}": f"LA4.{n}" for n in range(14, 16)},
           **{f"ch{n:02d}": f"MA.{n}" for n in range(16, 22)},
           "ch22": "GEO.22", "ch23": "AL4.8", "ch24": "NLA.24"}


def atlas_chapter(path):
    m = SECTION.match(path or "")
    if not m:
        return None
    ch, sec = m.groups()
    if ch == "ch00":
        return CH00.get(sec)
    return CHAPTER.get(ch)  # ch24a (notation) and anything unknown -> None


def load_moves(path=MOVES):
    """label -> target chapter, for planned relocations in this book (registry/moves.yaml)."""
    if not path.exists():
        return {}, []
    rows = [m for m in (yaml.safe_load(path.read_text()) or []) if m.get("book") == "la"]
    return {m["label"]: m for m in rows}, rows


def compute(labels, moves=None, effects=None):
    """effects, if given, receives {(label, kind, chapter): citations changed} for each override in moves."""
    where = {k: atlas_chapter(v.get("file")) for k, v in labels.items()}
    effects = {} if effects is None else effects
    for label, m in (moves or {}).items():
        for kind in ("softened_for", "borrowed_by"):
            for ch in m.get(kind, ()):
                effects.setdefault((label, kind, ch), 0)
    moves = moves or {}
    for label, m in moves.items():
        if label in where:
            where[label] = m["to"]
    hard, borrow, soft = defaultdict(int), defaultdict(int), defaultdict(int)
    witnesses = defaultdict(list)
    for name, rec in sorted(labels.items()):
        dst = where.get(name)
        if dst is None:
            continue
        kinds_by = rec.get("uses_kinds") or {}
        for cited in rec.get("uses") or ():
            src = where.get(cited)
            if src is None or src == dst:
                continue
            kinds = set(kinds_by.get(cited) or ())
            is_hard = not rec.get("optional") and bool(kinds & HARD_KINDS)
            mv = moves.get(cited) or {}
            if is_hard and dst in mv.get("softened_for", ()):  # the planned rewrite cites it only as a pointer
                is_hard = False
                effects[(cited, "softened_for", dst)] += 1
            is_borrow = is_hard and dst in mv.get("borrowed_by", ())
            if is_borrow:
                effects[(cited, "borrowed_by", dst)] += 1
            (borrow if is_borrow else hard if is_hard else soft)[(dst, src)] += 1
            if is_hard and dst.split(".")[0] != src.split(".")[0] and len(witnesses[(dst, src)]) < 3:
                witnesses[(dst, src)].append([name, cited])
    edges = []
    for key in sorted(set(hard) | set(borrow) | set(soft)):
        h, b, s = hard.get(key, 0), borrow.get(key, 0), soft.get(key, 0)
        edges.append([key[0], key[1], "s" if h else "b" if b else "see", h + b, s])
    return edges, {f"{a}<-{b}": w for (a, b), w in sorted(witnesses.items())}


def vocabulary(labels, moves=None):
    """Chapter-level vocabulary edges for the statement reader (spec/03 §6.2): [to, from, all|stmt, citations].

    all: a non-optional result in `to` cites, from a statement or a proof, a definition in `from`, or a result
         whose statement cites a definition in `from` (the reader borrows the statement and needs its words).
    stmt: a definition or result in `to` cites a definition in `from` from its statement (not its proof); this is
          what a statement reader of `to` needs, since they read its definitions and statements but not its proofs.
    Only citations the book makes explicitly are seen, so closures over these edges are lower bounds.
    """
    where = {k: atlas_chapter(v.get("file")) for k, v in labels.items()}
    for label, m in (moves or {}).items():
        if label in where:
            where[label] = m["to"]

    def statement_defs(label):
        rec = labels.get(label) or {}
        kinds = rec.get("uses_kinds") or {}
        return [c for c in rec.get("uses") or () if c.startswith("def-") and set(kinds.get(c) or ()) & STATEMENT_KINDS]

    count = defaultdict(int)
    for name, rec in labels.items():
        dst = where.get(name)
        if dst is None or rec.get("optional"):
            continue
        kinds_by = rec.get("uses_kinds") or {}
        for cited in rec.get("uses") or ():
            kinds = set(kinds_by.get(cited) or ())
            if (name.split("-")[0] in STATEMENT_PREFIXES and cited.startswith("def-") and kinds & STATEMENT_KINDS
                    and where.get(cited) not in (None, dst)):
                count[(dst, where[cited], "stmt")] += 1
            if not kinds & (HARD_KINDS | STATEMENT_KINDS):
                continue
            for d in [cited] if cited.startswith("def-") else statement_defs(cited):
                if where.get(d) not in (None, dst):
                    count[(dst, where[d], "all")] += 1
    return [[to, frm, kind, n] for (to, frm, kind), n in sorted(count.items())]


TERMS = ROOT / "registry" / "terms.yaml"


def term_edges(labels, terms, moves=None):
    """[to, from, term, count, [term ids, most used first]]: a definition or statement in `to` uses a registered term whose canonical definition is
    in `from`, without citing it. An estimate of the vocabulary the book leaves implicit (spec/03 §6.2); common words
    give false positives, so closures over these edges overshoot. Terms marked meta in terms.yaml are not matched."""
    where = {k: atlas_chapter(v.get("file")) for k, v in labels.items()}
    for label, m in (moves or {}).items():
        if label in where:
            where[label] = m["to"]
    # meta terms are the metalanguage of reading mathematics (F1's logic), not vocabulary to go back for
    matcher = Matcher((f, t) for t in terms if not t.get("meta") for f in [t["en"], *(t.get("forms") or [])])
    count = defaultdict(int)
    which = defaultdict(lambda: defaultdict(int))  # (to, from) -> term id -> statements using it
    for name, rec in labels.items():
        dst = where.get(name)
        if dst is None or rec.get("optional") or name.split("-")[0] not in STATEMENT_PREFIXES:
            continue
        cited = set(rec.get("uses") or ())
        for t in {t["id"]: t for t in matcher.find(rec.get("html_content") or "")}.values():
            if t["ch"] != dst and t["def"] not in cited:
                count[(dst, t["ch"], "term")] += 1
                which[(dst, t["ch"])][t["id"]] += 1
    return [[to, frm, kind, n, [w for w, _ in sorted(which[(to, frm)].items(), key=lambda kv: (-kv[1], kv[0]))]]
            for (to, frm, kind), n in sorted(count.items())]


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--la", type=Path, default=DEFAULT_LA, help="linear-algebra repo")
    ap.add_argument("--out", type=Path, default=OUT)
    args = ap.parse_args(argv)
    src = args.la / "_build" / "crossref_labels.json"
    if not src.exists():
        sys.exit(f"{src} not found; run `./build.py html` in {args.la} first")
    labels = json.loads(src.read_text())["crossref_labels"]
    moves, rows = load_moves()
    overrides = []  # [label, kind, chapter, citations affected]; 0 means the book has caught up (atlas.py check)
    for m in rows:
        here = atlas_chapter((labels.get(m["label"]) or {}).get("file"))
        if here is None:
            print(f"warning: moves.yaml: {m['label']} not found in the book")
        elif here != m["from"]:
            print(f"warning: moves.yaml: {m['label']} is now in {here}, not {m['from']}; drop the row once the move is done")
        overrides.append([m["label"], "move", m["to"], int(here == m["from"])])
    effects = {}
    edges, witnesses = compute(labels, moves, effects)
    overrides += [[label, kind, ch, n] for (label, kind, ch), n in sorted(effects.items())]
    args.out.parent.mkdir(parents=True, exist_ok=True)
    header = (f"# Generated by tools/import_la.py from {src.relative_to(args.la.parent)}; do not edit.\n"
              + (f"# Applied planned moves from registry/moves.yaml: {', '.join(sorted(moves))}\n" if moves else "")
              + "# edges: [to, from, s|b|see, hard citations, soft citations]\n"
              + "# overrides: [label, move|softened_for|borrowed_by, chapter, citations it changed]\n"
              + "# vocab: [to, from, all|stmt|term, count(, term ids for term edges)]: definitions the statement reader needs (see vocabulary())\n")
    vocab = vocabulary(labels, moves)
    if TERMS.exists():
        vocab += term_edges(labels, yaml.safe_load(TERMS.read_text()) or [], moves)
    body = yaml.safe_dump({"edges": edges, "witnesses": witnesses, "overrides": overrides, "vocab": vocab},
                          allow_unicode=True, sort_keys=False, default_flow_style=None, width=200)
    args.out.write_text(header + body)
    print(f"{len(edges)} chapter edges ({sum(e[2] == 's' for e in edges)} hard) -> {args.out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
