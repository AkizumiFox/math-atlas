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
6. **共用記號表**：從 `registry/notation.yaml` 產生 `macros.tex` 和 MathJax 巨集，加上作用域 lint、原始字形 lint 和重載宣告；各書的 NOTATION.md 也由它產生，不再手寫（手寫的記號文件是第二個事實來源，會和規則脫節）。
   - **作用域 lint 也要檢查借用**：被 `borrows` 引用的陳述，其中每個語意巨集與術語都必須在借用處的作用域內（spec/03 §6 規則 3）。math-atlas 目前只能在章層級用手寫的 `scope` 代理，宣告漏寫就抓不到。例：`thm-unitary-exponential` 搬到 AN3.3 後，MA.21 借用它是否合法，取決於 MA.21 的作用域裡有沒有矩陣指數；這一點在 2026-10-09 是人工查出來的（有，經由 MA.21 ← LA2.10 的 s 邊），引擎上線後應由 build 自動判定。
7. **陳述雜湊**：每條 uses 邊存被引用陳述正規化後的雜湊，用來驅動 04 圖 3 的重審流程。正規化包括把 `registry/usage.yaml` 的 avoid 寫法換成 use 寫法，讓純拼寫的遷移不觸發重審。
8. **符號 hover**：語意巨集渲染時帶上 `data-sym` 屬性，前端顯示符號的定義位置。
9. **先備頁由 registry 產生**：每冊列出「需要／借用／不需要」三欄，不手寫。
10. **定義必須引用它用到的定義**：定義與定理陳述裡出現的既有術語，要以 crossref 或語意巨集連到其定義，並由 lint 檢查（未連結的已登記術語報錯）。atlas 的陳述讀者必讀集（spec/03 §6.2）目前只看得到明寫的引用，是下界；有了這條才會是精確值。原型是 `tools/import_la.py` 的 `term_edges`：拿 `registry/terms.yaml` 比對定義與陳述的文字，找出出現了術語卻沒有引用的地方。比對規則在 `tools/lexicon.py`：去掉數學式與 label 參照後切詞，最長比對，詞形還原（fields → field、matrices → matrix、Cauchy sequences → Cauchy sequence），不分大小寫；但含專有名詞的術語（Cauchy、Jordan、Hermitian，依兩本書中句中大寫的頻率判定）只比對原本的大小寫，人名也不還原（Givens 不會變成 Given）。
11. **跨書 label 唯一**：build 讀其他書匯出的 label 表，同一個 label 在兩本書裡指不同結果時報錯（線代書與 analysis-book 目前已有 22 個重複，見 `generated/diff.md`，其中 `def-image` 是真正的撞名：線性映射的像 vs 集合的像）。
12. **搬家錨點**：label 搬到另一章或另一本書時，舊位置自動產生「已移至⋯⋯」的錨點與重導，讓已發布的連結不失效（spec/01 的「發布」）。
13. **原創性檢查併入共用引擎**：書稿用英文，主要參考書（Rudin、Folland、Axler 等）也是英文，生成內容與原書句子重疊的風險很高，04 圖 1 的版權重疊檢測不可省略。analysis-book 的 `blueprint/originality.py` 已在做：以章在 book.yaml 列出的來源節點為對照，找出共享的 8-gram，並排除由常用詞與數學套語（`COMMON`、`STOCK`）組成的片段。把它搬進共用引擎，讓每本書都用：來源清單改由 registry 提供，閾值（n、套語表、容許的片段數）用英文語料校準：拿已知原創與已知抄寫的段落量出誤報率與漏報率再定，不憑感覺設定。
14. **英文用詞 lint**：讀 `registry/usage.yaml`，status 為 confirmed 的組，書稿散文裡出現 avoid 寫法就報出（檔案與行號）。比對規則與 `tools/usage_report.py` 相同：去掉數學式、程式碼、label 與參照，整詞、不分大小寫。
