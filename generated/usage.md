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
| map | 1310 | 21 | 1331 | **use** |
| maps | 542 | 5 | 547 | **use** |
| linear map* | 512 | 0 | 512 | **use** |
| function | 921 | 288 | 1209 | **use** |
| functions | 403 | 101 | 504 | **use** |
| a mapping | 0 | 0 | 0 | avoid |
| the mapping | 0 | 0 | 0 | avoid |
| mappings | 0 | 0 | 0 | avoid |
| linear mapping* | 0 | 0 | 0 | avoid |
| linear transformation* | 0 | 0 | 0 | avoid |

定義裡介紹同義詞的「a linear map (or linear transformation)」保留（keep），理由同 one-to-one。map 用於保持結構的映射（linear map 511 次），function 用於集合論與分析的一般函數（1,705 次）；operator 指 V → V 的線性映射。名詞 mapping 不用（現況 0 次）；linear transformation 1 次改成 linear map。動名詞 mapping（mapping X onto Y）照常使用，固定名稱列在 keep，不受 avoid 影響：spectral mapping theorem、open mapping theorem、Riemann mapping theorem、contraction mapping。（2026-10-10 修正：原提案把 mapping 整個列為 avoid，但書稿裡的 21 次全是定理名或動名詞。）

書稿裡沒有 avoid 寫法。

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
| `(?<![\w-])[Nn]on-[a-z][\w-]*`（正規表示式） | 3388 | 243 | 3631 | avoid |

連寫（2026-10-10 定案）。兩本書已是美式拼寫，美式數學出版（AMS、Chicago）的慣例是 non- 直接連寫；原本「美式拼寫＋連字號」是混搭。例外照 Chicago：後面接專有名詞或大寫字時保留連字號（non-Euclidean、non-Archimedean、non-Hausdorff），avoid 的規則只抓 non- 後接小寫字母的寫法。書稿現況是 100% 加連字號，遷移是純機械替換（spec/06），陳述雜湊先正規化 avoid 寫法再計算，所以不觸發重審（spec/04 圖 3）。

avoid 寫法出現處（290 個檔案）：

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
- `linear-algebra/src/index.md`：3 處，行 17, 39, 67

## 連寫的複合詞（`closed-compounds`，confirmed，機械替換）

| 寫法 | 線代書 | analysis-book | 合計 | |
|---|---:|---:|---:|---|
| codomain* | 45 | 42 | 87 | **use** |
| preimage* | 30 | 101 | 131 | **use** |
| counterexample* | 40 | 28 | 68 | **use** |
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
| well defined | 112 | 14 | 126 | **use** |
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
| formulae | 0 | 0 | 0 | avoid |
| lemmata | 0 | 0 | 0 | avoid |

zeros 188 比 zeroes 1，但那一處是動詞（a reflection zeroes a column），所以 zeroes 不列入 avoid；formulas 338 比 formulae 0；lemmas 10 比 lemmata 0；indices 171 比 indexes 2（indexes 也可能是動詞，不列入 avoid）。

書稿裡沒有 avoid 寫法。

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
| analyse | 0 | 0 | 0 | avoid |
| analysed | 0 | 0 | 0 | avoid |
| analysing | 0 | 0 | 0 | avoid |
| labelled | 0 | 1 | 1 | avoid |
| labelling | 0 | 0 | 0 | avoid |
| modelling | 0 | 0 | 0 | avoid |
| modelled | 0 | 0 | 0 | avoid |
| cancelled | 0 | 0 | 0 | avoid |
| cancelling | 0 | 0 | 0 | avoid |

兩本書都是美式拼寫：-ize 2,287 次，詞幹相同的 -ise 0 次。例外只有 labelled 1 次（analysis-book）。（2026-10-10 修正：原先以 analyse* 比對，把名詞複數 analyses 也算成英式拼寫；只禁動詞形 analyse、analysed、analysing。）

avoid 寫法出現處（1 個檔案）：

- `analysis-book/src/ch06-sets-and-functions/06-images-and-preimages.md`：1 處，行 200

## 序列逗號（Oxford comma）（`serial-comma`，confirmed，逐處判斷）

| 寫法 | 線代書 | analysis-book | 合計 | |
|---|---:|---:|---:|---|
| `,\s+(?:and|or)\s`（正規表示式） | 18865 | 3914 | 22779 | **use** |
| `,\s+(?:[A-Za-z][\w'’-]*\s+){1,4}(?:and|or)\s`（正規表示式） | 5427 | 894 | 6321 | avoid |

列舉三項以上時，最後的 and／or 前加逗號（A, B, and C）。2026-10-10 定案：和美式拼寫、non- 連寫一致，是美式數學出版（Chicago、AMS）的慣例；數學標題的項目本身常含 and，少了逗號就讀不出邊界（Direct and Semidirect Products, and Finite Abelian Groups）。章名由 atlas.py check 機械檢查；散文用 regex 分辨不出「A, B and C」是不是列舉（例如 if x, then y and z），所以報告列出候選處，逐處判斷。

avoid 寫法出現處（310 個檔案）：

- `analysis-book/src/ch01-connectives-and-derivations/01-statements-and-connectives.md`：15 處，行 1, 66, 69, 74, 76, 86, 124, 162, 186, 237, 240, 271, 379, 400, 409
- `analysis-book/src/ch01-connectives-and-derivations/02-derivations.md`：16 處，行 1, 3, 62, 82, 85, 95, 98, 99, 252, 297, 321, 337, 344, 360, 404, 418
- `analysis-book/src/ch01-connectives-and-derivations/03-conjunction.md`：25 處，行 54, 75, 133, 157, 160, 171, 223, 225, 245, 259, 283, 303, 316, 320, 343, 409, 427, 443, 453, 527, 572, 602, 606, 608, 609
- `analysis-book/src/ch01-connectives-and-derivations/04-using-an-implication.md`：17 處，行 30, 60, 62, 93, 97, 102, 115, 147, 187, 220, 269, 291, 333, 354, 442, 533, 535
- `analysis-book/src/ch01-connectives-and-derivations/05-proving-an-implication.md`：14 處，行 17, 57, 103, 160, 170, 235, 286, 573, 666, 671, 676, 730, 737, 893
- `analysis-book/src/ch01-connectives-and-derivations/06-disjunction-introduction.md`：11 處，行 48, 51, 57, 64, 162, 204, 207, 263, 287, 370, 467
- `analysis-book/src/ch01-connectives-and-derivations/07-disjunction-and-cases.md`：29 處，行 159, 216, 317, 322, 366, 389, 427, 431, 433, 438, 444, 468, 478, 571, 583, 595, 619, 671, 683, 697, 752, 772, 792, 800, 819, 825, 856, 968, 996
- `analysis-book/src/ch01-connectives-and-derivations/index.md`：3 處，行 7, 9, 13
- `analysis-book/src/ch02-negation-and-classical-logic/01-contradiction-and-vacuous-truth.md`：11 處，行 46, 58, 60, 70, 161, 294, 409, 443, 501, 547, 632
- `analysis-book/src/ch02-negation-and-classical-logic/02-negation-and-contradiction.md`：12 處，行 13, 64, 89, 140, 144, 223, 238, 283, 310, 316, 328, 456
- `analysis-book/src/ch02-negation-and-classical-logic/03-derived-rules.md`：22 處，行 52, 92, 120, 144, 279, 282, 293, 299, 341, 345, 350, 384, 404, 439, 445, 449, 453, 456, 473, 613, 620, 657
- `analysis-book/src/ch02-negation-and-classical-logic/04-biconditional-and-definitions.md`：18 處，行 7, 50, 177, 243, 247, 249, 295, 314, 329, 332, 342, 353, 486, 544, 548, 591, 603, 612
- `analysis-book/src/ch02-negation-and-classical-logic/05-reductio-and-classical-rules.md`：18 處，行 32, 60, 63, 313, 333, 385, 535, 550, 552, 571, 609, 671, 749, 817, 824, 830, 984, 996
- `analysis-book/src/ch02-negation-and-classical-logic/06-finding-derivations.md`：28 處，行 3, 35, 46, 58, 61, 66, 69, 92, 108, 186, 246, 286, 313, 466, 475, 479, 487, 496, 705, 706, 719, 759, 788, 867, 892, 1030, 1148, 1234
- `analysis-book/src/ch02-negation-and-classical-logic/index.md`：6 處，行 1, 5, 7, 9, 14, 15
- `analysis-book/src/ch03-semantics-soundness-completeness/01-formulas-and-parse-trees.md`：18 處，行 3, 21, 26, 69, 71, 94, 118, 141, 167, 175, 177, 184, 242, 264, 273, 338, 340, 369
- `analysis-book/src/ch03-semantics-soundness-completeness/02-induction.md`：19 處，行 13, 17, 42, 46, 180, 191, 203, 234, 238, 322, 335, 359, 453, 517, 522, 559, 564, 567, 645
- `analysis-book/src/ch03-semantics-soundness-completeness/03-valuations-and-truth-tables.md`：18 處，行 11, 49, 115, 119, 144, 167, 181, 183, 187, 203, 220, 266, 311, 314, 444, 496, 508, 533
- `analysis-book/src/ch03-semantics-soundness-completeness/04-entailment-and-equivalence.md`：25 處，行 1, 3, 21, 23, 80, 95, 107, 121, 129, 142, 152, 156, 208, 244, 251, 262, 278, 284, 290, 306, 320, 349, 399, 409, 568
- `analysis-book/src/ch03-semantics-soundness-completeness/05-soundness.md`：27 處，行 29, 35, 47, 90, 177, 181, 185, 189, 204, 206, 208, 210, 212, 259, 282, 284, 290, 321, 334, 340, 344, 346, 394, 408, 453, 513, 540
- `analysis-book/src/ch03-semantics-soundness-completeness/06-completeness.md`：24 處，行 13, 19, 75, 96, 232, 249, 284, 290, 296, 312, 314, 336, 346, 358, 436, 450, 469, 578, 596, 672, 747, 839, 843, 845
- `analysis-book/src/ch03-semantics-soundness-completeness/07-normal-forms.md`：23 處，行 3, 18, 28, 71, 93, 113, 238, 318, 321, 322, 324, 327, 329, 393, 403, 409, 430, 453, 495, 499, 510, 618, 624
- `analysis-book/src/ch03-semantics-soundness-completeness/index.md`：7 處，行 1, 3, 5, 9, 13, 14, 16
- `analysis-book/src/ch04-predicate-logic/01-predicates-and-quantifiers.md`：12 處，行 3, 21, 80, 106, 153, 160, 169, 178, 216, 223, 224, 350
- `analysis-book/src/ch04-predicate-logic/02-terms-formulas-substitution.md`：23 處，行 1, 3, 35, 41, 45, 61, 70, 77, 81, 83, 94, 106, 116, 165, 183, 346, 386, 443, 454, 534, 559, 585, 588
- `analysis-book/src/ch04-predicate-logic/07-equality-and-uniqueness.md`：21 處，行 3, 45, 64, 74, 92, 95, 117, 129, 146, 160, 166, 192, 280, 330, 417, 419, 484, 547, 549, 556, 572
- `analysis-book/src/ch04-predicate-logic/08-translation.md`：17 處，行 3, 17, 46, 89, 96, 145, 149, 230, 258, 327, 330, 366, 398, 442, 465, 486, 491
- `analysis-book/src/ch04-predicate-logic/11-models.md`：25 處，行 23, 30, 42, 44, 51, 72, 98, 124, 142, 149, 156, 161, 176, 217, 235, 260, 269, 309, 311, 324, 341, 362, 392, 451, 539
- `analysis-book/src/ch04-predicate-logic/12-first-order-soundness.md`：14 處，行 3, 11, 58, 71, 81, 125, 133, 165, 187, 195, 202, 226, 307, 360
- `analysis-book/src/ch04-predicate-logic/index.md`：8 處，行 7, 9, 13, 14, 18, 19, 32, 33
- `analysis-book/src/ch06-sets-and-functions/01-sets-and-subsets.md`：17 處，行 1, 31, 33, 55, 62, 140, 144, 155, 157, 166, 174, 274, 283, 417, 419, 452, 509
- `analysis-book/src/ch06-sets-and-functions/02-set-operations.md`：24 處，行 1, 3, 5, 34, 97, 121, 134, 136, 170, 172, 218, 265, 312, 347, 349, 363, 375, 389, 397, 406, 433, 445, 447, 456
- `analysis-book/src/ch06-sets-and-functions/03-products-and-relations.md`：19 處，行 1, 24, 35, 78, 84, 89, 105, 160, 162, 184, 186, 203, 227, 268, 307, 350, 370, 427, 439
- `analysis-book/src/ch06-sets-and-functions/04-functions.md`：22 處，行 1, 7, 31, 33, 73, 92, 100, 130, 171, 180, 192, 240, 265, 334, 379, 427, 439, 474, 476, 511, 585, 636
- `analysis-book/src/ch06-sets-and-functions/05-inverses.md`：17 處，行 1, 44, 48, 67, 81, 86, 127, 138, 167, 267, 336, 370, 376, 391, 405, 435, 504
- `analysis-book/src/ch06-sets-and-functions/06-images-and-preimages.md`：17 處，行 5, 13, 43, 50, 129, 148, 166, 170, 177, 200, 368, 400, 426, 458, 460, 561, 638
- `analysis-book/src/ch06-sets-and-functions/index.md`：11 處，行 1, 3, 7, 9, 13, 14, 15, 16, 17, 18, 25
- `analysis-book/src/ch11-least-upper-bound/01-ordered-fields.md`：22 處，行 13, 20, 68, 69, 78, 96, 102, 131, 151, 153, 164, 168, 204, 218, 242, 261, 274, 306, 368, 380, 392, 410
- `analysis-book/src/ch11-least-upper-bound/02-suprema.md`：12 處，行 1, 7, 25, 59, 176, 207, 219, 225, 261, 276, 278, 350
- `analysis-book/src/ch11-least-upper-bound/03-the-axiom.md`：11 處，行 26, 48, 50, 99, 127, 134, 139, 163, 177, 183, 187
- `analysis-book/src/ch11-least-upper-bound/04-epsilon-characterization.md`：18 處，行 132, 139, 153, 154, 159, 211, 254, 292, 298, 310, 330, 344, 346, 348, 364, 366, 378, 380
- `analysis-book/src/ch11-least-upper-bound/05-archimedean-property.md`：16 處，行 3, 28, 52, 58, 103, 213, 306, 326, 327, 328, 343, 349, 351, 359, 361, 365
- `analysis-book/src/ch11-least-upper-bound/06-density-and-roots.md`：12 處，行 28, 34, 64, 79, 155, 167, 252, 315, 353, 387, 402, 449
- `analysis-book/src/ch11-least-upper-bound/07-nested-intervals.md`：22 處，行 21, 47, 72, 101, 124, 128, 138, 156, 192, 202, 215, 229, 260, 272, 283, 289, 313, 323, 333, 343, 377, 387
- `analysis-book/src/ch11-least-upper-bound/index.md`：4 處，行 3, 7, 9, 14
- `analysis-book/src/index.md`：4 處，行 3, 9, 20, 21
- `linear-algebra/src/ch00-foundations/01-logic.md`：17 處，行 1, 88, 110, 119, 229, 240, 262, 278, 337, 409, 447, 452, 477, 479, 493, 495, 513
- `linear-algebra/src/ch00-foundations/02-proofs.md`：19 處，行 3, 28, 36, 46, 51, 62, 77, 104, 117, 121, 145, 150, 160, 189, 202, 373, 386, 473, 512
- `linear-algebra/src/ch00-foundations/03-sets.md`：27 處，行 3, 5, 7, 18, 37, 120, 124, 163, 169, 181, 183, 188, 190, 232, 245, 257, 271, 288, 298, 302, 334, 341, 484, 486, 526, 539, 551
- `linear-algebra/src/ch00-foundations/04-functions.md`：11 處，行 3, 79, 119, 163, 352, 359, 385, 445, 479, 546, 611
- `linear-algebra/src/ch00-foundations/05-relations.md`：10 處，行 1, 7, 42, 239, 241, 271, 330, 374, 406, 554
- `linear-algebra/src/ch00-foundations/06-complex-numbers.md`：24 處，行 20, 58, 61, 68, 100, 129, 131, 221, 228, 234, 246, 255, 259, 285, 300, 373, 426, 452, 501, 530, 569, 586, 592, 600
- `linear-algebra/src/ch00-foundations/07-fields.md`：18 處，行 16, 51, 55, 68, 106, 115, 121, 131, 181, 231, 235, 249, 264, 283, 294, 303, 385, 410
- `linear-algebra/src/ch00-foundations/08-polynomials.md`：25 處，行 3, 9, 75, 133, 157, 172, 194, 212, 219, 227, 304, 319, 331, 336, 343, 347, 355, 359, 362, 369, 373, 405, 408, 447, 495
- `linear-algebra/src/ch00-foundations/09-matrices.md`：29 處，行 41, 52, 72, 214, 219, 256, 260, 364, 370, 378, 394, 427, 441, 494, 508, 518, 575, 580, 707, 712, 767, 785, 814, 871, 879, 899, 943, 1004, 1005
- `linear-algebra/src/ch00-foundations/10-groups.md`：11 處，行 38, 65, 67, 90, 152, 158, 275, 281, 323, 324, 325
- `linear-algebra/src/ch00-foundations/index.md`：8 處，行 3, 13, 14, 16, 17, 18, 21, 30
- `linear-algebra/src/ch01-vector-spaces/01-vector-spaces.md`：19 處，行 31, 91, 93, 129, 156, 158, 169, 173, 189, 201, 203, 205, 368, 386, 431, 450, 559, 574, 576
- `linear-algebra/src/ch01-vector-spaces/02-subspaces.md`：26 處，行 11, 13, 15, 75, 119, 173, 203, 233, 257, 293, 302, 307, 364, 368, 374, 382, 456, 462, 503, 523, 555, 563, 592, 598, 622, 626
- `linear-algebra/src/ch01-vector-spaces/03-span.md`：9 處，行 7, 153, 201, 204, 260, 346, 357, 378, 416
- `linear-algebra/src/ch01-vector-spaces/04-independence.md`：9 處，行 132, 135, 198, 277, 284, 327, 352, 414, 428
- `linear-algebra/src/ch01-vector-spaces/05-basis.md`：9 處，行 11, 66, 95, 117, 181, 217, 315, 334, 501
- `linear-algebra/src/ch01-vector-spaces/06-dimension.md`：12 處，行 7, 19, 91, 118, 152, 240, 450, 452, 469, 498, 520, 549
- `linear-algebra/src/ch01-vector-spaces/07-sums-and-direct-sums.md`：20 處，行 18, 39, 68, 111, 166, 170, 174, 190, 207, 217, 283, 288, 306, 311, 317, 319, 520, 555, 566, 629
- `linear-algebra/src/ch01-vector-spaces/08-infinite-dimensional.md`：13 處，行 9, 31, 90, 96, 110, 144, 163, 209, 241, 248, 324, 346, 348
- `linear-algebra/src/ch01-vector-spaces/09-changing-the-field.md`：9 處，行 22, 41, 132, 150, 152, 195, 200, 350, 356
- `linear-algebra/src/ch01-vector-spaces/index.md`：2 處，行 7, 11
- `linear-algebra/src/ch02-linear-maps/01-linear-maps.md`：21 處，行 3, 19, 38, 96, 220, 223, 238, 309, 316, 384, 430, 434, 466, 468, 514, 528, 536, 538, 571, 588, 659
- `linear-algebra/src/ch02-linear-maps/02-kernel-image.md`：14 處，行 3, 67, 83, 86, 150, 213, 220, 235, 244, 280, 288, 331, 350, 356
- `linear-algebra/src/ch02-linear-maps/03-rank-nullity.md`：11 處，行 121, 158, 166, 172, 268, 289, 312, 324, 332, 335, 351
- `linear-algebra/src/ch02-linear-maps/04-algebra-of-linear-maps.md`：20 處，行 3, 11, 24, 33, 41, 45, 54, 69, 130, 156, 160, 177, 211, 215, 241, 257, 261, 290, 377, 430
- `linear-algebra/src/ch02-linear-maps/05-isomorphisms.md`：18 處，行 3, 11, 13, 47, 80, 96, 100, 102, 130, 137, 155, 243, 313, 354, 430, 432, 445, 449
- `linear-algebra/src/ch02-linear-maps/index.md`：5 處，行 7, 9, 13, 16, 22
- `linear-algebra/src/ch03-linear-systems/01-linear-systems.md`：11 處，行 85, 87, 103, 104, 146, 180, 184, 190, 206, 265, 430
- `linear-algebra/src/ch03-linear-systems/02-gaussian-elimination.md`：10 處，行 29, 58, 83, 94, 142, 188, 351, 390, 435, 440
- `linear-algebra/src/ch03-linear-systems/03-rref-uniqueness.md`：14 處，行 22, 34, 46, 52, 97, 101, 103, 111, 124, 204, 234, 244, 321, 333
- `linear-algebra/src/ch03-linear-systems/04-elementary-matrices-and-inverses.md`：15 處，行 20, 113, 128, 167, 183, 188, 228, 255, 276, 395, 400, 413, 441, 453, 571
- `linear-algebra/src/ch03-linear-systems/05-rank.md`：21 處，行 1, 5, 46, 121, 125, 195, 205, 256, 285, 337, 355, 367, 383, 396, 413, 440, 490, 567, 656, 706, 730
- `linear-algebra/src/ch03-linear-systems/06-lu-factorization.md`：25 處，行 5, 20, 73, 137, 172, 189, 231, 314, 327, 339, 395, 400, 417, 423, 429, 475, 513, 538, 560, 580, 637, 654, 703, 709, 710
- `linear-algebra/src/ch03-linear-systems/07-applications.md`：17 處，行 42, 62, 76, 78, 152, 240, 256, 288, 313, 317, 350, 400, 404, 468, 476, 535, 599
- `linear-algebra/src/ch03-linear-systems/index.md`：6 處，行 5, 12, 15, 16, 22, 23
- `linear-algebra/src/ch04-matrices-of-maps/01-matrix-of-a-map.md`：20 處，行 17, 45, 94, 121, 190, 205, 216, 241, 258, 275, 287, 320, 345, 349, 351, 362, 377, 389, 495, 547
- `linear-algebra/src/ch04-matrices-of-maps/02-change-of-basis.md`：21 處，行 9, 26, 38, 39, 66, 68, 96, 135, 140, 144, 191, 242, 267, 284, 300, 305, 353, 366, 379, 380, 426
- `linear-algebra/src/ch04-matrices-of-maps/03-rank-factorization.md`：13 處，行 1, 73, 75, 90, 91, 98, 156, 182, 201, 220, 308, 323, 377
- `linear-algebra/src/ch04-matrices-of-maps/04-products-and-quotients.md`：28 處，行 3, 7, 9, 11, 31, 56, 91, 155, 157, 164, 171, 209, 230, 256, 281, 283, 297, 346, 355, 360, 487, 515, 535, 537, 557, 582, 600, 629
- `linear-algebra/src/ch04-matrices-of-maps/05-projections-and-trace.md`：17 處，行 30, 47, 56, 58, 84, 111, 156, 157, 160, 168, 180, 211, 228, 232, 237, 269, 395
- `linear-algebra/src/ch04-matrices-of-maps/index.md`：6 處，行 5, 7, 9, 11, 15, 17
- `linear-algebra/src/ch05-duality/01-linear-functionals.md`：16 處，行 10, 14, 90, 115, 142, 146, 209, 211, 300, 326, 353, 357, 388, 456, 476, 510
- `linear-algebra/src/ch05-duality/02-annihilators.md`：14 處，行 87, 104, 117, 159, 183, 210, 224, 256, 270, 280, 315, 321, 333, 347
- `linear-algebra/src/ch05-duality/03-double-dual.md`：18 處，行 9, 54, 56, 61, 90, 114, 133, 140, 176, 228, 242, 250, 262, 333, 355, 365, 393, 421
- `linear-algebra/src/ch05-duality/04-dual-map.md`：13 處，行 24, 33, 89, 128, 217, 277, 288, 356, 370, 412, 418, 438, 505
- `linear-algebra/src/ch05-duality/05-duality-subspaces-quotients.md`：14 處，行 3, 18, 87, 99, 126, 149, 231, 262, 296, 308, 310, 318, 347, 367
- `linear-algebra/src/ch05-duality/06-hyperplanes-and-systems.md`：7 處，行 73, 111, 213, 218, 334, 402, 404
- `linear-algebra/src/ch05-duality/index.md`：1 處，行 7
- `linear-algebra/src/ch06-polynomials/01-division.md`：24 處，行 3, 43, 49, 51, 61, 85, 97, 144, 162, 171, 173, 178, 198, 230, 242, 265, 275, 293, 303, 349, 365, 370, 392, 446
- `linear-algebra/src/ch06-polynomials/02-ideals-and-gcd.md`：21 處，行 84, 94, 126, 131, 144, 163, 297, 354, 390, 403, 427, 441, 456, 475, 477, 524, 548, 549, 550, 551, 574
- `linear-algebra/src/ch06-polynomials/03-unique-factorization.md`：22 處，行 24, 56, 62, 64, 84, 104, 127, 146, 157, 161, 163, 177, 228, 294, 349, 384, 407, 426, 432, 433, 434, 435
- `linear-algebra/src/ch06-polynomials/04-roots-and-multiplicity.md`：14 處，行 1, 51, 73, 144, 162, 215, 228, 230, 263, 364, 368, 408, 421, 490
- `linear-algebra/src/ch06-polynomials/05-fundamental-theorem-of-algebra.md`：21 處，行 35, 59, 78, 104, 143, 173, 181, 197, 199, 223, 300, 302, 318, 348, 443, 450, 470, 521, 526, 533, 537
- `linear-algebra/src/ch06-polynomials/06-interpolation-and-crt.md`：13 處，行 7, 30, 113, 141, 182, 200, 218, 233, 265, 280, 284, 353, 508
- `linear-algebra/src/ch06-polynomials/07-polynomials-of-operators.md`：17 處，行 3, 27, 43, 50, 69, 177, 220, 242, 284, 338, 349, 440, 447, 451, 457, 491, 503
- `linear-algebra/src/ch06-polynomials/index.md`：6 處，行 3, 7, 11, 12, 14, 24
- `linear-algebra/src/ch07-determinants/01-area-and-volume.md`：8 處，行 112, 118, 125, 205, 206, 323, 325, 342
- `linear-algebra/src/ch07-determinants/02-multilinear-alternating-forms.md`：12 處，行 3, 9, 23, 45, 65, 83, 178, 196, 210, 300, 344, 346
- `linear-algebra/src/ch07-determinants/03-permutations-and-sign.md`：16 處，行 39, 60, 127, 128, 139, 186, 191, 208, 260, 266, 274, 284, 288, 324, 345, 347
- `linear-algebra/src/ch07-determinants/04-existence-and-uniqueness.md`：16 處，行 13, 36, 47, 67, 95, 140, 142, 148, 154, 182, 204, 237, 294, 301, 303, 377
- `linear-algebra/src/ch07-determinants/05-properties.md`：16 處，行 45, 103, 105, 131, 135, 139, 149, 187, 209, 217, 260, 281, 309, 322, 379, 440
- `linear-algebra/src/ch07-determinants/06-cofactor-expansion.md`：13 處，行 1, 42, 86, 88, 144, 181, 314, 317, 458, 461, 468, 471, 472
- `linear-algebra/src/ch07-determinants/07-minors-and-rank.md`：12 處，行 1, 106, 121, 133, 134, 159, 165, 195, 221, 254, 339, 345
- `linear-algebra/src/ch07-determinants/08-special-determinants.md`：17 處，行 40, 44, 81, 122, 132, 136, 140, 146, 177, 254, 304, 346, 355, 377, 386, 388, 394
- `linear-algebra/src/ch07-determinants/09-orientation-and-volume.md`：17 處，行 41, 46, 51, 56, 68, 80, 91, 134, 163, 172, 178, 183, 210, 215, 218, 353, 403
- `linear-algebra/src/ch07-determinants/10-characteristic-polynomial.md`：16 處，行 17, 31, 86, 116, 139, 142, 186, 199, 222, 248, 267, 294, 367, 389, 391, 402
- `linear-algebra/src/ch07-determinants/index.md`：6 處，行 5, 7, 16, 17, 18, 24
- `linear-algebra/src/ch08-block-matrices/01-block-multiplication.md`：21 處，行 64, 72, 78, 98, 115, 119, 122, 157, 164, 214, 219, 238, 250, 254, 266, 369, 451, 474, 486, 488, 513
- `linear-algebra/src/ch08-block-matrices/02-rank-of-block-matrices.md`：13 處，行 32, 46, 88, 117, 127, 143, 149, 173, 263, 300, 302, 369, 391
- `linear-algebra/src/ch08-block-matrices/03-block-determinants-and-schur-complements.md`：16 處，行 3, 65, 85, 110, 128, 148, 179, 253, 282, 290, 389, 400, 423, 447, 472, 479
- `linear-algebra/src/ch08-block-matrices/04-kronecker-product.md`：20 處，行 33, 64, 84, 97, 103, 112, 133, 150, 152, 157, 171, 177, 179, 186, 220, 317, 373, 417, 437, 466
- `linear-algebra/src/ch08-block-matrices/05-commutators-and-shoda.md`：19 處，行 3, 5, 33, 74, 87, 115, 129, 133, 153, 171, 181, 193, 230, 300, 384, 413, 421, 459, 473
- `linear-algebra/src/ch08-block-matrices/index.md`：4 處，行 5, 7, 11, 13
- `linear-algebra/src/ch09-eigenvalues/01-invariant-subspaces.md`：18 處，行 7, 39, 40, 55, 127, 159, 165, 176, 236, 238, 251, 316, 320, 340, 344, 346, 352, 367
- `linear-algebra/src/ch09-eigenvalues/02-eigenvalues-and-eigenvectors.md`：23 處，行 13, 28, 53, 54, 79, 89, 97, 99, 120, 137, 173, 191, 206, 240, 284, 296, 323, 326, 335, 346, 419, 426, 444
- `linear-algebra/src/ch09-eigenvalues/03-multiplicities.md`：25 處，行 18, 39, 45, 46, 54, 57, 65, 120, 123, 129, 146, 155, 157, 159, 174, 187, 218, 224, 226, 240, 268, 275, 277, 298, 300
- `linear-algebra/src/ch09-eigenvalues/04-diagonalization.md`：25 處，行 7, 19, 25, 33, 81, 85, 104, 126, 137, 153, 159, 191, 248, 271, 275, 316, 343, 353, 397, 417, 449, 454, 460, 464, 474
- `linear-algebra/src/ch09-eigenvalues/05-minimal-polynomial.md`：21 處，行 29, 31, 76, 78, 80, 87, 107, 127, 134, 200, 212, 232, 246, 256, 328, 375, 395, 405, 414, 420, 424
- `linear-algebra/src/ch09-eigenvalues/06-cayley-hamilton.md`：10 處，行 84, 117, 137, 234, 238, 261, 297, 339, 380, 382
- `linear-algebra/src/ch09-eigenvalues/07-triangularization.md`：12 處，行 3, 7, 12, 49, 66, 161, 234, 249, 272, 334, 350, 357
- `linear-algebra/src/ch09-eigenvalues/08-primary-decomposition.md`：12 處，行 48, 56, 65, 67, 74, 186, 204, 224, 228, 289, 397, 405
- `linear-algebra/src/ch09-eigenvalues/09-commuting-operators.md`：20 處，行 37, 41, 50, 60, 68, 72, 81, 103, 150, 183, 185, 210, 318, 340, 370, 379, 386, 401, 409, 411
- `linear-algebra/src/ch09-eigenvalues/10-spectral-mapping.md`：27 處，行 7, 42, 46, 50, 72, 86, 122, 130, 134, 140, 144, 146, 157, 183, 207, 233, 256, 274, 287, 330, 360, 388, 422, 434, 464, 475, 495
- `linear-algebra/src/ch09-eigenvalues/11-powers-recurrences-markov.md`：21 處，行 1, 7, 43, 62, 115, 249, 257, 264, 293, 303, 306, 323, 327, 450, 463, 484, 496, 507, 508, 516, 530
- `linear-algebra/src/ch09-eigenvalues/index.md`：4 處，行 7, 19, 20, 21
- `linear-algebra/src/ch10-canonical-forms/01-generalized-eigenspaces.md`：18 處，行 28, 41, 57, 61, 134, 176, 192, 196, 212, 250, 256, 299, 313, 324, 342, 390, 400, 422
- `linear-algebra/src/ch10-canonical-forms/02-nilpotent-operators.md`：21 處，行 25, 34, 50, 62, 64, 66, 84, 107, 109, 121, 171, 212, 271, 277, 281, 289, 389, 453, 548, 606, 608
- `linear-algebra/src/ch10-canonical-forms/03-jordan-canonical-form.md`：22 處，行 21, 32, 83, 125, 162, 201, 221, 227, 229, 243, 274, 294, 410, 420, 426, 432, 457, 470, 479, 483, 517, 527
- `linear-algebra/src/ch10-canonical-forms/04-real-jordan-and-weyr-forms.md`：17 處，行 13, 31, 52, 89, 120, 143, 145, 204, 208, 212, 250, 391, 415, 426, 475, 496, 627
- `linear-algebra/src/ch10-canonical-forms/05-cyclic-subspaces-and-companion-matrices.md`：28 處，行 3, 14, 66, 91, 124, 151, 175, 198, 214, 228, 232, 251, 253, 287, 289, 308, 318, 332, 374, 412, 420, 422, 426, 446, 515, 521, 542, 548
- `linear-algebra/src/ch10-canonical-forms/06-rational-canonical-form.md`：36 處，行 30, 46, 50, 54, 60, 80, 114, 133, 135, 165, 200, 218, 252, 260, 266, 270, 316, 318, 339, 354, 383, 385, 435, 466, 496, 516, 557, 567, 573, 577, 599, 605, 611, 631, 644, 672
- `linear-algebra/src/ch10-canonical-forms/07-smith-normal-form.md`：20 處，行 22, 134, 167, 171, 255, 259, 351, 371, 397, 399, 403, 423, 426, 486, 502, 539, 545, 565, 584, 593
- `linear-algebra/src/ch10-canonical-forms/08-jordan-chevalley.md`：28 處，行 9, 55, 70, 72, 84, 88, 110, 119, 140, 142, 150, 156, 158, 178, 216, 219, 242, 276, 282, 301, 309, 322, 323, 330, 336, 345, 346, 354
- `linear-algebra/src/ch10-canonical-forms/09-functions-of-matrices-and-odes.md`：23 處，行 1, 22, 37, 91, 105, 130, 139, 159, 172, 177, 254, 359, 390, 398, 406, 428, 475, 495, 506, 568, 587, 592, 605
- `linear-algebra/src/ch10-canonical-forms/10-convergent-matrices.md`：25 處，行 29, 94, 100, 119, 121, 152, 201, 207, 238, 241, 265, 297, 299, 317, 346, 373, 380, 390, 423, 433, 434, 440, 446, 470, 472
- `linear-algebra/src/ch10-canonical-forms/index.md`：4 處，行 3, 5, 7, 19
- `linear-algebra/src/ch11-inner-products/01-inner-products.md`：19 處，行 57, 160, 180, 223, 245, 283, 295, 303, 353, 365, 369, 373, 396, 402, 434, 472, 520, 579, 580
- `linear-algebra/src/ch11-inner-products/02-orthonormal-bases.md`：13 處，行 7, 45, 97, 166, 249, 251, 317, 334, 341, 385, 508, 526, 536
- `linear-algebra/src/ch11-inner-products/03-orthogonal-complements-and-projections.md`：19 處，行 23, 32, 51, 75, 89, 93, 133, 138, 159, 166, 221, 244, 297, 301, 330, 354, 372, 382, 459
- `linear-algebra/src/ch11-inner-products/04-least-squares.md`：19 處，行 7, 19, 39, 61, 67, 71, 131, 167, 200, 204, 209, 241, 269, 279, 349, 367, 397, 442, 458
- `linear-algebra/src/ch11-inner-products/05-riesz-and-duality.md`：14 處，行 24, 57, 61, 75, 107, 117, 121, 134, 182, 241, 245, 265, 267, 271
- `linear-algebra/src/ch11-inner-products/06-adjoints.md`：18 處，行 5, 73, 137, 180, 233, 361, 386, 450, 452, 469, 512, 523, 576, 586, 626, 655, 703, 714
- `linear-algebra/src/ch11-inner-products/07-isometries-and-unitary-maps.md`：30 處，行 5, 24, 29, 64, 95, 108, 142, 148, 225, 245, 262, 266, 270, 333, 352, 361, 369, 378, 380, 421, 423, 441, 449, 473, 474, 524, 526, 595, 661, 678
- `linear-algebra/src/ch11-inner-products/08-qr-and-householder.md`：36 處，行 1, 3, 27, 31, 48, 52, 72, 75, 132, 182, 187, 188, 221, 254, 276, 294, 300, 302, 310, 328, 342, 362, 378, 384, 407, 423, 454, 467, 542, 586, 591, 617, 625, 649, 670, 701
- `linear-algebra/src/ch11-inner-products/09-bessel-parseval-fourier.md`：24 處，行 1, 23, 43, 77, 92, 110, 137, 139, 193, 249, 288, 299, 379, 392, 408, 412, 420, 445, 477, 481, 483, 492, 496, 498
- `linear-algebra/src/ch11-inner-products/10-orthogonal-polynomials.md`：24 處，行 15, 28, 79, 135, 145, 151, 179, 210, 212, 218, 228, 235, 274, 286, 316, 327, 338, 340, 344, 381, 389, 472, 474, 491
- `linear-algebra/src/ch11-inner-products/index.md`：5 處，行 5, 7, 17, 18, 19
- `linear-algebra/src/ch12-spectral-theory/01-schur-triangularization.md`：9 處，行 65, 132, 175, 244, 285, 303, 320, 338, 387
- `linear-algebra/src/ch12-spectral-theory/02-self-adjoint-operators.md`：21 處，行 3, 31, 49, 71, 110, 128, 132, 144, 187, 282, 302, 344, 351, 358, 388, 399, 408, 416, 434, 466, 468
- `linear-algebra/src/ch12-spectral-theory/03-normal-operators.md`：19 處，行 5, 19, 39, 63, 97, 143, 155, 167, 187, 193, 216, 220, 238, 346, 372, 388, 404, 426, 453
- `linear-algebra/src/ch12-spectral-theory/04-spectral-theorem-complex.md`：15 處，行 19, 54, 182, 232, 258, 285, 287, 297, 306, 331, 354, 384, 408, 412, 455
- `linear-algebra/src/ch12-spectral-theory/05-spectral-theorem-real.md`：20 處，行 86, 140, 179, 215, 235, 244, 253, 269, 277, 303, 336, 346, 355, 362, 370, 380, 382, 427, 438, 445
- `linear-algebra/src/ch12-spectral-theory/06-orthogonal-matrices-and-rotations.md`：42 處，行 32, 38, 40, 52, 71, 73, 79, 87, 110, 119, 132, 195, 199, 220, 224, 253, 277, 286, 296, 298, 315, 356, 362, 372, 384, 388, 410, 431, 433, 437, 449, 460, 462, 464, 489, 509, 533, 538, 558, 560, 562, 591
- `linear-algebra/src/ch12-spectral-theory/07-commuting-normal-families.md`：14 處，行 28, 66, 68, 88, 92, 114, 118, 175, 179, 287, 293, 295, 369, 379
- `linear-algebra/src/ch12-spectral-theory/08-spectral-resolutions-and-functional-calculus.md`：37 處，行 3, 15, 38, 60, 66, 68, 96, 109, 128, 137, 225, 243, 249, 261, 268, 333, 365, 387, 391, 412, 448, 454, 471, 494, 526, 528, 530, 544, 554, 562, 570, 633, 635, 645, 674, 686, 704
- `linear-algebra/src/ch12-spectral-theory/09-circulants-and-the-dft.md`：17 處，行 7, 86, 98, 101, 118, 129, 261, 352, 383, 432, 459, 485, 499, 583, 590, 604, 627
- `linear-algebra/src/ch12-spectral-theory/10-sylvester-equation.md`：16 處，行 9, 27, 37, 50, 63, 123, 125, 191, 213, 266, 301, 330, 392, 430, 460, 510
- `linear-algebra/src/ch12-spectral-theory/11-defect-from-normality.md`：20 處，行 3, 14, 43, 49, 69, 165, 269, 291, 302, 308, 329, 331, 335, 348, 364, 374, 376, 382, 400, 483
- `linear-algebra/src/ch12-spectral-theory/index.md`：2 處，行 7, 30
- `linear-algebra/src/ch13-psd-and-svd/01-positive-definite-matrices.md`：16 處，行 115, 191, 197, 207, 303, 331, 355, 359, 374, 412, 452, 476, 478, 480, 489, 514
- `linear-algebra/src/ch13-psd-and-svd/02-square-roots-and-cholesky.md`：17 處，行 69, 85, 106, 157, 194, 201, 205, 207, 218, 257, 292, 302, 306, 314, 359, 365, 402
- `linear-algebra/src/ch13-psd-and-svd/03-gram-matrices.md`：10 處，行 5, 40, 52, 76, 192, 218, 259, 314, 372, 388
- `linear-algebra/src/ch13-psd-and-svd/04-simultaneous-diagonalization.md`：16 處，行 11, 13, 22, 44, 88, 119, 128, 147, 174, 186, 272, 276, 288, 332, 341, 376
- `linear-algebra/src/ch13-psd-and-svd/05-the-loewner-order.md`：21 處，行 9, 29, 36, 59, 81, 100, 101, 123, 132, 139, 180, 191, 195, 221, 235, 245, 269, 271, 279, 337, 339
- `linear-algebra/src/ch13-psd-and-svd/06-block-positive-matrices.md`：24 處，行 39, 61, 74, 78, 80, 113, 117, 196, 205, 209, 214, 259, 273, 275, 281, 314, 318, 360, 366, 370, 378, 406, 491, 493
- `linear-algebra/src/ch13-psd-and-svd/07-determinant-inequalities.md`：16 處，行 61, 73, 79, 85, 99, 107, 118, 148, 173, 220, 279, 293, 312, 332, 336, 342
- `linear-algebra/src/ch13-psd-and-svd/08-schur-product-theorem.md`：9 處，行 123, 161, 232, 252, 270, 306, 320, 384, 390
- `linear-algebra/src/ch13-psd-and-svd/09-singular-value-decomposition.md`：25 處，行 3, 5, 33, 38, 39, 40, 57, 67, 85, 105, 109, 196, 200, 231, 236, 282, 330, 341, 365, 429, 469, 477, 493, 495, 514
- `linear-algebra/src/ch13-psd-and-svd/10-polar-decomposition.md`：25 處，行 42, 44, 48, 54, 104, 123, 143, 147, 189, 228, 232, 236, 261, 277, 287, 291, 302, 305, 372, 386, 388, 413, 431, 455, 461
- `linear-algebra/src/ch13-psd-and-svd/11-low-rank-approximation.md`：12 處，行 31, 42, 101, 135, 166, 277, 334, 338, 392, 414, 424, 446
- `linear-algebra/src/ch13-psd-and-svd/12-pseudoinverse.md`：19 處，行 32, 85, 86, 101, 109, 113, 152, 223, 232, 238, 291, 317, 379, 385, 459, 477, 569, 593, 599
- `linear-algebra/src/ch13-psd-and-svd/13-projections-revisited.md`：15 處，行 30, 60, 122, 130, 202, 206, 210, 255, 275, 314, 328, 381, 385, 387, 400
- `linear-algebra/src/ch13-psd-and-svd/index.md`：5 處，行 3, 7, 11, 29, 31
- `linear-algebra/src/ch14-forms/01-bilinear-forms.md`：17 處，行 9, 11, 54, 90, 107, 116, 197, 203, 255, 259, 291, 375, 389, 391, 393, 415, 467
- `linear-algebra/src/ch14-forms/02-congruence.md`：23 處，行 14, 46, 84, 123, 189, 192, 203, 211, 228, 230, 235, 238, 264, 277, 318, 338, 356, 382, 406, 408, 422, 424, 426
- `linear-algebra/src/ch14-forms/03-symmetric-alternating-hermitian.md`：18 處，行 29, 112, 129, 139, 176, 186, 209, 272, 276, 314, 317, 345, 355, 370, 374, 402, 432, 469
- `linear-algebra/src/ch14-forms/04-diagonalizing-symmetric-forms.md`：15 處，行 3, 22, 63, 86, 110, 112, 113, 167, 206, 208, 234, 252, 284, 302, 320
- `linear-algebra/src/ch14-forms/05-sylvesters-law-of-inertia.md`：18 處，行 3, 17, 32, 75, 87, 131, 133, 138, 147, 209, 211, 215, 286, 288, 310, 318, 363, 375
- `linear-algebra/src/ch14-forms/06-definiteness-and-second-derivatives.md`：14 處，行 3, 29, 54, 63, 65, 99, 152, 170, 184, 196, 286, 290, 310, 338
- `linear-algebra/src/ch14-forms/07-isotropic-vectors-and-hyperbolic-planes.md`：19 處，行 57, 58, 122, 164, 187, 202, 212, 220, 224, 226, 260, 266, 285, 295, 337, 413, 437, 485, 503
- `linear-algebra/src/ch14-forms/08-witts-theorems.md`：22 處，行 5, 21, 32, 100, 156, 172, 186, 217, 224, 248, 263, 273, 307, 349, 361, 368, 409, 439, 441, 454, 460, 500
- `linear-algebra/src/ch14-forms/09-symplectic-forms.md`：23 處，行 3, 48, 76, 87, 125, 141, 143, 171, 261, 264, 267, 309, 320, 352, 389, 425, 427, 435, 446, 450, 452, 499, 522
- `linear-algebra/src/ch14-forms/10-the-classical-groups.md`：11 處，行 29, 169, 180, 210, 218, 255, 284, 319, 393, 397, 411
- `linear-algebra/src/ch14-forms/11-minkowski-space.md`：18 處，行 23, 29, 60, 78, 108, 171, 176, 233, 247, 280, 292, 300, 316, 327, 338, 352, 356, 373
- `linear-algebra/src/ch14-forms/12-clifford-algebras.md`：13 處，行 62, 77, 108, 130, 190, 206, 221, 265, 276, 319, 355, 392, 402
- `linear-algebra/src/ch14-forms/index.md`：8 處，行 3, 7, 9, 13, 15, 17, 24, 32
- `linear-algebra/src/ch15-tensors/01-multilinear-maps.md`：19 處，行 11, 15, 35, 70, 72, 85, 89, 109, 137, 175, 201, 245, 309, 313, 315, 351, 390, 395, 439
- `linear-algebra/src/ch15-tensors/02-tensor-product.md`：22 處，行 3, 7, 25, 40, 44, 61, 111, 113, 118, 123, 140, 146, 179, 189, 206, 230, 286, 320, 348, 403, 463, 509
- `linear-algebra/src/ch15-tensors/03-tensor-products-of-maps.md`：18 處，行 20, 28, 73, 132, 218, 228, 288, 294, 309, 321, 327, 331, 351, 374, 414, 519, 539, 543
- `linear-algebra/src/ch15-tensors/04-contraction-and-trace.md`：12 處，行 29, 34, 70, 84, 108, 118, 152, 168, 172, 183, 361, 365
- `linear-algebra/src/ch15-tensors/05-index-notation.md`：8 處，行 5, 82, 130, 143, 187, 220, 296, 347
- `linear-algebra/src/ch15-tensors/06-tensor-algebra.md`：13 處，行 5, 29, 31, 60, 63, 135, 148, 192, 196, 334, 348, 375, 385
- `linear-algebra/src/ch15-tensors/07-symmetric-powers.md`：12 處，行 174, 225, 245, 263, 345, 379, 450, 460, 484, 490, 496, 500
- `linear-algebra/src/ch15-tensors/08-exterior-powers.md`：11 處，行 3, 25, 48, 81, 149, 162, 176, 213, 343, 370, 450
- `linear-algebra/src/ch15-tensors/09-determinant-as-top-exterior-power.md`：13 處，行 50, 179, 206, 244, 261, 265, 330, 338, 359, 361, 381, 405, 437
- `linear-algebra/src/ch15-tensors/10-grassmann-and-clifford.md`：30 處，行 5, 56, 64, 82, 106, 190, 204, 243, 264, 272, 366, 368, 375, 409, 427, 454, 464, 472, 476, 516, 521, 546, 569, 592, 615, 633, 655, 673, 683, 705
- `linear-algebra/src/ch15-tensors/11-tensors-in-quantum-mechanics.md`：18 處，行 3, 7, 15, 31, 43, 176, 228, 241, 258, 295, 322, 328, 338, 401, 424, 434, 444, 446
- `linear-algebra/src/ch15-tensors/index.md`：3 處，行 11, 19, 31
- `linear-algebra/src/ch16-norms/01-vector-norms.md`：19 處，行 9, 131, 160, 203, 247, 257, 262, 283, 335, 340, 354, 379, 442, 446, 461, 463, 483, 495, 506
- `linear-algebra/src/ch16-norms/02-equivalence-of-norms.md`：15 處，行 3, 18, 46, 91, 104, 106, 121, 139, 187, 204, 236, 298, 322, 338, 417
- `linear-algebra/src/ch16-norms/03-matrix-and-operator-norms.md`：16 處，行 5, 57, 88, 112, 121, 185, 238, 240, 267, 279, 333, 363, 387, 404, 414, 506
- `linear-algebra/src/ch16-norms/04-spectral-radius.md`：18 處，行 28, 116, 152, 167, 221, 243, 255, 279, 280, 300, 360, 362, 370, 374, 387, 396, 444, 466
- `linear-algebra/src/ch16-norms/05-neumann-series.md`：6 處，行 5, 45, 111, 213, 362, 397
- `linear-algebra/src/ch16-norms/06-matrix-exponential-and-calculus.md`：18 處，行 7, 16, 84, 127, 153, 165, 185, 193, 195, 200, 222, 341, 420, 447, 453, 455, 527, 554
- `linear-algebra/src/ch16-norms/07-continuity-of-eigenvalues.md`：17 處，行 18, 22, 32, 35, 64, 75, 161, 164, 203, 216, 297, 313, 315, 333, 347, 365, 389
- `linear-algebra/src/ch16-norms/08-condition-numbers.md`：19 處，行 45, 61, 81, 128, 166, 173, 274, 280, 296, 305, 309, 337, 369, 418, 446, 450, 469, 478, 531
- `linear-algebra/src/ch16-norms/index.md`：7 處，行 5, 22, 33, 34, 38, 58, 60
- `linear-algebra/src/ch17-variational/01-the-rayleigh-quotient.md`：24 處，行 5, 9, 65, 69, 75, 110, 155, 173, 214, 250, 257, 264, 276, 316, 370, 384, 388, 409, 413, 416, 418, 448, 484, 506
- `linear-algebra/src/ch17-variational/02-courant-fischer.md`：17 處，行 5, 20, 63, 86, 109, 133, 155, 221, 226, 256, 262, 265, 298, 395, 421, 432, 456
- `linear-algebra/src/ch17-variational/03-weyl-inequalities.md`：25 處，行 7, 37, 54, 63, 107, 112, 150, 182, 226, 238, 244, 268, 303, 363, 411, 413, 415, 427, 458, 467, 477, 510, 516, 523, 539
- `linear-algebra/src/ch17-variational/04-cauchy-interlacing.md`：31 處，行 3, 7, 16, 28, 34, 66, 141, 252, 263, 271, 274, 288, 301, 316, 352, 366, 388, 404, 426, 440, 460, 464, 468, 496, 525, 573, 583, 611, 613, 615, 634
- `linear-algebra/src/ch17-variational/05-rank-one-updates.md`：12 處，行 9, 41, 43, 98, 180, 195, 210, 340, 342, 419, 431, 462
- `linear-algebra/src/ch17-variational/06-poincare-and-ky-fan.md`：12 處，行 53, 82, 119, 252, 281, 382, 399, 421, 468, 470, 477, 495
- `linear-algebra/src/ch17-variational/07-wielandt-and-lidskii.md`：19 處，行 13, 68, 78, 197, 199, 233, 235, 253, 261, 265, 288, 318, 406, 408, 431, 444, 527, 539, 567
- `linear-algebra/src/ch17-variational/08-majorization-and-schur.md`：35 處，行 5, 25, 70, 81, 92, 162, 204, 289, 293, 310, 322, 329, 335, 345, 349, 354, 375, 409, 440, 454, 481, 506, 509, 517, 531, 536, 573, 581, 595, 597, 603, 634, 654, 664, 701
- `linear-algebra/src/ch17-variational/09-singular-values-variationally.md`：22 處，行 3, 7, 72, 78, 150, 162, 256, 302, 304, 324, 342, 389, 446, 458, 468, 470, 502, 580, 614, 630, 634, 642
- `linear-algebra/src/ch17-variational/10-inertia-revisited.md`：34 處，行 1, 14, 23, 29, 77, 79, 103, 109, 149, 183, 185, 186, 187, 189, 214, 241, 246, 259, 286, 330, 349, 357, 404, 420, 435, 437, 457, 459, 469, 475, 499, 517, 519, 529
- `linear-algebra/src/ch17-variational/11-monotone-matrix-functions.md`：23 處，行 3, 5, 71, 95, 111, 114, 147, 185, 220, 228, 236, 341, 344, 350, 352, 359, 419, 439, 454, 493, 521, 539, 556
- `linear-algebra/src/ch17-variational/index.md`：15 處，行 3, 5, 7, 15, 27, 28, 29, 30, 43, 44, 49, 51, 52, 54, 55
- `linear-algebra/src/ch18-convexity/01-convex-sets.md`：22 處，行 5, 36, 42, 54, 115, 139, 168, 195, 224, 232, 248, 268, 272, 277, 400, 417, 432, 440, 448, 451, 550, 575
- `linear-algebra/src/ch18-convexity/02-caratheodory.md`：13 處，行 52, 113, 115, 150, 170, 204, 229, 266, 381, 383, 406, 452, 493
- `linear-algebra/src/ch18-convexity/03-separation.md`：28 處，行 9, 56, 130, 134, 164, 179, 193, 253, 288, 313, 329, 349, 372, 376, 420, 451, 456, 464, 485, 491, 499, 525, 533, 549, 569, 573, 574, 587
- `linear-algebra/src/ch18-convexity/04-gauges-support-functions-dual-norms.md`：29 處，行 1, 26, 80, 91, 93, 100, 105, 108, 139, 162, 178, 195, 211, 253, 265, 312, 346, 361, 367, 371, 381, 394, 405, 415, 449, 472, 521, 523, 563
- `linear-algebra/src/ch18-convexity/05-cones-and-farkas.md`：14 處，行 47, 60, 75, 142, 219, 236, 240, 308, 312, 337, 363, 394, 426, 561
- `linear-algebra/src/ch18-convexity/06-linear-programming-duality.md`：9 處，行 11, 118, 199, 201, 252, 259, 355, 414, 455
- `linear-algebra/src/ch18-convexity/07-minimax.md`：9 處，行 11, 106, 150, 195, 205, 255, 291, 349, 362
- `linear-algebra/src/ch18-convexity/08-extreme-points.md`：37 處，行 46, 63, 97, 111, 119, 136, 158, 168, 174, 176, 185, 187, 194, 220, 223, 241, 243, 245, 270, 303, 305, 338, 355, 363, 428, 431, 456, 458, 508, 535, 546, 563, 565, 587, 607, 611, 613
- `linear-algebra/src/ch18-convexity/09-polytopes.md`：21 處，行 3, 5, 29, 114, 139, 141, 174, 216, 241, 282, 307, 313, 319, 408, 439, 445, 462, 481, 483, 505, 527
- `linear-algebra/src/ch18-convexity/10-convex-functions.md`：21 處，行 11, 72, 76, 89, 163, 223, 243, 251, 267, 283, 287, 296, 312, 350, 366, 379, 385, 409, 427, 446, 494
- `linear-algebra/src/ch18-convexity/11-classical-inequalities.md`：24 處，行 15, 17, 30, 37, 41, 62, 68, 71, 107, 154, 158, 176, 197, 200, 201, 203, 204, 212, 214, 227, 236, 252, 303, 328
- `linear-algebra/src/ch18-convexity/index.md`：6 處，行 5, 11, 28, 47, 50, 52
- `linear-algebra/src/ch19-nonnegative/01-positive-matrices.md`：22 處，行 5, 36, 39, 42, 110, 118, 189, 214, 219, 226, 230, 236, 252, 260, 266, 284, 314, 375, 432, 456, 458, 460
- `linear-algebra/src/ch19-nonnegative/02-irreducibility-and-graphs.md`：21 處，行 5, 33, 58, 75, 81, 116, 180, 183, 206, 232, 242, 263, 275, 309, 317, 360, 399, 432, 441, 449, 464
- `linear-algebra/src/ch19-nonnegative/03-perron-frobenius.md`：18 處，行 25, 27, 84, 98, 117, 123, 135, 174, 188, 210, 231, 275, 285, 287, 301, 342, 368, 372
- `linear-algebra/src/ch19-nonnegative/04-collatz-wielandt.md`：15 處，行 5, 15, 76, 94, 151, 185, 194, 199, 203, 221, 272, 284, 350, 364, 436
- `linear-algebra/src/ch19-nonnegative/05-primitive-matrices.md`：24 處，行 5, 11, 79, 82, 88, 93, 176, 179, 186, 208, 210, 226, 232, 244, 248, 262, 264, 278, 305, 385, 393, 407, 410, 458
- `linear-algebra/src/ch19-nonnegative/06-markov-chains.md`：13 處，行 3, 130, 184, 194, 217, 257, 279, 286, 298, 312, 382, 468, 482
- `linear-algebra/src/ch19-nonnegative/07-birkhoff.md`：26 處，行 3, 5, 21, 29, 55, 96, 110, 112, 142, 146, 162, 168, 183, 206, 220, 271, 282, 304, 332, 405, 406, 414, 418, 424, 435, 458
- `linear-algebra/src/ch19-nonnegative/08-pagerank.md`：16 處，行 5, 9, 11, 40, 46, 77, 87, 95, 143, 236, 243, 331, 383, 403, 422, 424
- `linear-algebra/src/ch19-nonnegative/09-m-matrices.md`：25 處，行 5, 26, 63, 69, 77, 84, 104, 149, 173, 183, 200, 227, 251, 316, 323, 328, 367, 369, 371, 372, 380, 383, 407, 435, 526
- `linear-algebra/src/ch19-nonnegative/index.md`：5 處，行 3, 15, 28, 30, 35
- `linear-algebra/src/ch20-perturbation/01-gershgorin.md`：13 處，行 37, 151, 240, 261, 277, 295, 307, 317, 346, 371, 373, 385, 408
- `linear-algebra/src/ch20-perturbation/02-inclusion-regions.md`：18 處，行 5, 49, 75, 132, 149, 167, 204, 208, 210, 216, 262, 269, 276, 286, 396, 416, 441, 478
- `linear-algebra/src/ch20-perturbation/03-continuity-of-roots.md`：15 處，行 5, 110, 133, 163, 197, 242, 244, 280, 282, 343, 362, 366, 399, 403, 427
- `linear-algebra/src/ch20-perturbation/04-bauer-fike.md`：19 處，行 5, 42, 53, 55, 71, 87, 96, 108, 134, 137, 179, 214, 225, 239, 255, 274, 277, 324, 388
- `linear-algebra/src/ch20-perturbation/05-hoffman-wielandt.md`：20 處，行 17, 21, 32, 55, 62, 71, 84, 88, 126, 150, 183, 230, 234, 306, 308, 329, 356, 385, 402, 435
- `linear-algebra/src/ch20-perturbation/06-hermitian-perturbations.md`：20 處，行 41, 44, 48, 73, 90, 101, 130, 142, 149, 172, 184, 196, 215, 221, 243, 277, 285, 299, 363, 383
- `linear-algebra/src/ch20-perturbation/07-sylvester-bounds.md`：14 處，行 39, 44, 115, 183, 232, 283, 298, 351, 362, 377, 379, 421, 432, 434
- `linear-algebra/src/ch20-perturbation/08-principal-angles.md`：23 處，行 5, 64, 101, 107, 115, 134, 157, 195, 207, 211, 228, 239, 261, 269, 280, 282, 285, 318, 395, 401, 469, 489, 493
- `linear-algebra/src/ch20-perturbation/09-davis-kahan.md`：21 處，行 3, 5, 30, 47, 57, 74, 124, 142, 160, 196, 201, 222, 224, 285, 356, 358, 383, 417, 425, 457, 479
- `linear-algebra/src/ch20-perturbation/10-singular-values-and-polar.md`：16 處，行 5, 14, 30, 38, 43, 73, 82, 182, 229, 316, 362, 389, 391, 428, 432, 485
- `linear-algebra/src/ch20-perturbation/11-eigenvalue-condition.md`：29 處，行 3, 15, 20, 46, 55, 147, 161, 180, 186, 200, 220, 229, 241, 312, 326, 357, 375, 393, 407, 415, 417, 441, 445, 490, 503, 507, 536, 538, 540
- `linear-algebra/src/ch20-perturbation/index.md`：6 處，行 29, 31, 33, 34, 36, 53
- `linear-algebra/src/ch21-inequalities/01-hardy-littlewood-polya.md`：25 處，行 3, 5, 15, 27, 45, 64, 104, 114, 128, 162, 164, 170, 185, 196, 218, 258, 273, 303, 305, 365, 369, 387, 411, 446, 510
- `linear-algebra/src/ch21-inequalities/02-convex-functions-and-majorization.md`：18 處，行 114, 129, 170, 198, 208, 296, 331, 346, 370, 374, 413, 450, 464, 473, 483, 498, 556, 609
- `linear-algebra/src/ch21-inequalities/03-symmetric-gauge-functions.md`：19 處，行 5, 11, 33, 57, 80, 173, 181, 194, 214, 317, 355, 359, 377, 403, 423, 438, 443, 474, 478
- `linear-algebra/src/ch21-inequalities/04-unitarily-invariant-norms.md`：13 處，行 9, 13, 34, 111, 119, 160, 226, 274, 288, 301, 396, 406, 438
- `linear-algebra/src/ch21-inequalities/05-von-neumann-trace-inequality.md`：16 處，行 34, 52, 92, 100, 132, 138, 141, 173, 177, 191, 195, 214, 220, 254, 258, 301
- `linear-algebra/src/ch21-inequalities/06-ky-fan-dominance.md`：8 處，行 109, 216, 264, 272, 276, 301, 350, 357
- `linear-algebra/src/ch21-inequalities/07-lidskii-and-its-consequences.md`：13 處，行 56, 112, 116, 137, 157, 176, 225, 234, 262, 298, 303, 332, 344
- `linear-algebra/src/ch21-inequalities/08-operator-convexity.md`：20 處，行 3, 43, 66, 72, 76, 114, 132, 152, 166, 216, 230, 245, 250, 276, 286, 306, 335, 368, 370, 484
- `linear-algebra/src/ch21-inequalities/09-loewner-matrices.md`：31 處，行 26, 73, 78, 167, 188, 196, 203, 207, 211, 213, 241, 253, 277, 290, 327, 338, 342, 362, 380, 405, 416, 424, 456, 476, 485, 487, 493, 556, 578, 604, 610
- `linear-algebra/src/ch21-inequalities/10-loewners-theorem.md`：28 處，行 37, 63, 100, 112, 197, 260, 304, 334, 336, 380, 386, 394, 418, 431, 433, 437, 444, 477, 485, 556, 562, 601, 620, 624, 641, 651, 670, 672
- `linear-algebra/src/ch21-inequalities/11-matrix-means-and-inequalities.md`：31 處，行 5, 22, 26, 40, 77, 87, 106, 114, 149, 154, 170, 174, 180, 191, 221, 247, 256, 260, 284, 288, 314, 367, 390, 396, 409, 430, 432, 440, 497, 506, 515
- `linear-algebra/src/ch21-inequalities/12-golden-thompson.md`：34 處，行 43, 63, 95, 120, 128, 136, 158, 169, 211, 220, 226, 263, 268, 270, 311, 337, 346, 363, 365, 388, 421, 425, 430, 433, 477, 489, 533, 539, 541, 587, 589, 591, 608, 637
- `linear-algebra/src/ch21-inequalities/index.md`：14 處，行 3, 9, 10, 21, 43, 45, 46, 47, 49, 50, 51, 57, 58, 68
- `linear-algebra/src/ch22-geometry/01-affine-spaces.md`：29 處，行 7, 27, 60, 88, 155, 168, 204, 225, 237, 241, 300, 328, 331, 348, 350, 352, 354, 356, 368, 372, 434, 436, 505, 533, 544, 546, 552, 562, 570
- `linear-algebra/src/ch22-geometry/02-affine-subspaces.md`：26 處，行 1, 3, 35, 45, 59, 63, 107, 120, 141, 156, 162, 202, 208, 226, 373, 425, 449, 453, 455, 471, 474, 514, 516, 538, 582, 592
- `linear-algebra/src/ch22-geometry/03-polyhedra-and-linear-programming.md`：27 處，行 3, 5, 9, 30, 67, 71, 95, 135, 159, 191, 206, 251, 274, 276, 303, 305, 309, 370, 414, 448, 450, 468, 503, 523, 536, 544, 548
- `linear-algebra/src/ch22-geometry/04-euclidean-motions.md`：32 處，行 3, 5, 20, 32, 89, 116, 194, 214, 256, 260, 262, 279, 285, 288, 335, 397, 425, 433, 435, 441, 445, 455, 477, 502, 517, 527, 537, 539, 541, 574, 639, 641
- `linear-algebra/src/ch22-geometry/05-quadrics.md`：26 處，行 39, 58, 82, 105, 178, 212, 231, 245, 254, 262, 278, 297, 301, 304, 343, 345, 355, 377, 397, 405, 502, 512, 516, 556, 573, 575
- `linear-algebra/src/ch22-geometry/06-projective-space.md`：20 處，行 22, 72, 77, 84, 113, 123, 125, 178, 184, 202, 267, 297, 383, 468, 470, 472, 478, 556, 578, 580
- `linear-algebra/src/ch22-geometry/07-projective-transformations.md`：21 處，行 5, 23, 46, 52, 58, 104, 114, 248, 252, 264, 266, 353, 387, 389, 424, 432, 438, 440, 525, 654, 660
- `linear-algebra/src/ch22-geometry/08-projective-duality.md`：13 處，行 5, 66, 88, 90, 94, 111, 116, 131, 264, 286, 291, 333, 352
- `linear-algebra/src/ch22-geometry/09-desargues-and-pappus.md`：24 處，行 3, 70, 97, 111, 132, 136, 142, 144, 163, 171, 183, 185, 189, 199, 233, 294, 310, 321, 402, 418, 434, 485, 564, 566
- `linear-algebra/src/ch22-geometry/10-conics-and-plucker.md`：31 處，行 3, 43, 44, 49, 53, 55, 59, 135, 139, 171, 185, 251, 288, 307, 327, 346, 350, 384, 422, 493, 508, 543, 553, 571, 640, 656, 664, 668, 670, 672, 680
- `linear-algebra/src/ch22-geometry/index.md`：10 處，行 36, 47, 49, 64, 69, 70, 74, 75, 76, 77
- `linear-algebra/src/ch23-algebras/01-associative-algebras.md`：22 處，行 3, 9, 15, 41, 52, 67, 91, 98, 109, 121, 152, 170, 177, 197, 216, 410, 437, 453, 483, 503, 531, 540
- `linear-algebra/src/ch23-algebras/02-ideals-and-quotients.md`：15 處，行 28, 56, 95, 145, 176, 195, 197, 241, 268, 308, 377, 401, 405, 407, 453
- `linear-algebra/src/ch23-algebras/03-simple-and-semisimple.md`：13 處，行 5, 94, 107, 147, 151, 201, 253, 257, 323, 331, 371, 377, 474
- `linear-algebra/src/ch23-algebras/04-schurs-lemma.md`：15 處，行 3, 7, 22, 25, 35, 59, 61, 63, 89, 102, 171, 220, 226, 292, 304
- `linear-algebra/src/ch23-algebras/05-double-commutant.md`：14 處，行 42, 63, 71, 170, 209, 221, 225, 260, 262, 272, 276, 323, 381, 399
- `linear-algebra/src/ch23-algebras/06-wedderburn.md`：12 處，行 5, 58, 95, 123, 125, 132, 167, 175, 237, 280, 284, 364
- `linear-algebra/src/ch23-algebras/07-group-representations.md`：22 處，行 18, 35, 36, 74, 100, 113, 124, 132, 173, 180, 210, 230, 254, 256, 287, 289, 315, 365, 422, 424, 426, 442
- `linear-algebra/src/ch23-algebras/08-characters.md`：18 處，行 37, 120, 153, 220, 232, 306, 335, 414, 451, 491, 502, 548, 578, 580, 609, 626, 628, 694
- `linear-algebra/src/ch23-algebras/09-the-abelian-case.md`：14 處，行 5, 26, 51, 61, 73, 87, 176, 182, 276, 327, 386, 509, 579, 617
- `linear-algebra/src/ch23-algebras/10-summary-and-transfer.md`：9 處，行 25, 48, 53, 68, 104, 106, 153, 177, 189
- `linear-algebra/src/ch23-algebras/index.md`：23 處，行 11, 15, 38, 40, 51, 52, 61, 63, 66, 69, 74, 76, 77, 83, 85, 86, 87, 88, 89, 91, 92, 97, 102
- `linear-algebra/src/ch24-applied/01-floating-point-and-backward-error.md`：8 處，行 71, 100, 121, 186, 191, 274, 447, 504
- `linear-algebra/src/ch24-applied/02-elimination-pivoting-and-cost.md`：19 處，行 1, 24, 65, 88, 106, 114, 127, 268, 282, 357, 385, 393, 414, 435, 591, 598, 600, 641, 659
- `linear-algebra/src/ch24-applied/03-numerical-least-squares.md`：26 處，行 7, 24, 117, 129, 143, 162, 214, 218, 224, 256, 275, 312, 318, 333, 344, 352, 380, 385, 403, 431, 434, 437, 465, 507, 553, 586
- `linear-algebra/src/ch24-applied/04-power-method-and-inverse-iteration.md`：22 處，行 87, 177, 197, 247, 273, 281, 301, 309, 313, 354, 443, 469, 482, 494, 500, 531, 580, 603, 605, 607, 615, 631
- `linear-algebra/src/ch24-applied/05-the-qr-algorithm.md`：22 處，行 3, 16, 25, 30, 38, 52, 58, 131, 135, 139, 193, 202, 211, 235, 267, 310, 331, 347, 456, 516, 581, 587
- `linear-algebra/src/ch24-applied/06-krylov-subspaces.md`：36 處，行 5, 9, 18, 33, 43, 71, 93, 128, 135, 137, 148, 158, 171, 177, 192, 209, 215, 248, 256, 262, 272, 287, 289, 336, 382, 392, 406, 427, 429, 456, 458, 460, 479, 494, 538, 544
- `linear-algebra/src/ch24-applied/07-conjugate-gradient.md`：21 處，行 5, 43, 81, 109, 140, 159, 219, 265, 273, 287, 294, 310, 353, 359, 381, 430, 444, 483, 574, 599, 697
- `linear-algebra/src/ch24-applied/08-lax-pairs-and-the-toda-flow.md`：21 處，行 5, 76, 107, 109, 116, 153, 158, 176, 214, 221, 226, 231, 257, 285, 300, 335, 343, 461, 465, 475, 507
- `linear-algebra/src/ch24-applied/09-vibrations.md`：22 處，行 11, 96, 115, 209, 227, 242, 279, 310, 318, 358, 371, 383, 401, 452, 472, 487, 522, 524, 542, 550, 558, 568
- `linear-algebra/src/ch24-applied/10-principal-components.md`：14 處，行 16, 133, 137, 188, 246, 270, 285, 299, 303, 326, 338, 373, 407, 429
- `linear-algebra/src/ch24-applied/11-graph-laplacians.md`：30 處，行 5, 47, 80, 110, 114, 116, 118, 141, 150, 170, 176, 227, 248, 279, 289, 295, 307, 309, 327, 379, 401, 427, 475, 481, 543, 570, 574, 580, 586, 594
- `linear-algebra/src/ch24-applied/12-the-fast-fourier-transform.md`：21 處，行 7, 23, 40, 100, 109, 222, 234, 236, 293, 311, 315, 335, 354, 366, 380, 382, 408, 410, 481, 483, 485
- `linear-algebra/src/ch24-applied/13-fast-matrix-multiplication.md`：20 處，行 15, 34, 58, 151, 190, 212, 232, 235, 238, 273, 283, 290, 305, 316, 389, 426, 492, 573, 583, 642
- `linear-algebra/src/ch24-applied/index.md`：16 處，行 5, 7, 19, 30, 34, 47, 53, 57, 60, 64, 65, 70, 76, 78, 81, 86
- `linear-algebra/src/ch24a-notation/index.md`：13 處，行 15, 27, 31, 81, 155, 170, 232, 242, 254, 268, 273, 284, 353
- `linear-algebra/src/index.md`：12 處，行 5, 9, 11, 13, 15, 17, 23, 29, 43, 53, 55, 59

