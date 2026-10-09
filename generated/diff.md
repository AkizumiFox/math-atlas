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

（無）

## b 邊尚未宣告記號作用域（`scope`，spec/03 §6.1）

（無）

## 跨書重複的 label（registry/computed/labels.yaml）

同一章的重複是遷移時要合併的同一份內容；不同章的重複是撞名。

- `def-cartesian-product`：la F2.1、ab F2.1
- `def-composition`：la F2.1、ab F2.1
- `def-empty-set`：la F2.1、ab F2.1
- `def-function`：la F2.1、ab F2.1
- `def-image`：la LA1.2、ab F2.1　**不同章**：同一結果就在遷移時決定歸屬；意義不同（例如線性映射的像 vs 集合的像）就要改名
- `def-indexed-family`：la F2.1、ab F2.1
- `def-inverse-function`：la F2.1、ab F2.1
- `def-left-right-inverse`：la F2.1、ab F2.1
- `def-power-set`：la F2.1、ab F2.1
- `def-relation`：la F2.2、ab F2.1　**不同章**：同一結果就在遷移時決定歸屬；意義不同（例如線性映射的像 vs 集合的像）就要改名
- `def-set-builder`：la F2.1、ab F2.1
- `def-set-equality`：la F2.1、ab F2.1
- `def-subset`：la F2.1、ab F2.1
- `exr-functions-a1`：la F2.1、ab F2.1
- `exr-functions-b1`：la F2.1、ab F2.1
- `exr-functions-b2`：la F2.1、ab F2.1
- `exr-functions-b3`：la F2.1、ab F2.1
- `exr-functions-c1`：la F2.1、ab F2.1
- `exr-functions-c2`：la F2.1、ab F2.1
- `thm-left-inverse-iff-injective`：la F2.1、ab F2.1
- `thm-sqrt2-irrational`：la F1.5、ab F1.2　**不同章**：同一結果就在遷移時決定歸屬；意義不同（例如線性映射的像 vs 集合的像）就要改名
- `thm-strong-induction`：la F1.5、ab F1.3　**不同章**：同一結果就在遷移時決定歸屬；意義不同（例如線性映射的像 vs 集合的像）就要改名

## 陳述 ID 對到的書稿 label 不在同一章

- `thm-induction`：地圖放在 F2.2，書稿目前在 la F1.5
- `thm-zorn`：地圖放在 F2.4，書稿目前在 la LA1.1

## 外部科目圖的對照（registry/external/subject-dag.yaml）

共 32 項差異，其中 32 項已記在 `registry/field-deviations.yaml`。以下只列新出現的：

（無）

