# math-atlas

一套「零基礎到數學研究所資格考」教科書的地圖與規格。全套有 25 冊、167 章，以一張分型別的依賴圖串起來；各冊的書稿在各自的 repo（`analysis-book`、`linear-algebra` 等）。

- 先讀 `spec/00-overview.md`。
- 要看圖：`generated/README.md`（Mermaid，GitHub 會直接渲染），或用瀏覽器開 `generated/atlas.html`（互動版，需要網路載入 elkjs）。
- 要看數字：`generated/report.md`（最長鏈、資格考必讀集合、瓶頸、領域覆蓋），`generated/diff.md`（計畫邊和計算邊的差異）。

## 目錄

```
spec/        全套約定：ID 與邊、記號、A／R 深度、流程圖、引擎需求、遷移與待決事項
registry/    唯一的事實來源
  volumes.yaml        冊
  chapters.yaml       章（列表順序＝冊內章序）
  plan-edges.yaml     手寫的章層級計畫邊（s／b／see／revisits，b 要附 why）
  computed/           由書稿 build 計算出的邊（目前：線代書）
  statements.yaml     陳述層種子（F 系列＋九個主幹）
  exam-targets.yaml   資格考目標與考綱覆蓋
  fields.yaml         數學各領域 → 章的覆蓋表
tools/       atlas.py（check／stats／render／diff）、graph.py、import_la.py
generated/   工具的產出，勿手改
```

## 指令

只需要 Python 3 和 PyYAML。

```sh
python3 tools/import_la.py          # 從 ../linear-algebra/_build/crossref_labels.json 重算線代邊
python3 tools/atlas.py check        # 無環、章序、選讀、b 的 why；失敗時結束碼為 1
python3 tools/atlas.py all          # check＋stats＋diff＋render，寫入 generated/
python3 -m unittest discover -s tools -p "test_*.py"
```

修改 registry 之後，跑一次 `atlas.py all`，連同 `generated/` 一起提交。

## 授權

內容（`registry/`、`spec/`、`generated/`）採 CC BY-SA 4.0；程式（`tools/`）採 MIT。詳見 `LICENSE`。
