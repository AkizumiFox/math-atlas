# 教材地圖（由 `tools/atlas.py render` 產生，勿手改）

實線＝s（需讀），虛線＝b（借用具名結果）。see／revisits 不畫。圖已做傳遞約簡，只為了好讀；
完整的直接邊在 registry 與 `atlas.html`。互動版：用瀏覽器開 `atlas.html`。

## 冊層級

```mermaid
flowchart TD
  F1["F1 邏輯與證明"]:::found
  F2["F2 集合、函數與關係"]:::found
  AN1["AN1 實數線上的分析"]:::analysis
  F3["F3 數系與代數預備"]:::found
  LA1["LA1 空間與映射"]:::linalg
  AL1["AL1 群"]:::algebra
  LA2["LA2 行列式與算子的結構"]:::linalg
  LA3["LA3 內積與譜理論"]:::linalg
  LA4["LA4 形式與多線性代數"]:::linalg
  AN2["AN2 度量空間與拓樸"]:::analysis
  AN3["AN3 多變數分析"]:::analysis
  AL2["AL2 環與體"]:::algebra
  AL3["AL3 Galois 理論"]:::algebra
  HA["HA Fourier 分析"]:::analysis
  MT["MT 測度與積分"]:::analysis
  CA["CA 複分析"]:::analysis
  FA["FA 泛函分析"]:::analysis
  AL4["AL4 模、表示與同調入門"]:::algebra
  AL5["AL5 交換代數"]:::algebra
  MA["MA 矩陣分析"]:::linalg
  PR["PR 測度論機率"]:::side
  PDE["PDE 分佈與 Sobolev 空間"]:::side
  GEO["GEO 仿射與射影幾何"]:::side
  NLA["NLA 計算與應用"]:::side
  ST["ST 公理集合論"]:::side
  F1 --> F2
  F2 --> AN1
  AN1 --> F3
  F3 --> LA1
  F3 --> AL1
  AL1 --> LA2
  LA1 --> LA2
  LA2 --> LA3
  LA3 --> LA4
  LA3 -.-> AN2
  AN2 --> AN3
  LA4 --> AN3
  AL1 --> AL2
  LA1 --> AL2
  AL2 --> AL3
  AN2 --> AL3
  AN3 --> HA
  AN3 --> MT
  FA --> CA
  CA --> FA
  AL2 --> AL4
  LA4 --> AL4
  AL4 --> AL5
  CA --> MA
  HA -.-> PR
  MT --> PR
  MA --> GEO
  MA --> NLA
  MT --> ST
  classDef found fill:#e8e2f4,stroke:#888,color:#222
  classDef analysis fill:#dcebf7,stroke:#888,color:#222
  classDef linalg fill:#dff2e1,stroke:#888,color:#222
  classDef algebra fill:#fbe6d4,stroke:#888,color:#222
  classDef side fill:#eeeeee,stroke:#888,color:#222
```

## F1 邏輯與證明

```mermaid
flowchart LR
  F1_1["1 連接詞與推導"]
  F1_2["2 否定、古典邏輯與推導的尋找"]
  F1_3["3 真值、健全性與完備性"]
  F1_4["4 述詞邏輯與量詞規則"]
  F1_5["5 從推導到數學文字"]
  F1_1 --> F1_2
  F1_2 --> F1_3
  F1_2 --> F1_4
  F1_4 --> F1_5
  classDef ext fill:#e6e6e6,stroke:#999,color:#555
  classDef opt fill:#fff,stroke:#999,stroke-dasharray:4 3,color:#555
  classDef segb fill:#f6f6fb,stroke:#99a,color:#333
```

## F2 集合、函數與關係

```mermaid
flowchart LR
  F1_5["F1.5 從推導到數學文字"]:::ext
  F2_1["1 集合、函數、像與原像"]
  F2_2["2 等價關係、序與歸納"]
  F2_3["3 基數：可數與不可數（含選擇公理的陳述）"]
  F2_4["4 Zorn 引理（使用者層級）"]
  F1_5 --> F2_1
  F2_1 --> F2_2
  F2_2 --> F2_3
  F2_3 --> F2_4
  classDef ext fill:#e6e6e6,stroke:#999,color:#555
  classDef opt fill:#fff,stroke:#999,stroke-dasharray:4 3,color:#555
  classDef segb fill:#f6f6fb,stroke:#99a,color:#333
```

## AN1 實數線上的分析

```mermaid
flowchart LR
  F2_2["F2.2 等價關係、序與歸納"]:::ext
  F2_3["F2.3 基數：可數與不可數（含選擇公理的陳述）"]:::ext
  AN1_1["1 有序體與最小上界公理"]
  AN1_2["2 數列、子列與 Cauchy 列"]
  AN1_3["3 無窮級數"]
  AN1_4["4 ℝ 的開集、閉集與緊集"]
  AN1_5["5 函數極限與連續"]
  AN1_6["6 緊集與區間上的連續函數"]
  AN1_7["7 導數與均值定理"]
  AN1_8["8 Riemann–Darboux 積分"]
  AN1_9["9 函數列與函數級數"]
  AN1_10["10 冪級數、Taylor 級數與初等函數"]
  AN1_11["11 完備性的各種形式"]
  F2_2 --> AN1_1
  AN1_1 --> AN1_2
  F2_3 --> AN1_3
  AN1_2 --> AN1_3
  F2_3 --> AN1_4
  AN1_2 --> AN1_4
  AN1_4 --> AN1_5
  AN1_5 --> AN1_6
  AN1_6 --> AN1_7
  AN1_7 --> AN1_8
  AN1_3 --> AN1_9
  AN1_8 --> AN1_9
  AN1_9 --> AN1_10
  AN1_6 --> AN1_11
  classDef ext fill:#e6e6e6,stroke:#999,color:#555
  classDef opt fill:#fff,stroke:#999,stroke-dasharray:4 3,color:#555
  classDef segb fill:#f6f6fb,stroke:#99a,color:#333
```

## F3 數系與代數預備

```mermaid
flowchart LR
  F2_2["F2.2 等價關係、序與歸納"]:::ext
  F2_3["F2.3 基數：可數與不可數（含選擇公理的陳述）"]:::ext
  AN1_1["AN1.1 有序體與最小上界公理"]:::ext
  F3_1["1 自然數的 von Neumann 建構（ZF 的必要片段）"]:::opt
  F3_2["2 以等價類建構 ℤ 與 ℚ"]:::opt
  F3_3["3 以 Dedekind 分割建構 ℝ"]:::opt
  F3_4["4 完備有序體的唯一性"]:::opt
  F3_5["5 整除、帶餘除法與 ℤ/nℤ"]
  F3_6["6 複數"]
  F3_7["7 體"]
  F3_8["8 形式多項式"]
  F2_3 --> F3_1
  F3_1 --> F3_2
  AN1_1 --> F3_3
  F3_2 --> F3_3
  AN1_1 --> F3_4
  F2_2 --> F3_5
  AN1_1 -.-> F3_6
  F3_5 --> F3_7
  F3_7 --> F3_8
  classDef ext fill:#e6e6e6,stroke:#999,color:#555
  classDef opt fill:#fff,stroke:#999,stroke-dasharray:4 3,color:#555
  classDef segb fill:#f6f6fb,stroke:#99a,color:#333
```

## LA1 空間與映射

```mermaid
flowchart LR
  F3_8["F3.8 形式多項式"]:::ext
  LA1_0["0 矩陣"]
  LA1_1["1 向量空間"]
  LA1_2["2 線性映射"]
  LA1_3["3 線性系統與矩陣"]
  LA1_4["4 映射的矩陣"]
  LA1_5["5 對偶"]
  F3_8 --> LA1_0
  F3_8 --> LA1_1
  LA1_0 --> LA1_2
  LA1_1 --> LA1_2
  LA1_0 --> LA1_3
  LA1_1 --> LA1_3
  LA1_2 --> LA1_4
  LA1_3 --> LA1_4
  LA1_4 --> LA1_5
  classDef ext fill:#e6e6e6,stroke:#999,color:#555
  classDef opt fill:#fff,stroke:#999,stroke-dasharray:4 3,color:#555
  classDef segb fill:#f6f6fb,stroke:#99a,color:#333
```

## AL1 群

```mermaid
flowchart LR
  F3_5["F3.5 整除、帶餘除法與 ℤ/nℤ"]:::ext
  AL1_1["1 群、子群與同態"]
  AL1_2["2 循環群"]
  AL1_3["3 對稱群與置換的符號"]
  AL1_4["4 陪集與 Lagrange 定理"]
  AL1_5["5 正規子群、商群與同構定理"]
  AL1_6["6 群作用、軌道—穩定子與類方程"]
  AL1_7["7 Sylow 定理"]
  AL1_8["8 直積、半直積與有限 Abel 群"]
  AL1_9["9 合成列、可解群與冪零群"]
  AL1_10["10 Aₙ 的單純性"]
  AL1_11["11 自由群與表現"]
  F3_5 --> AL1_1
  AL1_1 --> AL1_2
  AL1_1 --> AL1_3
  AL1_2 --> AL1_4
  AL1_4 --> AL1_5
  AL1_3 --> AL1_6
  AL1_5 --> AL1_6
  AL1_6 --> AL1_7
  AL1_7 --> AL1_8
  AL1_7 --> AL1_9
  AL1_6 --> AL1_10
  AL1_5 --> AL1_11
  classDef ext fill:#e6e6e6,stroke:#999,color:#555
  classDef opt fill:#fff,stroke:#999,stroke-dasharray:4 3,color:#555
  classDef segb fill:#f6f6fb,stroke:#99a,color:#333
```

## LA2 行列式與算子的結構

```mermaid
flowchart LR
  AN1_6["AN1.6 緊集與區間上的連續函數"]:::ext
  AN1_10["AN1.10 冪級數、Taylor 級數與初等函數"]:::ext
  F3_6["F3.6 複數"]:::ext
  LA1_5["LA1.5 對偶"]:::ext
  AL1_1["AL1.1 群、子群與同態"]:::ext
  LA2_6["6 多項式"]
  LA2_7["7 行列式"]
  LA2_8["8 分塊矩陣"]
  LA2_9["9 特徵值與對角化"]
  LA2_10["10 標準形"]
  AN1_6 -.-> LA2_6
  F3_6 --> LA2_6
  LA1_5 --> LA2_6
  LA2_6 --> LA2_7
  AL1_1 --> LA2_7
  LA2_7 --> LA2_8
  LA2_8 --> LA2_9
  AN1_10 -.-> LA2_10
  LA2_9 --> LA2_10
  classDef ext fill:#e6e6e6,stroke:#999,color:#555
  classDef opt fill:#fff,stroke:#999,stroke-dasharray:4 3,color:#555
  classDef segb fill:#f6f6fb,stroke:#99a,color:#333
```

## LA3 內積與譜理論

```mermaid
flowchart LR
  LA2_9["LA2.9 特徵值與對角化"]:::ext
  LA3_11["11 內積空間"]
  LA3_12["12 譜理論"]
  LA3_13["13 正定矩陣與奇異值分解"]
  LA2_9 --> LA3_11
  LA3_11 --> LA3_12
  LA3_12 --> LA3_13
  classDef ext fill:#e6e6e6,stroke:#999,color:#555
  classDef opt fill:#fff,stroke:#999,stroke-dasharray:4 3,color:#555
  classDef segb fill:#f6f6fb,stroke:#99a,color:#333
```

## LA4 形式與多線性代數

```mermaid
flowchart LR
  LA3_13["LA3.13 正定矩陣與奇異值分解"]:::ext
  LA4_14["14 雙線性形式與二次型"]
  LA4_15["15 張量與外代數"]
  LA3_13 --> LA4_14
  LA4_14 --> LA4_15
  classDef ext fill:#e6e6e6,stroke:#999,color:#555
  classDef opt fill:#fff,stroke:#999,stroke-dasharray:4 3,color:#555
  classDef segb fill:#f6f6fb,stroke:#99a,color:#333
```

## AN2 度量空間與拓樸

```mermaid
flowchart LR
  AN1_9["AN1.9 函數列與函數級數"]:::ext
  AN1_10["AN1.10 冪級數、Taylor 級數與初等函數"]:::ext
  AN1_11["AN1.11 完備性的各種形式"]:::ext
  LA3_11["LA3.11 內積空間"]:::ext
  AN2_1["1 度量空間、開集與連續"]
  AN2_2["2 完備性與完備化"]
  AN2_3["3 度量空間的緊緻性與連通性"]
  AN2_4["4 壓縮映射與 Picard–Lindelöf 定理"]
  AN2_5["5 等度連續、Arzelà–Ascoli 與 Peano 定理"]
  AN2_6["6 C(K) 的稠密與範疇：Stone–Weierstrass 與 Baire"]
  AN2_7["7 拓樸空間、積與緊緻性"]:::segb
  AN2_8["8 分離公理、Urysohn–Tietze 與局部緊空間"]:::segb
  LA3_11 -.-> AN2_1
  AN1_9 --> AN2_2
  AN1_11 --> AN2_2
  AN2_1 --> AN2_2
  AN2_2 --> AN2_3
  AN1_10 --> AN2_4
  AN2_2 --> AN2_4
  AN2_3 --> AN2_5
  AN2_4 --> AN2_5
  AN2_3 --> AN2_6
  AN2_3 --> AN2_7
  AN2_7 --> AN2_8
  classDef ext fill:#e6e6e6,stroke:#999,color:#555
  classDef opt fill:#fff,stroke:#999,stroke-dasharray:4 3,color:#555
  classDef segb fill:#f6f6fb,stroke:#99a,color:#333
```

## AN3 多變數分析

```mermaid
flowchart LR
  LA2_10["LA2.10 標準形"]:::ext
  LA4_14["LA4.14 雙線性形式與二次型"]:::ext
  LA4_15["LA4.15 張量與外代數"]:::ext
  AN2_3["AN2.3 度量空間的緊緻性與連通性"]:::ext
  AN2_4["AN2.4 壓縮映射與 Picard–Lindelöf 定理"]:::ext
  AN3_1["1 ℝⁿ 上的導數"]
  AN3_2["2 反函數、隱函數與 Lagrange 乘數"]
  AN3_3["3 線性微分方程組、矩陣指數與流"]
  AN3_4["4 ℝⁿ 上的 Riemann 積分"]
  AN3_5["5 ℝⁿ 的子流形與切空間"]:::segb
  AN3_6["6 微分形式與外微分"]:::segb
  AN3_7["7 流形上的積分與 Stokes 定理"]:::segb
  LA4_14 -.-> AN3_1
  AN2_3 --> AN3_1
  AN2_4 --> AN3_2
  AN3_1 --> AN3_2
  LA2_10 --> AN3_3
  AN2_4 --> AN3_3
  AN3_1 --> AN3_3
  AN2_3 --> AN3_4
  AN3_2 --> AN3_5
  LA4_15 --> AN3_6
  AN3_1 --> AN3_6
  AN3_4 --> AN3_7
  AN3_5 --> AN3_7
  AN3_6 --> AN3_7
  classDef ext fill:#e6e6e6,stroke:#999,color:#555
  classDef opt fill:#fff,stroke:#999,stroke-dasharray:4 3,color:#555
  classDef segb fill:#f6f6fb,stroke:#99a,color:#333
```

## AL2 環與體

```mermaid
flowchart LR
  F2_4["F2.4 Zorn 引理（使用者層級）"]:::ext
  F3_7["F3.7 體"]:::ext
  F3_8["F3.8 形式多項式"]:::ext
  LA1_1["LA1.1 向量空間"]:::ext
  AL1_5["AL1.5 正規子群、商群與同構定理"]:::ext
  AL2_1["1 環、理想與商環"]
  AL2_2["2 整環與分式體"]
  AL2_3["3 極大理想與質理想"]
  AL2_4["4 中國剩餘定理"]
  AL2_5["5 歐氏整環、PID 與 UFD"]
  AL2_6["6 多項式環、Gauss 引理與 Eisenstein 判別法"]
  AL2_7["7 體擴張與次數"]
  AL2_8["8 代數擴張、分裂體與代數閉包"]
  AL2_9["9 有限體"]
  AL2_10["10 尺規作圖"]
  AL1_5 --> AL2_1
  F3_7 --> AL2_2
  AL2_1 --> AL2_2
  F2_4 -.-> AL2_3
  AL2_1 --> AL2_3
  AL2_1 --> AL2_4
  AL2_2 --> AL2_5
  AL2_3 --> AL2_5
  F3_8 --> AL2_6
  AL2_5 --> AL2_6
  LA1_1 --> AL2_7
  AL2_6 --> AL2_7
  AL2_7 --> AL2_8
  AL2_8 --> AL2_9
  AL2_7 --> AL2_10
  classDef ext fill:#e6e6e6,stroke:#999,color:#555
  classDef opt fill:#fff,stroke:#999,stroke-dasharray:4 3,color:#555
  classDef segb fill:#f6f6fb,stroke:#99a,color:#333
```

## AL3 Galois 理論

```mermaid
flowchart LR
  AN2_7["AN2.7 拓樸空間、積與緊緻性"]:::ext
  AL1_7["AL1.7 Sylow 定理"]:::ext
  AL1_9["AL1.9 合成列、可解群與冪零群"]:::ext
  AL2_8["AL2.8 代數擴張、分裂體與代數閉包"]:::ext
  AL2_9["AL2.9 有限體"]:::ext
  AL3_1["1 正規擴張與可分擴張"]
  AL3_2["2 Galois 群與 Artin 定理"]
  AL3_3["3 Galois 基本定理"]
  AL3_4["4 有限體與分圓擴張"]
  AL3_5["5 對稱多項式與判別式"]
  AL3_6["6 原始元定理"]
  AL3_7["7 根式可解性"]
  AL3_8["8 Galois 群的計算"]
  AL3_9["9 無限 Galois 理論"]:::opt
  AL2_8 --> AL3_1
  AL3_1 --> AL3_2
  AL3_2 --> AL3_3
  AL2_9 --> AL3_4
  AL3_3 --> AL3_4
  AL3_3 --> AL3_5
  AL3_1 --> AL3_6
  AL1_9 --> AL3_7
  AL3_3 --> AL3_7
  AL1_7 --> AL3_8
  AL3_5 --> AL3_8
  AN2_7 --> AL3_9
  AL3_3 --> AL3_9
  classDef ext fill:#e6e6e6,stroke:#999,color:#555
  classDef opt fill:#fff,stroke:#999,stroke-dasharray:4 3,color:#555
  classDef segb fill:#f6f6fb,stroke:#99a,color:#333
```

## HA Fourier 分析

```mermaid
flowchart LR
  AN1_10["AN1.10 冪級數、Taylor 級數與初等函數"]:::ext
  F3_6["F3.6 複數"]:::ext
  LA3_12["LA3.12 譜理論"]:::ext
  AN2_2["AN2.2 完備性與完備化"]:::ext
  AN2_6["AN2.6 C(K) 的稠密與範疇：Stone–Weierstrass 與 Baire"]:::ext
  AN3_4["AN3.4 ℝⁿ 上的 Riemann 積分"]:::ext
  HA_1["1 Fourier 級數：起源與基本性質"]
  HA_2["2 好核、可和性與 Fejér 定理"]
  HA_3["3 均方收斂與逐點收斂"]
  HA_4["4 Fourier 級數的應用"]
  HA_5["5 ℝ 上的 Fourier 變換"]
  HA_6["6 ℝᵈ 上的 Fourier 變換與波動方程"]
  HA_7["7 有限 Abel 群上的 Fourier 分析"]:::opt
  HA_8["8 算術級數中的質數：Dirichlet 定理"]:::opt
  HA_9["9 Riemann 積分的不足"]
  AN1_10 --> HA_1
  F3_6 --> HA_1
  HA_1 --> HA_2
  AN2_2 --> HA_3
  HA_2 --> HA_3
  HA_3 --> HA_4
  AN3_4 --> HA_5
  HA_2 --> HA_5
  HA_5 --> HA_6
  LA3_12 --> HA_7
  HA_3 --> HA_7
  HA_7 --> HA_8
  AN2_6 --> HA_9
  HA_3 --> HA_9
  classDef ext fill:#e6e6e6,stroke:#999,color:#555
  classDef opt fill:#fff,stroke:#999,stroke-dasharray:4 3,color:#555
  classDef segb fill:#f6f6fb,stroke:#99a,color:#333
```

## MT 測度與積分

```mermaid
flowchart LR
  AN3_2["AN3.2 反函數、隱函數與 Lagrange 乘數"]:::ext
  AN3_4["AN3.4 ℝⁿ 上的 Riemann 積分"]:::ext
  MT_1["1 ℝᵈ 上的 Lebesgue 測度與可測函數"]
  MT_2["2 Lebesgue 積分與收斂定理"]
  MT_3["3 抽象測度空間與 Carathéodory 構造"]
  MT_4["4 乘積測度與 Fubini–Tonelli 定理"]
  MT_5["5 線性映射、變數變換與極座標"]
  MT_6["6 曲面、曲面測度與散度定理"]
  MT_7["7 Lᵖ 空間、摺積與磨光子"]
  MT_8["8 收斂模式、一致可積與弱 Lᵖ"]
  MT_9["9 極大函數與 Lebesgue 微分定理"]
  MT_10["10 有界變差、絕對連續與微積分基本定理"]
  MT_11["11 符號測度、Radon–Nikodym 與 Lebesgue 分解"]
  AN3_4 --> MT_1
  MT_1 --> MT_2
  MT_2 --> MT_3
  MT_3 --> MT_4
  AN3_2 --> MT_5
  MT_4 --> MT_5
  MT_5 --> MT_6
  MT_4 --> MT_7
  MT_7 --> MT_8
  MT_7 --> MT_9
  MT_9 --> MT_10
  MT_7 --> MT_11
  classDef ext fill:#e6e6e6,stroke:#999,color:#555
  classDef opt fill:#fff,stroke:#999,stroke-dasharray:4 3,color:#555
  classDef segb fill:#f6f6fb,stroke:#99a,color:#333
```

## CA 複分析

```mermaid
flowchart LR
  AN1_10["AN1.10 冪級數、Taylor 級數與初等函數"]:::ext
  AN2_5["AN2.5 等度連續、Arzelà–Ascoli 與 Peano 定理"]:::ext
  AN3_1["AN3.1 ℝⁿ 上的導數"]:::ext
  AN3_4["AN3.4 ℝⁿ 上的 Riemann 積分"]:::ext
  HA_4["HA.4 Fourier 級數的應用"]:::ext
  FA_2["FA.2 Radon 測度與 C₀(X) 的對偶"]:::ext
  FA_5["FA.5 弱拓樸、Tychonoff 與 Banach–Alaoglu"]:::ext
  CA_1["1 全純函數與冪級數"]
  CA_2["2 Cauchy 定理及其初步推論"]
  CA_3["3 Laurent 級數、奇點與留數"]
  CA_4["4 環繞數、整體 Cauchy 定理與零點計數"]
  CA_5["5 共形映射、正規族與 Riemann 映射定理"]
  CA_6["6 調和函數與次調和函數"]
  CA_7["7 無窮乘積與整函數"]
  CA_8["8 解析延拓、單值性與 Picard 定理"]
  CA_9["9 正調和函數與 Herglotz–Nevanlinna 表示（交會章：CA × FA）"]:::opt
  AN1_10 --> CA_1
  AN3_1 -.-> CA_1
  AN3_4 -.-> CA_2
  CA_1 --> CA_2
  CA_2 --> CA_3
  CA_3 --> CA_4
  AN2_5 --> CA_5
  CA_4 --> CA_5
  CA_2 --> CA_6
  CA_4 --> CA_7
  HA_4 -.-> CA_8
  CA_7 --> CA_8
  CA_5 --> CA_9
  CA_6 --> CA_9
  FA_2 --> CA_9
  FA_5 --> CA_9
  classDef ext fill:#e6e6e6,stroke:#999,color:#555
  classDef opt fill:#fff,stroke:#999,stroke-dasharray:4 3,color:#555
  classDef segb fill:#f6f6fb,stroke:#99a,color:#333
```

## FA 泛函分析

```mermaid
flowchart LR
  F2_4["F2.4 Zorn 引理（使用者層級）"]:::ext
  AN2_3["AN2.3 度量空間的緊緻性與連通性"]:::ext
  AN2_5["AN2.5 等度連續、Arzelà–Ascoli 與 Peano 定理"]:::ext
  AN2_6["AN2.6 C(K) 的稠密與範疇：Stone–Weierstrass 與 Baire"]:::ext
  AN2_7["AN2.7 拓樸空間、積與緊緻性"]:::ext
  AN2_8["AN2.8 分離公理、Urysohn–Tietze 與局部緊空間"]:::ext
  MT_3["MT.3 抽象測度空間與 Carathéodory 構造"]:::ext
  MT_11["MT.11 符號測度、Radon–Nikodym 與 Lebesgue 分解"]:::ext
  CA_2["CA.2 Cauchy 定理及其初步推論"]:::ext
  FA_1a["1a Banach 空間、有界算子與對偶空間（ℓᵖ、C(K)）"]
  FA_1b["1b Lᵖ 的對偶"]
  FA_2["2 Radon 測度與 C₀(X) 的對偶"]
  FA_3["3 Hahn–Banach 定理"]
  FA_4["4 Baire 範疇與算子的基本定理"]
  FA_5["5 弱拓樸、Tychonoff 與 Banach–Alaoglu"]
  FA_6["6 Hilbert 空間"]
  FA_7["7 緊算子、Fredholm 選擇與譜定理"]
  FA_8["8 Banach 代數與 Gelfand 理論"]:::opt
  AN2_3 --> FA_1a
  MT_11 --> FA_1b
  FA_1a --> FA_1b
  AN2_8 --> FA_2
  MT_3 --> FA_2
  FA_1a --> FA_2
  F2_4 -.-> FA_3
  FA_1a --> FA_3
  AN2_6 --> FA_4
  FA_1a --> FA_4
  AN2_7 --> FA_5
  FA_3 --> FA_5
  FA_4 --> FA_5
  FA_1a --> FA_6
  AN2_5 --> FA_7
  CA_2 -.-> FA_7
  FA_6 --> FA_7
  FA_7 --> FA_8
  classDef ext fill:#e6e6e6,stroke:#999,color:#555
  classDef opt fill:#fff,stroke:#999,stroke-dasharray:4 3,color:#555
  classDef segb fill:#f6f6fb,stroke:#99a,color:#333
```

## AL4 模、表示與同調入門

```mermaid
flowchart LR
  F2_4["F2.4 Zorn 引理（使用者層級）"]:::ext
  LA1_2["LA1.2 線性映射"]:::ext
  LA2_10["LA2.10 標準形"]:::ext
  LA4_15["LA4.15 張量與外代數"]:::ext
  AL1_6["AL1.6 群作用、軌道—穩定子與類方程"]:::ext
  AL2_1["AL2.1 環、理想與商環"]:::ext
  AL2_5["AL2.5 歐氏整環、PID 與 UFD"]:::ext
  AL4_1["1 模、子模、商與同態"]
  AL4_2["2 自由模、直和與正合列"]
  AL4_3["3 PID 上有限生成模的結構定理"]
  AL4_4["4 應用：有限生成 Abel 群與標準形"]
  AL4_5["5 張量積、Hom 與伴隨"]
  AL4_6["6 投射模、內射模與平坦模"]
  AL4_7["7 範疇、函子與泛性質"]
  AL4_8["8 代數與表示"]
  AL4_9["9 有限群表示：Maschke 與 Schur"]
  AL4_10["10 特徵標理論"]
  AL4_11["11 複形、同調、Tor 與 Ext 入門"]
  LA1_2 --> AL4_1
  AL2_1 --> AL4_1
  AL4_1 --> AL4_2
  LA2_10 --> AL4_3
  AL2_5 --> AL4_3
  AL4_2 --> AL4_3
  AL4_3 --> AL4_4
  AL4_2 --> AL4_5
  F2_4 -.-> AL4_6
  AL4_5 --> AL4_6
  AL4_5 --> AL4_7
  LA2_10 --> AL4_8
  LA4_15 --> AL4_8
  AL1_6 --> AL4_9
  AL4_8 --> AL4_9
  AL4_9 --> AL4_10
  AL4_6 --> AL4_11
  AL4_7 --> AL4_11
  classDef ext fill:#e6e6e6,stroke:#999,color:#555
  classDef opt fill:#fff,stroke:#999,stroke-dasharray:4 3,color:#555
  classDef segb fill:#f6f6fb,stroke:#99a,color:#333
```

## AL5 交換代數

```mermaid
flowchart LR
  AL2_3["AL2.3 極大理想與質理想"]:::ext
  AL2_6["AL2.6 多項式環、Gauss 引理與 Eisenstein 判別法"]:::ext
  AL2_7["AL2.7 體擴張與次數"]:::ext
  AL4_2["AL4.2 自由模、直和與正合列"]:::ext
  AL5_1["1 局部化與分式模"]
  AL5_2["2 Noether 環與 Hilbert 基底定理"]
  AL5_3["3 整擴張與 going-up／going-down"]
  AL5_4["4 Hilbert 零點定理（Nullstellensatz）"]
  AL5_5["5 準素分解"]
  AL5_6["6 Dedekind 整環"]
  AL5_7["7 Krull 維數入門"]
  AL2_3 --> AL5_1
  AL4_2 --> AL5_1
  AL2_6 --> AL5_2
  AL4_2 --> AL5_2
  AL2_7 --> AL5_3
  AL5_1 --> AL5_3
  AL5_2 --> AL5_4
  AL5_3 --> AL5_4
  AL5_1 --> AL5_5
  AL5_2 --> AL5_5
  AL5_2 --> AL5_6
  AL5_3 --> AL5_6
  AL5_4 --> AL5_7
  classDef ext fill:#e6e6e6,stroke:#999,color:#555
  classDef opt fill:#fff,stroke:#999,stroke-dasharray:4 3,color:#555
  classDef segb fill:#f6f6fb,stroke:#99a,color:#333
```

## MA 矩陣分析

```mermaid
flowchart LR
  LA2_10["LA2.10 標準形"]:::ext
  LA3_13["LA3.13 正定矩陣與奇異值分解"]:::ext
  AN2_3["AN2.3 度量空間的緊緻性與連通性"]:::ext
  AN3_3["AN3.3 線性微分方程組、矩陣指數與流"]:::ext
  CA_9["CA.9 正調和函數與 Herglotz–Nevanlinna 表示（交會章：CA × FA）"]:::ext
  MA_16["16 範數與矩陣分析"]
  MA_17["17 變分原理與交錯"]
  MA_18["18 凸性"]
  MA_19["19 非負矩陣"]
  MA_20["20 擾動理論"]
  MA_21["21 矩陣不等式"]
  MA_21b["21b Löwner 定理的 Pick 函數形式（交會章：MA × CA × FA）"]:::opt
  LA2_10 --> MA_16
  LA3_13 --> MA_16
  AN2_3 -.-> MA_16
  MA_16 --> MA_17
  MA_17 --> MA_18
  MA_18 --> MA_19
  MA_19 --> MA_20
  AN3_3 -.-> MA_21
  MA_20 --> MA_21
  CA_9 --> MA_21b
  MA_21 --> MA_21b
  classDef ext fill:#e6e6e6,stroke:#999,color:#555
  classDef opt fill:#fff,stroke:#999,stroke-dasharray:4 3,color:#555
  classDef segb fill:#f6f6fb,stroke:#99a,color:#333
```

## PR 測度論機率

```mermaid
flowchart LR
  HA_6["HA.6 ℝᵈ 上的 Fourier 變換與波動方程"]:::ext
  MT_8["MT.8 收斂模式、一致可積與弱 Lᵖ"]:::ext
  MT_11["MT.11 符號測度、Radon–Nikodym 與 Lebesgue 分解"]:::ext
  PR_1["1 測度空間上的機率"]
  PR_2["2 條件期望"]
  PR_3["3 離散時間鞅"]
  PR_4["4 弱收斂與特徵函數"]
  MT_8 --> PR_1
  MT_11 --> PR_2
  PR_1 --> PR_2
  PR_2 --> PR_3
  HA_6 -.-> PR_4
  PR_1 --> PR_4
  classDef ext fill:#e6e6e6,stroke:#999,color:#555
  classDef opt fill:#fff,stroke:#999,stroke-dasharray:4 3,color:#555
  classDef segb fill:#f6f6fb,stroke:#99a,color:#333
```

## PDE 分佈與 Sobolev 空間

```mermaid
flowchart LR
  AN2_5["AN2.5 等度連續、Arzelà–Ascoli 與 Peano 定理"]:::ext
  HA_6["HA.6 ℝᵈ 上的 Fourier 變換與波動方程"]:::ext
  MT_6["MT.6 曲面、曲面測度與散度定理"]:::ext
  MT_7["MT.7 Lᵖ 空間、摺積與磨光子"]:::ext
  MT_8["MT.8 收斂模式、一致可積與弱 Lᵖ"]:::ext
  MT_10["MT.10 有界變差、絕對連續與微積分基本定理"]:::ext
  CA_4["CA.4 環繞數、整體 Cauchy 定理與零點計數"]:::ext
  FA_1b["FA.1b Lᵖ 的對偶"]:::ext
  FA_7["FA.7 緊算子、Fredholm 選擇與譜定理"]:::ext
  PDE_1["1 分佈"]
  PDE_2["2 緩增分佈、Fourier 變換與 Plancherel"]
  PDE_3["3 插值：Riesz–Thorin、Young 與 Hausdorff–Young"]
  PDE_4["4 Sobolev 空間"]
  PDE_5["5 H¹₀、Poincaré 不等式與 Rellich 緊緻性"]
  PDE_6["6 總結：Dirichlet 問題與 Dirichlet–Laplace 特徵基"]
  MT_6 --> PDE_1
  MT_7 --> PDE_1
  HA_6 --> PDE_2
  PDE_1 --> PDE_2
  MT_8 --> PDE_3
  CA_4 -.-> PDE_3
  FA_1b --> PDE_3
  MT_10 --> PDE_4
  PDE_1 --> PDE_4
  AN2_5 --> PDE_5
  PDE_4 --> PDE_5
  FA_7 --> PDE_6
  PDE_5 --> PDE_6
  classDef ext fill:#e6e6e6,stroke:#999,color:#555
  classDef opt fill:#fff,stroke:#999,stroke-dasharray:4 3,color:#555
  classDef segb fill:#f6f6fb,stroke:#99a,color:#333
```

## GEO 仿射與射影幾何

```mermaid
flowchart LR
  LA4_15["LA4.15 張量與外代數"]:::ext
  MA_18["MA.18 凸性"]:::ext
  GEO_22["22 仿射與射影幾何"]
  LA4_15 --> GEO_22
  MA_18 --> GEO_22
  classDef ext fill:#e6e6e6,stroke:#999,color:#555
  classDef opt fill:#fff,stroke:#999,stroke-dasharray:4 3,color:#555
  classDef segb fill:#f6f6fb,stroke:#99a,color:#333
```

## NLA 計算與應用

```mermaid
flowchart LR
  MA_17["MA.17 變分原理與交錯"]:::ext
  NLA_24["24 計算與應用"]
  MA_17 --> NLA_24
  classDef ext fill:#e6e6e6,stroke:#999,color:#555
  classDef opt fill:#fff,stroke:#999,stroke-dasharray:4 3,color:#555
  classDef segb fill:#f6f6fb,stroke:#99a,color:#333
```

## ST 公理集合論

```mermaid
flowchart LR
  F2_4["F2.4 Zorn 引理（使用者層級）"]:::ext
  AL1_11["AL1.11 自由群與表現"]:::ext
  MT_1["MT.1 ℝᵈ 上的 Lebesgue 測度與可測函數"]:::ext
  ST_1["1 完整的 ZF 公理系統（重訪 F3.1）"]
  ST_2["2 序數與超限歸納"]
  ST_3["3 基數算術"]
  ST_4["4 選擇公理的等價形式"]
  ST_5["5 可構造宇宙與獨立性概觀"]
  ST_6["6 不可測集與 Banach–Tarski"]
  F2_4 --> ST_1
  ST_1 --> ST_2
  ST_2 --> ST_3
  ST_2 --> ST_4
  ST_4 --> ST_5
  AL1_11 -.-> ST_6
  MT_1 --> ST_6
  ST_4 --> ST_6
  classDef ext fill:#e6e6e6,stroke:#999,color:#555
  classDef opt fill:#fff,stroke:#999,stroke-dasharray:4 3,color:#555
  classDef segb fill:#f6f6fb,stroke:#99a,color:#333
```

圖例：灰底＝冊外來源；虛框＝選讀章；淡紫＝B 段。
