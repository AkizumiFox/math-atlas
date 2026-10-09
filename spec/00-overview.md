# 00 總覽

math-atlas 是一整套「零基礎 → 數學研究所資格考」教科書的**地圖與規格**。各冊書稿分散在各自的 repo（`analysis-book`、`linear-algebra`，以及之後的代數書），這個 repo 只放三樣東西：

1. **registry**：冊、章、陳述、依賴邊、資格考目標與領域覆蓋表。它是全套結構唯一的事實來源。
2. **spec**：全套共用的約定，包括 ID、邊型別、記號、深度編碼、流程，以及給建置引擎的需求。
3. **tools**：驗證、統計與畫圖工具（`tools/atlas.py`），產出放在 `generated/`。

## 終點

| 分級 | 內容 | 主幹或支線 |
|---|---|---|
| T1 碩士班入學 | 高微、線代、大學代數 | 主幹 |
| T2 資格考核心 | 測度論實分析、群環體模與 Galois、有限群表示入門、Ahlfors 程度複分析 | 主幹到此為止 |
| T3 延伸 | 代數拓樸、代數幾何、微分幾何、機率、PDE 等 | 支線冊，不進主幹 |

資格考的對照目標寫在 `registry/exam-targets.yaml`，必讀章數由 `atlas.py stats` 計算（見 `generated/report.md`）。

## 冊

冊的清單在 `registry/volumes.yaml`，分五個分支（冊數與章數見 `generated/report.md`；規格只寫規則，數字一律引用產出）：

- **基礎**：F1 邏輯與證明、F2 集合函數與關係、F3 數系與代數預備。
- **分析**：AN1 實數線、AN2 度量與拓樸、AN3 多變數、HA Fourier、MT 測度、CA 複分析、FA 泛函分析。
- **線代**：LA1–LA4，以及 MA 矩陣分析。
- **代數**：AL1 群、AL2 環與體、AL3 Galois、AL4 模、表示與同調，以及支線 AL5 交換代數。
- **支線**：PR 機率、PDE 分佈與 Sobolev、GEO 幾何、NLA 計算、ST 公理集合論。

書稿來源：

- **分析線**沿用 analysis-book 的章節藍圖，依 Part 拆冊。逐章對照見 `generated/migration.md`，對照的理由見 `06-migration.md`。
- **線代線**沿用 linear-algebra 現有的章，第 0 章拆到 F 冊和 AL1。
- **代數與 ST** 目前沒有書稿，章名是計畫。

## 設計原則

1. **地圖是 DAG，不是一條鏈。** 一冊不必等上一冊讀完才開始，只要它需要的章讀過即可。預設的閱讀順序仍然是線性的（`volumes.yaml` 與 `chapters.yaml` 的列表順序）；依賴圖是導覽用的。這個取捨參考了 Khan Academy 移除 knowledge map 的經驗。
2. **邊由證明計算，手寫的邊只是計畫。** 有書稿的地方一律以 build 回溯出的邊為準：兩章都有書稿時，計算值取代計畫值，過時的計畫 s 邊不會留在圖上灌水必讀量（合併規則見 spec/01）。線代線已經是計算值（`registry/computed/la-edges.yaml`），`atlas.py diff` 會列出計畫和計算不一致的地方。
3. **集合論分兩段。** 開頭先教樸素集合論，用到 F2.4 的使用者層級 Zorn 引理為止；ZFC、序數和選擇公理的等價形式放在最後的 ST 冊。
4. **ℝ 公理化優先。** AN1.1 直接給出完備有序體公理；從 ℕ 一路建構到 ℝ 的路線放在 F3.1–F3.4，標為選讀。這是 analysis-book 已經採用的路線，可以縮短分析主幹。
5. **主幹只到 T2。** T3 的科目一律做成支線冊。`registry/fields.yaml` 記錄每一科在地圖上的接點。
6. **授權分三層**（2026-10-09 定案）：
   - **書稿**：CC BY-NC-SA 4.0，全套一致。三本既有的書（analysis-book、linear-algebra、regression）本來就是這個授權，不需遷移。
   - **atlas 的 registry、spec 與 generated**：CC BY 4.0。它們是後設資料，越寬鬆越容易和其他先備知識編碼的專案共用。
   - **tools**：MIT。

   對外部素材的影響：Open Logic（CC BY）可以改編進書稿；Napkin（CC BY-SA）**不能**，因為 BY-SA 的改編作只能以 BY-SA 或相容授權釋出，NC-SA 不相容，只能當參考；Book of Proof（ND）不能改編。
7. **語言**（2026-10-10 定案）：
   - **書稿用英文。** 給讀者看的一切也用英文：章名、先備頁、閱讀路徑、依賴圖（`chapters.yaml` 的 `title`、`generated/README.md`、`atlas.html`、各冊的 Mermaid 圖）。
   - **atlas 的規格與給作者看的報告維持中文**（`spec/`、`generated/report.md`、`diff.md`、`migration.md`）。
   - **術語以英文為正式名稱**，用詞變體依 spec/02 的英文用詞約定統一。中文只是選填欄位：術語表的 `zh`、章的 `title_zh`，日後用來做雙語詞彙表與 hover 時附上中文，不擋任何進度。
   - 因為主要參考書（Rudin、Folland、Axler 等）也是英文，與原書句子重疊的風險比中文高得多，原創性檢查（04 圖 1）不可省略，見 spec/05 第 13 項。

## 文件索引

| 文件 | 內容 |
|---|---|
| `01-ids-and-edges.md` | 穩定 ID、四層結構、邊型別與合法性規則 |
| `02-notation.md` | 語意巨集、記號表 schema、待拍板的約定 |
| `03-depth-encoding.md` | A／R 深度編碼的定義草稿 |
| `04-flows.md` | 五張流程圖 |
| `05-engine-requirements.md` | 給共用建置引擎（book-engine）的需求 |
| `06-migration.md` | 書稿到冊的對照、待決事項 |
