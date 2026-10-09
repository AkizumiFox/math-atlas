"""Render text containing semantic macros (registry/notation.yaml) to plain Unicode.

Titles and other reader-facing names write their mathematics as \\( ... \\) with semantic macros, e.g.
'The Derivative in \\(\\nR^n\\)'. Plain-text outputs (Mermaid labels, hover cards, reports) need Unicode: macros are
expanded through their `unicode` template and ^ / _ become superscript and subscript characters.
"""
import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
TABLE = ROOT / "registry" / "notation.yaml"
MATH = re.compile(r"\\\((.*?)\\\)")
SUP = dict(zip("0123456789+-=()nipdkx", "⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾ⁿⁱᵖᵈᵏˣ"))
SUB = dict(zip("0123456789+-=()aeoxnkmijp", "₀₁₂₃₄₅₆₇₈₉₊₋₌₍₎ₐₑₒₓₙₖₘᵢⱼₚ"))
# Unicode lacks most super/subscript letters: a script with no glyph falls back to ^( ) or _( ).
GLYPH = re.compile(r"[ℝℤℚℂℕℓ⁰¹²³⁴⁵⁶⁷⁸⁹ⁿᵖᵈ₀₁₂₃₄₅₆₇₈₉ₙₚ]")


def load(path=TABLE):
    """{macro name without backslash: (number of arguments, unicode template)}."""
    out = {}
    for row in (yaml.safe_load(path.read_text()) or []) if path.exists() else []:
        m = re.match(r"\\([A-Za-z]+)", row["macro"])
        out[m.group(1)] = (len(set(re.findall(r"#\d", row["macro"]))), row["unicode"])
    return out


def _script(body, table, mark):
    if all(c in table for c in body):
        return "".join(table[c] for c in body)
    return f"{mark}({body})" if len(body) > 1 else mark + body


def _group(s, i):
    """(content, end) of the braced group or single character at s[i]."""
    if s[i] == "{":
        depth, j = 0, i
        while True:
            depth += {"{": 1, "}": -1}.get(s[j], 0)
            if depth == 0:
                return s[i + 1:j], j + 1
            j += 1
    return s[i], i + 1


def math_to_unicode(expr, macros):
    """Unicode for one \\( ... \\) expression. Unknown macros raise KeyError."""
    out, i = "", 0
    while i < len(expr):
        c = expr[i]
        if c == "\\":
            m = re.match(r"\\([A-Za-z]+)|\\(.)", expr[i:])
            name = m.group(1)
            i += len(m.group(0))
            if name is None:
                out += m.group(2)
                continue
            if name == "infty":
                out += "∞"
                continue
            n, template = macros[name]
            args = []
            for _ in range(n):
                while expr[i] == " ":
                    i += 1
                arg, i = _group(expr, i)
                args.append(math_to_unicode(arg, macros))
            text = template
            for k, a in enumerate(args, 1):
                text = text.replace(f"#{k}", a)
            out += math_to_unicode(text, macros) if "\\" in text or "^" in text or "_" in text else text
        elif c in "^_":
            body, i = _group(expr, i + 1)
            out += _script(math_to_unicode(body, macros), SUP if c == "^" else SUB, c)
        elif c in "{}":
            i += 1
        else:
            out += c
            i += 1
    return out


def render(text, macros=None):
    """Text with every \\( ... \\) expression rendered to Unicode."""
    macros = load() if macros is None else macros
    return MATH.sub(lambda m: math_to_unicode(m.group(1), macros), text)


def problems(text, macros=None):
    """Raw math glyphs outside \\( ... \\), and macros the notation table does not define."""
    macros = load() if macros is None else macros
    out = []
    outside = MATH.sub(" ", text)
    if GLYPH.search(outside):
        out.append(f"raw mathematical glyph '{GLYPH.search(outside).group(0)}': write it as a semantic macro in \\( \\)")
    for m in MATH.finditer(text):
        for name in re.findall(r"\\([A-Za-z]+)", m.group(1)):
            if name not in macros and name != "infty":
                out.append(f"\\{name} is not in registry/notation.yaml")
    return out
