"""Apply the mechanical English usage migration (registry/usage.yaml) to a manuscript.

Only the confirmed groups without `review` are rewritten, and only in running text: the prose that
usage_report.py counts, plus the words inside \\text{...} in mathematics, which readers see too. Labels,
references, code, link targets and the rest of the mathematics are never touched, so no published anchor
of a label changes. A heading whose text changes would change its automatic anchor, so it gets the old
anchor written out ({#old-id}); every such id is checked against the built site when one is given.

    python3 tools/usage_apply.py ../linear-algebra-conventions [--site ../linear-algebra/_build/html] [--dry-run]
"""
import argparse
import re
import sys
from pathlib import Path

import usage_report as u

TEXT = re.compile(r"\\(?:text|textup|textrm|mbox)\{([^{}]*)\}")
MATH = re.compile(r"\$\$.*?\$\$|\\\[.*?\\\]|\\\(.*?\\\)|\$[^$\n]*\$|"
                  r"\\begin\{(tikzpicture|align\*?|equation\*?|gather\*?)\}.*?\\end\{\1\}", re.S)

# avoided form -> replacement, for the mechanical groups. Case is kept for the first letter.
RULES = [
    (re.compile(r"(?<![\w-])([Nn])on-([a-z])"), r"\1on\2"),
    (re.compile(r"\b(is|are|be|not) one-to-one\b"), r"\1 injective"),
    (re.compile(r"\bone-one\b"), "injective"),
    (re.compile(r"\bone-to-one correspondence(s?)\b"), r"bijection\1"),
    (re.compile(r"\blinear transformation(s?)\b"), r"linear map\1"),
    (re.compile(r"\bnullspace(s?)\b"), r"null space\1"),
    (re.compile(r"\b([Cc])o-domain"), r"\1odomain"),
    (re.compile(r"\b([Pp])re-image"), r"\1reimage"),
    (re.compile(r"\b([Cc])ounter-example"), r"\1ounterexample"),
    (re.compile(r"\b([Ff]inite|[Ii]nfinite) dimensional\b"), r"\1-dimensional"),
    (re.compile(r"\b(positive|negative)(?:-| semi-|-semi)(definite|semidefinite)\b"),
     lambda m: f"{m.group(1)} {'semidefinite' if 'semi' in m.group(0) else m.group(2)}"),
    (re.compile(r"\b([Ss])elf ?adjoint\b"), r"\1elf-adjoint"),
    (re.compile(r"\b(is|are|be|been) well-defined\b"), r"\1 well defined"),
    (re.compile(r"\b(a|an|the) well defined\b"), r"\1 well-defined"),
    (re.compile(r"\bformulae\b"), "formulas"),
    (re.compile(r"\blemmata\b"), "lemmas"),
    (re.compile(r"\b([Nn])eighbour"), r"\1eighbor"),
    (re.compile(r"\b([Bb])ehaviour"), r"\1ehavior"),
    (re.compile(r"\b([Cc])entre(s|d)?\b"), r"\1enter\2"),
    (re.compile(r"\b([Ff])ibre"), r"\1iber"),
    (re.compile(r"\b([Cc])olour"), r"\1olor"),
    (re.compile(r"\b([Ff])avour"), r"\1avor"),
    (re.compile(r"\b([Aa])nalys(e|ed|ing)\b"), r"\1nalyz\2"),
    (re.compile(r"\b(label|model|cancel)l(ed|ing)\b"), r"\1\2"),
]


def protected(text):
    """A mask: True where the text must not change (everything usage_report.prose blanks out, except the
    words inside \\text{} in mathematics)."""
    mask = [False] * len(text)
    for pat in u.STRIP:
        for m in pat.finditer(text):
            mask[m.start():m.end()] = [True] * (m.end() - m.start())
    for m in MATH.finditer(text):
        for t in TEXT.finditer(m.group(0)):
            a, b = m.start() + t.start(1), m.start() + t.end(1)
            mask[a:b] = [False] * (b - a)
    return mask


def pandoc_id(heading):
    """Pandoc's automatic identifier for a heading's text."""
    t = re.sub(r"\\\(.*?\\\)|\$[^$]*\$", "", heading)
    t = re.sub(r"[*_`]", "", t).lower()
    t = re.sub(r"[^\w\s.-]", "", t)
    t = re.sub(r"\s+", "-", t.strip())
    return re.sub(r"^[^a-z]+", "", t) or "section"


def kept_spans(text, groups):
    spans = []
    for g in groups:
        for k in g.get("keep") or ():
            spans += [(m.start(), m.end()) for m in u.pattern(k).finditer(text)]
    return spans


def rewrite(text, groups):
    """(new text, number of replacements, [(old heading id, new heading line)])."""
    mask = protected(text)
    keep = kept_spans(text, groups)
    edits = []
    for pat, rep in RULES:
        for m in pat.finditer(text):
            a, b = m.span()
            if any(mask[a:b]) or any(s < b and a < e for s, e in keep):
                continue
            edits.append((a, b, m.expand(rep) if isinstance(rep, str) else rep(m)))
    edits.sort()
    out, last, n = [], 0, 0
    for a, b, new in edits:
        if a < last:
            continue  # two rules on the same span: the first wins
        out += [text[last:a], new]
        last, n = b, n + 1
    new_text = "".join(out) + text[last:]
    anchors = []
    old_lines, new_lines = text.split("\n"), new_text.split("\n")
    for i, (o, nl) in enumerate(zip(old_lines, new_lines)):
        if o != nl and re.match(r"#{1,6} ", o) and "{#" not in o:
            old_id = pandoc_id(o.lstrip("#").strip())
            new_lines[i] = f"{nl} {{#{old_id}}}"
            anchors.append((old_id, new_lines[i]))
    return "\n".join(new_lines), n, anchors


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("book", type=Path, help="manuscript repository (its src/ is rewritten)")
    ap.add_argument("--site", type=Path, help="built site of the published book, to check the kept anchors")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    groups = [g for g in u.yaml.safe_load(u.USAGE.read_text())
              if g.get("status") == "confirmed" and not g.get("review")]
    total, missing = 0, []
    for path in sorted((args.book / "src").rglob("*.md")):
        text = path.read_text(encoding="utf-8")
        new, n, anchors = rewrite(text, groups)
        if not n:
            continue
        total += n
        for old_id, line in anchors:
            print(f"{path.relative_to(args.book)}: kept anchor #{old_id}")
            if args.site:
                page = args.site / path.relative_to(args.book / "src").with_suffix(".html")
                if not page.exists() or f'id="{old_id}"' not in page.read_text(encoding="utf-8"):
                    missing.append(f"{path.relative_to(args.book)}: #{old_id} is not on {page}")
        if not args.dry_run:
            path.write_text(new, encoding="utf-8")
    print(f"{total} replacements" + (" (dry run)" if args.dry_run else ""))
    if missing:
        print("\n".join(missing))
        sys.exit(1)


if __name__ == "__main__":
    main()
