# 地圖統計（由 `tools/atlas.py stats` 產生，勿手改）

- 冊：29；章：210（選讀 11）
- 章層級邊：s 680、b 23、軟邊 137；其中 286 條 s 邊是從線代書的證明計算出來的，其餘是計畫值

除非欄位註明「含選讀」，以下統計都排除選讀章（opt）。

## 最長硬依賴鏈（只計 s）

**39 章**，終點 PR.5 Brownian Motion：

F1.1 → F1.2 → F1.7 → F1.3 → F1.4 → F1.8 → F1.5 → F2.1 → F2.6 → F2.2 → F2.3 → F2.5 → F3.1 → F3.2 → F3.9 → F3.10 → F3.4 → F4.6 → F4.8 → F4.11 → AN2.1 → AN1.2 → AN1.5 → AN1.6 → AN1.7 → AN1.8 → AN1.9 → AN2.6 → HA.9 → MT.1 → MT.2 → MT.3 → MT.4 → MT.7 → MT.8 → PR.1 → PR.2 → PR.3 → PR.5

各冊最高的章（高度＝從零讀到該章至少要依序讀的章數）：PDE 39（PDE.6）、PR 39（PR.5）、FA 37（FA.10）、MT 36（FA.1b）、CA2 35（CA.13）、HA 35（HA.10）、MA 34（MA.21）、CA 33（CA.5）、AL4 33（AL4.10）、AM 33（AM.2）、GEO 32（GEO.22）、NLA 31（NLA.24）、ST 31（ST.6a）、AN2 30（AN2.5）、AL3 30（AL3.8）、AN3 30（AN3.3）、LA4 30（LA4.15）、LA3 28（LA3.13）、AL5 27（AL5.7）、AN1 26（AN1.11）、AL2 26（AL2.9）、LA2 26（LA2.10）、AL1 22（AL1.8）、F4 21（F4.10）、LA1 21（LA1.5）、F5 19（F5.5）、F3 17（F3.4）、F2 13（F2.4）、F1 7（F1.5）

### 章高度直方圖

| 高度 | 章數 |
|---:|---:|
| 1 | 1 |
| 2 | 1 |
| 3 | 1 |
| 4 | 1 |
| 5 | 1 |
| 6 | 1 |
| 7 | 2 |
| 8 | 1 |
| 9 | 1 |
| 10 | 1 |
| 11 | 2 |
| 12 | 1 |
| 13 | 2 |
| 14 | 2 |
| 15 | 3 |
| 16 | 5 |
| 17 | 5 |
| 18 | 5 |
| 19 | 6 |
| 20 | 7 |
| 21 | 9 |
| 22 | 6 |
| 23 | 7 |
| 24 | 7 |
| 25 | 8 |
| 26 | 12 |
| 27 | 11 |
| 28 | 9 |
| 29 | 12 |
| 30 | 10 |
| 31 | 13 |
| 32 | 10 |
| 33 | 8 |
| 34 | 7 |
| 35 | 7 |
| 36 | 4 |
| 37 | 6 |
| 38 | 2 |
| 39 | 2 |

高度超過 20 的章（150 個，逐一檢查能否把 s 降成 b）：F4.10、AN2.1、AN1.2、AN2.2、AN1.5、AN1.6、AN2.3、AN1.7、AN1.11、LA1.5、AL1.7、AL1.8、AL1.9、AL1.10、LA2.6、LA2.7、LA2.8、LA2.9、LA2.10、LA3.11、LA3.12、LA3.13、AL2.2、AL2.3、AL2.4、AL2.5、AL2.6、AL2.7、AL2.8、AL2.9、AL2.10、LA4.14、LA4.15、AN2.9、AN1.8、AN2.10、AN1.3、AN2.12、AN1.9、AN1.10、AN2.11、AN2.13、AN2.4、AN2.5、AN2.6、AN2.7、AN2.8、AN3.1、AN3.2、AN3.4、AN3.3、CA.1、CA.10、CA.2、CA.3、CA.4、CA.6、CA.5、AL3.1、AL3.2、AL3.3、AL3.4、AL3.5、AL3.6、AL3.7、AL3.8、CA.11、CA.7、CA.12、CA.8a、CA.13、CA.14、AM.1、AN3.5、AN3.6、AN3.7、AM.2、AM.3、HA.9、MT.1、MT.2、MT.3、MT.4、MT.5、MT.6、FA.1a、FA.4、FA.3、MT.7、MT.8、MT.9、MT.10、FA.6、MT.11、FA.1b、FA.9、FA.7、FA.2、FA.5、FA.10、FA.11、FA.8、FA.12、FA.13、FA.14、AL4.1、AL4.2、AL4.3、AL4.4、AL4.5、AL4.6、AL4.7、AL4.8、AL4.9、AL4.10、AL4.11、AL5.1、AL5.2、AL5.3、AL5.4、AL5.5、AL5.6、AL5.7、MA.16、MA.17、MA.18、MA.19、MA.20、MA.21、HA.1、HA.2、HA.3、HA.4、HA.5、HA.6、HA.10、PR.1、PR.2、PR.3、PR.4、PR.5、PDE.1、PDE.2、PDE.3、PDE.4、PDE.5、PDE.6、GEO.22、NLA.24、ST.6a

## 資格考目標的最短必讀集合

必讀＝目標章在 s 圖上的祖先閉包（含目標本身）；b 的來源不計入。

| 目標 | 目標章數 | 必讀章數 | 對話報告手算值 | 涉及的冊 |
|---|---:|---:|---:|---|
| Complex Analysis (Ahlfors level) | 12 | **53** | 49 | F1 8、F2 5、F3 6、F4 7、AN1 9、AN2 6、CA 7、CA2 5 |
| Real Analysis (NTU qualifying exam, minimal) | 15 | **60** | 57 | F1 8、F2 5、F3 6、F4 4、F5 2、AN1 9、LA1 3、AN2 6、AN3 1、MT 15、FA 1 |
| Real Analysis (Harvard, with Fourier series) | 22 | **80** | 66 | F1 8、F2 5、F3 6、F4 5、F5 3、AN1 9、LA1 6、LA2 4、LA3 1、AN2 7、AN3 3、MT 16、FA 2、HA 5 |
| Algebra (Harvard) | 18 | **75** | 74 | F1 8、F2 5、F3 6、F4 1、F5 3、LA1 6、AL1 10、LA2 5、LA3 3、AL2 10、LA4 2、AL3 8、AL4 8 |
| Linear Algebra (Berkeley prelim) | 3 | **44** | — | F1 8、F2 5、F3 6、F4 1、F5 3、LA1 6、AL1 5、LA2 5、LA3 3、AL2 1、LA4 1 |
| Central Limit Theorem (longest-chain check) | 1 | **50** | — | F1 8、F2 5、F3 6、F4 4、F5 2、AN1 9、LA1 3、AN2 4、AN3 1、MT 7、PR 1 |
| Apostol, Mathematical Analysis, 2nd ed. (backbone) | 31 | **63** | — | F1 8、F2 5、F3 6、F4 7、F5 2、AN1 9、LA1 5、AN2 12、AN3 3、CA 6 |
| Rudin, Principles of Mathematical Analysis | 24 | **57** | — | F1 8、F2 5、F3 6、F4 5、F5 4、AN1 9、LA1 6、LA2 2、AN2 10、AN3 2 |
| Pugh, Real Mathematical Analysis | 20 | **50** | — | F1 8、F2 5、F3 6、F4 4、F5 2、AN1 9、LA1 5、AN2 8、AN3 3 |
| Axler, Measure, Integration & Real Analysis | 15 | **60** | — | F1 8、F2 5、F3 6、F4 4、F5 2、AN1 9、LA1 3、AN2 7、AN3 1、MT 15 |
| Ahlfors, Complex Analysis, 3rd ed. | 14 | **54** | — | F1 8、F2 5、F3 6、F4 7、AN1 9、AN2 6、CA 7、CA2 6 |

### Complex Analysis (Ahlfors level)

Berkeley prelim、Harvard quals、Princeton generals 的共同科目，以 UCLA／Cambridge 型的第二層為出口。Picard 走 Bloch 路線（CA.14）列入；theta 函數路線（CA.8b）是選讀，不列入。

必讀：F1.1、F1.2、F1.7、F1.3、F1.4、F1.8、F1.6、F1.5、F2.1、F2.6、F2.2、F2.3、F2.5、F3.1、F3.2、F3.5、F3.9、F3.10、F3.4、F4.6、F4.7、F4.8、F4.9、F4.1、F4.10、F4.11、AN1.1、AN1.4、AN2.1、AN1.2、AN2.2、AN1.5、AN1.6、AN2.3、AN1.7、AN1.8、AN1.3、AN1.9、AN1.10、AN2.4、AN2.5、CA.1、CA.10、CA.2、CA.3、CA.4、CA.6、CA.5、CA.11、CA.7、CA.12、CA.8a、CA.14

只借用（不必讀）：AN2.11、AN3.1、AN3.4

### Real Analysis (NTU qualifying exam, minimal)

台大博士班資格考必考實分析；考綱原文未取得，範圍依 Folland 第 1–5 章（Wisconsin 的參考範圍）推估。

必讀：F1.1、F1.2、F1.7、F1.3、F1.4、F1.8、F1.6、F1.5、F2.1、F2.6、F2.2、F2.3、F2.5、F3.1、F3.2、F3.5、F3.9、F3.10、F3.4、F4.6、F4.7、F4.8、F4.11、F5.2、F5.4、AN1.1、AN1.4、AN2.1、AN1.2、AN2.2、AN1.5、AN1.6、AN2.3、AN1.7、LA1.0、LA1.1、LA1.2、AN1.8、AN1.3、AN1.9、AN2.6、AN2.7、AN2.8、AN3.4、HA.9、MT.1、MT.2、MT.3、MT.4、FA.1a、FA.4、FA.3、MT.7、MT.8、MT.9、MT.10、FA.6、MT.11、FA.1b、FA.2

只借用（不必讀）：F2.4、LA2.7

### Real Analysis (Harvard, with Fourier series)

台大版再加 Fourier 級數與變換、弱拓樸。

必讀：F1.1、F1.2、F1.7、F1.3、F1.4、F1.8、F1.6、F1.5、F2.1、F2.6、F2.2、F2.3、F2.5、F3.1、F3.2、F3.5、F3.9、F3.10、F3.4、F4.6、F4.7、F4.8、F4.1、F4.11、F5.2、F5.3、F5.4、AN1.1、AN1.4、AN2.1、AN1.2、AN2.2、AN1.5、AN1.6、AN2.3、AN1.7、LA1.0、LA1.1、LA1.2、LA1.3、LA1.4、LA1.5、LA2.6、LA2.7、LA2.8、LA2.9、LA3.11、AN1.8、AN1.3、AN1.9、AN1.10、AN2.6、AN2.7、AN2.8、AN3.1、AN3.2、AN3.4、HA.9、MT.1、MT.2、MT.3、MT.4、MT.5、FA.1a、FA.4、FA.3、MT.7、MT.8、MT.9、MT.10、FA.6、MT.11、FA.1b、FA.2、FA.5、HA.1、HA.2、HA.3、HA.5、HA.6

只借用（不必讀）：F2.4、LA4.14、AN2.9

### Algebra (Harvard)

Harvard 考綱：Sylow、p 群、可解群、自由群；張量積、行列式、Jordan 標準形、PID、UFD；分裂體、可分擴張；Serre 表示論 §1–6。

必讀：F1.1、F1.2、F1.7、F1.3、F1.4、F1.8、F1.6、F1.5、F2.1、F2.6、F2.2、F2.3、F2.5、F3.1、F3.2、F3.5、F3.9、F3.10、F3.4、F4.1、F5.2、F5.3、F5.4、LA1.0、LA1.1、LA1.2、LA1.3、LA1.4、LA1.5、AL1.2、AL1.3、AL1.4、AL1.5、AL1.6、AL1.7、AL1.8、AL1.9、AL1.10、AL1.11、LA2.6、LA2.7、LA2.8、LA2.9、LA2.10、LA3.11、LA3.12、LA3.13、AL2.1、AL2.2、AL2.3、AL2.4、AL2.5、AL2.6、AL2.7、AL2.8、AL2.9、AL2.10、LA4.14、LA4.15、AL3.1、AL3.2、AL3.3、AL3.4、AL3.5、AL3.6、AL3.7、AL3.8、AL4.1、AL4.2、AL4.3、AL4.4、AL4.5、AL4.8、AL4.9、AL4.10

只借用（不必讀）：F2.4、AN1.6、AN1.10

### Linear Algebra (Berkeley prelim)

Berkeley prelim 線代題，程度為大學 honors 課。

必讀：F1.1、F1.2、F1.7、F1.3、F1.4、F1.8、F1.6、F1.5、F2.1、F2.6、F2.2、F2.3、F2.5、F3.1、F3.2、F3.5、F3.9、F3.10、F3.4、F4.1、F5.2、F5.3、F5.4、LA1.0、LA1.1、LA1.2、LA1.3、LA1.4、LA1.5、AL1.2、AL1.3、AL1.4、AL1.5、AL1.6、LA2.6、LA2.7、LA2.8、LA2.9、LA2.10、LA3.11、LA3.12、LA3.13、AL2.1、LA4.14

只借用（不必讀）：F2.4、AN1.6、AN1.10

### Central Limit Theorem (longest-chain check)

對話報告的最長鏈終點。PR.1 已含 Lindeberg CLT。

必讀：F1.1、F1.2、F1.7、F1.3、F1.4、F1.8、F1.6、F1.5、F2.1、F2.6、F2.2、F2.3、F2.5、F3.1、F3.2、F3.5、F3.9、F3.10、F3.4、F4.6、F4.7、F4.8、F4.11、F5.2、F5.4、AN1.1、AN1.4、AN2.1、AN1.2、AN2.2、AN1.5、AN1.6、AN2.3、AN1.7、LA1.0、LA1.1、LA1.2、AN1.8、AN1.3、AN1.9、AN2.6、AN3.4、HA.9、MT.1、MT.2、MT.3、MT.4、MT.7、MT.8、PR.1

只借用（不必讀）：F2.4、LA2.7

### Apostol, Mathematical Analysis, 2nd ed. (backbone)

大學部分析的冊與章序照 Apostol MA 的章序與廣度走（作者 2026-10-25 更正）；10、15 延後到 MT，11 是支線 HA。

必讀：F1.1、F1.2、F1.7、F1.3、F1.4、F1.8、F1.6、F1.5、F2.1、F2.6、F2.2、F2.3、F2.5、F3.1、F3.2、F3.5、F3.9、F3.10、F3.4、F4.6、F4.7、F4.8、F4.9、F4.1、F4.10、F4.11、F5.2、F5.4、AN1.1、AN1.4、AN2.1、AN1.2、AN2.2、AN1.5、AN1.6、AN2.3、AN1.7、LA1.0、LA1.1、LA1.2、LA1.3、LA1.4、AN2.9、AN1.8、AN2.10、AN1.3、AN2.12、AN1.9、AN1.10、AN2.11、AN2.13、AN2.4、AN2.5、AN2.6、AN3.1、AN3.2、AN3.4、CA.1、CA.2、CA.3、CA.4、CA.6、CA.5

只借用（不必讀）：F2.4、LA2.7、LA4.14

支線覆蓋（不計入必讀）：HA.1、HA.2、HA.3、HA.4、HA.5

延後覆蓋（不計入必讀）：MT.1、MT.2、MT.4、MT.5、MT.7

### Rudin, Principles of Mathematical Analysis

讀完 AN1、AN2、AN3、CA 應已吸收 PMA 1–7、9；PMA 8 的 Fourier 部分由支線 HA 覆蓋，10、11 延後。

必讀：F1.1、F1.2、F1.7、F1.3、F1.4、F1.8、F1.6、F1.5、F2.1、F2.6、F2.2、F2.3、F2.5、F3.1、F3.2、F3.5、F3.9、F3.10、F3.4、F4.6、F4.7、F4.8、F4.1、F4.11、F5.2、F5.3、F5.4、F5.5、AN1.1、AN1.4、AN2.1、AN1.2、AN2.2、AN1.5、AN1.6、AN2.3、AN1.7、LA1.0、LA1.1、LA1.2、LA1.3、LA1.4、LA1.5、LA2.6、LA2.7、AN2.9、AN1.8、AN2.10、AN1.3、AN1.9、AN1.10、AN2.11、AN2.4、AN2.5、AN2.6、AN3.1、AN3.2

只借用（不必讀）：F2.4、LA4.14

選讀的目標章（不計入必讀）：F3.3

支線覆蓋（不計入必讀）：HA.1、HA.2、HA.3

延後覆蓋（不計入必讀）：AN3.6、AN3.7、AM.1、MT.1、MT.2、MT.7

### Pugh, Real Mathematical Analysis

Pugh 1–5（不含 forms、Stokes、Brouwer）在主線上覆蓋；Brouwer 屬 FX 支線，不列入。

必讀：F1.1、F1.2、F1.7、F1.3、F1.4、F1.8、F1.6、F1.5、F2.1、F2.6、F2.2、F2.3、F2.5、F3.1、F3.2、F3.5、F3.9、F3.10、F3.4、F4.6、F4.7、F4.8、F4.11、F5.2、F5.4、AN1.1、AN1.4、AN2.1、AN1.2、AN2.2、AN1.5、AN1.6、AN2.3、AN1.7、LA1.0、LA1.1、LA1.2、LA1.3、LA1.4、AN1.8、AN1.3、AN2.12、AN1.9、AN1.10、AN2.4、AN2.5、AN2.6、AN3.1、AN3.2、AN3.4

只借用（不必讀）：F2.4、LA2.7、LA4.14

選讀的目標章（不計入必讀）：F3.3

延後覆蓋（不計入必讀）：AM.1、AN3.6、AN3.7、MT.1、MT.2、MT.4、MT.9、MT.10

### Axler, Measure, Integration & Real Analysis

MT 冊照 MIRA 1–10 的骨架重劃（spec/08 決策 8）；11 Fourier、12 機率屬支線。

必讀：F1.1、F1.2、F1.7、F1.3、F1.4、F1.8、F1.6、F1.5、F2.1、F2.6、F2.2、F2.3、F2.5、F3.1、F3.2、F3.5、F3.9、F3.10、F3.4、F4.6、F4.7、F4.8、F4.11、F5.2、F5.4、AN1.1、AN1.4、AN2.1、AN1.2、AN2.2、AN1.5、AN1.6、AN2.3、AN1.7、LA1.0、LA1.1、LA1.2、AN1.8、AN1.3、AN1.9、AN1.10、AN2.4、AN2.5、AN2.6、AN3.4、HA.9、MT.1、MT.2、MT.3、MT.4、FA.1a、FA.4、FA.3、MT.7、MT.9、FA.6、MT.11、FA.1b、FA.9、FA.7

只借用（不必讀）：F2.4、LA2.7

支線覆蓋（不計入必讀）：HA.10、PR.1

### Ahlfors, Complex Analysis, 3rd ed.

CA 與 CA2 兩冊合起來覆蓋 Ahlfors 1–8；橢圓函數（CA.15）是選讀。

必讀：F1.1、F1.2、F1.7、F1.3、F1.4、F1.8、F1.6、F1.5、F2.1、F2.6、F2.2、F2.3、F2.5、F3.1、F3.2、F3.5、F3.9、F3.10、F3.4、F4.6、F4.7、F4.8、F4.9、F4.1、F4.10、F4.11、AN1.1、AN1.4、AN2.1、AN1.2、AN2.2、AN1.5、AN1.6、AN2.3、AN1.7、AN1.8、AN1.3、AN1.9、AN1.10、AN2.4、AN2.5、CA.1、CA.10、CA.2、CA.3、CA.4、CA.6、CA.5、CA.11、CA.7、CA.12、CA.8a、CA.13、CA.14

只借用（不必讀）：AN2.11、AN3.1、AN3.4

選讀的目標章（不計入必讀）：CA.15

## 瓶頸：後代最多的章（s ∪ b）

| 章 | 後代章數 | 約簡後 s 入度 | 後代涉及冊數 |
|---|---:|---:|---:|
| F1.1 Connectives and Derivations | 198 | 0 | 28 |
| F1.2 Negation and Classical Logic | 197 | 1 | 28 |
| F1.7 Finding Derivations | 196 | 1 | 28 |
| F1.3 Truth, Soundness, and Completeness | 195 | 1 | 28 |
| F1.4 Predicate Logic and the Quantifier Rules | 194 | 1 | 28 |
| F1.8 Working with Quantifiers: Translation, Laws, and Search | 193 | 1 | 28 |
| F1.6 Models and Theories | 192 | 1 | 28 |
| F1.5 From Derivations to Mathematical Prose | 191 | 1 | 28 |
| F2.1 Sets | 190 | 1 | 27 |
| F2.6 Functions | 189 | 1 | 27 |
| F2.2 Induction and Recursion | 188 | 2 | 27 |
| F2.3 Cardinality | 186 | 1 | 27 |
| F2.5 Relations | 185 | 1 | 27 |
| F3.1 The ZF Fragment and the von Neumann Natural Numbers | 178 | 1 | 26 |
| F3.2 Building the Integers and the Rationals from Equivalence Classes | 177 | 1 | 26 |
| F3.5 Divisibility, Division with Remainder, and Modular Arithmetic | 175 | 1 | 26 |
| F2.4 The Axiom of Choice | 128 | 1 | 22 |
| F3.9 Ordered Fields and Sequences in an Ordered Field | 125 | 1 | 21 |
| F5.2 Fields | 125 | 1 | 21 |
| F3.10 Constructing the Real Numbers from Cauchy Sequences | 124 | 2 | 21 |

## 每冊的外部必讀量

讀完該冊主幹章之前，冊外至少要讀的章數（s 祖先閉包，扣掉本冊）。上游冊只計本冊非選讀章的邊。

| 冊 | 本冊章數（選讀） | 冊外必讀章數 | 含選讀 | 直接上游冊（s） | 只借用的冊（b） |
|---|---:|---:|---:|---|---|
| F1 Logic and Proof | 8 | 0 | 0 | — | — |
| F2 Sets and Functions | 6 | 8 | 8 | F1 | — |
| F3 Number Systems: From ℕ to ℝ | 7（1） | 13 | 13 | F2 | — |
| F4 Analytic Preliminaries | 7 | 19 | 19 | F1、F2、F3 | AN2 |
| F5 Algebraic Preliminaries | 4 | 20 | 20 | F1、F2、F3、F4 | — |
| AN1 Real Numbers, Metric Spaces, and Derivatives | 10 | 23 | 23 | F1、F2、F4 | — |
| LA1 Spaces and Maps | 6 | 18 | 18 | F1、F2、F5 | — |
| AL1 Groups | 10 | 17 | 17 | F2、F3、F5 | — |
| LA2 Determinants and the Structure of Operators | 5 | 29 | 29 | F1、F2、F4、F5、LA1 | AN1、AN2 |
| LA3 Inner Products and Spectral Theory | 3 | 33 | 33 | F2、F4、F5、LA1、LA2 | — |
| AL2 Rings and Fields | 10 | 23 | 23 | AL1、F5、LA1 | F2 |
| LA4 Forms and Multilinear Algebra | 2 | 42 | 42 | AL1、AL2、F5、LA1、LA2、LA3 | — |
| AN2 Integration, Series, and Function Spaces | 16（2） | 32 | 32 | AN1、F2、F4 | — |
| AN3 Analysis in Several Variables | 4 | 54 | 54 | AN1、AN2、LA1、LA2、LA3 | LA4 |
| CA Complex Analysis | 7 | 41 | 41 | AN1、AN2、F4 | AN3 |
| AL3 Galois Theory | 9（1） | 35 | 51 | AL1、AL2、LA1 | — |
| CA2 Complex Analysis II: Global Theory | 8（2） | 47 | 65 | CA | AN2 |
| AM Analysis on Manifolds | 6 | 68 | 68 | AN2、AN3、LA4 | — |
| MT Measure, Integration, and Real Analysis | 19 | 57 | 57 | AN1、AN2、AN3、F2、LA1、LA2、LA3 | — |
| FA Functional Analysis | 9（1） | 66 | 70 | AN2、CA、MT | — |
| AL4 Modules, Representations, and Homological Algebra | 11 | 48 | 48 | AL1、AL2、F1、F4、F5、LA1、LA2、LA3、LA4 | F2 |
| AL5 Commutative Algebra | 7 | 33 | 33 | AL2、AL4 | — |
| MA Matrix Analysis | 7（1） | 37 | 78 | F1、F4、LA1、LA2、LA3 | AN1、AN3 |
| HA Fourier Analysis | 9（2） | 61 | 62 | AN1、AN2、AN3、F4、LA3、MT | — |
| PR Measure-Theoretic Probability | 5 | 54 | 54 | AN2、F4、MT | AN1、HA |
| PDE Distributions and Sobolev Spaces | 6 | 85 | 85 | AN2、CA、HA、MT | — |
| GEO Affine and Projective Geometry | 1 | 48 | 48 | AL1、F2、F5、LA1、LA2、LA3、LA4、MA | — |
| NLA Computation and Applications | 1 | 39 | 39 | F4、LA1、LA2、LA3、MA | — |
| ST Axiomatic Set Theory | 7（1） | 45 | 52 | F2、MT | — |

## 領域覆蓋

依 `registry/fields.yaml`。「入口必讀」＝支線候選的入口先修（hook）在 s 圖上的祖先閉包章數。

| 領域 | 科目數 | 已涵蓋 | 部分 | 支線候選 | 範圍外 |
|---|---:|---:|---:|---:|---:|
| 基礎與邏輯 | 8 | 1 | 2 | 3 | 2 |
| 代數 | 13 | 6 | 3 | 1 | 3 |
| 分析 | 20 | 6 | 10 | 2 | 2 |
| 幾何與拓樸 | 13 | 1 | 2 | 4 | 6 |
| 數論 | 8 | 0 | 3 | 1 | 4 |
| 組合與離散數學 | 8 | 0 | 0 | 2 | 6 |
| 機率與統計 | 10 | 1 | 1 | 2 | 6 |
| 資訊與計算 | 9 | 0 | 2 | 0 | 7 |
| 最佳化與應用數學 | 10 | 0 | 1 | 0 | 9 |
| 數學物理 | 6 | 0 | 0 | 0 | 6 |

### 支線候選（未涵蓋，但先修已在地圖上）

入口必讀＝自己的入口先修，加上 `after` 科目（遞移）的章與入口先修，再取 s 祖先閉包。

| 科目 | 入口先修 | 先讀科目（after） | 入口必讀章數 | 備註 |
|---|---|---|---:|---|
| 模型論（Model Theory） | F1.6、ST.4 |  | 17 |  |
| 證明論（Proof Theory） | F1.3、F1.7、F1.4 |  | 5 |  |
| 可計算性理論（Computability / Recursion Theory） | F1.6、F2.3 |  | 12 |  |
| 李群與李代數（Lie Groups & Lie Algebras） | AN3.5、AL4.9、LA2.10 |  | 63 |  |
| 動力系統（Dynamical Systems） | AN3.3、AN2.4 |  | 56 |  |
| 遍歷理論（Ergodic Theory） | MT.11、FA.6、PR.1 | 動力系統 | 69 |  |
| 代數拓樸（Algebraic Topology） | AN2.7、AL1.11、AL4.11 |  | 49 | T3；Harvard quals 科目 |
| 微分拓樸（Differential Topology） | AN3.5、AN3.7 |  | 65 |  |
| 微分幾何（Differential Geometry） | AN3.5、AN3.6、AN3.7 |  | 65 | T3；Harvard quals 科目 |
| 代數幾何（Algebraic Geometry） | AL5.4、AL5.7、AN2.7 |  | 54 | T3；入口是 AL5 |
| 代數數論（Algebraic Number Theory） | AL3.3、AL5.6 |  | 41 |  |
| 計數組合學（Enumerative Combinatorics） | F2.3、AL1.6 |  | 22 | analysis-book 已刪 HAM.3（counting） |
| 圖論（Graph Theory） | F2.5、LA3.12、MA.19 |  | 41 |  |
| 隨機過程（Stochastic Processes） | PR.3 |  | 53 |  |
| 隨機微積分（Stochastic Calculus） | PR.3、FA.6 |  | 55 |  |

## 陳述讀者必讀集（spec/03 §6.2）

陳述讀者只讀定義與陳述、會套用定理，不讀證明（對應 b 邊的 R ≤ R1 門檻，不是 R1 程度的讀者）。要讀的是：目標章引用到的定義、借用的定理陳述所用的定義，以及這些章的定義與陳述再引用到的定義（遞移）。這個集合只能由書稿的 crossref 算出，目前只有純線代章有資料。書稿沒有明寫引用的隱含語彙（例如定義裡直接使用「矩陣」而不引用）看不到，所以「下界」偏低。「術語比對」再加上 `registry/terms.yaml` 的術語在定義與陳述文字裡出現、卻沒有引用的情形，常用詞會造成假陽性，所以偏高。比對只在該章的 s 閉包裡走（完整讀者讀得到的語彙，陳述讀者不會需要更多），所以估計不超過上界。真實值夾在下界與估計值之間。

結構性的章（例如 AL4.8：結合代數、自由向量空間、群作用、張量積）以定義為主，幾乎沒有「只需套用、可以跳過證明」的定理，陳述讀者必讀量本來就接近 s 閉包；這是指標在區分兩種讀者，不是計算出錯。

| 章 | 下界 | 術語比對估計 | s 閉包（上界） | 估計比下界多出的章 |
|---|---:|---:|---:|---|
| AL4.8 Algebras and Representations | 19 | 23 | 45 | F1.5（divide）、F4.1（modulus，經 LA3.12）、F5.4（degree、polynomial）、LA3.13（with-multiplicity） |
| MA.16 Norms and Matrix Analysis | 7 | 21 | 37 | F1.5（even，經 LA3.11）、F2.1（invertible、function）、F2.5（reflexive、symmetric）、F4.1（modulus，經 LA2.10）、F5.2（addition）、F5.3（group、subgroup，經 LA3.11）、F5.4（polynomial、coefficient）、LA1.0（entry、matrix）、LA1.1（vector-space、over）、LA1.2（rank）、LA1.4（equivalent、entrywise）、LA1.5（any-subset，經 LA3.11）、LA2.8（block-diagonal，經 LA2.9）、LA3.12（stable、symbol） |
| MA.17 Variational Principles and Interlacing | 11 | 22 | 38 | F1.5（even，經 LA3.11）、F2.1（function、invertible）、F2.5（symmetric）、F4.1（imaginary-part）、F5.2（field）、F5.3（group、subgroup，經 LA3.11）、F5.4（monic、polynomial，經 LA3.11）、LA1.0（matrix、diagonal）、LA1.1（subspace、over）、LA1.4（entrywise、equivalent）、LA1.5（any-subset，經 LA3.11） |
| MA.18 Convexity | 10 | 23 | 39 | F1.5（even，經 LA1.4）、F4.1（modulus，經 LA2.10）、F5.2（addition）、F5.3（subgroup、group，經 LA2.7）、F5.4（coefficient）、LA1.0（matrix、entry）、LA1.2（rank）、LA1.3（solution、permutation-matrix）、LA1.5（linear-functional、hyperplane）、LA2.7（increasing、linear）、LA2.8（schur-complement，經 LA3.13）、LA3.12（stable、symbol，經 MA.16）、MA.17（same-number，經 LA1.3） |
| MA.19 Nonnegative Matrices | 15 | 24 | 40 | F1.5（even、odd，經 LA2.7）、F2.5（block、symmetric）、F4.1（modulus、real-part）、F5.2（multiplication）、F5.3（subgroup、group，經 LA2.7）、F5.4（coefficient、degree，經 LA2.7）、LA1.0（matrix、entry）、LA1.1（vector、length）、LA1.5（linear-functional、hyperplane，經 MA.18） |
| MA.20 Perturbation Theory | 15 | 25 | 41 | F1.5（even，經 LA3.11）、F2.5（block）、F4.1（modulus）、F5.2（field，經 MA.17）、F5.3（group、subgroup，經 LA3.11）、F5.4（monic、degree）、LA1.0（matrix、diagonal）、LA1.1（over、coordinate）、LA1.5（any-subset，經 LA3.11）、MA.19（edge，經 LA1.3） |
| MA.21 Matrix Inequalities | 14 | 25 | 42 | F1.5（prime，經 LA2.10）、F2.5（symmetric、partition）、F4.1（imaginary-part，經 MA.17）、F5.2（field，經 MA.17）、F5.3（subgroup、group，經 LA2.7）、F5.4（polynomial、coefficient，經 MA.16）、LA1.0（matrix、entry）、LA1.1（list、over）、LA1.5（linear-functional、hyperplane，經 MA.18）、LA2.7（increasing、inversion）、MA.19（edge，經 LA1.3） |
| GEO.22 Affine and Projective Geometry | 20 | 26 | 48 | F1.5（even、odd，經 LA4.14）、F4.1（imaginary-part，經 MA.17）、F5.2（field）、F5.4（polynomial）、LA1.0（matrix、diagonal）、LA4.15（form、order） |
| NLA.24 Computation and Applications | 14 | 23 | 39 | F1.5（even）、F2.5（symmetric、block）、F4.1（modulus）、F5.2（field、multiplication）、F5.3（group、subgroup，經 LA3.11）、F5.4（degree、coefficient）、LA1.1（vector、dimension）、LA1.5（annihilator）、LA2.7（characteristic-polynomial、determinant） |

影響最大的術語：「支撐」＝上表多出的章裡，有幾章（各列合計）是經由這個詞的比對進來的；「唯一」＝只拿掉這個詞，估計合計會少幾章（多數章同時被好幾個詞拉進來，所以通常很小）。分流 terms.yaml 的 `also` 時從上面幾個詞開始：常用詞（even、over 之類）多半是假陽性，可以加進 seed_terms.py 的 STOP 或標成 meta。F1 的邏輯用語已標為 `meta`，不參與比對。

| 術語 | 正式定義所在 | 支撐 | 唯一 |
|---|---|---:|---:|
| degree | F5.4 | 9 | 0 |
| coefficient | F5.4 | 9 | 0 |
| leading-coefficient | F5.4 | 9 | 0 |
| monic | F5.4 | 9 | 0 |
| polynomial | F5.4 | 9 | 0 |
| odd | F1.5 | 9 | 0 |
| divide | F1.5 | 9 | 0 |
| even | F1.5 | 9 | 0 |
| prime | F1.5 | 9 | 0 |
| modulus | F4.1 | 9 | 2 |
| characteristic | F5.2 | 8 | 0 |
| addition | F5.2 | 8 | 0 |
| multiplication | F5.2 | 8 | 0 |
| field | F5.2 | 8 | 0 |
| annihilator | LA1.5 | 7 | 0 |

術語比對找到、但不在該章 s 閉包裡的章（同形異義、前向提及，或地圖漏了一條邊；分流 terms.yaml 的 also 之後會減少）：

- AL4.8：F5.5、MA.18、HA.5
- MA.16：AN1.1、AN1.2、AN1.5、MA.18、GEO.22、NLA.24
- MA.17：AN1.1、LA4.14、LA4.15、MA.18、GEO.22、NLA.24
- MA.18：AN1.1、AN2.1、AN1.5、LA4.15、AL4.8、GEO.22、NLA.24
- MA.19：F5.5、LA4.14、LA4.15、AL4.8、NLA.24
- MA.20：F5.5、AN1.1、LA4.14、LA4.15、GEO.22、NLA.24
- MA.21：AN1.1、AN1.5、LA4.14、LA4.15、GEO.22
- GEO.22：AN1.1、AL4.8、MA.19
- NLA.24：AN1.1、LA4.14、LA4.15、AL4.8、MA.18、MA.19、GEO.22

## 線代書計算邊的抽查：LA3 能否跳過 LA2 第 10 章

- LA3.12 ← LA2.10：see，硬引用 0、軟引用 9。

結論：LA3 的 s 祖先閉包不含 LA2.10，可以跳過第 10 章（已套用 registry/moves.yaml 的計畫搬家，書稿尚未改）。

