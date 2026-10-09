# 英文用詞變體（由 `tools/usage_report.py` 從兩本書稿統計，勿手改）

約定在 `registry/usage.yaml`。每組選一個（use），其餘列為 avoid；status 為 proposed 的組待作者確認，confirmed 的組列出書稿裡每一處 avoid 寫法（將來由引擎在 build 時檢查，spec/05）。統計只看散文：數學式、程式碼、TikZ、label 與參照都已去掉。

## 單射（`injective`，proposed）

| 寫法 | 線代書 | analysis-book | 合計 | |
|---|---:|---:|---:|---|
| injective | 489 | 118 | 607 | **use** |
| injection* | 7 | 5 | 12 | **use** |
| injectivity | 61 | 41 | 102 | **use** |
| one-to-one | 11 | 1 | 12 | avoid |
| one-one | 0 | 0 | 0 | avoid |

injective 系列 721 次，one-to-one 12 次（線代書 11、analysis-book 1）。injective／surjective／bijective 成組，不會和 one-to-one correspondence（＝bijection）混淆。

## 滿射（`surjective`，proposed）

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

## 雙射（`bijective`，proposed）

| 寫法 | 線代書 | analysis-book | 合計 | |
|---|---:|---:|---:|---|
| bijective | 122 | 28 | 150 | **use** |
| bijection* | 227 | 21 | 248 | **use** |
| one-to-one correspondence* | 1 | 0 | 1 | avoid |

bijective／bijection 398 次，one-to-one correspondence 1 次。

## 像（`image`，proposed）

| 寫法 | 線代書 | analysis-book | 合計 | |
|---|---:|---:|---:|---|
| image* | 408 | 74 | 482 | **use** |

f(X) 一律稱 image（482 次）。range 出現 161 次，幾乎都是別的意思（range over、a range of lines），所以不列入 avoid、也不做 lint；只有線代書一處把 range 當成 image 的同義詞，改寫時順手改掉。range 不用來指對應域（codomain）。

## 核與零空間（`kernel`，proposed）

| 寫法 | 線代書 | analysis-book | 合計 | |
|---|---:|---:|---:|---|
| kernel* | 416 | 0 | 416 | **use** |
| null space* | 80 | 0 | 80 | **use** |
| nullspace* | 0 | 0 | 0 | avoid |

兩個都保留，各有用途，不是變體：kernel 是映射的核（ker T，416 次），null space 是矩陣的零空間（nul A ⊆ Fⁿ，80 次），這是線代書 NOTATION.md 的既有約定。nullspace（連寫）0 次，列入 avoid 防止日後出現。

## 映射與函數（`map`，proposed）

| 寫法 | 線代書 | analysis-book | 合計 | |
|---|---:|---:|---:|---|
| map | 1309 | 21 | 1330 | **use** |
| maps | 540 | 5 | 545 | **use** |
| linear map* | 511 | 0 | 511 | **use** |
| function | 921 | 288 | 1209 | **use** |
| functions | 400 | 96 | 496 | **use** |
| mapping | 21 | 0 | 21 | avoid |
| mappings | 0 | 0 | 0 | avoid |
| linear mapping* | 0 | 0 | 0 | avoid |
| linear transformation* | 1 | 0 | 1 | avoid |

map 用於保持結構的映射（linear map 511 次），function 用於集合論與分析的一般函數（1,705 次）；operator 指 V → V 的線性映射。mapping 21 次、linear transformation 1 次是同一意思的第三種寫法，改成 map。

## non- 字首（`non-prefix`，proposed）

| 寫法 | 線代書 | analysis-book | 合計 | |
|---|---:|---:|---:|---|
| non-negative | 634 | 28 | 662 | **use** |
| non-zero | 1714 | 22 | 1736 | **use** |
| non-empty | 228 | 150 | 378 | **use** |
| non-singular | 60 | 0 | 60 | **use** |
| non-trivial | 39 | 0 | 39 | **use** |
| non-decreasing | 28 | 0 | 28 | **use** |
| non-increasing | 6 | 0 | 6 | **use** |
| non-degenerate | 144 | 0 | 144 | **use** |
| non-invertible | 5 | 0 | 5 | **use** |
| non-positive | 8 | 0 | 8 | **use** |
| non-measurable | 0 | 0 | 0 | **use** |
| nonnegative | 0 | 0 | 0 | avoid |
| nonzero | 0 | 0 | 0 | avoid |
| nonempty | 0 | 0 | 0 | avoid |
| nonsingular | 0 | 0 | 0 | avoid |
| nontrivial | 0 | 0 | 0 | avoid |
| nondecreasing | 0 | 0 | 0 | avoid |
| nonincreasing | 0 | 0 | 0 | avoid |
| nondegenerate | 0 | 0 | 0 | avoid |
| noninvertible | 0 | 0 | 0 | avoid |
| nonpositive | 0 | 0 | 0 | avoid |
| nonmeasurable | 0 | 0 | 0 | avoid |

兩本書都 100% 加連字號（non-zero 1,736 次、non-negative 662 次、non-empty 378 次，連寫 0 次），提案照現況。注意：美式數學出版（AMS、Chicago）多半連寫（nonnegative）；若要改成連寫，改動的是兩本書全部的既有用法，請作者決定。

## 連寫的複合詞（`closed-compounds`，proposed）

| 寫法 | 線代書 | analysis-book | 合計 | |
|---|---:|---:|---:|---|
| codomain* | 45 | 42 | 87 | **use** |
| preimage* | 30 | 101 | 131 | **use** |
| counterexample* | 39 | 28 | 67 | **use** |
| co-domain* | 0 | 0 | 0 | avoid |
| pre-image* | 0 | 0 | 0 | avoid |
| counter-example* | 0 | 0 | 0 | avoid |

連寫 87／131／67 次，加連字號 0 次。

## finite-dimensional（`dimensional`，proposed）

| 寫法 | 線代書 | analysis-book | 合計 | |
|---|---:|---:|---:|---|
| finite-dimensional | 659 | 0 | 659 | **use** |
| infinite-dimensional | 64 | 0 | 64 | **use** |
| finite dimensional | 0 | 0 | 0 | avoid |
| infinite dimensional | 0 | 0 | 0 | avoid |

加連字號 723 次，分寫 0 次；不論修飾名詞或當述語都加連字號。

## 正定與半正定（`definite`，proposed）

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

## 自伴（`self-adjoint`，proposed）

| 寫法 | 線代書 | analysis-book | 合計 | |
|---|---:|---:|---:|---|
| self-adjoint | 237 | 0 | 237 | **use** |
| selfadjoint | 0 | 0 | 0 | avoid |
| self adjoint | 0 | 0 | 0 | avoid |

self-adjoint 237 次，其他寫法 0 次。

## well-defined（`well-defined`，proposed）

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

## if and only if（`iff`，proposed）

| 寫法 | 線代書 | analysis-book | 合計 | |
|---|---:|---:|---:|---|
| if and only if | 778 | 83 | 861 | **use** |
| iff | 40 | 40 | 80 | avoid |

if and only if 861 次，iff 80 次。iff 多半出現在 F1 談連接詞本身的地方（an "iff"、iff-introduction），那是在講符號，不是縮寫；其餘當縮寫用的改成 if and only if。lint 會把 F1 的用法也列出來，由作者逐處判斷。

## 複數形（`plurals`，proposed）

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

## 美式拼寫（`us-spelling`，proposed）

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

