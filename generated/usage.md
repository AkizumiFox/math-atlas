# 英文用詞變體（由 `tools/usage_report.py` 從兩本書稿統計，勿手改）

約定在 `registry/usage.yaml`。每組選一個（use），其餘列為 avoid；status 為 proposed 的組待作者確認，confirmed 的組列出書稿裡每一處 avoid 寫法（將來由引擎在 build 時檢查，spec/05）。統計只看散文：數學式、程式碼、TikZ、label 與參照都已去掉。

## 單射（`injective`，confirmed，機械替換）

| 寫法 | 線代書 | analysis-book | 合計 | |
|---|---:|---:|---:|---|
| injective | 489 | 118 | 607 | **use** |
| injection* | 7 | 5 | 12 | **use** |
| injectivity | 61 | 41 | 102 | **use** |
| is one-to-one | 1 | 0 | 1 | avoid |
| are one-to-one | 0 | 0 | 0 | avoid |
| be one-to-one | 0 | 0 | 0 | avoid |
| not one-to-one | 0 | 0 | 0 | avoid |
| one-one | 0 | 0 | 0 | avoid |

injective 系列 721 次。one-to-one 只禁形容詞用法（is one-to-one 等）：副詞用法（matches it one-to-one with、correspond one-to-one to）是正確的英文，定義裡介紹同義詞的「injective (one-to-one)」也保留，讓讀者認得其他書的寫法。（2026-10-10 修正：原提案把 one-to-one 整個列為 avoid。）

avoid 寫法出現處（1 個檔案）：

- `linear-algebra/src/ch05-duality/04-dual-map.md`：1 處，行 507

## 滿射（`surjective`，confirmed，逐處判斷）

| 寫法 | 線代書 | analysis-book | 合計 | |
|---|---:|---:|---:|---|
| surjective | 340 | 88 | 428 | **use** |
| surjection* | 15 | 12 | 27 | **use** |
| surjectivity | 48 | 18 | 66 | **use** |
| is onto | 20 | 1 | 21 | avoid |
| are onto | 1 | 0 | 1 | avoid |
| be onto | 0 | 0 | 0 | avoid |
| not onto | 1 | 0 | 1 | avoid |

surjective 系列 521 次。onto 出現 368 次，但絕大多數是介系詞（projection onto a subspace），不能整個禁用；只禁用形容詞用法（is onto 等，共 23 次）。

avoid 寫法出現處（15 個檔案）：

- `analysis-book/src/ch06-sets-and-functions/04-functions.md`：1 處，行 347
- `linear-algebra/src/ch03-linear-systems/05-rank.md`：1 處，行 752
- `linear-algebra/src/ch04-matrices-of-maps/04-products-and-quotients.md`：1 處，行 396
- `linear-algebra/src/ch05-duality/03-double-dual.md`：3 處，行 163, 265, 435
- `linear-algebra/src/ch08-block-matrices/05-commutators-and-shoda.md`：1 處，行 272
- `linear-algebra/src/ch12-spectral-theory/08-spectral-resolutions-and-functional-calculus.md`：1 處，行 637
- `linear-algebra/src/ch14-forms/03-symmetric-alternating-hermitian.md`：1 處，行 257
- `linear-algebra/src/ch14-forms/08-witts-theorems.md`：3 處，行 32, 224, 307
- `linear-algebra/src/ch15-tensors/04-contraction-and-trace.md`：2 處，行 118, 345
- `linear-algebra/src/ch18-convexity/01-convex-sets.md`：1 處，行 358
- `linear-algebra/src/ch21-inequalities/04-unitarily-invariant-norms.md`：1 處，行 122
- `linear-algebra/src/ch22-geometry/01-affine-spaces.md`：4 處，行 348, 350, 354, 568
- `linear-algebra/src/ch22-geometry/03-polyhedra-and-linear-programming.md`：1 處，行 100
- `linear-algebra/src/ch22-geometry/04-euclidean-motions.md`：1 處，行 3
- `linear-algebra/src/ch24-applied/09-vibrations.md`：1 處，行 401

## 雙射（`bijective`，confirmed，機械替換）

| 寫法 | 線代書 | analysis-book | 合計 | |
|---|---:|---:|---:|---|
| bijective | 122 | 28 | 150 | **use** |
| bijection* | 227 | 21 | 248 | **use** |
| one-to-one correspondence* | 1 | 0 | 1 | avoid |

bijective／bijection 398 次，one-to-one correspondence 1 次。

avoid 寫法出現處（1 個檔案）：

- `linear-algebra/src/ch01-vector-spaces/05-basis.md`：1 處，行 220

## 像（`image`，confirmed，機械替換）

| 寫法 | 線代書 | analysis-book | 合計 | |
|---|---:|---:|---:|---|
| image* | 408 | 74 | 482 | **use** |

f(X) 一律稱 image（482 次）。range 出現 161 次，幾乎都是別的意思（range over、a range of lines），所以不列入 avoid、也不做 lint；只有線代書一處把 range 當成 image 的同義詞，改寫時順手改掉。range 不用來指對應域（codomain）。

書稿裡沒有 avoid 寫法。

## 核與零空間（`kernel`，confirmed，機械替換）

| 寫法 | 線代書 | analysis-book | 合計 | |
|---|---:|---:|---:|---|
| kernel* | 416 | 0 | 416 | **use** |
| null space* | 80 | 0 | 80 | **use** |
| nullspace* | 0 | 0 | 0 | avoid |

兩個都保留，各有用途，不是變體：kernel 是映射的核（ker T，416 次），null space 是矩陣的零空間（nul A ⊆ Fⁿ，80 次），這是線代書 NOTATION.md 的既有約定。nullspace（連寫）0 次，列入 avoid 防止日後出現。

書稿裡沒有 avoid 寫法。

## 映射與函數（`map`，confirmed，機械替換）

| 寫法 | 線代書 | analysis-book | 合計 | |
|---|---:|---:|---:|---|
| map | 1309 | 21 | 1330 | **use** |
| maps | 540 | 5 | 545 | **use** |
| linear map* | 511 | 0 | 511 | **use** |
| function | 921 | 288 | 1209 | **use** |
| functions | 400 | 96 | 496 | **use** |
| a mapping | 0 | 0 | 0 | avoid |
| the mapping | 0 | 0 | 0 | avoid |
| mappings | 0 | 0 | 0 | avoid |
| linear mapping* | 0 | 0 | 0 | avoid |
| linear transformation* | 1 | 0 | 1 | avoid |

map 用於保持結構的映射（linear map 511 次），function 用於集合論與分析的一般函數（1,705 次）；operator 指 V → V 的線性映射。名詞 mapping 不用（現況 0 次）；linear transformation 1 次改成 linear map。動名詞 mapping（mapping X onto Y）照常使用，固定名稱列在 keep，不受 avoid 影響：spectral mapping theorem、open mapping theorem、Riemann mapping theorem、contraction mapping。（2026-10-10 修正：原提案把 mapping 整個列為 avoid，但書稿裡的 21 次全是定理名或動名詞。）

avoid 寫法出現處（1 個檔案）：

- `linear-algebra/src/ch02-linear-maps/01-linear-maps.md`：1 處，行 28

## non- 字首（`non-prefix`，confirmed，機械替換）

| 寫法 | 線代書 | analysis-book | 合計 | |
|---|---:|---:|---:|---|
| nonnegative | 0 | 0 | 0 | **use** |
| nonzero | 0 | 0 | 0 | **use** |
| nonempty | 0 | 0 | 0 | **use** |
| nonsingular | 0 | 0 | 0 | **use** |
| nontrivial | 0 | 0 | 0 | **use** |
| nondecreasing | 0 | 0 | 0 | **use** |
| nonincreasing | 0 | 0 | 0 | **use** |
| nondegenerate | 0 | 0 | 0 | **use** |
| noninvertible | 0 | 0 | 0 | **use** |
| nonpositive | 0 | 0 | 0 | **use** |
| nonmeasurable | 0 | 0 | 0 | **use** |
| `(?<![\w-])[Nn]on-[a-z][\w-]*`（正規表示式） | 3385 | 243 | 3628 | avoid |

連寫（2026-10-10 定案）。兩本書已是美式拼寫，美式數學出版（AMS、Chicago）的慣例是 non- 直接連寫；原本「美式拼寫＋連字號」是混搭。例外照 Chicago：後面接專有名詞或大寫字時保留連字號（non-Euclidean、non-Archimedean、non-Hausdorff），avoid 的規則只抓 non- 後接小寫字母的寫法。書稿現況是 100% 加連字號，遷移是純機械替換（spec/06），陳述雜湊先正規化 avoid 寫法再計算，所以不觸發重審（spec/04 圖 3）。

avoid 寫法出現處（289 個檔案）：

- `analysis-book/src/ch01-connectives-and-derivations/01-statements-and-connectives.md`：3 處，行 36, 110, 387
- `analysis-book/src/ch01-connectives-and-derivations/02-derivations.md`：1 處，行 64
- `analysis-book/src/ch01-connectives-and-derivations/06-disjunction-introduction.md`：1 處，行 61
- `analysis-book/src/ch01-connectives-and-derivations/07-disjunction-and-cases.md`：1 處，行 275
- `analysis-book/src/ch01-connectives-and-derivations/index.md`：1 處，行 7
- `analysis-book/src/ch02-negation-and-classical-logic/02-negation-and-contradiction.md`：1 處，行 64
- `analysis-book/src/ch02-negation-and-classical-logic/04-biconditional-and-definitions.md`：2 處，行 329, 548
- `analysis-book/src/ch02-negation-and-classical-logic/05-reductio-and-classical-rules.md`：2 處，行 181, 665
- `analysis-book/src/ch02-negation-and-classical-logic/06-finding-derivations.md`：1 處，行 39
- `analysis-book/src/ch03-semantics-soundness-completeness/01-formulas-and-parse-trees.md`：1 處，行 404
- `analysis-book/src/ch03-semantics-soundness-completeness/02-induction.md`：11 處，行 42, 264, 291, 294, 549, 551, 553, 555, 557, 563, 564
- `analysis-book/src/ch03-semantics-soundness-completeness/03-valuations-and-truth-tables.md`：3 處，行 67, 144, 520
- `analysis-book/src/ch03-semantics-soundness-completeness/04-entailment-and-equivalence.md`：4 處，行 24, 158, 568, 577
- `analysis-book/src/ch03-semantics-soundness-completeness/05-soundness.md`：1 處，行 310
- `analysis-book/src/ch03-semantics-soundness-completeness/06-completeness.md`：1 處，行 839
- `analysis-book/src/ch03-semantics-soundness-completeness/07-normal-forms.md`：1 處，行 58
- `analysis-book/src/ch04-predicate-logic/01-predicates-and-quantifiers.md`：1 處，行 243
- `analysis-book/src/ch04-predicate-logic/07-equality-and-uniqueness.md`：5 處，行 52, 74, 283, 528, 536
- `analysis-book/src/ch04-predicate-logic/11-models.md`：21 處，行 25, 33, 48, 53, 57, 84, 149, 193, 227, 229, 233, 235, 237, 269, 303, 311, 332, 452, 464, 482, 490
- `analysis-book/src/ch04-predicate-logic/12-first-order-soundness.md`：3 處，行 209, 313, 315
- `analysis-book/src/ch06-sets-and-functions/01-sets-and-subsets.md`：1 處，行 113
- `analysis-book/src/ch06-sets-and-functions/02-set-operations.md`：12 處，行 42, 148, 213, 216, 229, 235, 270, 272, 419, 439, 451, 456
- `analysis-book/src/ch06-sets-and-functions/03-products-and-relations.md`：5 處，行 46, 264, 266, 281, 445
- `analysis-book/src/ch06-sets-and-functions/04-functions.md`：7 處，行 45, 150, 201, 212, 391, 393, 541
- `analysis-book/src/ch06-sets-and-functions/05-inverses.md`：6 處，行 107, 186, 216, 286, 374, 424
- `analysis-book/src/ch06-sets-and-functions/06-images-and-preimages.md`：2 處，行 75, 552
- `analysis-book/src/ch06-sets-and-functions/index.md`：1 處，行 17
- `analysis-book/src/ch11-least-upper-bound/01-ordered-fields.md`：13 處，行 13, 32, 46, 109, 161, 164, 177, 194, 218, 280, 304, 347, 370
- `analysis-book/src/ch11-least-upper-bound/02-suprema.md`：7 處，行 25, 145, 174, 176, 198, 203, 217
- `analysis-book/src/ch11-least-upper-bound/03-the-axiom.md`：25 處，行 3, 14, 32, 35, 48, 56, 68, 113, 120, 123, 125, 127, 131, 134, 159, 173, 177, 183, 187, 189, 199, 205, 207, 216, 227
- `analysis-book/src/ch11-least-upper-bound/04-epsilon-characterization.md`：24 處，行 113, 132, 136, 139, 150, 153, 154, 163, 168, 188, 207, 264, 288, 292, 298, 306, 321, 322, 344, 354, 366, 378, 393, 394
- `analysis-book/src/ch11-least-upper-bound/05-archimedean-property.md`：21 處，行 28, 58, 76, 83, 126, 145, 147, 153, 178, 184, 229, 259, 300, 302, 304, 326, 327, 347, 351, 357, 380
- `analysis-book/src/ch11-least-upper-bound/06-density-and-roots.md`：13 處，行 18, 28, 76, 125, 199, 298, 311, 331, 341, 382, 400, 436, 449
- `analysis-book/src/ch11-least-upper-bound/07-nested-intervals.md`：12 處，行 43, 45, 50, 72, 88, 130, 149, 239, 258, 266, 289, 406
- `analysis-book/src/ch11-least-upper-bound/index.md`：1 處，行 5
- `linear-algebra/src/ch00-foundations/01-logic.md`：4 處，行 294, 383, 397, 475
- `linear-algebra/src/ch00-foundations/02-proofs.md`：7 處，行 104, 325, 369, 373, 507, 510, 519
- `linear-algebra/src/ch00-foundations/03-sets.md`：4 處，行 328, 336, 353, 356
- `linear-algebra/src/ch00-foundations/04-functions.md`：9 處，行 37, 46, 183, 192, 323, 327, 347, 350, 555
- `linear-algebra/src/ch00-foundations/05-relations.md`：12 處，行 26, 76, 113, 150, 190, 198, 233, 244, 308, 312, 483, 523
- `linear-algebra/src/ch00-foundations/06-complex-numbers.md`：14 處，行 49, 54, 58, 126, 171, 183, 211, 225, 243, 270, 373, 426, 439, 452
- `linear-algebra/src/ch00-foundations/07-fields.md`：23 處，行 16, 20, 37, 45, 106, 121, 123, 147, 163, 166, 210, 213, 229, 231, 249, 290, 312, 316, 371, 375, 483, 510, 558
- `linear-algebra/src/ch00-foundations/08-polynomials.md`：23 處，行 3, 16, 44, 57, 59, 142, 155, 186, 194, 198, 205, 319, 321, 395, 430, 478, 496, 501, 516, 517, 522, 530, 537
- `linear-algebra/src/ch00-foundations/09-matrices.md`：15 處，行 254, 294, 382, 398, 498, 538, 565, 620, 622, 625, 640, 824, 888, 948, 967
- `linear-algebra/src/ch00-foundations/10-groups.md`：6 處，行 3, 7, 36, 45, 107, 267
- `linear-algebra/src/ch00-foundations/index.md`：1 處，行 22
- `linear-algebra/src/ch01-vector-spaces/01-vector-spaces.md`：9 處，行 115, 208, 210, 221, 223, 224, 363, 565, 571
- `linear-algebra/src/ch01-vector-spaces/02-subspaces.md`：11 處，行 69, 97, 101, 288, 311, 315, 320, 356, 388, 557, 565
- `linear-algebra/src/ch01-vector-spaces/03-span.md`：2 處，行 168, 225
- `linear-algebra/src/ch01-vector-spaces/04-independence.md`：14 處，行 19, 65, 89, 135, 137, 140, 149, 166, 170, 192, 204, 228, 264, 436
- `linear-algebra/src/ch01-vector-spaces/05-basis.md`：6 處，行 104, 117, 127, 497, 509, 527
- `linear-algebra/src/ch01-vector-spaces/06-dimension.md`：7 處，行 60, 66, 95, 118, 189, 191, 361
- `linear-algebra/src/ch01-vector-spaces/07-sums-and-direct-sums.md`：10 處，行 41, 255, 349, 381, 425, 498, 572, 599, 609, 611
- `linear-algebra/src/ch01-vector-spaces/08-infinite-dimensional.md`：13 處，行 40, 42, 56, 104, 107, 128, 130, 177, 269, 283, 292, 294, 366
- `linear-algebra/src/ch01-vector-spaces/09-changing-the-field.md`：2 處，行 32, 130
- `linear-algebra/src/ch01-vector-spaces/index.md`：1 處，行 11
- `linear-algebra/src/ch02-linear-maps/01-linear-maps.md`：6 處，行 263, 325, 342, 371, 452, 594
- `linear-algebra/src/ch02-linear-maps/02-kernel-image.md`：3 處，行 98, 100, 299
- `linear-algebra/src/ch02-linear-maps/03-rank-nullity.md`：2 處，行 35, 324
- `linear-algebra/src/ch02-linear-maps/04-algebra-of-linear-maps.md`：6 處，行 88, 252, 257, 368, 369, 428
- `linear-algebra/src/ch02-linear-maps/05-isomorphisms.md`：3 處，行 89, 297, 400
- `linear-algebra/src/ch02-linear-maps/index.md`：1 處，行 13
- `linear-algebra/src/ch03-linear-systems/01-linear-systems.md`：5 處，行 104, 127, 143, 310, 405
- `linear-algebra/src/ch03-linear-systems/02-gaussian-elimination.md`：27 處，行 17, 21, 37, 125, 127, 135, 151, 170, 172, 179, 198, 201, 207, 220, 224, 226, 230, 367, 390, 408, 421, 429, 435, 461, 463, 655, 685
- `linear-algebra/src/ch03-linear-systems/03-rref-uniqueness.md`：13 處，行 3, 57, 77, 97, 107, 178, 193, 206, 208, 237, 246, 256, 350
- `linear-algebra/src/ch03-linear-systems/04-elementary-matrices-and-inverses.md`：11 處，行 5, 33, 128, 161, 167, 188, 195, 231, 273, 378, 571
- `linear-algebra/src/ch03-linear-systems/05-rank.md`：14 處，行 57, 115, 118, 167, 171, 251, 269, 277, 281, 285, 367, 369, 712, 716
- `linear-algebra/src/ch03-linear-systems/06-lu-factorization.md`：24 處，行 14, 76, 112, 126, 137, 158, 183, 196, 311, 331, 335, 348, 360, 395, 419, 456, 479, 493, 504, 574, 643, 659, 669, 679
- `linear-algebra/src/ch03-linear-systems/07-applications.md`：13 處，行 17, 54, 58, 65, 67, 78, 141, 254, 306, 309, 495, 511, 599
- `linear-algebra/src/ch04-matrices-of-maps/01-matrix-of-a-map.md`：5 處，行 104, 109, 115, 397, 543
- `linear-algebra/src/ch04-matrices-of-maps/02-change-of-basis.md`：5 處，行 45, 221, 230, 501, 513
- `linear-algebra/src/ch04-matrices-of-maps/03-rank-factorization.md`：9 處，行 12, 24, 32, 40, 95, 172, 308, 315, 384
- `linear-algebra/src/ch04-matrices-of-maps/04-products-and-quotients.md`：4 處，行 49, 168, 260, 262
- `linear-algebra/src/ch04-matrices-of-maps/05-projections-and-trace.md`：4 處，行 32, 200, 237, 289
- `linear-algebra/src/ch05-duality/01-linear-functionals.md`：10 處，行 3, 84, 96, 101, 108, 300, 329, 510, 523, 529
- `linear-algebra/src/ch05-duality/02-annihilators.md`：4 處，行 24, 64, 106, 290
- `linear-algebra/src/ch05-duality/03-double-dual.md`：4 處，行 59, 68, 72, 299
- `linear-algebra/src/ch05-duality/04-dual-map.md`：3 處，行 62, 64, 509
- `linear-algebra/src/ch05-duality/05-duality-subspaces-quotients.md`：15 處，行 178, 190, 195, 199, 203, 208, 221, 231, 235, 251, 266, 302, 310, 339, 351
- `linear-algebra/src/ch05-duality/06-hyperplanes-and-systems.md`：10 處，行 17, 38, 151, 262, 266, 300, 439, 440, 455, 461
- `linear-algebra/src/ch06-polynomials/01-division.md`：25 處，行 29, 43, 49, 70, 117, 132, 135, 139, 144, 147, 171, 173, 178, 217, 226, 230, 240, 249, 263, 271, 294, 303, 304, 306, 334
- `linear-algebra/src/ch06-polynomials/02-ideals-and-gcd.md`：34 處，行 17, 37, 75, 82, 86, 89, 102, 116, 120, 124, 131, 144, 165, 171, 178, 185, 257, 266, 313, 334, 358, 383, 386, 399, 427, 445, 476, 477, 512, 534, 537, 548, 550, 551
- `linear-algebra/src/ch06-polynomials/03-unique-factorization.md`：34 處，行 3, 7, 9, 17, 21, 24, 26, 43, 46, 62, 73, 76, 98, 129, 139, 142, 146, 161, 163, 169, 182, 321, 322, 323, 376, 380, 384, 407, 421, 422, 426, 431, 434, 435
- `linear-algebra/src/ch06-polynomials/04-roots-and-multiplicity.md`：27 處，行 3, 14, 21, 30, 47, 91, 97, 104, 120, 135, 137, 144, 160, 162, 215, 236, 246, 259, 263, 267, 289, 336, 364, 381, 385, 433, 515
- `linear-algebra/src/ch06-polynomials/05-fundamental-theorem-of-algebra.md`：27 處，行 12, 21, 104, 109, 152, 188, 197, 213, 216, 238, 246, 249, 277, 282, 287, 322, 324, 326, 328, 340, 386, 391, 434, 451, 480, 494, 531
- `linear-algebra/src/ch06-polynomials/06-interpolation-and-crt.md`：16 處，行 9, 25, 33, 191, 200, 208, 233, 299, 308, 316, 338, 397, 488, 496, 520, 522
- `linear-algebra/src/ch06-polynomials/07-polynomials-of-operators.md`：18 處，行 74, 82, 89, 93, 103, 107, 138, 146, 148, 157, 339, 351, 402, 440, 443, 449, 457, 492
- `linear-algebra/src/ch06-polynomials/index.md`：2 處，行 5, 22
- `linear-algebra/src/ch07-determinants/01-area-and-volume.md`：1 處，行 125
- `linear-algebra/src/ch07-determinants/02-multilinear-alternating-forms.md`：5 處，行 90, 154, 213, 288, 318
- `linear-algebra/src/ch07-determinants/03-permutations-and-sign.md`：2 處，行 81, 87
- `linear-algebra/src/ch07-determinants/04-existence-and-uniqueness.md`：10 處，行 186, 198, 202, 215, 219, 289, 294, 320, 402, 408
- `linear-algebra/src/ch07-determinants/05-properties.md`：8 處，行 90, 103, 268, 301, 309, 431, 448, 453
- `linear-algebra/src/ch07-determinants/06-cofactor-expansion.md`：4 處，行 44, 193, 412, 450
- `linear-algebra/src/ch07-determinants/07-minors-and-rank.md`：22 處，行 43, 48, 61, 66, 69, 70, 75, 79, 81, 83, 106, 195, 211, 236, 250, 273, 277, 345, 371, 382, 389, 391
- `linear-algebra/src/ch07-determinants/08-special-determinants.md`：9 處，行 3, 81, 104, 122, 163, 197, 266, 276, 278
- `linear-algebra/src/ch07-determinants/09-orientation-and-volume.md`：7 處，行 41, 43, 170, 179, 181, 218, 254
- `linear-algebra/src/ch07-determinants/10-characteristic-polynomial.md`：14 處，行 3, 62, 81, 86, 216, 224, 236, 284, 375, 389, 412, 423, 430, 432
- `linear-algebra/src/ch08-block-matrices/01-block-multiplication.md`：6 處，行 47, 179, 207, 214, 332, 426
- `linear-algebra/src/ch08-block-matrices/02-rank-of-block-matrices.md`：2 處，行 249, 387
- `linear-algebra/src/ch08-block-matrices/03-block-determinants-and-schur-complements.md`：9 處，行 47, 306, 357, 384, 417, 437, 498, 532, 576
- `linear-algebra/src/ch08-block-matrices/04-kronecker-product.md`：9 處，行 51, 55, 64, 283, 417, 421, 432, 437, 445
- `linear-algebra/src/ch08-block-matrices/05-commutators-and-shoda.md`：5 處，行 35, 193, 206, 355, 457
- `linear-algebra/src/ch09-eigenvalues/01-invariant-subspaces.md`：6 處，行 3, 44, 320, 336, 340, 346
- `linear-algebra/src/ch09-eigenvalues/02-eigenvalues-and-eigenvectors.md`：26 處，行 17, 22, 26, 28, 31, 47, 52, 56, 58, 74, 93, 173, 177, 191, 203, 219, 240, 246, 307, 356, 358, 426, 446, 454, 460, 486
- `linear-algebra/src/ch09-eigenvalues/03-multiplicities.md`：5 處，行 11, 52, 138, 240, 275
- `linear-algebra/src/ch09-eigenvalues/04-diagonalization.md`：7 處，行 28, 71, 81, 83, 429, 460, 462
- `linear-algebra/src/ch09-eigenvalues/05-minimal-polynomial.md`：15 處，行 11, 29, 31, 42, 65, 74, 80, 92, 111, 121, 160, 174, 219, 235, 358
- `linear-algebra/src/ch09-eigenvalues/06-cayley-hamilton.md`：3 處，行 7, 133, 301
- `linear-algebra/src/ch09-eigenvalues/07-triangularization.md`：8 處，行 53, 98, 124, 293, 309, 359, 373, 387
- `linear-algebra/src/ch09-eigenvalues/08-primary-decomposition.md`：11 處，行 26, 236, 244, 265, 348, 359, 365, 369, 397, 401, 403
- `linear-algebra/src/ch09-eigenvalues/09-commuting-operators.md`：18 處，行 13, 15, 43, 50, 89, 93, 97, 103, 105, 111, 121, 183, 206, 252, 254, 318, 322, 379
- `linear-algebra/src/ch09-eigenvalues/10-spectral-mapping.md`：20 處，行 28, 42, 50, 90, 126, 130, 140, 144, 152, 160, 169, 202, 204, 249, 258, 362, 398, 407, 416, 505
- `linear-algebra/src/ch09-eigenvalues/11-powers-recurrences-markov.md`：10 處，行 148, 154, 156, 175, 194, 245, 313, 377, 427, 516
- `linear-algebra/src/ch09-eigenvalues/index.md`：1 處，行 20
- `linear-algebra/src/ch10-canonical-forms/01-generalized-eigenspaces.md`：11 處，行 34, 57, 68, 74, 140, 149, 151, 176, 196, 214, 289
- `linear-algebra/src/ch10-canonical-forms/02-nilpotent-operators.md`：10 處，行 21, 31, 34, 159, 165, 248, 407, 451, 477, 552
- `linear-algebra/src/ch10-canonical-forms/03-jordan-canonical-form.md`：6 處，行 47, 49, 83, 286, 420, 432
- `linear-algebra/src/ch10-canonical-forms/04-real-jordan-and-weyr-forms.md`：14 處，行 43, 87, 178, 212, 218, 337, 349, 368, 395, 411, 440, 473, 560, 625
- `linear-algebra/src/ch10-canonical-forms/05-cyclic-subspaces-and-companion-matrices.md`：8 處，行 51, 70, 77, 106, 116, 314, 350, 521
- `linear-algebra/src/ch10-canonical-forms/06-rational-canonical-form.md`：25 處，行 9, 54, 64, 74, 76, 114, 133, 147, 165, 174, 183, 252, 256, 260, 270, 276, 285, 289, 312, 316, 318, 346, 403, 518, 567
- `linear-algebra/src/ch10-canonical-forms/07-smith-normal-form.md`：28 處，行 3, 35, 42, 49, 53, 89, 96, 118, 126, 130, 132, 140, 167, 186, 190, 321, 374, 387, 397, 450, 452, 545, 553, 565, 579, 583, 591, 593
- `linear-algebra/src/ch10-canonical-forms/08-jordan-chevalley.md`：6 處，行 32, 34, 51, 55, 76, 84
- `linear-algebra/src/ch10-canonical-forms/09-functions-of-matrices-and-odes.md`：2 處，行 337, 622
- `linear-algebra/src/ch10-canonical-forms/10-convergent-matrices.md`：2 處，行 236, 250
- `linear-algebra/src/ch11-inner-products/01-inner-products.md`：27 處，行 9, 19, 41, 47, 100, 102, 108, 128, 130, 132, 138, 140, 142, 144, 160, 169, 187, 189, 210, 249, 251, 266, 301, 336, 396, 578, 595
- `linear-algebra/src/ch11-inner-products/02-orthonormal-bases.md`：7 處，行 34, 38, 134, 152, 180, 341, 379
- `linear-algebra/src/ch11-inner-products/03-orthogonal-complements-and-projections.md`：6 處，行 54, 166, 225, 248, 447, 459
- `linear-algebra/src/ch11-inner-products/04-least-squares.md`：1 處，行 213
- `linear-algebra/src/ch11-inner-products/05-riesz-and-duality.md`：6 處，行 153, 253, 265, 273, 294, 296
- `linear-algebra/src/ch11-inner-products/06-adjoints.md`：7 處，行 132, 161, 361, 454, 473, 509, 512
- `linear-algebra/src/ch11-inner-products/07-isometries-and-unitary-maps.md`：7 處，行 120, 136, 229, 278, 513, 526, 628
- `linear-algebra/src/ch11-inner-products/08-qr-and-householder.md`：9 處，行 54, 58, 168, 182, 186, 191, 196, 229, 725
- `linear-algebra/src/ch11-inner-products/09-bessel-parseval-fourier.md`：7 處，行 39, 48, 113, 137, 412, 459, 490
- `linear-algebra/src/ch11-inner-products/10-orthogonal-polynomials.md`：12 處，行 15, 17, 83, 88, 90, 145, 184, 210, 212, 218, 302, 340
- `linear-algebra/src/ch11-inner-products/index.md`：1 處，行 7
- `linear-algebra/src/ch12-spectral-theory/01-schur-triangularization.md`：8 處，行 3, 49, 65, 77, 257, 285, 417, 457
- `linear-algebra/src/ch12-spectral-theory/02-self-adjoint-operators.md`：5 處，行 194, 296, 333, 400, 412
- `linear-algebra/src/ch12-spectral-theory/03-normal-operators.md`：8 處，行 9, 105, 147, 208, 281, 314, 350, 426
- `linear-algebra/src/ch12-spectral-theory/04-spectral-theorem-complex.md`：7 處，行 52, 58, 63, 169, 188, 448, 461
- `linear-algebra/src/ch12-spectral-theory/05-spectral-theorem-real.md`：3 處，行 81, 182, 300
- `linear-algebra/src/ch12-spectral-theory/06-orthogonal-matrices-and-rotations.md`：9 處，行 259, 274, 320, 325, 362, 372, 410, 425, 589
- `linear-algebra/src/ch12-spectral-theory/07-commuting-normal-families.md`：6 處，行 26, 42, 88, 189, 228, 232
- `linear-algebra/src/ch12-spectral-theory/08-spectral-resolutions-and-functional-calculus.md`：15 處，行 5, 54, 165, 169, 185, 222, 343, 345, 357, 371, 375, 412, 518, 633, 712
- `linear-algebra/src/ch12-spectral-theory/09-circulants-and-the-dft.md`：8 處，行 65, 86, 150, 152, 507, 533, 583, 616
- `linear-algebra/src/ch12-spectral-theory/10-sylvester-equation.md`：9 處，行 35, 92, 266, 280, 309, 428, 445, 452, 458
- `linear-algebra/src/ch12-spectral-theory/11-defect-from-normality.md`：10 處，行 3, 43, 100, 107, 113, 142, 193, 304, 398, 481
- `linear-algebra/src/ch13-psd-and-svd/01-positive-definite-matrices.md`：13 處，行 3, 7, 9, 25, 96, 175, 195, 197, 293, 383, 418, 476, 536
- `linear-algebra/src/ch13-psd-and-svd/02-square-roots-and-cholesky.md`：8 處，行 3, 24, 34, 106, 135, 207, 249, 453
- `linear-algebra/src/ch13-psd-and-svd/03-gram-matrices.md`：7 處，行 32, 40, 65, 72, 189, 247, 257
- `linear-algebra/src/ch13-psd-and-svd/04-simultaneous-diagonalization.md`：4 處，行 42, 81, 302, 376
- `linear-algebra/src/ch13-psd-and-svd/05-the-loewner-order.md`：7 處，行 3, 9, 31, 89, 123, 132, 180
- `linear-algebra/src/ch13-psd-and-svd/06-block-positive-matrices.md`：1 處，行 117
- `linear-algebra/src/ch13-psd-and-svd/07-determinant-inequalities.md`：1 處，行 181
- `linear-algebra/src/ch13-psd-and-svd/08-schur-product-theorem.md`：9 處，行 33, 85, 110, 115, 126, 352, 360, 396, 400
- `linear-algebra/src/ch13-psd-and-svd/09-singular-value-decomposition.md`：24 處，行 15, 33, 40, 42, 49, 71, 75, 83, 101, 121, 176, 191, 208, 231, 288, 332, 343, 397, 447, 458, 475, 477, 486, 493
- `linear-algebra/src/ch13-psd-and-svd/10-polar-decomposition.md`：9 處，行 3, 44, 61, 147, 149, 165, 182, 336, 352
- `linear-algebra/src/ch13-psd-and-svd/11-low-rank-approximation.md`：5 處，行 68, 188, 225, 359, 367
- `linear-algebra/src/ch13-psd-and-svd/12-pseudoinverse.md`：13 處，行 42, 66, 88, 96, 152, 232, 383, 446, 448, 531, 545, 583, 593
- `linear-algebra/src/ch13-psd-and-svd/13-projections-revisited.md`：3 處，行 46, 206, 222
- `linear-algebra/src/ch13-psd-and-svd/index.md`：3 處，行 5, 7, 22
- `linear-algebra/src/ch14-forms/01-bilinear-forms.md`：27 處，行 28, 65, 208, 227, 229, 232, 235, 242, 259, 277, 283, 287, 291, 305, 317, 319, 358, 375, 406, 408, 413, 415, 417, 430, 444, 459, 469
- `linear-algebra/src/ch14-forms/02-congruence.md`：17 處，行 87, 104, 135, 139, 181, 197, 200, 235, 277, 288, 324, 396, 406, 417, 422, 424, 426
- `linear-algebra/src/ch14-forms/03-symmetric-alternating-hermitian.md`：8 處，行 25, 30, 112, 123, 174, 265, 425, 436
- `linear-algebra/src/ch14-forms/04-diagonalizing-symmetric-forms.md`：17 處，行 49, 63, 75, 100, 179, 183, 186, 188, 189, 190, 206, 208, 213, 236, 320, 371, 379
- `linear-algebra/src/ch14-forms/05-sylvesters-law-of-inertia.md`：6 處，行 24, 39, 75, 113, 310, 316
- `linear-algebra/src/ch14-forms/06-definiteness-and-second-derivatives.md`：11 處，行 19, 21, 29, 31, 50, 179, 187, 255, 298, 310, 312
- `linear-algebra/src/ch14-forms/07-isotropic-vectors-and-hyperbolic-planes.md`：59 處，行 3, 20, 26, 30, 32, 38, 51, 56, 59, 76, 83, 89, 101, 105, 120, 122, 125, 127, 131, 135, 141, 164, 171, 175, 179, 198, 202, 212, 220, 224, 228, 232, 244, 251, 266, 271, 298, 313, 314, 329, 337, 340, 356, 358, 366, 370, 372, 384, 390, 392, 422, 433, 445, 463, 469, 479, 496, 503, 505
- `linear-algebra/src/ch14-forms/08-witts-theorems.md`：34 處，行 3, 31, 67, 108, 141, 146, 156, 158, 168, 172, 182, 188, 192, 224, 273, 285, 286, 335, 349, 361, 363, 368, 374, 409, 419, 451, 462, 468, 472, 473, 486, 493, 494, 495
- `linear-algebra/src/ch14-forms/09-symplectic-forms.md`：20 處，行 18, 26, 31, 45, 53, 67, 72, 120, 147, 153, 327, 329, 379, 393, 429, 474, 511, 512, 520, 522
- `linear-algebra/src/ch14-forms/10-the-classical-groups.md`：22 處，行 16, 22, 26, 31, 36, 44, 55, 64, 83, 108, 110, 162, 163, 171, 210, 224, 246, 354, 375, 381, 395, 411
- `linear-algebra/src/ch14-forms/11-minkowski-space.md`：9 處，行 23, 31, 33, 49, 63, 160, 171, 266, 302
- `linear-algebra/src/ch14-forms/12-clifford-algebras.md`：1 處，行 37
- `linear-algebra/src/ch14-forms/index.md`：6 處，行 5, 13, 14, 19, 21, 30
- `linear-algebra/src/ch15-tensors/01-multilinear-maps.md`：5 處，行 83, 352, 371, 407, 421
- `linear-algebra/src/ch15-tensors/02-tensor-product.md`：6 處，行 111, 260, 340, 362, 529, 533
- `linear-algebra/src/ch15-tensors/03-tensor-products-of-maps.md`：4 處，行 11, 62, 225, 591
- `linear-algebra/src/ch15-tensors/04-contraction-and-trace.md`：2 處，行 37, 74
- `linear-algebra/src/ch15-tensors/05-index-notation.md`：4 處，行 309, 357, 367, 380
- `linear-algebra/src/ch15-tensors/06-tensor-algebra.md`：7 處，行 5, 143, 218, 306, 394, 400, 440
- `linear-algebra/src/ch15-tensors/07-symmetric-powers.md`：25 處，行 3, 25, 27, 32, 58, 129, 137, 141, 143, 166, 168, 170, 174, 206, 235, 280, 284, 345, 349, 361, 369, 401, 520, 530, 537
- `linear-algebra/src/ch15-tensors/08-exterior-powers.md`：14 處，行 25, 88, 117, 260, 276, 282, 288, 302, 308, 418, 436, 446, 468, 470
- `linear-algebra/src/ch15-tensors/09-determinant-as-top-exterior-power.md`：12 處，行 5, 59, 137, 149, 172, 199, 201, 204, 244, 279, 287, 294
- `linear-algebra/src/ch15-tensors/10-grassmann-and-clifford.md`：14 處，行 60, 120, 153, 171, 184, 225, 243, 460, 476, 486, 546, 557, 653, 709
- `linear-algebra/src/ch15-tensors/11-tensors-in-quantum-mechanics.md`：18 處，行 65, 83, 124, 136, 140, 142, 196, 204, 207, 212, 241, 295, 370, 386, 409, 422, 428, 446
- `linear-algebra/src/ch15-tensors/index.md`：3 處，行 20, 21, 32
- `linear-algebra/src/ch16-norms/01-vector-norms.md`：6 處，行 28, 31, 50, 184, 188, 381
- `linear-algebra/src/ch16-norms/02-equivalence-of-norms.md`：5 處，行 104, 169, 194, 204, 220
- `linear-algebra/src/ch16-norms/03-matrix-and-operator-norms.md`：13 處，行 57, 121, 149, 158, 181, 287, 297, 301, 393, 494, 499, 506, 508
- `linear-algebra/src/ch16-norms/04-spectral-radius.md`：9 處，行 20, 23, 124, 167, 215, 340, 344, 458, 470
- `linear-algebra/src/ch16-norms/05-neumann-series.md`：2 處，行 43, 238
- `linear-algebra/src/ch16-norms/06-matrix-exponential-and-calculus.md`：4 處，行 11, 16, 119, 195
- `linear-algebra/src/ch16-norms/07-continuity-of-eigenvalues.md`：2 處，行 201, 211
- `linear-algebra/src/ch16-norms/08-condition-numbers.md`：4 處，行 61, 202, 274, 282
- `linear-algebra/src/ch16-norms/index.md`：3 處，行 14, 17, 22
- `linear-algebra/src/ch17-variational/01-the-rayleigh-quotient.md`：12 處，行 3, 42, 57, 118, 173, 306, 325, 344, 350, 364, 419, 488
- `linear-algebra/src/ch17-variational/02-courant-fischer.md`：14 處，行 15, 36, 65, 100, 120, 295, 343, 371, 421, 438, 462, 464, 479, 488
- `linear-algebra/src/ch17-variational/03-weyl-inequalities.md`：6 處，行 112, 242, 353, 357, 359, 363
- `linear-algebra/src/ch17-variational/04-cauchy-interlacing.md`：17 處，行 66, 72, 203, 212, 233, 249, 259, 265, 284, 301, 312, 327, 366, 371, 578, 583, 617
- `linear-algebra/src/ch17-variational/05-rank-one-updates.md`：9 處，行 3, 51, 114, 176, 193, 195, 210, 311, 367
- `linear-algebra/src/ch17-variational/07-wielandt-and-lidskii.md`：14 處，行 104, 114, 119, 121, 148, 171, 175, 179, 205, 229, 431, 471, 484, 529
- `linear-algebra/src/ch17-variational/08-majorization-and-schur.md`：18 處，行 80, 98, 103, 121, 219, 459, 467, 471, 481, 487, 494, 509, 515, 517, 521, 539, 712, 718
- `linear-algebra/src/ch17-variational/09-singular-values-variationally.md`：7 處，行 3, 78, 112, 342, 381, 452, 614
- `linear-algebra/src/ch17-variational/10-inertia-revisited.md`：12 處，行 60, 70, 101, 103, 113, 117, 351, 463, 491, 519, 523, 529
- `linear-algebra/src/ch17-variational/11-monotone-matrix-functions.md`：14 處，行 77, 103, 126, 153, 159, 183, 262, 282, 310, 316, 338, 439, 473, 491
- `linear-algebra/src/ch17-variational/index.md`：3 處，行 5, 24, 49
- `linear-algebra/src/ch18-convexity/01-convex-sets.md`：12 處，行 25, 35, 80, 105, 195, 199, 226, 332, 358, 432, 568, 572
- `linear-algebra/src/ch18-convexity/02-caratheodory.md`：9 處，行 37, 89, 95, 196, 229, 255, 292, 438, 497
- `linear-algebra/src/ch18-convexity/03-separation.md`：24 處，行 19, 64, 139, 148, 164, 186, 210, 268, 276, 280, 288, 298, 310, 335, 349, 364, 400, 428, 479, 480, 489, 549, 569, 587
- `linear-algebra/src/ch18-convexity/04-gauges-support-functions-dual-norms.md`：12 處，行 26, 87, 93, 124, 144, 178, 211, 253, 312, 416, 419, 424
- `linear-algebra/src/ch18-convexity/05-cones-and-farkas.md`：31 處，行 3, 19, 26, 33, 39, 45, 49, 51, 53, 75, 87, 101, 127, 129, 154, 168, 194, 212, 236, 240, 269, 314, 371, 390, 396, 420, 448, 458, 460, 474, 503
- `linear-algebra/src/ch18-convexity/06-linear-programming-duality.md`：9 處，行 3, 48, 88, 105, 144, 281, 289, 323, 420
- `linear-algebra/src/ch18-convexity/07-minimax.md`：5 處，行 50, 66, 70, 154, 201
- `linear-algebra/src/ch18-convexity/08-extreme-points.md`：28 處，行 48, 52, 145, 154, 164, 170, 176, 181, 185, 201, 216, 243, 262, 285, 309, 315, 338, 355, 360, 363, 372, 376, 390, 443, 508, 517, 535, 546
- `linear-algebra/src/ch18-convexity/09-polytopes.md`：16 處，行 38, 60, 79, 91, 141, 207, 250, 296, 317, 381, 441, 453, 461, 475, 481, 494
- `linear-algebra/src/ch18-convexity/10-convex-functions.md`：21 處，行 16, 76, 89, 91, 96, 120, 134, 148, 175, 267, 274, 310, 334, 350, 366, 383, 436, 440, 446, 503, 529
- `linear-algebra/src/ch18-convexity/11-classical-inequalities.md`：4 處，行 28, 213, 311, 322
- `linear-algebra/src/ch18-convexity/index.md`：2 處，行 3, 37
- `linear-algebra/src/ch19-nonnegative/01-positive-matrices.md`：46 處，行 9, 14, 20, 32, 33, 36, 39, 42, 44, 59, 63, 103, 129, 149, 179, 186, 189, 200, 208, 230, 236, 266, 284, 300, 310, 314, 328, 333, 335, 347, 357, 359, 367, 375, 390, 396, 410, 412, 414, 416, 464, 466, 470, 472, 474, 503
- `linear-algebra/src/ch19-nonnegative/02-irreducibility-and-graphs.md`：29 處，行 3, 9, 19, 25, 51, 53, 58, 67, 75, 124, 143, 158, 190, 193, 202, 209, 238, 247, 252, 266, 360, 387, 389, 432, 441, 447, 464, 477, 484
- `linear-algebra/src/ch19-nonnegative/03-perron-frobenius.md`：37 處，行 3, 7, 12, 14, 23, 27, 29, 32, 35, 60, 63, 68, 73, 78, 88, 90, 104, 115, 117, 123, 169, 174, 177, 178, 190, 200, 250, 259, 285, 287, 289, 291, 338, 346, 398, 400, 417
- `linear-algebra/src/ch19-nonnegative/04-collatz-wielandt.md`：17 處，行 3, 5, 37, 52, 80, 86, 118, 134, 137, 147, 168, 171, 176, 199, 392, 414, 438
- `linear-algebra/src/ch19-nonnegative/05-primitive-matrices.md`：14 處，行 3, 7, 9, 34, 65, 69, 169, 208, 210, 262, 297, 416, 436, 458
- `linear-algebra/src/ch19-nonnegative/06-markov-chains.md`：11 處，行 18, 24, 32, 149, 162, 257, 279, 283, 286, 348, 387
- `linear-algebra/src/ch19-nonnegative/07-birkhoff.md`：31 處，行 3, 67, 86, 88, 102, 106, 108, 110, 117, 120, 124, 162, 168, 170, 183, 190, 228, 294, 295, 306, 308, 310, 334, 338, 352, 370, 418, 424, 435, 454, 464
- `linear-algebra/src/ch19-nonnegative/08-pagerank.md`：8 處，行 5, 76, 87, 183, 194, 231, 303, 405
- `linear-algebra/src/ch19-nonnegative/09-m-matrices.md`：75 處，行 3, 20, 31, 33, 42, 54, 76, 77, 79, 81, 84, 88, 92, 95, 104, 109, 123, 128, 133, 141, 145, 149, 151, 153, 159, 165, 178, 183, 186, 190, 194, 204, 208, 216, 220, 232, 239, 255, 268, 316, 318, 367, 369, 370, 372, 374, 383, 393, 394, 395, 397, 403, 407, 411, 419, 421, 433, 459, 466, 512, 513, 520, 524, 526, 537, 538, 539, 545, 547, 549, 551, 555, 561, 568, 570
- `linear-algebra/src/ch19-nonnegative/index.md`：8 處，行 1, 9, 15, 23, 36, 47, 48, 50
- `linear-algebra/src/ch20-perturbation/01-gershgorin.md`：10 處，行 5, 39, 151, 261, 271, 280, 307, 371, 456, 458
- `linear-algebra/src/ch20-perturbation/02-inclusion-regions.md`：11 處，行 42, 103, 108, 127, 130, 204, 214, 240, 264, 269, 476
- `linear-algebra/src/ch20-perturbation/03-continuity-of-roots.md`：5 處，行 125, 139, 246, 280, 364
- `linear-algebra/src/ch20-perturbation/04-bauer-fike.md`：2 處，行 137, 216
- `linear-algebra/src/ch20-perturbation/05-hoffman-wielandt.md`：6 處，行 39, 59, 62, 101, 176, 316
- `linear-algebra/src/ch20-perturbation/06-hermitian-perturbations.md`：3 處，行 80, 168, 178
- `linear-algebra/src/ch20-perturbation/07-sylvester-bounds.md`：6 處，行 39, 75, 162, 172, 174, 208
- `linear-algebra/src/ch20-perturbation/08-principal-angles.md`：9 處，行 89, 100, 127, 205, 282, 285, 401, 426, 469
- `linear-algebra/src/ch20-perturbation/09-davis-kahan.md`：2 處，行 110, 138
- `linear-algebra/src/ch20-perturbation/10-singular-values-and-polar.md`：9 處，行 138, 197, 239, 243, 294, 318, 449, 451, 483
- `linear-algebra/src/ch20-perturbation/11-eigenvalue-condition.md`：16 處，行 9, 23, 33, 46, 88, 101, 115, 133, 141, 186, 200, 229, 241, 393, 465, 475
- `linear-algebra/src/ch20-perturbation/index.md`：1 處，行 47
- `linear-algebra/src/ch21-inequalities/01-hardy-littlewood-polya.md`：11 處，行 5, 64, 185, 224, 305, 355, 371, 446, 454, 471, 484
- `linear-algebra/src/ch21-inequalities/02-convex-functions-and-majorization.md`：15 處，行 3, 29, 201, 227, 232, 239, 243, 249, 260, 421, 448, 475, 509, 556, 590
- `linear-algebra/src/ch21-inequalities/03-symmetric-gauge-functions.md`：26 處，行 9, 11, 57, 74, 80, 83, 90, 169, 189, 194, 246, 261, 267, 270, 329, 331, 355, 359, 383, 403, 411, 423, 437, 451, 466, 474
- `linear-algebra/src/ch21-inequalities/04-unitarily-invariant-norms.md`：9 處，行 65, 67, 78, 111, 193, 315, 341, 406, 454
- `linear-algebra/src/ch21-inequalities/05-von-neumann-trace-inequality.md`：11 處，行 18, 34, 36, 48, 70, 80, 122, 132, 173, 250, 295
- `linear-algebra/src/ch21-inequalities/06-ky-fan-dominance.md`：13 處，行 23, 27, 33, 51, 83, 128, 179, 185, 206, 245, 276, 338, 359
- `linear-algebra/src/ch21-inequalities/07-lidskii-and-its-consequences.md`：3 處，行 40, 139, 148
- `linear-algebra/src/ch21-inequalities/08-operator-convexity.md`：10 處，行 43, 122, 128, 150, 174, 193, 306, 368, 415, 518
- `linear-algebra/src/ch21-inequalities/09-loewner-matrices.md`：8 處，行 36, 45, 78, 378, 408, 435, 548, 608
- `linear-algebra/src/ch21-inequalities/10-loewners-theorem.md`：13 處，行 98, 105, 129, 146, 166, 209, 290, 304, 511, 614, 620, 670, 672
- `linear-algebra/src/ch21-inequalities/11-matrix-means-and-inequalities.md`：6 處，行 61, 77, 164, 176, 342, 345
- `linear-algebra/src/ch21-inequalities/12-golden-thompson.md`：15 處，行 5, 182, 192, 224, 286, 295, 311, 315, 329, 379, 455, 539, 608, 623, 637
- `linear-algebra/src/ch21-inequalities/index.md`：1 處，行 21
- `linear-algebra/src/ch22-geometry/01-affine-spaces.md`：9 處，行 16, 70, 119, 121, 126, 310, 505, 516, 537
- `linear-algebra/src/ch22-geometry/02-affine-subspaces.md`：19 處，行 11, 16, 19, 24, 43, 54, 59, 78, 156, 257, 363, 418, 434, 451, 492, 496, 558, 578, 610
- `linear-algebra/src/ch22-geometry/03-polyhedra-and-linear-programming.md`：38 處，行 40, 55, 56, 63, 71, 73, 97, 100, 108, 113, 177, 195, 199, 243, 245, 248, 255, 265, 269, 271, 274, 337, 355, 359, 386, 392, 404, 406, 414, 450, 458, 466, 488, 507, 523, 554, 563, 565
- `linear-algebra/src/ch22-geometry/04-euclidean-motions.md`：6 處，行 32, 385, 429, 463, 647, 664
- `linear-algebra/src/ch22-geometry/05-quadrics.md`：20 處，行 32, 39, 55, 58, 105, 122, 167, 187, 283, 304, 316, 331, 336, 367, 438, 447, 529, 542, 560, 567
- `linear-algebra/src/ch22-geometry/06-projective-space.md`：21 處，行 61, 76, 81, 84, 113, 125, 167, 178, 182, 321, 339, 343, 367, 374, 383, 442, 510, 532, 538, 549, 556
- `linear-algebra/src/ch22-geometry/07-projective-transformations.md`：18 處，行 3, 23, 41, 80, 131, 133, 148, 156, 162, 219, 225, 246, 264, 513, 519, 575, 612, 656
- `linear-algebra/src/ch22-geometry/08-projective-duality.md`：13 處，行 33, 44, 49, 62, 68, 70, 86, 94, 397, 414, 424, 434, 438
- `linear-algebra/src/ch22-geometry/09-desargues-and-pappus.md`：14 處，行 14, 80, 87, 91, 97, 136, 223, 310, 327, 337, 352, 483, 505, 562
- `linear-algebra/src/ch22-geometry/10-conics-and-plucker.md`：27 處，行 16, 20, 23, 29, 40, 53, 55, 67, 85, 135, 147, 155, 165, 169, 171, 175, 225, 229, 249, 302, 341, 348, 382, 527, 531, 557, 672
- `linear-algebra/src/ch22-geometry/index.md`：8 處，行 30, 51, 55, 61, 62, 70, 71, 74
- `linear-algebra/src/ch23-algebras/01-associative-algebras.md`：12 處，行 13, 15, 69, 111, 158, 226, 340, 387, 406, 509, 547, 552
- `linear-algebra/src/ch23-algebras/02-ideals-and-quotients.md`：14 處，行 3, 56, 106, 110, 119, 123, 170, 197, 298, 318, 367, 425, 427, 429
- `linear-algebra/src/ch23-algebras/03-simple-and-semisimple.md`：25 處，行 23, 27, 42, 77, 96, 99, 107, 112, 175, 181, 233, 235, 268, 282, 361, 367, 373, 377, 384, 402, 431, 499, 508, 515, 517
- `linear-algebra/src/ch23-algebras/04-schurs-lemma.md`：22 處，行 7, 35, 53, 61, 66, 85, 112, 171, 197, 199, 204, 226, 251, 259, 261, 263, 275, 304, 306, 320, 330, 358
- `linear-algebra/src/ch23-algebras/05-double-commutant.md`：13 處，行 47, 52, 59, 65, 73, 221, 260, 305, 323, 343, 373, 381, 422
- `linear-algebra/src/ch23-algebras/06-wedderburn.md`：12 處，行 49, 76, 95, 120, 123, 167, 237, 282, 344, 384, 386, 388
- `linear-algebra/src/ch23-algebras/07-group-representations.md`：12 處，行 38, 41, 84, 89, 137, 210, 222, 240, 289, 416, 424, 453
- `linear-algebra/src/ch23-algebras/08-characters.md`：10 處，行 82, 155, 300, 304, 306, 556, 626, 628, 634, 701
- `linear-algebra/src/ch23-algebras/09-the-abelian-case.md`：1 處，行 55
- `linear-algebra/src/ch23-algebras/10-summary-and-transfer.md`：6 處，行 19, 56, 65, 98, 148, 157
- `linear-algebra/src/ch23-algebras/index.md`：13 處，行 15, 20, 30, 32, 50, 61, 78, 83, 84, 86, 88, 89, 98
- `linear-algebra/src/ch24-applied/01-floating-point-and-backward-error.md`：1 處，行 71
- `linear-algebra/src/ch24-applied/02-elimination-pivoting-and-cost.md`：12 處，行 14, 51, 106, 107, 114, 122, 208, 224, 251, 309, 604, 704
- `linear-algebra/src/ch24-applied/03-numerical-least-squares.md`：6 處，行 7, 256, 281, 372, 434, 575
- `linear-algebra/src/ch24-applied/04-power-method-and-inverse-iteration.md`：11 處，行 44, 74, 87, 154, 167, 197, 225, 247, 358, 474, 580
- `linear-algebra/src/ch24-applied/05-the-qr-algorithm.md`：11 處，行 123, 246, 259, 267, 296, 304, 306, 310, 448, 512, 516
- `linear-algebra/src/ch24-applied/06-krylov-subspaces.md`：17 處，行 33, 98, 135, 148, 184, 332, 352, 357, 454, 502, 512, 514, 529, 536, 546, 580, 590
- `linear-algebra/src/ch24-applied/07-conjugate-gradient.md`：8 處，行 140, 181, 258, 270, 273, 303, 351, 353
- `linear-algebra/src/ch24-applied/08-lax-pairs-and-the-toda-flow.md`：6 處，行 35, 59, 169, 197, 373, 417
- `linear-algebra/src/ch24-applied/09-vibrations.md`：12 處，行 48, 82, 195, 279, 305, 316, 367, 373, 446, 535, 542, 557
- `linear-algebra/src/ch24-applied/10-principal-components.md`：1 處，行 137
- `linear-algebra/src/ch24-applied/11-graph-laplacians.md`：8 處，行 118, 176, 279, 283, 287, 293, 357, 375
- `linear-algebra/src/ch24-applied/12-the-fast-fourier-transform.md`：1 處，行 293
- `linear-algebra/src/ch24-applied/13-fast-matrix-multiplication.md`：3 處，行 49, 58, 283
- `linear-algebra/src/ch24a-notation/index.md`：14 處，行 98, 108, 149, 176, 242, 247, 251, 265, 270, 271, 288, 294, 355, 388

## 連寫的複合詞（`closed-compounds`，confirmed，機械替換）

| 寫法 | 線代書 | analysis-book | 合計 | |
|---|---:|---:|---:|---|
| codomain* | 45 | 42 | 87 | **use** |
| preimage* | 30 | 101 | 131 | **use** |
| counterexample* | 39 | 28 | 67 | **use** |
| co-domain* | 0 | 0 | 0 | avoid |
| pre-image* | 0 | 0 | 0 | avoid |
| counter-example* | 0 | 0 | 0 | avoid |

連寫 87／131／67 次，加連字號 0 次。

書稿裡沒有 avoid 寫法。

## finite-dimensional（`dimensional`，confirmed，機械替換）

| 寫法 | 線代書 | analysis-book | 合計 | |
|---|---:|---:|---:|---|
| finite-dimensional | 659 | 0 | 659 | **use** |
| infinite-dimensional | 64 | 0 | 64 | **use** |
| finite dimensional | 0 | 0 | 0 | avoid |
| infinite dimensional | 0 | 0 | 0 | avoid |

加連字號 723 次，分寫 0 次；不論修飾名詞或當述語都加連字號。

書稿裡沒有 avoid 寫法。

## 正定與半正定（`definite`，confirmed，機械替換）

| 寫法 | 線代書 | analysis-book | 合計 | |
|---|---:|---:|---:|---|
| positive definite | 278 | 0 | 278 | **use** |
| positive semidefinite | 283 | 0 | 283 | **use** |
| negative definite | 18 | 0 | 18 | **use** |
| negative semidefinite | 10 | 0 | 10 | **use** |
| positive-definite | 0 | 0 | 0 | avoid |
| positive semi-definite | 0 | 0 | 0 | avoid |
| positive-semidefinite | 0 | 0 | 0 | avoid |
| negative-definite | 0 | 0 | 0 | avoid |
| negative semi-definite | 0 | 0 | 0 | avoid |

分寫 561 次，其他寫法 0 次。

書稿裡沒有 avoid 寫法。

## 自伴（`self-adjoint`，confirmed，機械替換）

| 寫法 | 線代書 | analysis-book | 合計 | |
|---|---:|---:|---:|---|
| self-adjoint | 237 | 0 | 237 | **use** |
| selfadjoint | 0 | 0 | 0 | avoid |
| self adjoint | 0 | 0 | 0 | avoid |

self-adjoint 237 次，其他寫法 0 次。

書稿裡沒有 avoid 寫法。

## well-defined（`well-defined`，confirmed，機械替換）

| 寫法 | 線代書 | analysis-book | 合計 | |
|---|---:|---:|---:|---|
| well-defined | 38 | 1 | 39 | **use** |
| well defined | 111 | 14 | 125 | **use** |
| is well-defined | 0 | 0 | 0 | avoid |
| are well-defined | 0 | 0 | 0 | avoid |
| be well-defined | 0 | 0 | 0 | avoid |
| been well-defined | 0 | 0 | 0 | avoid |
| a well defined | 0 | 0 | 0 | avoid |
| an well defined | 0 | 0 | 0 | avoid |
| the well defined | 0 | 0 | 0 | avoid |

Chicago 規則：放在名詞前加連字號（a well-defined map，36 次），當述語分寫（is well defined，81 次）。兩本書已經完全照這條規則，反例 0 次。

書稿裡沒有 avoid 寫法。

## if and only if（`iff`，confirmed，逐處判斷）

| 寫法 | 線代書 | analysis-book | 合計 | |
|---|---:|---:|---:|---|
| if and only if | 778 | 83 | 861 | **use** |
| iff | 40 | 40 | 80 | avoid |

if and only if 861 次，iff 80 次。iff 多半出現在 F1 談連接詞本身的地方（an "iff"、iff-introduction），那是在講符號，不是縮寫；其餘當縮寫用的改成 if and only if。lint 會把 F1 的用法也列出來，由作者逐處判斷。

avoid 寫法出現處（16 個檔案）：

- `analysis-book/src/ch01-connectives-and-derivations/01-statements-and-connectives.md`：1 處，行 88
- `analysis-book/src/ch01-connectives-and-derivations/index.md`：1 處，行 5
- `analysis-book/src/ch02-negation-and-classical-logic/04-biconditional-and-definitions.md`：18 處，行 1, 3, 55, 60, 69, 113, 119, 171, 177, 276, 346, 359, 382, 387, 400, 461, 496, 502
- `analysis-book/src/ch02-negation-and-classical-logic/06-finding-derivations.md`：4 處，行 673, 674, 675, 685
- `analysis-book/src/ch02-negation-and-classical-logic/index.md`：2 處，行 16, 26
- `analysis-book/src/ch04-predicate-logic/11-models.md`：4 處，行 174, 178, 184, 225
- `analysis-book/src/ch04-predicate-logic/12-first-order-soundness.md`：3 處，行 73, 77, 79
- `analysis-book/src/ch06-sets-and-functions/06-images-and-preimages.md`：1 處，行 479
- `analysis-book/src/ch06-sets-and-functions/index.md`：1 處，行 7
- `linear-algebra/src/ch00-foundations/01-logic.md`：2 處，行 144, 153
- `linear-algebra/src/ch00-foundations/02-proofs.md`：2 處，行 145, 382
- `linear-algebra/src/ch00-foundations/04-functions.md`：1 處，行 457
- `linear-algebra/src/ch04-matrices-of-maps/01-matrix-of-a-map.md`：3 處，行 347, 477, 507
- `linear-algebra/src/ch05-duality/03-double-dual.md`：3 處，行 355, 357, 393
- `linear-algebra/src/ch05-duality/04-dual-map.md`：9 處，行 215, 250, 308, 310, 412, 424, 460, 469, 471
- `linear-algebra/src/ch10-canonical-forms/10-convergent-matrices.md`：1 處，行 342

## 複數形（`plurals`，confirmed，機械替換）

| 寫法 | 線代書 | analysis-book | 合計 | |
|---|---:|---:|---:|---|
| zeros | 187 | 1 | 188 | **use** |
| formulas | 57 | 281 | 338 | **use** |
| lemmas | 6 | 4 | 10 | **use** |
| indices | 167 | 4 | 171 | **use** |
| zeroes | 1 | 0 | 1 | avoid |
| formulae | 0 | 0 | 0 | avoid |
| lemmata | 0 | 0 | 0 | avoid |

zeros 188 比 zeroes 1；formulas 338 比 formulae 0；lemmas 10 比 lemmata 0；indices 171 比 indexes 2（indexes 也可能是動詞，不列入 avoid）。

avoid 寫法出現處（1 個檔案）：

- `linear-algebra/src/ch11-inner-products/08-qr-and-householder.md`：1 處，行 366

## 美式拼寫（`us-spelling`，confirmed，機械替換）

| 寫法 | 線代書 | analysis-book | 合計 | |
|---|---:|---:|---:|---|
| neighborhood* | 4 | 0 | 4 | **use** |
| behavior* | 24 | 0 | 24 | **use** |
| center* | 329 | 20 | 349 | **use** |
| fiber* | 4 | 0 | 4 | **use** |
| color* | 4 | 8 | 12 | **use** |
| favor* | 4 | 0 | 4 | **use** |
| analyze* | 7 | 0 | 7 | **use** |
| labeled | 9 | 9 | 18 | **use** |
| labeling | 9 | 2 | 11 | **use** |
| modeling | 6 | 0 | 6 | **use** |
| modeled | 3 | 1 | 4 | **use** |
| canceled | 6 | 1 | 7 | **use** |
| canceling | 38 | 2 | 40 | **use** |
| neighbourhood* | 0 | 0 | 0 | avoid |
| behaviour* | 0 | 0 | 0 | avoid |
| centre* | 0 | 0 | 0 | avoid |
| fibre* | 0 | 0 | 0 | avoid |
| colour* | 0 | 0 | 0 | avoid |
| favour* | 0 | 0 | 0 | avoid |
| analyse* | 2 | 0 | 2 | avoid |
| labelled | 0 | 1 | 1 | avoid |
| labelling | 0 | 0 | 0 | avoid |
| modelling | 0 | 0 | 0 | avoid |
| modelled | 0 | 0 | 0 | avoid |
| cancelled | 0 | 0 | 0 | avoid |
| cancelling | 0 | 0 | 0 | avoid |

兩本書都是美式拼寫：-ize 2,287 次，詞幹相同的 -ise 0 次。例外只有 analyse 2 次（線代書）與 labelled 1 次（analysis-book）。

avoid 寫法出現處（3 個檔案）：

- `analysis-book/src/ch06-sets-and-functions/06-images-and-preimages.md`：1 處，行 200
- `linear-algebra/src/ch24-applied/03-numerical-least-squares.md`：1 處，行 331
- `linear-algebra/src/ch24-applied/13-fast-matrix-multiplication.md`：1 處，行 427

