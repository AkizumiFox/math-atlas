# 05 給共用建置引擎（book-engine）的需求

## 現況

同一套 Pandoc＋Lua＋Python 引擎，目前以**複製**的方式存在四個 repo：

- `book-template`
- `linear-algebra`
- `regression`
- `analysis-book`

這些複製已經開始分歧。例如 `filters/theorems.lua` 在 regression 和 linear-algebra 之間不同，在 analysis-book 和 book-template 之間也不同。已定案：引擎抽成獨立的 `book-engine` repo，各書共用；math-atlas 不放引擎。

## 已經可以直接沿用的部分

| 能力 | 位置（以 linear-algebra 為準） |
|---|---|
| label 與 uses 掃描、`uses_kinds` | `filters/theorems.lua`、`build/manifest.py` → `_build/crossref_labels.json` |
| 硬邊與軟邊的政策（`HARD_KINDS`、optional 結果） | `tools/reading_path.py` |
| 前向引用、optional 結果的檢查 | `tools/check_forward_deps.py`、`tools/check_optional.py` |
| 章層級圖、閱讀路徑頁 | `build/extras.py` → `graph.json`、`path-*.html` |
| 巨集統一給 PDF 和網頁 | `build/macros.py` 讀 `latex/macros.tex` |

## 新需求（依優先序）

1. **一份共用的引擎 package**：各書以版本號依賴它，不再複製；各書可以覆寫模板（現有的 `--book` 機制）。
2. **跨冊 ID 解析**：`@thm-x` 可以指向其他書的 label。build 讀 math-atlas 的 registry，或讀各書匯出的 `crossref_labels.json`，產生正確的連結和顯示編號（例如「LA3 定理 11.5.2」）。
3. **`borrows` 語法**：例如 `@thm-x{.borrow}` 或 `::: {.borrows}` 區塊，讓 (A1)–(A7) 這類借用事實成為真正的邊，而不是散文清單。lint 規則見 01 的「b 的合法性」。
4. **`see` 與 `revisits` 標記**：允許前向的 see；revisits 指向同一概念的舊版本，用來產生概念頁。
5. **匯出 atlas 格式**：每次 build 都輸出 `atlas-edges.yaml`，格式和 `registry/computed/la-edges.yaml` 相同。這樣 math-atlas 可以直接收下計算邊，取代 `tools/import_la.py` 的手動 section 對照。
6. **共用記號表**：從 `registry/notation.yaml` 產生 `macros.tex` 和 MathJax 巨集，加上作用域 lint、原始字形 lint 和重載宣告。
   - **作用域 lint 也要檢查借用**：被 `borrows` 引用的陳述，其中每個語意巨集與術語都必須在借用處的作用域內（spec/03 §6 規則 3）。math-atlas 目前只能在章層級用手寫的 `scope` 代理，宣告漏寫就抓不到。例：`thm-unitary-exponential` 搬到 AN3.3 後，MA.21 借用它是否合法，取決於 MA.21 的作用域裡有沒有矩陣指數；這一點在 2026-10-09 是人工查出來的（有，經由 MA.21 ← LA2.10 的 s 邊），引擎上線後應由 build 自動判定。
7. **陳述雜湊**：每條 uses 邊存被引用陳述正規化後的雜湊，用來驅動 04 圖 3 的重審流程。
8. **符號 hover**：語意巨集渲染時帶上 `data-sym` 屬性，前端顯示符號的定義位置。
9. **先備頁由 registry 產生**：每冊列出「需要／借用／不需要」三欄，不手寫。
