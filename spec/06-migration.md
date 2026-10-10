# 06 書稿 → 冊的對照，以及待決事項

逐章的對照以 `registry/chapters.yaml` 的 `src` 欄為準：`ab:N` 是 analysis-book 第 N 章，`la:chNN` 或 `la:ch00/NN` 是線代書的章或節。本文件只列摘要與決策。

## 書稿 → 冊

逐章對照由 `chapters.yaml` 的 `src` 欄自動產生，見 `generated/migration.md`，這裡不再手寫表格。以下只記對照背後的決定：

- **analysis-book**：依 Part 拆冊。Part I 第 22–23 章（選讀的 ℝ 建構）移到 F3，讓 ℝ 的建構路線集中在一冊；Part VI 第 63–64 章（一般拓樸）提前到 AN2 的 B 段，FA 與 AL3.9 從這裡取用；第 54 章是機率支線 PR 的入口；第 73–78 章成為支線冊 PDE。AN3.5–3.7（子流形、微分形式、Stokes）是新章，屬 B 段。
- **選擇公理**：陳述放在 F2.3，因為「可數個可數集的聯集可數」要用到；F2.4 Zorn 引理是新章。
- **linear-algebra**：第 0 章拆到 F1.5、F2.1、F2.2、F3.6–3.8 與 AL1.1；§0.9 矩陣成為新的 LA1.0（它被第 2 章引用，所以不能併進第 3 章）。第 24 章之後可拆成多章。
- analysis-book 本身不必拆 repo。它可以繼續以單一書稿的形式寫作，冊只是 registry 上的切面。等引擎支援跨冊 ID 之後，再決定是否真的分成多本出版。

## 由計算邊得到的發現

以下各點都可以由 `generated/report.md` 和 `generated/diff.md` 重現。

1. **LA3 對第 10 章的依賴很窄。** 硬依賴只來自 `thm-unitary-exponential` 對 §10.9 矩陣指數的兩條引用。已定案搬到 AN3.3（見待決事項 5），套用後 LA3 可以跳過 Jordan 標準形。
2. **LA2.7 行列式依賴 AL1.1。** 依賴的是 §0.10 的「對換生成 Sₙ」。這和先前對話推測的「AL1.3 置換符號」不同，以計算值為準。
3. **LA4 和 AN3 在冊層級成環。** LA4.14 借用 AN3.1（§14.6 的二階導數判別法），AN3.6 又需要 LA4.15（外冪）。章層級沒有環，所以不影響閱讀；但冊之間排不出先後。已定案：§14.6 的判別法移到 AN3.1（見待決事項 4）。
4. ~~**複分析需要 HA 的兩章。**~~ CA.6 調和函數原本用 HA.2 的好核框架導出 Poisson 核（analysis-book 的設計）。**已定（2026-10-09）**：改照 Ahlfors，由 Cauchy 積分公式導出 Poisson 核；好核的觀點以 revisits 指回 HA.2。冊層級的 HA → CA 消失，CA 讀完 AN2 就能開始。書稿待辦見下方。
5. **選擇公理的位置要調整。** 原計畫把選擇公理放在 F2.4，但 F2.3 的「可數個可數集的聯集」已經需要它。現在把陳述移到 F2.3，F2.4 只放 Zorn 引理。
6. **必讀章數和先前對話的手算值不同。** 對話報告是 49／57／66／74，現值見 report.md。差異有三個原因：章節清單換成了 analysis-book 的（章比較粗）；ℝ 改走公理化路線，省掉建構；FA 不再 s 依賴 LA3。

## 待作者決定

| # | 事項 | 選項 | 影響 |
|---|---|---|---|
| 1 | ~~ℕ 是否含 0~~ | **已定：含 0**（2026-10-09） | analysis-book 要改寫，見下方待辦 |
| 2 | ~~粗體向量~~ | **已定：依型別決定**（2026-10-09） | 線代書第 1–5 章要逐處分類，見下方待辦 |
| 3 | ~~A／R 的正式定義~~ | **已定：spec/03 v0.3.0-draft**（v0.2 定稿＋三項 pilot 修改＋地圖語意，2026-10-09） | statements.yaml、習題分級；三條 lint 見 spec/03 §6.1 |
| 4 | ~~LA4 §14.6 二階判別法~~ | **已定：移到 AN3.1**（2026-10-09；舊章號的「AN3.2 高階導數與極值」＝現在的 AN3.1） | 冊層級的環消失 |
| 5 | ~~LA3 是否要能跳過第 10 章~~ | **已定：`thm-unitary-exponential` 搬到 AN3.3**（2026-10-09） | 不能改成 b（跳過 LA2.10 的讀者沒有矩陣指數的記號）；MA.21 對它的引用改為 b，合法：MA.21 本身就以 s 引用 LA2.10（`thm-exponential-properties`，4 處），矩陣指數在作用域內；`moves.yaml` 的 `scope` 讓 lint 持續檢查這件事 |
| 6 | ~~交換代數~~ | **已定：獨立成支線冊 AL5**（2026-10-09） | 不增加代數資格考的必讀量；代數幾何與代數數論從 AL5 進入 |
| 7 | ~~MA 的 (A7)~~ | **已定：Pick–Nevanlinna，移到選讀交會章 MA.21b**（2026-10-09） | 陳述跨 MA、CA、測度三套語彙，不能是 b。Herglotz 放新的選讀章 CA.9（依賴 CA.5、CA.6、FA.2、FA.5）。主線必讀量不變 |
| 8 | ~~授權~~ | **已定：書稿 CC BY-NC-SA 4.0；atlas 的 registry／spec CC BY 4.0；tools MIT**（2026-10-09） | 三本既有的書已是 NC-SA，不必遷移；Napkin（BY-SA）不能改編進書稿 |
| 9 | ~~AN3.5–3.7 流形三章~~ | **已定：保留，維持 B 段**（2026-10-09） | 它們是微分幾何、微分拓樸兩條支線（Harvard 資格考科目）唯一的入口，刪掉的話支線要自己重寫 Stokes。MT.6 的散度定理與 AN3.7 的 Stokes 以 generalizes 連起來（陳述層），章層級是 AN3.7 revisits MT.6 |
| 10 | ~~ZF 出現兩次~~ | **已定：分工**（2026-10-09） | F3.1 只放建構 ω 所需的 ZF 片段與 von Neumann 自然數（$0=\varnothing$），ST.1 是完整的公理系統，以 revisits 指回 F3.1 |
| 11 | ~~計算方向的線代必讀量~~ | **已定：另算陳述讀者必讀集（原稱 R1 讀者必讀集），不分流 NLA.24 的邊**（2026-10-09） | 把 NLA.24 只套用定理的邊改成 b，s 閉包仍是 27 章（定義所在的章本身就 s 依賴譜理論與行列式）。改成和 s 閉包並列的陳述讀者必讀集下界（spec/03 §6.2），NLA.24 為 14 章；要變成精確值，需要 spec/05 第 10 項 |

## b 邊分流（2026-10-09）

依 spec/01 規則 7，把 28 條未宣告 `scope` 的 b 邊逐一分類。原本是 29 條，MA.21 ← CA.2 已由 MA.21b 取代。

**1. 宣告 scope（已套用，15 條）**

| 邊 | scope | 說明 |
|---|---|---|
| AN1.11 ← F2.3 | F2.1 | 選擇公理的陳述只用集合與函數。另注意：why 提到的超實數超濾子，其存在要靠 Zorn（F2.4），不是選擇公理的陳述本身；那一節若不是選讀，要補 b F2.4 |
| F3.6 ← AN1.1 | （空） | 只用到 ℝ 的四則運算，中學程度即可陳述 |
| AN2.1 ← LA3.11 | LA1.1 | 只借 ℝⁿ 上的點積與 Cauchy–Schwarz |
| AL2.3、AL2.8、AL4.6、FA.3 ← F2.4 | F2.2 | Zorn 引理的語彙是偏序、鏈、上界 |
| CA.2 ← AN3.4 | AN1.7、AN1.8、AN2.3 | 區間上積分號下微分，連續被積函數 |
| CA.8 ← AN1.10 | AN1.8、AN1.10 | Γ 積分 |
| PR.1 ← AN1.7 | AN1.7 | Taylor 餘項 |
| PR.4 ← HA.6 | PR.4、MT.2、AN1.10、F3.6 | Fourier 變換在 PR.4 以 Lebesgue 積分就地定義。lint 因此抓到計畫漏了 PR.4 對 F3.6、AN1.10 的 s 邊（特徵函數要用複指數），已補 |
| MA.16 ← AN1.11、AN2.3 | MA.16 | 線代書第 16 章開頭就地定義了連續、收斂等語彙（已核對書稿） |

**2. 改型別（已套用，4 條）**：沒有一條需要 R2 以上，但有四條其實不該是 b。

| 邊 | 改成 | 理由 |
|---|---|---|
| FA.8 ← CA.2 | s | FA.8 本來就是選讀章，直接當 FA × CA 的交會章 |
| MT.7 ← LA3.11 | see | L² 上的 Cauchy–Schwarz 就是本章 Hölder 的 p = 2 |
| AL4.5 ← LA4.15 | revisits | 模的張量積在本章自行構造，向量空間是特例 |
| PDE.1 ← CA.6 | see | ℝᵈ 的均值性質由散度定理（MT.6，已是 s）導出；CA.6 只有平面版本 |

**1′. 語彙來自另一個分支，但陳述不跨分支（7 條，已處理）**：依 spec/01 規則 8 就地定義，全部在三個以內，沒有一條需要改成 s。

| 邊 | 就地定義（`statements.yaml`） | 備註 |
|---|---|---|
| LA2.6 ← AN1.6 | 連續（限 ℂ 的子集上的實值函數） | 書稿：§6.05 補定義；第 16 章刪掉「本書至此不需要連續」，改為回指 §6.05 |
| LA2.10 ← AN1.10 | 複數數列與級數的收斂、ℝ→ℂ 的導數、t→∞ 的極限 | 剛好三個；cos、sin 由 F3.6 的極式提供 |
| MA.16 ← AN1.11、AN2.3 | 範數空間的 Cauchy 列、閉集 | 連續由 LA2.6 的就地定義提供 |
| AN3.1 ← LA2.7、LA4.14 | 行列式、正定／負定／不定 | 秩與可逆來自 LA1.3。二階判別法改用單位球面的緊緻性取最小值，不經譜定理，AN3.1 ← LA3.12 降為 see |
| AN3.4 ← LA2.7 | 行列式、初等矩陣 | AN3.1 不是 AN3.4 的祖先，所以 AN3.4 自己再就地定義一次行列式，同樣指向 LA2.7 |
| CA.1 ← AN3.1 | ℝ² 上的實可微、偏導數與 Jacobian | |

另外 PR.4 的 Fourier 變換（第 1 類）也登記為就地定義。

**3. 陳述跨分支（4 條，已定，2026-10-09）**

| 邊 | 決定 | 結果 |
|---|---|---|
| FA.7 ← CA.2 | 刪除；「譜非空」移到 FA.8 | 緊自伴算子的譜定理由 ‖T‖ = sup｜⟨Tx, x⟩｜ 取得特徵值，Fredholm 選擇也不需要譜非空；FA.8 本來就 s 依賴 CA.2 |
| PDE.3 ← CA.4 | 改成 s | 三線引理的陳述需要「解析」。PDE 的冊外必讀從 61 章增為 65 章 |
| CA.8 ← HA.4 | 拆章 | CA.8a「解析延拓與單值性」主線；CA.8b「Picard 定理」選讀交會章，s 依賴 CA.8a、HA.4 |
| ST.6 ← AL1.11 | 拆章 | ST.6a「Vitali 不可測集」主線，s 依賴 MT.1、F2.3；ST.6b「Banach–Tarski」選讀交會章，s 依賴 ST.6a、AL1.11、AL1.6、LA1.0 |

所有 b 邊現在都已宣告 `scope`。

## 書稿改寫（只針對已經寫好的內容）

還沒寫的章要照做的事不放這裡，寫在 `registry/chapter-constraints.yaml`，由生成管線的 Spec 步驟（spec/04 圖 1）帶進該章的生成規格；`atlas.py check` 會擋下掛在已寫章上的約束。這裡只列會改到已寫內容、因此要重審的工作。

已寫的章以 `registry/computed/labels.yaml` 的 `written` 為準（`tools/import_labels.py`）：線代書全部；analysis-book 第 1–4、6、11 章。

**順序**：約定變更（1–3）最先做。它們會改到陳述本身、觸發重審，拖得越久，受影響的已寫章越多。其餘各項彼此獨立。

1. - [ ] **ℕ 含 0**（2026-10-09 定案）：analysis-book 的 `\nN` 改為含 0；凡是「$n \in \mathbb{N}$」作為數列索引、從 1 開始的地方，改寫成 $(x_n)_{n \ge 1}$ 或 $n \in \mathbb{Z}_{>0}$。`\nNz` 巨集退役。已寫的第 1–4、6、11 章要重審。順序（2026-10-10）：作者 commit 第 4、6 章 → 合併 `usage-hash`（ledger 的雜湊先正規化 avoid 寫法）→ 在新的 worktree 分支做 ℕ 含 0 與用詞遷移 → review 後合併。
   - 進度（2026-10-10）：第 4、6 章已 commit（7ea0008），`usage-hash` 已合併；分支 `conventions`（worktree `analysis-book-conventions`）完成用詞遷移（ledger stale 前後相同）與 ℕ 含 0（第 1、3、4、6、11 章，`\nNz` 退役），經獨立數學審查修正。待重審的 verdict 46 個（ch01 1、ch03 11、ch11 34）；ch04、ch06 尚無 ledger。未合併。
   - 合併前另外要做（2026-10-10）：(a) check 目前失敗的 26 個未解析引用（ch04 §§07、08、11、12 指向尚未寫的 §§4.3–4.6）列進一份基準清單，做法同 `field-deviations.yaml`，check 只報清單外新出現的未解析引用，清單裡的引用一旦解析就要從清單刪掉；(b) `ch01v2.yaml` 移到 `archive/`（或加狀態欄標成封存），工具不再讀它，不和正式 ledger 並列；(c) ch11 §02、§04 在 §05 定義 `\nZ_{>0}` 之前就用到，在第一次出現處定義（或把定義提前）。(c) 這類「先用後定義」正是記號作用域 lint（05 第 6 項）要抓的，該 lint 要儘早上線。agent 只在 `analysis-book-*` worktree 裡寫；合併由作者親手執行。
2. - [ ] **粗體依型別**（2026-10-09 定案；2026-10-10 定名與範圍）：線代書的 `\v`、`\u`、`\w`、`\x`、`\y` 依型別拆成 `\cvec{}`（𝔽ⁿ 的座標向量，粗體）與 `\elem{}`（抽象元素，不加粗）。範圍是全書（約 3.3 萬處），逐章進行、一章一個 commit，每一處由 AI 依上下文分類，每章附抽審清單給作者人工抽審；從第 1–5 章開始。矩陣巨集 `\A … \Z`、`\e_i` 不變；`\0` 依所在空間拆成 `\cvec{0}`（𝔽ⁿ 的零向量）與 `\elem{0}`，零矩陣寫 `\O`（粗體 O）（判斷準則見 02，2026-10-10 補：𝔽^ℕ 與商空間的元素不加粗，代表元保留自己的型別）。analysis-book 不受影響。
   - 進度（2026-10-10）：第 0–24a 章已轉換並依 02 的準則重判（分支 `conventions-rewrite`，含零矩陣約 920 處改粗體、`tools/check_macros.py` lint）。獨立抽查 15%（9,584／63,115 處）錯 10 處，已修。已發布的 id 與 label 對照無缺漏。線上站另有 9 個 id 因已發布 repo 自己的 §13.6 拆頁而失效，這違反合併條件 (4)，所以合併順序是（2026-10-10）：先在分支 `moved-ids` 加引擎的 `moved-ids` 設定（06 頁的舊錨點轉到 07 頁；改名頁的 redirect stub 也保留 `#錨點`），作者 review 合併後，再合併 `conventions-rewrite`。1×1 零矩陣寫 `\O_1`（2026-10-10）。合併由作者親手執行；條件 (2) 的抽查也由作者自己做，agent 的抽查不算。合併進線代書 main 的條件（2026-10-10，main 可能直接部署）：(1) PROVISIONAL 依 02 的準則處理完，分支不留任何 PROVISIONAL 標記；(2) 隨機抽 10–20% 檢查分類；(3) build 與 check 通過；(4) 沒有已發布的 label 被刪，改名的都留錨點。
   - NOTATION.md 是第二個事實來源：現在照規則全部更新，並加 lint（NOTATION.md 的程式碼範例要通過書稿同一套巨集檢查）；05 第 6 項落地後改由 `registry/notation.yaml` 產生，不再手寫。
3. - [ ] **英文用詞遷移**（2026-10-10 定案，`registry/usage.yaml` 15 組全部 confirmed）：兩本書稿裡每一處 avoid 寫法換成 use 寫法，清單在 `generated/usage.md`（`tools/usage_report.py`，依檔案列出行號）。大宗是 non- 改連寫（non-zero → nonzero 等，3,628 處；non- 後接大寫字時保留連字號，例如 non-Euclidean），其次是形容詞的 is one-to-one、linear transformation、analyse、labelled，都是純機械替換：用 regex 改寫後由 lint 守住；陳述雜湊先正規化 avoid 寫法（spec/04 圖 3），所以不觸發重審。標為 `review` 的兩組（is onto、iff）要逐處判斷：is onto 也可能是介系詞片語（the projections are onto U），iff 在 F1 談連接詞本身的地方保留。第 16 組序列逗號在散文裡也是 review；書稿的章名則照 `chapters.yaml` 的英文章名機械更新（序列逗號、Nonnegative 等）。
4. - [ ] **第 6 章 §6.05 的連續**（2026-10-09）：就地定義「連續」，限 ℂ 的子集上的實值函數，註明完整定義在 AN1.5（`def-continuous-local`）。
5. - [ ] **第 10 章 §10.9**（2026-10-09）：就地定義複數數列與級數的收斂、ℝ→ℂ 的導數、t→∞ 的極限（`def-seq-limit-local`、`def-derivative-local`、`def-limit-infinity-local`），各自註明完整定義的位置。
6. - [ ] **第 12 章：`thm-unitary-exponential` 移出**（2026-10-09 定案，`todo:unitary-exp`）：移到 analysis-book 第 32 章（AN3.3，見 chapter-constraints），原處留一條 see 與「已移至⋯⋯」的錨點（線代書已發布）。MA.21（第 21 章）對它的引用改成借用（等引擎支援 borrows 語法）。搬完之後刪掉 `registry/moves.yaml` 的這一列。
7. - [ ] **第 14 章 §14.6**（2026-10-09 定案）：刪除二階導數判別法的應用，只保留純代數的定性判準，留一條 see 指向 AN3.1（判別法寫進 analysis-book 第 30 章，見 chapter-constraints）。
8. - [ ] **第 16 章**（2026-10-09）：就地定義範數空間的 Cauchy 列與閉集（`def-cauchy-local`、`def-closed-local`）；刪掉「本書至此不需要連續」，改為回指 §6.05。
9. - [ ] **第 17 章 §11 的 `thm-loewner-statement`**（2026-10-09 發現，違反 spec/03 §6 規則 3）：它在第 17 章就陳述了條件 (ii) 的正測度與條件 (iii) 的上半平面解析性，讀者讀不懂。主線只留矩陣語言的版本（非正式說法，或連續密度版），完整陳述移到 MA.21b，原處留 see 與錨點。
10. - [ ] **第 21 章沿作用域切開**（2026-10-09 定案，`todo:ch21-split`）：§10 拆成兩半，搬法記在 `registry/moves.yaml`。搬走的 label 在原處留「已移至⋯⋯」的錨點。
   - 留在 MA.21：§10 的「Integrating a matrix-valued function」、「The powers」、「The logarithm and the exponential」，以及 §§01–09、11、12。易方向（積分表示 ⇒ 算子單調）改寫成主線引理，只處理連續密度 \( w(s)\,\dd s \)，用 `def-matrix-integral` 與 `lem-integral-preserves-loewner` 即可。`cor-operator-convex-log` 目前引用 `thm-loewner` 的 Step 1，改引這個引理。`cor-log-operator-monotone` 與 `exm-exp-not-monotone` 對 Löwner 定理和 (A7) 的提及只是 remark，改成 see。
   - 移到 MA.21b（選讀）：「The one fact this chapter quotes」（`thm-pick-nevanlinna`）、`thm-loewner` 的三條件等價與難方向、習題 A1。
   - 第 21 章開頭的「The analysis this chapter imports」改寫：(A7) 不再是本章的借用，改說明 MA.21b 的位置。
11. - [ ] **跨書重複的 label**（2026-10-10 分流，見 `registry/label-triage.yaml`）：
    - `def-image`、`def-relation` 是**特例**：集合的像、「從 A 到 B 的關係」當正式定義（F2.1）；線代書的 label 改名為 `def-image-linear-map`、`def-relation-on-set`，以 `specializes` 指回，舊 label 留錨點。
    - `exr-functions-*` 六題是**撞名**：題目完全不同，線代書第 0 章遷移到 F 冊重編時改名。
    - 其餘 14 個是**同一內容**：遷移時以 analysis-book 為準合併。
12. - [ ] **`thm-zorn`、`thm-induction` 的接手**（2026-10-10）：線代書 §1.8 改成以 b 借用 F2.4 的 Zorn 引理（地圖已記 LA1.1 ← F2.4，scope F2.2）。F2.4、F2.2 寫好後接手這兩個 label（`chapter-constraints.yaml` 的 `takes`），線代書原處留錨點。

## 書稿巨集的待辦

- [ ] **新增六個語意巨集**（2026-10-10 確認，`registry/notation.yaml` 中 status 為 confirmed 的條目）：`\Lp{p}`、`\ellp{p}`、`\Cont{K}`、`\Cz{X}`、`\Hz{1}`、`\AltGroup{n}`。寫到用得上的章之前，加進該書的 `latex/macros.tex`（網站版由 `build/macros.py` 讀同一檔）。analysis-book 的 `\Alt` 是交錯形式的運算子，不要和 `\AltGroup` 混用。

## 授權的待辦

不需要遷移：analysis-book、linear-algebra、regression 的書稿都已是 CC BY-NC-SA 4.0（2026-10-09 確認各 repo 的 `LICENSE`）。新冊（代數、ST 等）建 repo 時沿用同一份 `LICENSE`。

- [ ] `analysis-book`：它的 `book.yaml` 引用大量受版權保護的教科書作為「來源節點」，只能取結構，不能取文字；originality 檢查（`blueprint/originality.py`）要保留。
