"""Import the computed citation graph of the linear-algebra book into atlas chapters.

Reads linear-algebra/_build/crossref_labels.json (written by its build) and maps
each section to an atlas chapter. The edge policy is the book's own
(tools/reading_path.py): a citation is hard when it is made from a proof-like
block of a non-optional result; everything else is soft.

Writes registry/computed/la-edges.yaml:
  edges: [[to, from, s|b|see, hard_count, soft_count], ...]
  (b only for citations that registry/moves.yaml reclassifies as borrows; its softened_for turns citations soft)
  witnesses: {"to<-from": [[citing_label, cited_label], ...]}  (hard, cross-volume, first few)
"""
import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_LA = ROOT.parent / "linear-algebra"
OUT = ROOT / "registry" / "computed" / "la-edges.yaml"
MOVES = ROOT / "registry" / "moves.yaml"

HARD_KINDS = {"proof", "proofofclaim", "claim", "idea"}
SECTION = re.compile(r"^(ch\d+[a-z]*)[^/]*/(\d+|index)")

CH00 = {"01": "F1.5", "02": "F1.5", "03": "F2.1", "04": "F2.1", "05": "F2.2",
        "06": "F3.6", "07": "F3.7", "08": "F3.8", "09": "LA1.0", "10": "AL1.1"}
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
              + "# overrides: [label, move|softened_for|borrowed_by, chapter, citations it changed]\n")
    body = yaml.safe_dump({"edges": edges, "witnesses": witnesses, "overrides": overrides},
                          allow_unicode=True, sort_keys=False, default_flow_style=None, width=200)
    args.out.write_text(header + body)
    print(f"{len(edges)} chapter edges ({sum(e[2] == 's' for e in edges)} hard) -> {args.out.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
