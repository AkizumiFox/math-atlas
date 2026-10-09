# 書稿 → 冊的對照（由 `tools/atlas.py stats` 從 `registry/chapters.yaml` 的 `src` 欄產生）

對照的理由與決策記在 spec/06。

## analysis-book（`ab:N` ＝ blueprint/book.yaml 第 N 章）

| 書稿 | 冊的章 |
|---|---|
| ab:1 | F1.1 連接詞與推導 |
| ab:2 | F1.2 否定、古典邏輯與推導的尋找 |
| ab:3 | F1.3 真值、健全性與完備性 |
| ab:4 | F1.4 述詞邏輯與量詞規則 |
| ab:5 | F1.5 從推導到數學文字 |
| ab:6 | F2.1 集合、函數、像與原像 |
| ab:7 | F2.2 等價關係、序與歸納 |
| ab:8 | F2.3 基數：可數與不可數（含選擇公理的陳述） |
| ab:9 | F3.1 自然數的 von Neumann 建構（ZF 的必要片段）（選讀） |
| ab:10 | F3.2 以等價類建構 ℤ 與 ℚ（選讀） |
| ab:11 | AN1.1 有序體與最小上界公理 |
| ab:12 | AN1.2 數列、子列與 Cauchy 列 |
| ab:13 | AN1.3 無窮級數 |
| ab:14 | AN1.4 ℝ 的開集、閉集與緊集 |
| ab:15 | AN1.5 函數極限與連續 |
| ab:16 | AN1.6 緊集與區間上的連續函數 |
| ab:17 | AN1.7 導數與均值定理 |
| ab:18 | AN1.8 Riemann–Darboux 積分 |
| ab:19 | AN1.9 函數列與函數級數 |
| ab:20 | AN1.10 冪級數、Taylor 級數與初等函數 |
| ab:21 | AN1.11 完備性的各種形式 |
| ab:22 | F3.3 以 Dedekind 分割建構 ℝ（選讀） |
| ab:23 | F3.4 完備有序體的唯一性（選讀） |
| ab:24 | AN2.1 度量空間、開集與連續 |
| ab:25 | AN2.2 完備性與完備化 |
| ab:26 | AN2.3 度量空間的緊緻性與連通性 |
| ab:27 | AN2.4 壓縮映射與 Picard–Lindelöf 定理 |
| ab:28 | AN2.5 等度連續、Arzelà–Ascoli 與 Peano 定理 |
| ab:29 | AN2.6 C(K) 的稠密與範疇：Stone–Weierstrass 與 Baire |
| ab:30 | AN3.1 ℝⁿ 上的導數 |
| ab:31 | AN3.2 反函數、隱函數與 Lagrange 乘數 |
| ab:32 | AN3.3 線性微分方程組、矩陣指數與流 |
| ab:33 | AN3.4 ℝⁿ 上的 Riemann 積分 |
| ab:34 | HA.1 Fourier 級數：起源與基本性質 |
| ab:35 | HA.2 好核、可和性與 Fejér 定理 |
| ab:36 | HA.3 均方收斂與逐點收斂 |
| ab:37 | HA.4 Fourier 級數的應用 |
| ab:38 | HA.5 ℝ 上的 Fourier 變換 |
| ab:39 | HA.6 ℝᵈ 上的 Fourier 變換與波動方程 |
| ab:40 | HA.7 有限 Abel 群上的 Fourier 分析（選讀） |
| ab:41 | HA.8 算術級數中的質數：Dirichlet 定理（選讀） |
| ab:42 | HA.9 Riemann 積分的不足 |
| ab:43 | MT.1 ℝᵈ 上的 Lebesgue 測度與可測函數 |
| ab:44 | MT.2 Lebesgue 積分與收斂定理 |
| ab:45 | MT.3 抽象測度空間與 Carathéodory 構造 |
| ab:46 | MT.4 乘積測度與 Fubini–Tonelli 定理 |
| ab:47 | MT.5 線性映射、變數變換與極座標 |
| ab:48 | MT.6 曲面、曲面測度與散度定理 |
| ab:49 | MT.7 Lᵖ 空間、摺積與磨光子 |
| ab:50 | MT.8 收斂模式、一致可積與弱 Lᵖ |
| ab:51 | MT.9 極大函數與 Lebesgue 微分定理 |
| ab:52 | MT.10 有界變差、絕對連續與微積分基本定理 |
| ab:53 | MT.11 符號測度、Radon–Nikodym 與 Lebesgue 分解 |
| ab:54 | PR.1 測度空間上的機率 |
| ab:55 | CA.1 全純函數與冪級數 |
| ab:56 | CA.2 Cauchy 定理及其初步推論 |
| ab:57 | CA.3 Laurent 級數、奇點與留數 |
| ab:58 | CA.4 環繞數、整體 Cauchy 定理與零點計數 |
| ab:59 | CA.5 共形映射、正規族與 Riemann 映射定理 |
| ab:60 | CA.6 調和函數與次調和函數 |
| ab:61 | CA.7 無窮乘積與整函數 |
| ab:62 | CA.8a 解析延拓與單值性；CA.8b Picard 定理（交會章：CA × HA）（選讀） |
| ab:63 | AN2.7 拓樸空間、積與緊緻性 |
| ab:64 | AN2.8 分離公理、Urysohn–Tietze 與局部緊空間 |
| ab:65 | FA.1a Banach 空間、有界算子與對偶空間（ℓᵖ、C(K)）；FA.1b Lᵖ 的對偶 |
| ab:66 | FA.2 Radon 測度與 C₀(X) 的對偶 |
| ab:67 | FA.3 Hahn–Banach 定理 |
| ab:68 | FA.4 Baire 範疇與算子的基本定理 |
| ab:69 | FA.5 弱拓樸、Tychonoff 與 Banach–Alaoglu |
| ab:70 | FA.6 Hilbert 空間 |
| ab:71 | FA.7 緊算子、Fredholm 選擇與譜定理 |
| ab:72 | FA.8 Banach 代數與 Gelfand 理論（選讀） |
| ab:73 | PDE.1 分佈 |
| ab:74 | PDE.2 緩增分佈、Fourier 變換與 Plancherel |
| ab:75 | PDE.3 插值：Riesz–Thorin、Young 與 Hausdorff–Young |
| ab:76 | PDE.4 Sobolev 空間 |
| ab:77 | PDE.5 H¹₀、Poincaré 不等式與 Rellich 緊緻性 |
| ab:78 | PDE.6 總結：Dirichlet 問題與 Dirichlet–Laplace 特徵基 |

## linear-algebra（`la:chNN` ＝ 第 NN 章；`la:ch00/NN` ＝ 第 0 章第 NN 節）

| 書稿 | 冊的章 |
|---|---|
| la:ch00/01 | F1.5 從推導到數學文字 |
| la:ch00/02 | F1.5 從推導到數學文字 |
| la:ch00/03 | F2.1 集合、函數、像與原像 |
| la:ch00/04 | F2.1 集合、函數、像與原像 |
| la:ch00/05 | F2.2 等價關係、序與歸納 |
| la:ch00/06 | F3.6 複數 |
| la:ch00/07 | F3.7 體 |
| la:ch00/08 | F3.8 形式多項式 |
| la:ch00/09 | LA1.0 矩陣 |
| la:ch00/10 | AL1.1 群、子群與同態 |
| la:ch01 | LA1.1 向量空間 |
| la:ch02 | LA1.2 線性映射 |
| la:ch03 | LA1.3 線性系統與矩陣 |
| la:ch04 | LA1.4 映射的矩陣 |
| la:ch05 | LA1.5 對偶 |
| la:ch06 | LA2.6 多項式 |
| la:ch07 | LA2.7 行列式 |
| la:ch08 | LA2.8 分塊矩陣 |
| la:ch09 | LA2.9 特徵值與對角化 |
| la:ch10 | LA2.10 標準形 |
| la:ch11 | LA3.11 內積空間 |
| la:ch12 | LA3.12 譜理論 |
| la:ch13 | LA3.13 正定矩陣與奇異值分解 |
| la:ch14 | LA4.14 雙線性形式與二次型 |
| la:ch15 | LA4.15 張量與外代數 |
| la:ch16 | MA.16 範數與矩陣分析 |
| la:ch17 | MA.17 變分原理與交錯 |
| la:ch18 | MA.18 凸性 |
| la:ch19 | MA.19 非負矩陣 |
| la:ch20 | MA.20 擾動理論 |
| la:ch21 | MA.21 矩陣不等式 |
| la:ch21/10 | MA.21b Löwner 定理的 Pick 函數形式（交會章：MA × CA × FA）（選讀） |
| la:ch22 | GEO.22 仿射與射影幾何 |
| la:ch23 | AL4.8 代數與表示 |
| la:ch24 | NLA.24 計算與應用 |

## 尚無書稿（`new`）

- **F2**：F2.4 Zorn 引理（使用者層級）
- **F3**：F3.5 整除、帶餘除法與 ℤ/nℤ
- **AN3**：AN3.5 ℝⁿ 的子流形與切空間、AN3.6 微分形式與外微分、AN3.7 流形上的積分與 Stokes 定理
- **AL1**：AL1.2 循環群、AL1.3 對稱群與置換的符號、AL1.4 陪集與 Lagrange 定理、AL1.5 正規子群、商群與同構定理、AL1.6 群作用、軌道—穩定子與類方程、AL1.7 Sylow 定理、AL1.8 直積、半直積與有限 Abel 群、AL1.9 合成列、可解群與冪零群、AL1.10 Aₙ 的單純性、AL1.11 自由群與表現
- **AL2**：AL2.1 環、理想與商環、AL2.2 整環與分式體、AL2.3 極大理想與質理想、AL2.4 中國剩餘定理、AL2.5 歐氏整環、PID 與 UFD、AL2.6 多項式環、Gauss 引理與 Eisenstein 判別法、AL2.7 體擴張與次數、AL2.8 代數擴張、分裂體與代數閉包、AL2.9 有限體、AL2.10 尺規作圖
- **AL3**：AL3.1 正規擴張與可分擴張、AL3.2 Galois 群與 Artin 定理、AL3.3 Galois 基本定理、AL3.4 有限體與分圓擴張、AL3.5 對稱多項式與判別式、AL3.6 原始元定理、AL3.7 根式可解性、AL3.8 Galois 群的計算、AL3.9 無限 Galois 理論（選讀）
- **CA**：CA.9 正調和函數與 Herglotz–Nevanlinna 表示（交會章：CA × FA）（選讀）
- **AL4**：AL4.1 模、子模、商與同態、AL4.2 自由模、直和與正合列、AL4.3 PID 上有限生成模的結構定理、AL4.4 應用：有限生成 Abel 群與標準形、AL4.5 張量積、Hom 與伴隨、AL4.6 投射模、內射模與平坦模、AL4.7 範疇、函子與泛性質、AL4.9 有限群表示：Maschke 與 Schur、AL4.10 特徵標理論、AL4.11 複形、同調、Tor 與 Ext 入門
- **AL5**：AL5.1 局部化與分式模、AL5.2 Noether 環與 Hilbert 基底定理、AL5.3 整擴張與 going-up／going-down、AL5.4 Hilbert 零點定理（Nullstellensatz）、AL5.5 準素分解、AL5.6 Dedekind 整環、AL5.7 Krull 維數入門
- **PR**：PR.2 條件期望、PR.3 離散時間鞅、PR.4 弱收斂與特徵函數
- **ST**：ST.1 完整的 ZF 公理系統（重訪 F3.1）、ST.2 序數與超限歸納、ST.3 基數算術、ST.4 選擇公理的等價形式、ST.5 可構造宇宙與獨立性概觀、ST.6a Vitali 不可測集、ST.6b Banach–Tarski 悖論（交會章：ST × AL）（選讀）
