# 計畫 vs 計算 vs 陳述層（由 `tools/atlas.py diff` 產生）

## 計畫中的搬家（registry/moves.yaml，已套用在計算邊上，書稿尚未改）

- `thm-unitary-exponential`：LA3.12 → AN3.3（2026-10-09）；改以 b 借用的章：MA.21
- `thm-pick-nevanlinna`：MA.21 → MA.21b（2026-10-09）
- `thm-loewner`：MA.21 → MA.21b（2026-10-09）
- `exr-loewners-theorem-a1`：MA.21 → MA.21b（2026-10-09）

## b 被當成 s 使用

（無）

## 計畫中有、證明沒用（兩端都有書稿：已由計算值取代，不進入圖）

（無）

## 證明有用、計畫中沒有（只列混合來源的章；純線代章本來就以計算值為準）

- AN3.3 ← LA2.10：計算為 s（硬引用 2），計畫為 revisits
- AN3.3 ← LA3.11：計算為 s（硬引用 3），計畫為 無
- AN3.3 ← LA3.12：計算為 s（硬引用 4），計畫為 無

## 陳述層的 uses／borrows 在章層級找不到路徑

- `thm-dedekind-lub`（F3.3）uses `def-lub`（AN1.1）：章層級沒有 AN1.1 ⇒ F3.3 的硬路徑
- `thm-r-unique`（F3.4）uses `def-lub`（AN1.1）：章層級沒有 AN1.1 ⇒ F3.4 的硬路徑
- `thm-r-unique`（F3.4）uses `thm-naturals-unbounded`（AN1.1）：章層級沒有 AN1.1 ⇒ F3.4 的硬路徑

## b 邊尚未宣告記號作用域（`scope`，spec/03 §6.1）

（無）

## 跨書重複的 label（registry/computed/labels.yaml，分流見 registry/label-triage.yaml）

- `def-cartesian-product`：la F2.1、ab F2.1　同一內容，遷移時合併
- `def-composition`：la F2.1、ab F2.1　同一內容，遷移時合併
- `def-empty-set`：la F2.1、ab F2.1　同一內容，遷移時合併
- `def-function`：la F2.1、ab F2.1　同一內容，遷移時合併
- `def-image`：la LA1.2、ab F2.1　特例，改名並以 specializes 指回
- `def-indexed-family`：la F2.1、ab F2.1　同一內容，遷移時合併
- `def-inverse-function`：la F2.1、ab F2.1　同一內容，遷移時合併
- `def-left-right-inverse`：la F2.1、ab F2.1　同一內容，遷移時合併
- `def-power-set`：la F2.1、ab F2.1　同一內容，遷移時合併
- `def-relation`：la F2.2、ab F2.1　特例，改名並以 specializes 指回
- `def-set-builder`：la F2.1、ab F2.1　同一內容，遷移時合併
- `def-set-equality`：la F2.1、ab F2.1　同一內容，遷移時合併
- `def-subset`：la F2.1、ab F2.1　同一內容，遷移時合併
- `exr-functions-a1`：la F2.1、ab F2.1　撞名，改名
- `exr-functions-b1`：la F2.1、ab F2.1　撞名，改名
- `exr-functions-b2`：la F2.1、ab F2.1　撞名，改名
- `exr-functions-b3`：la F2.1、ab F2.1　撞名，改名
- `exr-functions-c1`：la F2.1、ab F2.1　撞名，改名
- `exr-functions-c2`：la F2.1、ab F2.1　撞名，改名
- `thm-left-inverse-iff-injective`：la F2.1、ab F2.1　同一內容，遷移時合併
- `thm-sqrt2-irrational`：la F1.5、ab F1.2　同一內容，遷移時合併
- `thm-strong-induction`：la F1.5、ab F1.3　同一內容，遷移時合併

## 陳述 ID 對到的書稿 label 不在同一章

- `def-complex-numbers`：地圖放在 F4.1，書稿目前在 la F3.6
- `def-field`：地圖放在 F5.2，書稿目前在 la F3.7
- `def-polynomial-ring`：地圖放在 F5.4，書稿目前在 la F3.8
- `thm-induction`：地圖放在 F2.2，書稿目前在 la F1.5　已知：F2.2 寫好後接手（chapter-constraints.yaml）
- `thm-transpositions-generate`：地圖放在 F5.3，書稿目前在 la AL1.1
- `thm-zorn`：地圖放在 F2.4，書稿目前在 la LA1.1　已知：F2.4 寫好後接手（chapter-constraints.yaml）

## 外部科目圖的對照（registry/external/subject-dag.yaml）

共 33 項差異，其中 33 項已記在 `registry/field-deviations.yaml`。以下只列新出現的：

（無）

