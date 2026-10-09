"""Count English usage variants in the manuscripts and check them against the house style.

Reads the prose of every chapter in BOOKS (Markdown under src/, with mathematics, code, TikZ, labels and references
removed) and counts each variant of each group in registry/usage.yaml. Writes generated/usage.md: a frequency table
per group, the chosen form, and for confirmed groups every occurrence of an avoided form (file:line), which is the
lint the engine will run on every build (spec/05).

    python3 tools/usage_report.py
"""
import re
from collections import Counter, defaultdict
from pathlib import Path

import yaml

from sync_constraints import tidy

ROOT = Path(__file__).resolve().parent.parent
USAGE = ROOT / "registry" / "usage.yaml"
OUT = ROOT / "generated" / "usage.md"
BOOKS = {"la": "linear-algebra", "ab": "analysis-book"}

STRIP = [
    re.compile(r"^---\n.*?\n---\n", re.S),                     # front matter
    re.compile(r"```.*?```", re.S),                             # code
    re.compile(r"<!--.*?-->", re.S),                            # comments
    re.compile(r"\\begin\{(tikzpicture|align\*?|equation\*?|gather\*?)\}.*?\\end\{\1\}", re.S),
    re.compile(r"\$\$.*?\$\$|\\\[.*?\\\]|\\\(.*?\\\)|\$[^$\n]*\$", re.S),  # mathematics
    re.compile(r"\{[#.][^}]*\}"),                               # attributes and labels
    re.compile(r"@?\b(?:def|thm|prp|cor|lem|exm|exr|eq|ax|cnj|sec|fig|tbl)-[\w-]+"),  # references
    re.compile(r"\]\([^)]*\)"),                                 # link targets
]


def prose(text):
    """The running text of a Markdown chapter, line structure kept (stripped spans become blanks on their lines)."""
    for pat in STRIP:
        text = pat.sub(lambda m: re.sub(r"[^\n]", " ", m.group(0)), text)
    return text


def files(book):
    return sorted((ROOT.parent / BOOKS[book] / "src").glob("ch*/*.md"))


def pattern(form):
    """A variant as a case-insensitive whole-word regex; '*' is a word stem wildcard, spaces match any whitespace."""
    body = r"\s+".join(re.escape(w).replace(r"\*", r"\w*") for w in form.split())
    return re.compile(rf"(?<![\w-]){body}(?![\w-])", re.I)


def scan(groups):
    """{(group id, form): {book: count}}, and {(group id, form): [(path, line)]} for every occurrence."""
    counts, where = defaultdict(Counter), defaultdict(list)
    pats = {(g["id"], f): pattern(f) for g in groups for f in [*g["use"], *g.get("avoid", [])]}
    for book in BOOKS:
        for path in files(book):
            lines = prose(path.read_text(encoding="utf-8")).split("\n")
            for n, line in enumerate(lines, 1):
                for key, pat in pats.items():
                    hits = len(pat.findall(line))
                    if hits:
                        counts[key][book] += hits
                        where[key].append((path.relative_to(ROOT.parent), n))
    return counts, where


def main():
    groups = yaml.safe_load(USAGE.read_text()) or []
    counts, where = scan(groups)
    lines = ["# 英文用詞變體（由 `tools/usage_report.py` 從兩本書稿統計，勿手改）", "",
             "約定在 `registry/usage.yaml`。每組選一個（use），其餘列為 avoid；status 為 proposed 的組待作者確認，"
             "confirmed 的組列出書稿裡每一處 avoid 寫法（將來由引擎在 build 時檢查，spec/05）。"
             "統計只看散文：數學式、程式碼、TikZ、label 與參照都已去掉。", ""]
    for g in groups:
        lines += [f"## {g['title']}（`{g['id']}`，{g['status']}）", "", "| 寫法 | 線代書 | analysis-book | 合計 | |", "|---|---:|---:|---:|---|"]
        for f in [*g["use"], *g.get("avoid", [])]:
            c = counts[(g["id"], f)]
            mark = "**use**" if f in g["use"] else "avoid"
            lines.append(f"| {f} | {c['la']} | {c['ab']} | {c['la'] + c['ab']} | {mark} |")
        lines += ["", tidy(g["why"]), ""]
        if g["status"] == "confirmed":
            hits = [f"- `{p}:{n}`：{f}" for f in g.get("avoid", []) for p, n in where[(g["id"], f)]]
            lines += (["avoid 寫法出現處：", ""] + hits + [""]) if hits else ["書稿裡沒有 avoid 寫法。", ""]
    OUT.write_text("\n".join(lines) + "\n")
    print(f"{len(groups)} groups -> {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
