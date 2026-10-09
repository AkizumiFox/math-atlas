# 02 記號

## 原則

作者和 AI 都只寫**語意巨集**，不寫字形：

- 寫 `\inner{u}{v}`，不寫 `\langle u, v \rangle`。
- 寫 `\transpose{A}`，不寫 `A^{\top}`。

渲染器因此知道每個符號代表什麼，可以：

- 一處修改，全套跟著改；
- 每個符號都能 hover，顯示它的定義在哪一章；
- 告訴讀者其他書怎麼寫同一個東西。

現況：線代書的 `latex/macros.tex` 混用兩種巨集。`\inner` 是語意型；`\tp`、`\sA`、`\T` 是表現型。遷移時需要一張對照表，見 06。

## 記號表 schema（`registry/notation.yaml`）

2026-10-10 建立，目前只收章名用到的記號（數系巨集，以及 Lᵖ、ℓᵖ、C(K)、C₀(X)、H¹₀、Aₙ 六個新巨集，2026-10-10 確認，status: confirmed）。另加一個 `unicode` 欄：純文字輸出（章名、hover、Mermaid）用的字形。

```yaml
- id: sym:inner
  macro: \inner{#1}{#2}
  render: \langle #1, #2 \rangle
  meaning: 內積
  convention: 對第一個變數線性      # 待拍板，見下表
  defined_at: def-inner-product  # 陳述 ID（與書稿 label 同一套）
  scope: global                      # 或冊／章 ID 列表
  forbid: ['\langle']                # 原始字形 lint
  outside_variants: ['(u|v)（物理與部分分析書）', 'u·v']
```

## 作用域與 import

- 一章的作用域 ＝ 自己定義的記號 ＋ 所有 s 祖先定義的記號 ＋ 本章登記的就地定義（spec/01 規則 8）。b 的來源章不在內：借用的意思是不必讀那一章，它的記號自然也不能進入作用域；被借用陳述的語彙必須已經在這個作用域裡（spec/01 規則 1）。
- 每冊開頭由 build 自動產生「本冊沿用的記號」表。
- 同一字形在重疊作用域裡有兩種語意時，build 報錯，除非記號表明文宣告這個重載和各自的作用域。例如 $(a,b)$ 可以是開區間、有序對或 gcd。

## 現況與待拍板的約定

兩本現有書稿的記號表是 `linear-algebra/authoring/NOTATION.md` 與 `analysis-book/authoring/NOTATION.md`。下表先列它們的現況，再給全套的約定。標「**已定**」的是定案；其餘仍是提案，待作者確認。一旦拍板，之後要改就必須走 04 的「約定變更治理」流程。

| 項目 | linear-algebra | analysis-book | 全套提案 |
|---|---|---|---|
| ℕ 是否含 0 | **含 0** | **不含 0**；ℕ₀ 只用在 Part 0 的建構路線 | **已定（2026-10-09）：含 0。** 正整數寫 $\mathbb{Z}_{>0}$。理由：F3.1 用 von Neumann 建構（$0 = \varnothing$），線代書與 mathlib 都含 0。analysis-book 要改寫，見 06 |
| 子集合 | — | `\subseteq`／`\subsetneq`，禁用裸 `\subset` | 照 analysis-book，全套禁用裸 `\subset` |
| 內積 | `\inner{u}{v}`，**對第一個變數線性** | 用到時沿用線代書 | 照線代書 |
| 轉置與共軛轉置 | `\tp`（`^{\top}`）、`^{*}`；對偶映射寫 `T'`，星號留給伴隨 | — | 照線代書；`\tp` 改名為語意巨集 `\transpose{}` |
| 粗體向量 | 一律粗體（`\v`、`\u`、`\x` 為 `\mathbf`） | **不加粗**（同一個字母會在 ℝ、ℝⁿ 與函數空間之間移動） | **已定（2026-10-09）：依型別決定**，見下方「粗體規則」 |
| 線性映射空間 | `\cL(V,W)`（$\mathcal{L}$）；第 23 章另用 $\operatorname{Hom}_A$ | — | 線代用 $\mathcal{L}$，模論用 $\operatorname{Hom}$，宣告為同一概念的兩個記號 |
| 對偶空間 | $V^{*}$；泛函用希臘字母 | — | $V^{*}$，FA 沿用 |
| 等價類 | — | 待查 | $[x]$；$\bar{x}$ 留給共軛與閉包 |
| 積分 | — | 待查 | $\int f \, d\mu$ |

### 粗體規則（2026-10-09 定案）

字形跟著 A 軸走（A 的定義見 03），讓讀者從字形就看出現在是在座標裡計算，還是在抽象結構裡推理：

| 物件 | A 軸 | 字形 | 例 |
|---|---|---|---|
| 座標向量、矩陣 | A1 | 粗體 | $\mathbf{x} \in \mathbb{F}^n$、$\mathbf{A} \in \mathbb{F}^{m \times n}$ |
| 抽象向量空間的元素 | A2 | 不加粗 | $v \in V$、$f \in L^2$ |
| 映射、算子、空間 | — | 不加粗（線代書現行規則不變） | $T$、$V$ |

實作上用兩個語意巨集區分：`\coord{x}` 是座標向量，`\elem{v}` 是抽象元素（不用 `\vec`：它是 LaTeX 內建的箭頭重音），渲染規則由記號表決定。線代書目前一律用 `\mathbf`（`\v`、`\u`、`\x`），所以第 1–5 章的每一處都要重新判斷型別。這適合交給 AI 分類、再人工抽審，見 06 的書稿待辦。

兩本書都已經有一部分語意型巨集（`\inner`、`\nN`），只是巨集檔各自獨立。合併成全套共用的記號表，是 05 引擎需求的第一項。

## 英文用詞約定（2026-10-10）

書稿用英文，而英文沒有樂詞網那樣的官方標準，同一個概念的寫法變體更多。約定記在 `registry/usage.yaml`：每組選定一個寫法（use），其餘列為 avoid。

- **先統計，再提案**：`tools/usage_report.py` 掃兩本書稿的散文（去掉數學式、程式碼、label 與參照），統計每組變體各出現幾次，寫成 `generated/usage.md`。提案依頻率與一般慣例，status 為 proposed；作者確認後改成 confirmed，報告就會列出書稿裡每一處 avoid 寫法。
- **涵蓋的組**（16 組）：序列逗號（Oxford comma）、injective／one-to-one、surjective／onto（只禁形容詞用法）、bijection、image／range、kernel 與 null space（兩者並存：映射的核 vs 矩陣的零空間）、map／mapping／function、non- 字首要不要連字號、codomain 等連寫詞、finite-dimensional、positive definite、self-adjoint、well-defined（名詞前加連字號、述語分寫）、if and only if／iff、複數形、美式拼寫。
- **不做 lint、只寫規則的**：range 不當 image 的同義詞（range 多半是別的意思，無法機械判斷）；人名之間用 en dash（Cauchy–Schwarz，兩本書已一致）。
- **2026-10-10 全部確認**。non- 改為連寫（nonzero、nonnegative），和美式拼寫一致；後接專有名詞或大寫字時保留連字號（non-Euclidean）。書稿的遷移見 spec/06，陳述雜湊先正規化 avoid 寫法，不觸發重審（spec/04 圖 3）。
- lint 本身屬於引擎（spec/05 第 14 項）；atlas 這邊的報告是它的原型。

術語表 `registry/terms.yaml` 所有冊共用，以英文術語為正式名稱（書稿用英文，spec/00 原則 7）。中文譯名是選填欄位 `zh`，取自國家教育研究院「樂詞網」，目前凍結：`choose`、`missing` 的術語不擋任何進度，等主線冊寫完再補，用途是雙語詞彙表與 hover。譯名的例外（例如 eigenvalue 要不要用「特徵值」而非樂詞網的「固有值」）只影響 `zh`，與書稿無關。它由 `tools/seed_terms.py` 從兩本書定義中的粗體字與 `statements.yaml` 產生，可重跑，手填的譯名會保留。每個術語只有一個正式定義（`def`）；同一個詞的其他定義列在 `also`，待分流成就地定義、同形異義或遷移時合併的重複。
