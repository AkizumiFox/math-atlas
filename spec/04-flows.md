# 04 流程圖

五張圖：

1. 每節的生成與審查
2. build 管線
3. 陳述雜湊與重審
4. 約定變更治理
5. 讀者路徑

## 1. 每節的生成與審查

一次只生成一節（Ghrist 的經驗）。生成者和審查者必須來自不同的模型家族，審查者也看不到生成者的推理過程。

```mermaid
flowchart TD
  A[Spec：本節在 registry 的節點、uses 的 ID、目標 A／R、必含的例子與反例] --> B[注入作用域：遞移上游的陳述 ID、記號巨集、術語]
  B --> C[生成一節：只帶 registry 摘要與記號表，不帶受版權保護的教科書全文]
  C --> D{lint：巨集、ID 解析、原始字形、前向引用}
  D -- 失敗 --> C
  D -- 通過 --> E[異質盲審 ×2：逐行檢查、嘗試構造反例、列出隱藏假設]
  E --> F{有未解決的標記？}
  F -- 有 --> C
  F -- 無 --> G[機械驗證：計算用 SymPy；抽樣核心定理做 Lean 陳述，再 back-translation 比對]
  G --> H[版權重疊檢測：n-gram 與 embedding]
  H --> I[人工抽審：20% 證明，加上全部易錯節點]
  I --> J[狀態：drafted → reviewed → lean-stated → lean-proved]
  E -. 抓到的真實錯誤 .-> K[validation 題庫：讓學生找錯的「有瑕疵證明」]
```

## 2. build 管線

```mermaid
flowchart LR
  S[書稿 Markdown] --> P[pandoc＋Lua 掃描：labels、uses、uses_kinds]
  P --> X[crossref_labels.json]
  X --> R[跨冊 ID 解析：全套 registry]
  R --> C1[computed edges：section → chapter]
  C1 --> D[atlas.py diff：計畫 vs 計算 vs 陳述]
  C1 --> CK[atlas.py check：無環、章序、選讀、b 的 why]
  R --> N[記號作用域 lint：只用遞移上游 import 的記號]
  R --> H[陳述雜湊：見圖 3]
  CK --> OUT[HTML／PDF、先備頁、依賴圖、概念頁]
  D --> OUT
  N --> OUT
```

## 3. 陳述雜湊與重審

每條 uses 邊都存下被引用陳述在**正規化**後的雜湊。正規化會去掉空白和排版差異，並展開巨集到語意層。所以只改記號的渲染方式，不會觸發重審。

```mermaid
flowchart TD
  A[上游陳述被修改] --> B[正規化後重算雜湊]
  B --> C{與下游邊上存的雜湊相同？}
  C -- 相同：只是排版或渲染 --> Z[不動作]
  C -- 不同 --> D[沿 uses／borrows 找出所有直接下游]
  D --> E[標記為 needs-review，狀態退回 drafted]
  E --> F[重跑圖 1 的 E–I]
  F --> G[更新邊上的雜湊]
  D --> H[errata：列出受影響的章與已發布版本]
```

## 4. 約定變更治理

記號約定（02）和邊型別規則（01）的變更，不能直接改檔。

```mermaid
flowchart TD
  A[提案：改哪一條約定、理由] --> B[影響分析：用到該巨集或規則的章數、重載碰撞、下游雜湊會不會變]
  B --> C{作者核准？}
  C -- 否 --> X[關閉]
  C -- 是 --> D[改 notation.yaml 或 spec，版本號 +1]
  D --> E[全套 rebuild]
  E --> F{lint 全過？}
  F -- 否 --> G[修受影響的章] --> E
  F -- 是 --> H[changelog＋讀者公告：哪些冊的記號變了]
```

## 5. 讀者路徑

```mermaid
flowchart TD
  A[讀者選目標：某章、某冊或某資格考] --> B[算 s 祖先閉包＝必讀集合]
  B --> C[扣掉已掌握的章：mastery 紀錄或入門測驗]
  C --> D[依全套章序排出待讀清單]
  D --> E[逐章閱讀]
  E --> F{遇到 b 邊的借用結果}
  F -- 接受黑盒 --> E
  F -- 想看證明 --> G[跳到來源章，讀完返回]
  G --> E
  E --> H[章末檢查：exit checks、L1–L3 習題]
  H -- 未過 --> I[回到 s 前驅的弱點：weakest links] --> E
  H -- 通過 --> J[更新 mastery；encompassing 權重讓複習效果回流到先修]
  J --> D
```
