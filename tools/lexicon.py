"""English word handling for matching registered terms in manuscript text.

Terms and text are both reduced to lemmas, so "fields" matches "field" and "Cauchy sequences" matches "Cauchy
sequence". Matching ignores case, except for proper nouns: a term that contains a capitalised name ("Cauchy",
"Hermitian", "Jordan") matches only that capitalisation, so "jordan" in running text does not count.
"""
import re

IRREGULAR = {
    "matrices": "matrix", "vertices": "vertex", "indices": "index", "bases": "basis", "axes": "axis",
    "radii": "radius", "polyhedra": "polyhedron", "criteria": "criterion", "spectra": "spectrum",
    "maxima": "maximum", "minima": "minimum", "extrema": "extremum", "infima": "infimum", "suprema": "supremum",
    "foci": "focus", "loci": "locus", "lemmata": "lemma", "simplices": "simplex", "analyses": "analysis",
    "hypotheses": "hypothesis", "parentheses": "parenthesis", "ellipses": "ellipse", "formulae": "formula",
    "moduli": "modulus", "tori": "torus", "automata": "automaton", "annuli": "annulus", "homotopies": "homotopy",
}
UNCHANGED = {"series", "species", "basis", "analysis", "axis", "thesis", "hypothesis", "parenthesis", "radius",
             "modulus", "locus", "focus", "torus", "annulus", "calculus", "corpus", "lemma", "always", "less",
             "was", "has", "is", "its", "this", "thus", "plus", "minus", "bias", "gauss", "lens", "news"}
WORD = re.compile(r"[A-Za-z][A-Za-z'’-]*")
MATH = re.compile(r'<span class="math[^"]*">.*?</span>|\\\(.*?\\\)|\\\[.*?\\\]|\$[^$]*\$', re.S)


def lemma(word):
    """The singular form of a (lowercase) English word; anything else is returned unchanged."""
    w = re.sub(r"['’]s$", "", word)
    if w in IRREGULAR:
        return IRREGULAR[w]
    if len(w) <= 3 or w in UNCHANGED or w.endswith(("ss", "us", "is", "ics")):
        return w
    if w.endswith("ies") and len(w) > 4:
        return w[:-3] + "y"
    if w.endswith(("sses", "xes", "ches", "shes", "zes")):
        return w[:-2]
    if w.endswith("oes"):
        return w[:-2]
    if w.endswith("s"):
        return w[:-1]
    return w


def is_proper(word):
    """A capitalised name, as written in a term: 'Cauchy', 'Hermitian'; not 'Field' at the start of a sentence."""
    return word[:1].isupper() and not word.isupper() and word[1:].islower()


REF = re.compile(r"@?\b(?:def|thm|prp|cor|lem|exm|exr|eq|ax|cnj|rmk|sec|fig|tbl)-[\w-]+")
BLOCK = re.compile(r"</?(?:p|li|ol|ul|div|h\d|br|td|th|tr|dt|dd|blockquote)\b[^>]*>", re.I)


def plain(text):
    """Running text of an HTML or Markdown fragment: mathematics and label references removed, and a sentence break
    ('.') wherever a block element starts or ends, so a list item's first word counts as sentence-initial."""
    text = BLOCK.sub(" . ", MATH.sub(" ", text))
    return REF.sub(" ", re.sub(r"<[^>]+>", " ", text))


def tokens(text):
    """Plain words of an HTML or Markdown fragment."""
    return WORD.findall(plain(text))


def norm_word(word):
    """Lemma of one word; a proper noun is a name and is never singularised ('Givens', 'Gauss')."""
    if is_proper(word):
        return re.sub(r"['’]s$", "", word)
    return lemma(word.lower())


def keys(words):
    """(case-insensitive key, cased key) for a word sequence: lemmas joined by spaces."""
    cased = [norm_word(w) for w in words]
    return " ".join(w.lower() for w in cased), " ".join(cased)


def proper_nouns(texts):
    """Capitalised words that are names: written capitalised mid-sentence more often than in lowercase."""
    from collections import Counter
    low, mid = Counter(), Counter()
    for text in texts:
        for m in re.finditer(r"(?<![.!?:]\s)(?<![.!?:]\s\s)(?<!^)\b([A-Za-z][a-z]+)\b", plain(text).strip()):
            w = m.group(1)
            (mid if w[0].isupper() else low)[w if w[0].isupper() else w] += 1
    return {w for w, n in mid.items() if n > low[w.lower()]}


class Matcher:
    """Longest-match lookup of registered terms in text. terms: iterable of (key, payload) where key is the English
    term (or one of its forms) as written; a key with a proper noun matches case-sensitively."""

    def __init__(self, terms):
        self.plain, self.cased = {}, {}
        for text, payload in terms:
            words = text.split()
            low, cased = keys(words)
            if any(is_proper(w) for w in words):
                self.cased.setdefault(cased, payload)
            else:
                self.plain.setdefault(low, payload)
        self.longest = max((len(k.split()) for k in [*self.plain, *self.cased]), default=0)

    def find(self, text):
        """Payloads of the terms occurring in text, longest match first, each occurrence counted once."""
        words = tokens(text)
        cased = [norm_word(w) for w in words]  # names as written, for terms with a proper noun
        low = [lemma(w.lower()) for w in words]  # everything else: a capitalised first word is still a common word
        out, i = [], 0
        while i < len(words):
            for n in range(min(self.longest, len(words) - i), 0, -1):
                hit = self.cased.get(" ".join(cased[i:i + n])) or self.plain.get(" ".join(low[i:i + n]))
                if hit is not None:
                    out.append(hit)
                    i += n
                    break
            else:
                i += 1
        return out
