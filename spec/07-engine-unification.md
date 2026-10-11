# 07 統一引擎與合併網站（計畫，2026-10-11）

由只讀調查產生的英文計畫原文如下；決策摘要：book-template 改名 book-engine，各書以 git submodule 掛在 engine/，`BOOK_ENGINE` 環境變數可指向工作副本；書專屬檢查改由 config 的 checks 清單掛入；合併網站由 `./build.py library` 依 math-atlas 的 manifest 組成。

# One engine, one site: unification plan

Read-only survey, 2026-10-11. Repos examined (HEADs):

| Repo / worktree | Branch | HEAD | Remote |
|---|---|---|---|
| book-template | main | 2efafef 2026-09-25 | github AkizumiFox/book-template (public) |
| linear-algebra | main | 822ab11 2026-09-25 | github AkizumiFox/linear-algebra (public), published at linear-algebra.akizumifox.com |
| linear-algebra-conventions | conventions-rewrite | 6f0cddb 2026-10-10 | same repo (worktree) |
| linear-algebra-moved-ids | moved-ids | f79e54b 2026-10-10 | same repo (worktree), **one unmerged engine commit** |
| analysis-book | master | 489e99d 2026-10-10 | **no remote** (local only) |
| analysis-book-conventions | conventions | 1e6fee9 2026-10-11 | same repo (worktree) |
| regression | main | 88a7771 2026-09-25 | github AkizumiFox/regression (public) |
| math-atlas | master (+ gh-pages preview 7e06676) | 336f860 | github AkizumiFox/math-atlas (public) |

spec/05-engine-requirements.md already decides: the engine becomes its own `book-engine`
repo, books depend on it by version, math-atlas does not hold the engine. This plan
implements that decision.

---

## 1. Drift inventory

Engine as it stands in book-template: 89 files, ~16.9k lines (build/ 17 modules, filters/
Lua, templates/, tools/ 3 checkers, latex/ 9 files, widgets/, tests/ 12 test modules +
fixture-book). `build.py` (the shim) and `widgets/` are **identical in all five copies**.

### 1a. Summary numbers (vs book-template)

| Copy | Shared files that differ | Changed lines in shared files (excl. macros.tex) | macros.tex diff | Book-only tracked files in engine dirs |
|---|---|---|---|---|
| linear-algebra (main) | 12 | 98 | 408 (book content) | 0 (+5 untracked LaTeX junk in templates/latex/) |
| linear-algebra-conventions | 13 | 114 | 413 | 3 (check_macros.py/.cjs, test_check_macros.py; 532 lines) |
| analysis-book-conventions | 21 | 944 | 28 | 29 (11 tools, 13 tests, fixture-companion, build/external.py, latex/fitch-book.sty; ~7.2k lines) |
| regression | 20 | 764 | 305 | 4 (check_numbers.py, check_prose_numbers.py, numbers.json, a woff2 font) |

Lineage (from commit messages and identical commit titles across repos): the author
ports changes by hand, commit by commit ("Stop publishing a built page whose source is
gone" exists in book-template, regression and LA on 09-25). book-template stopped
receiving changes on 2026-09-25. analysis-book was started on 09-27 "from book-template,
with regression's forward-proof gate and LaTeX text-safe shorthands", so **analysis-book-
conventions is the most advanced copy and already contains the regression improvements**
(regression vs analysis: theorem-envs.sty, chapter-style.sty, extras.py identical;
latex-template.sty 2 lines apart).

### 1b. Per directory

Who is ahead = latest engine-relevant commit; "upstream" = drift to merge into the engine;
"book" = genuine book customization that stays in the book (as override or plugin).

**build.py** - identical everywhere. Will be replaced by a thin shim (see 2).

**build/** (Python package)

| File | Differences | Verdict |
|---|---|---|
| book.py | analysis: `site_url` / `site_path` properties (`site-url` config: book under a sub-path) | **upstream** (needed for the combined site) |
| html.py, pandoc.py, pdf.py | analysis: canonical/page URLs from `site_url`; external-books metadata; fingerprint includes external refs | **upstream** |
| external.py (analysis only, 210 lines) | cross-book refs `@la:label`, `publish_labels` (labels.json at site root), URL or path registries, cache | **upstream** (spec/05 item 2) |
| manifest.py | analysis: external refs kept apart in `external_uses`; `axiom` is a statement type; sitemap/robots/404 under a sub-path. regression: docstring trims + `Counter` import only | **upstream analysis**; regression diff is noise |
| check.py | analysis (133 lines): `_tool(name)` loader, forward-deps gate (also in regression), external-ref checking, `config/known-unresolved.json` baseline, and **hard-wired** calls to check_structure / check_fitch / check_numbers gated on `authoring/STYLE.md` and `verify/`. LA-conventions: hard-wired `check_macros`. LA moved-ids: +29 lines `moved-ids` check | `_tool`, forward gate, external, known-unresolved, moved-ids: **upstream**. The book-specific calls: **replace by a plugin hook** (config `checks`) |
| extras.py | analysis = regression: forward citations not drawn on the chapter graph + wording. LA: one sentence ("For ten paths") is older wording | **upstream regression/analysis**; LA diff is the template's later generalisation (template ahead) |
| tikz.py | analysis: Fitch `nd` derivations compiled without `tikz` option, `DERIVATION_SCALE 2.0`, `\IfFileExists{fitch-book.sty}` | **upstream as a generic hook** (inactive unless the book ships fitch-book.sty) |
| math.py | regression: `tag_short_bold_greek` (marks short bold Greek glyphs for CSS) | **upstream** (bold-by-type makes bold Greek series-wide) |
| deploy.py | LA moved-ids: 4 lines | **upstream** with moved-ids |
| render_math.cjs, pandoc.py (regression) | em-dash -> `--` in comments | noise |

**filters/**

| File | Differences | Verdict |
|---|---|---|
| theorems.lua | template is ahead of regression: proof ownership (`RESULT_ENVS`, proofs credited to the last result), braced optional titles, `algorithminline`; regression lacks all three (48 lines). analysis = template + external-book references (112 lines). LA: header comment only | **engine = analysis version**; regression is simply behind |
| tikz.lua | analysis: `nd` in PICTURE_ENVS, `$...$` wrap, alt "Derivation" | **upstream** (generic, inert without `\begin{nd}`) |

**templates/**

| File | Differences | Verdict |
|---|---|---|
| html/main.js | analysis: tooltips for external refs (`data-base`, `data-book`). regression: comment rewording | **upstream analysis** |
| html/styles.css + fonts/stix-two-math-bold-greek.woff2 | regression: bold upright Greek web font + accent placement CSS | **upstream** (with math.py) |
| latex/template.aux/.out/.pdf/.synctex.gz/.toc (LA) | untracked build junk | delete/ignore |

**tools/**

| Tool | Where | Verdict |
|---|---|---|
| check_optional.py, reading_path.py | all; LA differs only by `ch24a` vs `ch23a` in docstrings | engine (template text is the generalised one) |
| check_forward_deps.py | template 142 lines; regression 237 / analysis 271: hard vs signpost via `uses_kinds`, `--signposts/--exercises/--external`, `axiom` | **upstream analysis version** |
| check_macros.py + .cjs (LA-conv) | config-driven (`macro-check` in config) retired/undefined macro lint; rule 3 (zero matrix) gated by `macro-check.zero-matrix` | **upstream**, opt-in by config (spec/05 item 6 wants it series-wide) |
| check_rendered.py (analysis) | lints built HTML and PDF logs for leaked source (`??`, `\qedhere`, stray `:::`) | **upstream** (generic) |
| check_structure.py (analysis) | the STYLE.md section contract | **book plugin** now; promote to engine opt-in when LA adopts the same house style |
| check_fitch.py + latex/fitch-book.sty (analysis, 1573 lines) | Fitch derivations / truth tables, Part 0 only | **book plugin of Foundations** after the split |
| check_numbers.py (analysis) | numeric sidecars in `verify/` | **book plugin** (analysis; Foundations if it uses verify/) |
| check_numbers.py, check_prose_numbers.py, numbers.json (regression) | different tool, **same name** as analysis's: runs `code/chNN/` scripts | **book plugin** of regression; rename to avoid the clash if either is ever promoted |
| ledger.py, metrics.py, promises.py, seed_errors.py, mdblocks.py, usage_forms.py, check_notation.py (analysis) | authoring-pipeline tools (claim ledger, metrics.csv, promise reconciliation, referee recall, usage) | **book plugins** for now. Candidates for an engine `authoring/` extra once the LA rewrite uses them (spec/05 items 7, 13, 14) |
| blueprint/ (analysis, regression) | planning pipeline incl. originality.py | out of engine scope now (spec/05 item 13 later) |

**latex/**

| File | Differences | Verdict |
|---|---|---|
| macros.tex | per book (template ships a 216-line generic one + `macros-linear-algebra.tex.example`) | **book** (already per-book via config `macros`) |
| chapter-style.sty | LA, analysis, regression all add `\raggedright` to headings (LA after the colour, analysis/regression before - same effect). LA also `\cftsubsecnumwidth 5.5em` for 4-level TOC numbers | **upstream** raggedright; cftsubsecnumwidth upstream too (harmless for 3-level books) |
| preamble.tex / preamble-book.tex | LA: `\emergencystretch=1em` (measured). analysis: `\IfFileExists{fitch-book.sty}`. regression: +47 lines (book-specific packages/shorthands) | **upstream** LA + analysis lines; regression's extra lines: book override (book's own latex/preamble.tex wins via TEXINPUTS / `engine_file`) - verify which of the 47 are generic |
| latex-template.sty | analysis = regression (+89): `upgreek[Euler]`, `\bt@textsafe` text-safe single-letter shorthands (fixes accented names in bibliographies) | **upstream** |
| theorem-envs.sty | analysis = regression: do not clobber `\check` (only replace names that are environments) | **upstream** |

**tests/**

- Engine tests run against `tests/fixture-book` (test_build, test_optional, test_forward_deps, ...). analysis adds `fixture-companion` + test_external_books, test_known_unresolved: **upstream**.
- Some "engine" tests actually test the host book: `test_proof_ownership.py`, `test_display_math_source.py` (read `../src`), `test_macros.py` (asserts the book's own macros: regression changed it to `\vect{X}`, `\bbeta`), `TestAgainstTheRealBook` in test_reading_path.py. These must be split: the rule moves into the engine (as a check or a test parameterised by `--book`), the book-specific assertions move to the book's own `tests/`.
- test_build.py: regression relaxes the braced-title assertion to a regex (because regression's theorems.lua is behind). Once regression uses the shared filter, the strict assertion is right again.
- Book-only tests (analysis test_check_fitch, test_ledger, test_metrics, ...; LA test_check_macros; LA moved-ids test_moved_ids) follow their tools (engine or book plugin).

**config/config.json**: per book by design. New keys introduced by drift that the engine must
document: `external-books` (analysis), `site-url` (analysis code, unused in config yet),
`macro-check` (LA-conv), `moved-ids` (LA moved-ids), `source-branch` (LA, regression),
`config/known-unresolved.json` (analysis).

### 1c. Engine superset = merge order

Base: book-template HEAD (has the 09-24/09-25 generalisations nobody else has fully:
proof ownership, braced titles, config-driven reading-path targets, generic docstrings).
Then, in this order:
1. regression/analysis LaTeX hardening (latex-template.sty textsafe, theorem-envs guard, raggedright), extras.py forward edges, check_forward_deps hard/signpost + `_tool` + forward gate in check.py.
2. analysis: site-url, external books (external.py, theorems.lua, main.js, manifest, check), axiom, known-unresolved, Fitch hooks in tikz.lua/tikz.py/preamble, check_rendered.
3. LA: emergencystretch, cftsubsecnumwidth, check_macros (config opt-in), moved-ids (from the moved-ids branch).
4. regression: bold-Greek font + math.py tagging.
5. The plugin hook replaces the hard-wired check_structure/fitch/numbers/macros calls.

---

## 2. Mechanism

### Options compared (solo author, local builds and deploys, many worktrees, GitHub Pages, CI only in LA-style "build and check" workflows)

| | git submodule at `engine/` | git subtree at `engine/` | pip package (`pip install -e` locally, `pip install git+...@vX` in CI) |
|---|---|---|---|
| One place to improve | Yes: edit `~/coding/book-engine`, books pin a commit | No: each book has a full copy that can be edited in place - the same drift risk as today, merged back with `subtree push` (slow, awkward) | Yes |
| Per-branch pin (conventions branch on a newer engine than main) | Yes, the pointer is per commit | Yes, but by merging | Only via requirements file per branch |
| Reproducible old builds (published LA site) | Yes | Yes | Only if pinned; an editable install changes every book at once |
| Worktrees (the author uses 2-3 per book) | Each worktree needs `git submodule update --init` (one command; or `BOOK_ENGINE` override, below) | Nothing to do | One venv shared - all worktrees silently on the same engine |
| CI | `actions/checkout@v4` with `submodules: true` (engine repo is public over https: no token) | Nothing | `pip install` step; needs packaging work |
| Restructuring needed | Small: shim + split engine/book roots (already half done: `--book`, `engine_file`, TEXINPUTS order) | Small | Larger: engine must become a proper package (`book_engine/` with Lua/LaTeX/templates as package data), `ENGINE_ROOT` moves; the top-level package name `build` also collides with PyPI's `build` |
| Failure mode | Forgetting to bump/commit the pointer; detached HEAD in engine/ | Drift returns | "It built yesterday" - an engine edit for book A breaks book B unseen |

### Recommendation: git submodule, plus a local override for development

- Rename `book-template` -> **`book-engine`** on GitHub (GitHub keeps a redirect from the old name). Strip it to engine-only: build/, filters/, templates/, tools/ (generic), latex/ (style files, no book macros), widgets/, tests/ (with fixture books), BUILD.md, a `starter/` directory holding what a new book needs (config/config.json, latex/macros.tex, src/index.md, authoring/, CI workflow, shim). Tag `v1.0.0` when the first book runs on it; tag after each upgrade a book adopts (spec/05 item 1 "by version" = the submodule pointer + tags).
- Each book: `engine/` submodule (`.gitmodules` url `https://github.com/AkizumiFox/book-engine.git`, so CI clones without a key; locally `git config url."git@github.com:".pushInsteadOf https://github.com/` for pushes). Book repo keeps only `build.py` (shim), `config/`, `latex/macros.tex` (+ optional overrides), `src/`, `authoring/`, `tests/` (book tests), `tools/` (book plugins), `.github/workflows/`.
- Shim (`build.py` in each book, ~15 lines): engine root = `$BOOK_ENGINE` if set, else `./engine`; `sys.path.insert(0, engine)`; `from build.cli import main; main(default_book=<dir of shim>)`. Setting `BOOK_ENGINE=~/coding/book-engine` builds any book against the working copy of the engine - the "edit once, try on every book" loop of an editable install without giving up the pin.
- Engine changes needed: `cli.main(default_book=...)` instead of `--book` defaulting to `ENGINE_ROOT`; `Book.__init__` without the ENGINE_ROOT default; `check.py` stops importing tools from `ENGINE_ROOT/tools` only.
- Book plugins (config-driven, no hard-wired names):
  ```json
  "checks": [
    {"tool": "tools/check_structure.py", "fatal": true,  "requires": "authoring/STYLE.md"},
    {"tool": "tools/check_fitch.py",     "fatal": true},
    {"tool": "tools/check_numbers.py",   "fatal": true,  "requires": "verify"},
    {"tool": "engine:check_macros",      "fatal": true}
  ]
  ```
  Resolution: a `tools/...` path is the book's file; `engine:` names an engine tool. Protocol: the module exposes `def run(book, labels) -> (errors, warnings)` (small adapters wrap the existing `find_violations`/`report` pairs). Engine-default checks (optional, forward deps, external refs, known-unresolved, links, numbering) always run; `"checks-disable": [...]` for a book that needs to opt out.
- Other per-book differences stay config or override: `macros`, `templates`, `styles` already go through `engine_file`; LaTeX overrides work because TEXINPUTS lists the book root before the engine.
- Tests: `python -m unittest discover -s engine/tests` (engine against its fixtures) and `python -m unittest discover -s tests` (book). The host-book tests listed in 1b move to the book or become engine checks run by `./build.py check`.
- Pre-commit guard (optional): engine's `doctor` warns when `engine/` has uncommitted changes or is not at a tagged commit.

---

## 3. The combined site

Target: one origin, e.g. `https://akizumifox.github.io/math-atlas/` (later a custom domain),
`/foundations/`, `/analysis/`, `/linear-algebra/`, `/atlas/`, landing `index.html`.

Problems visible in today's WIP preview (gh-pages 7e06676):
- linear-algebra pages carry `canonical` = `https://linear-algebra.akizumifox.com/...` (its `deploy-domain`) - fine while that is the primary site, wrong once the atlas site is.
- analysis/404.html links `/styles.css`, `/index.html` (root-absolute, no `site-url` set) - broken under a sub-path. And GitHub Pages serves only the **root** `404.html` for a project site, so per-book 404 pages are never used.
- analysis's `external-books.la.url` points at the production LA domain and its `labels` at `../linear-algebra/_build/...` (a sibling checkout), so cross-links leave the combined site.

Design:
- **Site manifest** in math-atlas (it already hosts the series hub and the gh-pages preview), e.g. `site/books.json`: per book `{id, title, blurb, repo dir or git url, ref, subdir, prefix}` plus landing-page text. Atlas pages (`generated/atlas.html`) go under `/atlas/`.
- **Assembler** in the engine: `./build.py library site/books.json --out _site` (new `build/library.py`), so it improves with the engine. For each book:
  1. check out the ref into a temporary worktree (or use a given local dir for previews),
  2. build with a **config overlay**: `site-url = <base>/<subdir>/`, every `external-books.<p>.url = ../<their subdir>/` and `labels = <their _build>/crossref_labels.json`, `deploy-domain` cleared. Engine change: `--config-overlay FILE` (deep merge) - also useful for a "preview" profile with `noindex`.
  3. copy `_build/html` into `_site/<subdir>/`.
  Build order: labels first for all books (`scan` pass), then HTML/PDF - so mutual citations (Analysis -> LA, LA -> Foundations) resolve without a fixed order; external.py already degrades to a warning if a registry is missing.
- **Landing page** generated from the manifest (the current hand-written index.html is the template), root `robots.txt`, `sitemap.xml` as a sitemap index of each book's sitemap (books under a sub-path already skip robots.txt), root `404.html` that maps the path prefix to the right book's home/search.
- **Shared assets**: phase 1 keeps per-book copies (styles, main.js, MathJax, fonts: a few MB each; simplest, each book versioned independently). Phase 2 optional: `assets-url` config so books reference `/<base>/_engine/<engine-version>/`.
- **Cross-book links**: already supported (`@la:thm-x`, tooltips via `data-base`, `labels.json` published per book). In the combined site every external `url` is relative, so links and hover previews stay same-origin (no CORS issue).
- **Search across books** (optional, last): each book already emits a search index; the landing page (and optionally each book's search box, via an `also-search` list in the overlay) loads all indexes and labels results with the book's short name.
- **Deploy**: same model as today: local `./build.py library ... --deploy --push` into a clone of math-atlas's gh-pages (or a dedicated `math-atlas-site` repo if math-atlas history should not carry built HTML). CI optional: a math-atlas workflow that only checks the assembled site builds.
- **Domains**: keep `linear-algebra.akizumifox.com` live from the LA repo until the atlas site is primary; then point it at the atlas `/linear-algebra/` (redirect stubs via the existing `redirects` machinery or a CNAME change). Decision for the author; until then the atlas copy should be `noindex` or canonical to the production site (current behaviour).

---

## 4. Migration steps (one commit each, on branches)

Gates used below:
- **E** = `python -m unittest discover -s tests` in book-engine (fixture book builds).
- **B(book)** = in that book: `./build.py doctor`, engine tests, book tests, `./build.py all`, `./build.py check`.
- **Same-output** = build the book before and after the step and `diff -r` the `_build/html` trees (ignore asset-version query strings and timestamps); PDFs: compare `book.aux` label numbers. This is the main safety net for steps 8-13.

### Phase A - build the engine (in book-template, branch `engine`)
1. Delete untracked junk; add `.gitignore` entries; no code change. Record baseline: E green, and run B on each book's current state (note existing failures so they are not blamed on the migration).
2. Upstream regression/analysis LaTeX hardening: latex-template.sty (textsafe, upgreek[Euler]), theorem-envs.sty (`\check` guard), chapter-style.sty raggedright + cftsubsecnumwidth, preamble*.tex emergencystretch + `\IfFileExists{fitch-book.sty}`. Gate: E, fixture PDF builds.
3. Upstream forward-dependency gate: `_tool()` loader in check.py, check_forward_deps.py (analysis version), test_forward_deps.py, extras.py forward-edge skip, `axiom` in STATEMENT_TYPES/RESULT_TYPES. Gate: E.
4. Upstream `site-url` (book.py, html.py, pandoc.py, manifest.py sitemap/robots/404). Test: fixture built with `site-url` under a sub-path has relative pages, sub-path 404 links, no robots.txt. Gate: E.
5. Upstream external books: build/external.py, theorems.lua, main.js, manifest/check/pdf changes, fixture-companion, test_external_books.py. Gate: E.
6. Upstream known-unresolved baseline + test; moved-ids (cherry-pick f79e54b's engine part + test_moved_ids.py); check_rendered.py (+ test); Fitch hooks in tikz.lua/tikz.py (inert). One commit per feature. Gate: E.
7. Upstream check_macros (LA-conv) as engine tool, opt-in by `macro-check` config; bold-Greek font + math.py tagging + CSS (regression). Gate: E.
8. Plugin hook: config `checks` / `checks-disable`, `run(book, labels)` protocol, adapters for check_optional/forward_deps/macros; remove hard-wired book-specific calls. Test with a fixture plugin. Gate: E.
9. Engine/book root split: `cli.main(default_book=...)`, no ENGINE_ROOT default for Book, `BOOK_ENGINE` honoured; move host-book tests (proof ownership, display-math source, real-book reading paths, book macros) into checks or into `starter/tests`. Gate: E.
10. Restructure the repo as engine-only + `starter/`; README/BUILD.md describe submodule use. Rename the GitHub repo to `book-engine`; tag `v1.0.0-rc1`. Gate: E, and `starter/` builds as a book via the shim.

### Phase B - move books onto it (each on its own branch; publish only after Same-output)
11. **analysis-book (conventions branch first)** - the copy closest to the engine. Add `engine/` submodule, shim, move check_structure/fitch/numbers into `"checks"`, delete engine dirs from the book, keep book tools in `tools/` and book tests in `tests/`. Gate: B(analysis), Same-output. Push analysis-book to a remote first (it has none - a backup risk regardless of this plan).
12. **Foundations** (new repo from `starter/`, created by the Part 0 split): born on the engine; carries check_fitch.py + latex/fitch-book.sty + their tests as plugins; `external-books` for `an`/`la` as needed. Gate: B(foundations).
13. **linear-algebra conventions-rewrite**: submodule + shim; check_macros now `engine:check_macros` via config; delete engine dirs. Gate: B(LA), Same-output against the branch's pre-migration build.
14. **linear-algebra main** (the published site): same as 13 but also update `.github/workflows/build-and-deploy.yml` (`actions/checkout@v4` with `submodules: true`; "Engine tests" -> run engine/tests and tests). Gate: B(LA), Same-output against the live `site/` clone (deploy with `./build.py deploy` without `--push`, then `git -C site diff --stat`: only asset version strings may change). Then push, watch CI, then `deploy --push`. Merge moved-ids and conventions-rewrite branches after this (their engine parts are already in the engine; resolve by deleting the engine dirs on the branch).
15. **regression** (lowest priority): submodule + shim; check_numbers/check_prose_numbers as plugins; book-specific part of preamble additions as `latex/` overrides; its test_macros assertions move to its own tests. Gate: B(regression), Same-output (expect real differences from the newer theorems.lua: proof ownership, braced titles - review them, they are fixes).

### Phase C - the combined site (book-engine + math-atlas)
16. Engine: `--config-overlay FILE` (deep merge) + test. Gate: E.
17. Engine: `build/library.py` assembler (two-pass labels-then-HTML, copy into subdirs, landing page from manifest, root robots/sitemap index/404) + fixture test with two fixture books citing each other. Gate: E.
18. math-atlas: `site/books.json` + landing text; `README` command. Build the preview with it and compare to today's hand-assembled gh-pages (cards, subdirs, atlas). Deploy to gh-pages.
19. Optional: cross-book search on the landing page; per-book `also-search`.
20. Optional: shared `_engine/<version>/` assets; custom domain; decide canonical/redirect for linear-algebra.akizumifox.com.

### Risks
- **Published LA site**: deploys are local (`./build.py deploy --push` from `site/`), so CI changes cannot publish by accident; the risk is a changed `site/` output. Mitigation: step 14's Same-output diff before `--push`; the existing stale-page and redirect logic must keep working with the engine path change (engine fingerprint hashes engine file *paths*, so the first build after the switch is a full rebuild - expected, ~40 min for LA).
- **LA CI** (`.github/workflows/build-and-deploy.yml`): without `submodules: true` the checkout has an empty `engine/` and every step fails. The engine repo must stay public (it is) and the `.gitmodules` URL must be https. The MathJax cache key `book-engine-mathjax-3.2.2` keeps working.
- **Worktrees**: each new worktree needs `git submodule update --init`; a worktree created without it fails at the shim - make the shim print that exact command when `engine/` is empty.
- **Package name `build`**: the engine package shadows PyPI `build` on `sys.path`; harmless today, rename to `book_engine` only if it bites.
- **analysis-book has no remote**: push it somewhere private before restructuring.
- **Name clash**: two different `tools/check_numbers.py` (analysis vs regression); fine as book plugins, rename before promoting either.
- **Behaviour changes in old copies**: regression gets proof ownership and braced titles; LA gets the forward-dependency gate, `axiom`, check_rendered - `check` may newly fail. Add a config kill-switch per new check (`checks-disable`) so migration and fixing are separate commits.
- **Branches in flight** (LA conventions-rewrite, moved-ids; analysis conventions): migrate the branch that is merged next first, then rebase the others onto it, deleting engine dirs rather than resolving conflicts in them.
