"""Apply a bold-by-type classification to the linear algebra book (spec/02 粗體規則, spec/06 書稿改寫 2).

Every single-letter vector macro (\\a ... \\z) and the zero vector \\0 becomes \\cvec{x} (a coordinate vector, still
bold) or \\elem{x} (an element of an abstract space, not bold), as a classification JSON says:

    {"<file>": {"default": {"v": "elem", "x": "cvec", "0": "elem"},
                "exceptions": [{"line": 120, "letter": "x", "type": "elem", "occurrence": null}],
                "audit": [...]}}

A macro written as an argument without braces (x^\\v, \\hat\\v) gets braces, so the result still compiles.
Writes the rewritten files and prints, per file, how many macros became each type.

    python3 tools/bold_apply.py <chapter dir> <classification.json> [--dry-run]
"""
import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

MACRO = re.compile(r"\\([a-z0])(?![a-zA-Z])")
# The macro is an unbraced argument when it follows ^ or _, or a command that takes an argument.
ARG_COMMANDS = {"hat", "bar", "tilde", "widehat", "widetilde", "overline", "underline", "vec", "dot", "ddot",
                "check", "breve", "acute", "grave", "mathring", "boldsymbol", "mathbf", "bm", "sqrt", "frac",
                "operatorname", "overrightarrow", "mathit", "mathrm"}


def rewrite(text, spec):
    """(new text, Counter of types, list of problems)."""
    default = spec.get("default", {})
    exc = {}
    for e in spec.get("exceptions", []):
        exc[(e["line"], e["letter"], e.get("occurrence"))] = e["type"]
    counts, problems, out = Counter(), [], []
    for n, line in enumerate(text.split("\n"), 1):
        seen = Counter()
        pieces, last = [], 0
        for m in MACRO.finditer(line):
            # A backslash preceded by an odd number of backslashes is the second half of a line break:
            # in "\\\\v" the v is a plain letter; in "\\\\\\v" it is the macro after a line break.
            k = m.start()
            while k > 0 and line[k - 1] == "\\":
                k -= 1
            if (m.start() - k) % 2:
                continue
            letter = m.group(1)
            seen[letter] += 1
            kind = exc.get((n, letter, seen[letter])) or exc.get((n, letter, None)) or default.get(letter)
            if kind not in ("cvec", "elem"):
                problems.append(f"line {n}: no type for \\{letter}")
                continue
            new = f"\\{kind}{{{letter}}}"
            before = line[:m.start()].rstrip()
            cmd = re.search(r"\\([A-Za-z]+)$", before)
            if before.endswith(("^", "_")) or (cmd and cmd.group(1) in ARG_COMMANDS):
                new = "{" + new + "}"
            pieces += [line[last:m.start()], new]
            last = m.end()
            counts[kind] += 1
        out.append("".join(pieces) + line[last:])
    return "\n".join(out), counts, problems


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("chapter", type=Path)
    ap.add_argument("classification", type=Path)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    spec = json.loads(args.classification.read_text())
    files = sorted(args.chapter.glob("*.md"))
    missing = [f.name for f in files if f.name not in spec and MACRO.search(f.read_text())]
    if missing:
        sys.exit(f"no classification for {', '.join(missing)}")
    total, bad = Counter(), False
    for f in files:
        if f.name not in spec:
            continue
        new, counts, problems = rewrite(f.read_text(encoding="utf-8"), spec[f.name])
        total += counts
        print(f"{f.name}: cvec {counts['cvec']}, elem {counts['elem']}" + (f"; {len(problems)} problems" if problems else ""))
        for p in problems[:10]:
            print("   ", p)
        bad |= bool(problems)
        if not args.dry_run and not problems:
            f.write_text(new, encoding="utf-8")
    print(f"total: cvec {total['cvec']}, elem {total['elem']}" + (" (dry run)" if args.dry_run else ""))
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
