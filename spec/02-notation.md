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

## 記號表 schema（`registry/notation.yaml`，尚未建立）

```yaml
- id: sym:inner
  macro: \inner{#1}{#2}
  render: \langle #1, #2 \rangle
  meaning: 內積
  convention: 對第一個變數線性      # 待拍板，見下表
  defined_at: la3.def.inner-product  # 陳述 ID
  scope: global                      # 或冊／章 ID 列表
  forbid: ['\langle']                # 原始字形 lint
  outside_variants: ['(u|v)（物理與部分分析書）', 'u·v']
```

## 作用域與 import

- 一章只能用兩類記號：自己定義的，以及沿 s ∪ b 遞移可達的上游章所定義的。
- 每冊開頭由 build 自動產生「本冊沿用的記號」表。
- 同一字形在重疊作用域裡有兩種語意時，build 報錯，除非記號表明文宣告這個重載和各自的作用域。例如 $(a,b)$ 可以是開區間、有序對或 gcd。

## 現況與待拍板的約定

兩本現有書稿的記號表是 `linear-algebra/authoring/NOTATION.md` 與 `analysis-book/authoring/NOTATION.md`。下表先列它們的現況，再給全套的提案。**提案都待作者確認**；一旦拍板，之後要改就必須走 04 的「約定變更治理」流程。

| 項目 | linear-algebra | analysis-book | 全套提案 |
|---|---|---|---|
| ℕ 是否含 0 | **含 0** | **不含 0**；ℕ₀ 只用在 Part 0 的建構路線 | **衝突，必須擇一**。若選含 0，改 analysis-book；若選不含 0，改線代書並另立 `\nNz`。兩書都已有 `\nN` 巨集，改的是渲染與內文中依賴這個約定的敘述 |
| 子集合 | — | `\subseteq`／`\subsetneq`，禁用裸 `\subset` | 照 analysis-book，全套禁用裸 `\subset` |
| 內積 | `\inner{u}{v}`，**對第一個變數線性** | 用到時沿用線代書 | 照線代書 |
| 轉置與共軛轉置 | `\tp`（`^{\top}`）、`^{*}`；對偶映射寫 `T'`，星號留給伴隨 | — | 照線代書；`\tp` 改名為語意巨集 `\transpose{}` |
| 粗體向量 | 粗體 | **不加粗**（同一個字母會在 ℝ、ℝⁿ 與函數空間之間移動） | **衝突**。提案：依型別決定，$\mathbb{F}^n$ 的座標向量與矩陣加粗，抽象向量空間的元素不加粗 |
| 線性映射空間 | `\cL(V,W)`（$\mathcal{L}$）；第 23 章另用 $\operatorname{Hom}_A$ | — | 線代用 $\mathcal{L}$，模論用 $\operatorname{Hom}$，宣告為同一概念的兩個記號 |
| 對偶空間 | $V^{*}$；泛函用希臘字母 | — | $V^{*}$，FA 沿用 |
| 等價類 | — | 待查 | $[x]$；$\bar{x}$ 留給共軛與閉包 |
| 積分 | — | 待查 | $\int f \, d\mu$ |

兩本書都已經有一部分語意型巨集（`\inner`、`\nN`），只是巨集檔各自獨立。合併成全套共用的記號表，是 05 引擎需求的第一項。

術語表（`registry/terms.yaml`，尚未建立）以國家教育研究院「樂詞網」為準，所有冊共用。
