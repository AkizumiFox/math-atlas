# 地圖統計（由 `tools/atlas.py stats` 產生，勿手改）

- 冊：25；章：172（選讀 12）
- 章層級邊：s 567、b 21、軟邊 91；其中 286 條 s 邊是從線代書的證明計算出來的，其餘是計畫值

除非欄位註明「含選讀」，以下統計都排除選讀章（opt）。

## 最長硬依賴鏈（只計 s）

**27 章**，終點 PDE.6 Capstone: The Dirichlet Problem and the Dirichlet-Laplacian Eigenbasis：

F1.1 → F1.2 → F1.4 → F1.5 → F2.1 → F2.2 → AN1.1 → AN1.2 → AN1.4 → AN1.5 → AN1.6 → AN1.7 → AN1.8 → AN1.9 → AN2.2 → AN2.3 → AN3.4 → MT.1 → MT.2 → MT.3 → MT.4 → MT.5 → MT.6 → PDE.1 → PDE.4 → PDE.5 → PDE.6

各冊最高的章（高度＝從零讀到該章至少要依序讀的章數）：PDE 27（PDE.6）、MA 26（MA.21）、PR 26（PR.3）、AL4 25（AL4.10）、AN3 24（AN3.7）、GEO 24（GEO.22）、FA 24（FA.1b）、MT 24（MT.10）、NLA 23（NLA.24）、AL3 22（AL3.8）、CA 22（CA.8a）、LA4 22（LA4.15）、HA 20（HA.4）、LA3 20（LA3.13）、AL5 19（AL5.7）、ST 19（ST.6a）、AL2 18（AL2.9）、AN2 18（AN2.8）、LA2 18（LA2.10）、AN1 15（AN1.10）、AL1 14（AL1.8）、LA1 13（LA1.5）、F3 9（F3.8）、F2 8（F2.4）、F1 4（F1.5）

### 章高度直方圖

| 高度 | 章數 |
|---:|---:|
| 1 | 1 |
| 2 | 1 |
| 3 | 2 |
| 4 | 1 |
| 5 | 1 |
| 6 | 2 |
| 7 | 3 |
| 8 | 4 |
| 9 | 6 |
| 10 | 5 |
| 11 | 7 |
| 12 | 7 |
| 13 | 8 |
| 14 | 6 |
| 15 | 6 |
| 16 | 8 |
| 17 | 14 |
| 18 | 14 |
| 19 | 14 |
| 20 | 8 |
| 21 | 9 |
| 22 | 6 |
| 23 | 8 |
| 24 | 8 |
| 25 | 7 |
| 26 | 3 |
| 27 | 1 |

高度超過 20 的章（42 個，逐一檢查能否把 s 降成 b）：LA4.14、LA4.15、AN3.6、AN3.7、AL3.4、AL3.5、AL3.7、AL3.8、MT.4、MT.5、MT.6、MT.7、MT.8、MT.9、MT.10、MT.11、CA.5、CA.7、CA.8a、FA.1b、FA.2、AL4.8、AL4.9、AL4.10、MA.16、MA.17、MA.18、MA.19、MA.20、MA.21、PR.1、PR.2、PR.3、PR.4、PDE.1、PDE.2、PDE.3、PDE.4、PDE.5、PDE.6、GEO.22、NLA.24

## 資格考目標的最短必讀集合

必讀＝目標章在 s 圖上的祖先閉包（含目標本身）；b 的來源不計入。

| 目標 | 目標章數 | 必讀章數 | 對話報告手算值 | 涉及的冊 |
|---|---:|---:|---:|---|
| Complex Analysis (Ahlfors level) | 7 | **37** | 49 | F1 4、F2 3、AN1 11、F3 4、LA1 3、AN2 5、CA 7 |
| Real Analysis (NTU qualifying exam, minimal) | 15 | **45** | 57 | F1 4、F2 3、AN1 10、F3 3、LA1 3、AN2 6、AN3 1、MT 9、FA 6 |
| Real Analysis (Harvard, with Fourier series) | 22 | **66** | 66 | F1 4、F2 3、AN1 11、F3 4、LA1 6、AL1 1、LA2 4、LA3 1、AN2 7、AN3 3、HA 5、MT 10、FA 7 |
| Algebra (Harvard) | 18 | **63** | 74 | F1 4、F2 2、F3 4、LA1 6、AL1 11、LA2 5、LA3 3、LA4 2、AL2 10、AL3 8、AL4 8 |
| Linear Algebra (Berkeley prelim) | 3 | **26** | — | F1 4、F2 2、F3 4、LA1 6、AL1 1、LA2 5、LA3 3、LA4 1 |
| Central Limit Theorem (longest-chain check) | 1 | **34** | — | F1 4、F2 3、AN1 10、F3 3、LA1 3、AN2 3、AN3 1、MT 6、PR 1 |

### Complex Analysis (Ahlfors level)

Berkeley prelim、Harvard quals、Princeton generals 的共同科目。Picard（CA.8b）不列入。

必讀：F1.1、F1.2、F1.4、F1.5、F2.1、F2.2、F2.3、AN1.1、AN1.2、AN1.3、AN1.4、AN1.5、AN1.6、AN1.7、AN1.8、AN1.9、AN1.10、AN1.11、F3.5、F3.6、F3.7、F3.8、LA1.0、LA1.1、LA1.2、AN2.1、AN2.2、AN2.3、AN2.4、AN2.5、CA.1、CA.2、CA.3、CA.4、CA.5、CA.6、CA.7

只借用（不必讀）：F2.4、LA3.11、AN3.1、AN3.4

### Real Analysis (NTU qualifying exam, minimal)

台大博士班資格考必考實分析；考綱原文未取得，範圍依 Folland 第 1–5 章（Wisconsin 的參考範圍）推估。

必讀：F1.1、F1.2、F1.4、F1.5、F2.1、F2.2、F2.3、AN1.1、AN1.2、AN1.3、AN1.4、AN1.5、AN1.6、AN1.7、AN1.8、AN1.9、AN1.11、F3.5、F3.7、F3.8、LA1.0、LA1.1、LA1.2、AN2.1、AN2.2、AN2.3、AN2.6、AN2.7、AN2.8、AN3.4、MT.1、MT.2、MT.3、MT.4、MT.7、MT.8、MT.9、MT.10、MT.11、FA.1a、FA.1b、FA.2、FA.3、FA.4、FA.6

只借用（不必讀）：F2.4、LA2.7、LA3.11

### Real Analysis (Harvard, with Fourier series)

台大版再加 Fourier 級數與變換、弱拓樸。

必讀：F1.1、F1.2、F1.4、F1.5、F2.1、F2.2、F2.3、AN1.1、AN1.2、AN1.3、AN1.4、AN1.5、AN1.6、AN1.7、AN1.8、AN1.9、AN1.10、AN1.11、F3.5、F3.6、F3.7、F3.8、LA1.0、LA1.1、LA1.2、LA1.3、LA1.4、LA1.5、LA2.6、LA2.7、LA2.8、LA2.9、LA3.11、AN2.1、AN2.2、AN2.3、AN2.4、AN2.6、AN2.7、AN2.8、AN3.1、AN3.2、AN3.4、AL1.1、HA.1、HA.2、HA.3、HA.5、HA.6、MT.1、MT.2、MT.3、MT.4、MT.5、MT.7、MT.8、MT.9、MT.10、MT.11、FA.1a、FA.1b、FA.2、FA.3、FA.4、FA.5、FA.6

只借用（不必讀）：F2.4、LA4.14

### Algebra (Harvard)

Harvard 考綱：Sylow、p 群、可解群、自由群；張量積、行列式、Jordan 標準形、PID、UFD；分裂體、可分擴張；Serre 表示論 §1–6。

必讀：F1.1、F1.2、F1.4、F1.5、F2.1、F2.2、F3.5、F3.6、F3.7、F3.8、LA1.0、LA1.1、LA1.2、LA1.3、LA1.4、LA1.5、LA2.6、LA2.7、LA2.8、LA2.9、LA2.10、LA3.11、LA3.12、LA3.13、LA4.14、LA4.15、AL1.1、AL1.2、AL1.3、AL1.4、AL1.5、AL1.6、AL1.7、AL1.8、AL1.9、AL1.10、AL1.11、AL2.1、AL2.2、AL2.3、AL2.4、AL2.5、AL2.6、AL2.7、AL2.8、AL2.9、AL2.10、AL3.1、AL3.2、AL3.3、AL3.4、AL3.5、AL3.6、AL3.7、AL3.8、AL4.1、AL4.2、AL4.3、AL4.4、AL4.5、AL4.8、AL4.9、AL4.10

只借用（不必讀）：F2.4、AN1.1、AN1.6、AN1.10

### Linear Algebra (Berkeley prelim)

Berkeley prelim 線代題，程度為大學 honors 課。

必讀：F1.1、F1.2、F1.4、F1.5、F2.1、F2.2、F3.5、F3.6、F3.7、F3.8、LA1.0、LA1.1、LA1.2、LA1.3、LA1.4、LA1.5、LA2.6、LA2.7、LA2.8、LA2.9、LA2.10、LA3.11、LA3.12、LA3.13、LA4.14、AL1.1

只借用（不必讀）：F2.4、AN1.1、AN1.6、AN1.10

### Central Limit Theorem (longest-chain check)

對話報告的最長鏈終點。PR.1 已含 Lindeberg CLT。

必讀：F1.1、F1.2、F1.4、F1.5、F2.1、F2.2、F2.3、AN1.1、AN1.2、AN1.3、AN1.4、AN1.5、AN1.6、AN1.7、AN1.8、AN1.9、AN1.11、F3.5、F3.7、F3.8、LA1.0、LA1.1、LA1.2、AN2.1、AN2.2、AN2.3、AN3.4、MT.1、MT.2、MT.3、MT.4、MT.7、MT.8、PR.1

只借用（不必讀）：F2.4、LA2.7、LA3.11

## 瓶頸：後代最多的章（s ∪ b）

| 章 | 後代章數 | 約簡後 s 入度 | 後代涉及冊數 |
|---|---:|---:|---:|
| F1.1 Connectives and Derivations | 159 | 0 | 24 |
| F1.2 Negation, Classical Logic and Finding Derivations | 158 | 1 | 24 |
| F1.4 Predicate Logic and the Quantifier Rules | 156 | 1 | 24 |
| F1.5 From Derivations to Mathematical Prose | 155 | 1 | 24 |
| F2.1 Sets, Functions, Images and Preimages | 154 | 1 | 23 |
| F2.2 Equivalence Relations, Orders, and Induction | 153 | 1 | 23 |
| F2.3 Cardinality: Countable and Uncountable Sets | 131 | 1 | 21 |
| F3.5 Divisibility, Division with Remainder and ℤ/nℤ | 131 | 1 | 21 |
| AL1.1 Groups, Subgroups and Homomorphisms | 121 | 1 | 19 |
| F2.4 Zorn's Lemma | 119 | 1 | 20 |
| F3.7 Fields | 116 | 1 | 20 |
| F3.8 Formal Polynomials | 113 | 1 | 20 |
| LA1.1 Vector Spaces | 110 | 1 | 19 |
| LA1.0 Matrices | 98 | 1 | 17 |
| LA1.2 Linear Maps | 96 | 2 | 17 |
| AN1.1 Ordered Fields and the Least Upper Bound Axiom | 94 | 1 | 17 |
| AN1.2 Sequences, Subsequences and Cauchy Sequences | 92 | 1 | 16 |
| AN1.4 Open, Closed and Compact Subsets of ℝ | 90 | 2 | 16 |
| AN1.5 Limits of Functions and Continuity | 89 | 1 | 16 |
| AN1.6 Continuous Functions on Compact Sets and Intervals | 88 | 1 | 16 |

## 每冊的外部必讀量

讀完該冊主幹章之前，冊外至少要讀的章數（s 祖先閉包，扣掉本冊）。上游冊只計本冊非選讀章的邊。

| 冊 | 本冊章數（選讀） | 冊外必讀章數 | 含選讀 | 直接上游冊（s） | 只借用的冊（b） |
|---|---:|---:|---:|---|---|
| F1 Logic and Proof | 5 | 0 | 0 | — | — |
| F2 Sets, Functions and Relations | 4 | 4 | 4 | F1 | — |
| AN1 Analysis on the Real Line | 11 | 7 | 7 | F1、F2 | — |
| F3 Number Systems and Algebraic Preliminaries | 8（4） | 6 | 8 | F1、F2 | AN1 |
| LA1 Spaces and Maps | 6 | 9 | 9 | F1、F2、F3 | — |
| AL1 Groups | 11 | 7 | 7 | F1、F2、F3 | — |
| LA2 Determinants and the Structure of Operators | 5 | 17 | 17 | AL1、F1、F2、F3、LA1 | AN1 |
| LA3 Inner Products and Spectral Theory | 3 | 21 | 21 | F2、F3、LA1、LA2 | — |
| LA4 Forms and Multilinear Algebra | 2 | 24 | 24 | AL1、F3、LA1、LA2、LA3 | — |
| AN2 Metric and Topological Spaces | 8 | 24 | 24 | AN1、F2、LA1 | LA3 |
| AN3 Analysis in Several Variables | 7 | 43 | 43 | AN1、AN2、LA1、LA2、LA3、LA4 | — |
| AL2 Rings and Fields | 10 | 14 | 14 | AL1、F3、LA1 | F2 |
| AL3 Galois Theory | 9（1） | 26 | 43 | AL1、AL2、LA1 | — |
| HA Fourier Analysis | 9（2） | 39 | 40 | AN1、AN2、AN3、F3、LA3 | — |
| MT Measure and Integration | 11 | 41 | 41 | AN1、AN2、AN3、F2、LA2、LA3 | — |
| CA Complex Analysis | 10（2） | 30 | 55 | AN1、AN2、F3 | AN3 |
| FA Functional Analysis | 9（1） | 39 | 42 | AN2、MT | F2 |
| AL4 Modules, Representations and Homological Algebra | 11 | 36 | 36 | AL1、AL2、F1、F3、LA1、LA2、LA3、LA4 | F2 |
| AL5 Commutative Algebra | 7 | 24 | 24 | AL2、AL4 | — |
| MA Matrix Analysis | 7（1） | 25 | 61 | F1、F3、LA1、LA2、LA3 | AN1、AN2、AN3 |
| PR Measure-Theoretic Probability | 4 | 36 | 36 | AN1、F3、MT | HA |
| PDE Distributions and Sobolev Spaces | 6 | 67 | 67 | AN2、CA、FA、HA、MT | — |
| GEO Affine and Projective Geometry | 1 | 30 | 30 | AL1、F2、LA1、LA2、LA3、LA4、MA | — |
| NLA Computation and Applications | 1 | 27 | 27 | F3、LA1、LA2、LA3、MA | — |
| ST Axiomatic Set Theory | 7（1） | 29 | 36 | F2、MT | — |

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
| 模型論（Model Theory） | F1.4、ST.4 |  | 11 |  |
| 證明論（Proof Theory） | F1.3、F1.4 |  | 4 |  |
| 可計算性理論（Computability / Recursion Theory） | F1.4、F2.3 |  | 7 |  |
| 李群與李代數（Lie Groups & Lie Algebras） | AN3.5、AL4.9、LA2.10 |  | 53 |  |
| 動力系統（Dynamical Systems） | AN3.3、AN2.4 |  | 42 |  |
| 遍歷理論（Ergodic Theory） | MT.11、FA.6、PR.1 | 動力系統 | 53 |  |
| 代數拓樸（Algebraic Topology） | AN2.7、AL1.11、AL4.11 |  | 39 | T3；Harvard quals 科目 |
| 微分拓樸（Differential Topology） | AN3.5、AN3.7 |  | 48 |  |
| 微分幾何（Differential Geometry） | AN3.5、AN3.6、AN3.7 |  | 48 | T3；Harvard quals 科目 |
| 代數幾何（Algebraic Geometry） | AL5.4、AL5.7、AN2.7 |  | 44 | T3；入口是 AL5 |
| 代數數論（Algebraic Number Theory） | AL3.3、AL5.6 |  | 32 |  |
| 計數組合學（Enumerative Combinatorics） | F2.3、AL1.6 |  | 14 | analysis-book 已刪 HAM.3（counting） |
| 圖論（Graph Theory） | F2.2、LA3.12、MA.19 |  | 29 |  |
| 隨機過程（Stochastic Processes） | PR.3 |  | 37 |  |
| 隨機微積分（Stochastic Calculus） | PR.3、FA.6 |  | 39 |  |

## 陳述讀者必讀集（spec/03 §6.2）

陳述讀者只讀定義與陳述、會套用定理，不讀證明（對應 b 邊的 R ≤ R1 門檻，不是 R1 程度的讀者）。要讀的是：目標章引用到的定義、借用的定理陳述所用的定義，以及這些章的定義與陳述再引用到的定義（遞移）。這個集合只能由書稿的 crossref 算出，目前只有純線代章有資料。書稿沒有明寫引用的隱含語彙（例如定義裡直接使用「矩陣」而不引用）看不到，所以「下界」偏低。「術語比對」再加上 `registry/terms.yaml` 的術語在定義與陳述文字裡出現、卻沒有引用的情形，常用詞會造成假陽性，所以偏高。比對只在該章的 s 閉包裡走（完整讀者讀得到的語彙，陳述讀者不會需要更多），所以估計不超過上界。真實值夾在下界與估計值之間。

結構性的章（例如 AL4.8：結合代數、自由向量空間、群作用、張量積）以定義為主，幾乎沒有「只需套用、可以跳過證明」的定理，陳述讀者必讀量本來就接近 s 閉包；這是指標在區分兩種讀者，不是計算出錯。

| 章 | 下界 | 術語比對估計 | s 閉包（上界） | 估計比下界多出的章 |
|---|---:|---:|---:|---|
| AL4.8 Algebras and Representations | 19 | 23 | 27 | F1.5（divide）、F3.6（modulus，經 LA3.12）、F3.8（degree、polynomial）、LA3.13（with-multiplicity） |
| MA.16 Norms and Matrix Analysis | 7 | 21 | 25 | F1.5（even、odd，經 LA2.7）、F2.1（invertible、function）、F2.2（reflexive、symmetric）、F3.6（modulus，經 LA2.10）、F3.7（addition）、F3.8（polynomial、coefficient）、LA1.0（entry、matrix）、LA1.1（vector-space、over）、LA1.2（rank）、LA1.4（equivalent、entrywise）、LA1.5（annihilator，經 LA2.10）、LA2.8（direct-sum、block-diagonal，經 LA2.10）、LA3.12（stable、symbol）、AL1.1（subgroup、group，經 LA2.7） |
| MA.17 Variational Principles and Interlacing | 11 | 22 | 26 | F1.5（even、odd，經 LA2.7）、F2.1（function、invertible）、F2.2（symmetric）、F3.6（imaginary-part）、F3.7（field）、F3.8（coefficient，經 LA1.3）、LA1.0（matrix、diagonal）、LA1.1（subspace、over）、LA1.4（entrywise、equivalent）、LA1.5（any-subset，經 LA3.11）、AL1.1（subgroup、group，經 LA2.7） |
| MA.18 Convexity | 10 | 23 | 27 | F1.5（even，經 LA1.4）、F3.6（modulus，經 LA2.10）、F3.7（addition）、F3.8（coefficient）、LA1.0（matrix、entry）、LA1.2（rank）、LA1.3（solution、permutation-matrix）、LA1.5（linear-functional、hyperplane）、LA2.7（increasing、linear）、LA2.8（schur-complement，經 LA3.13）、LA3.12（stable、symbol，經 MA.16）、AL1.1（subgroup、group，經 LA2.7）、MA.17（same-number，經 LA1.3） |
| MA.19 Non-negative Matrices | 15 | 24 | 28 | F1.5（even、odd，經 LA2.7）、F2.2（block、symmetric）、F3.6（modulus、real-part）、F3.7（multiplication）、F3.8（coefficient，經 LA1.3）、LA1.0（matrix、entry）、LA1.1（vector、length）、LA1.5（linear-functional、hyperplane，經 MA.18）、AL1.1（subgroup、group，經 LA2.7） |
| MA.20 Perturbation Theory | 15 | 25 | 29 | F1.5（even、odd，經 LA2.7）、F2.2（block）、F3.6（modulus）、F3.7（addition，經 MA.18）、F3.8（monic、degree）、LA1.0（matrix、diagonal）、LA1.1（over、coordinate）、LA1.5（linear-functional、hyperplane，經 MA.18）、AL1.1（subgroup、group，經 LA2.7）、MA.19（edge，經 LA1.3） |
| MA.21 Matrix Inequalities | 14 | 25 | 30 | F1.5（prime，經 LA2.10）、F2.2（symmetric、partition）、F3.6（imaginary-part，經 MA.17）、F3.7（field，經 LA1.3）、F3.8（coefficient，經 LA1.3）、LA1.0（matrix、entry）、LA1.1（list、over）、LA1.5（linear-functional、hyperplane，經 MA.18）、LA2.7（increasing、inversion）、AL1.1（subgroup、group，經 LA2.7）、MA.19（edge，經 LA1.3） |
| GEO.22 Affine and Projective Geometry | 20 | 26 | 30 | F1.5（even、odd，經 LA4.14）、F3.6（imaginary-part，經 MA.17）、F3.7（field）、F3.8（polynomial）、LA1.0（matrix、diagonal）、LA4.15（form、order） |
| NLA.24 Computation and Applications | 14 | 23 | 27 | F1.5（even）、F2.2（symmetric、block）、F3.6（modulus）、F3.7（field、multiplication）、F3.8（degree、coefficient）、LA1.1（vector、dimension）、LA1.5（annihilator）、LA2.7（characteristic-polynomial、determinant）、AL1.1（group、subgroup，經 LA3.11） |

影響最大的術語：「支撐」＝上表多出的章裡，有幾章（各列合計）是經由這個詞的比對進來的；「唯一」＝只拿掉這個詞，估計合計會少幾章（多數章同時被好幾個詞拉進來，所以通常很小）。分流 terms.yaml 的 `also` 時從上面幾個詞開始：常用詞（even、over 之類）多半是假陽性，可以加進 seed_terms.py 的 STOP 或標成 meta。F1 的邏輯用語已標為 `meta`，不參與比對。

| 術語 | 正式定義所在 | 支撐 | 唯一 |
|---|---|---:|---:|
| monic | F3.8 | 9 | 0 |
| polynomial | F3.8 | 9 | 0 |
| degree | F3.8 | 9 | 0 |
| coefficient | F3.8 | 9 | 0 |
| leading-coefficient | F3.8 | 9 | 0 |
| divide | F1.5 | 9 | 0 |
| even | F1.5 | 9 | 0 |
| prime | F1.5 | 9 | 0 |
| odd | F1.5 | 9 | 0 |
| modulus | F3.6 | 9 | 2 |
| characteristic | F3.7 | 8 | 0 |
| field | F3.7 | 8 | 0 |
| addition | F3.7 | 8 | 0 |
| multiplication | F3.7 | 8 | 0 |
| any-subset | LA1.5 | 7 | 0 |

術語比對找到、但不在該章 s 閉包裡的章（同形異義、前向提及，或地圖漏了一條邊；分流 terms.yaml 的 also 之後會減少）：

- AL4.8：HA.5、MA.18
- MA.16：AN1.1、AN1.2、AN1.5、MA.18、GEO.22、NLA.24
- MA.17：AN1.1、LA4.14、LA4.15、MA.18、GEO.22、NLA.24
- MA.18：AN1.1、AN1.5、LA4.15、AN2.1、AL4.8、GEO.22、NLA.24
- MA.19：LA4.14、LA4.15、AL4.8、NLA.24
- MA.20：AN1.1、LA4.14、LA4.15、GEO.22、NLA.24
- MA.21：AN1.1、AN1.5、LA4.14、LA4.15、GEO.22
- GEO.22：AN1.1、AL4.8、MA.19
- NLA.24：AN1.1、LA4.14、LA4.15、AL4.8、MA.18、MA.19、GEO.22

## 線代書計算邊的抽查：LA3 能否跳過 LA2 第 10 章

- LA3.12 ← LA2.10：see，硬引用 0、軟引用 9。

結論：LA3 的 s 祖先閉包不含 LA2.10，可以跳過第 10 章（已套用 registry/moves.yaml 的計畫搬家，書稿尚未改）。

