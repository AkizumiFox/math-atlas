# 樂詞網數學名詞（政府開放資料）

- `univ.csv`：國家教育研究院「數學名詞—兩岸數學學術名詞」，https://data.gov.tw/dataset/15445
- `hs.csv`：國家教育研究院「數學名詞—高中含以下數學學術名詞」，https://data.gov.tw/dataset/15446

依政府資料開放授權條款第 1 版（https://data.gov.tw/license）使用，與 CC BY 4.0 相容；出處標示見 repo 根目錄的 `LICENSE`。
下載日期 2026-10-10，原檔未修改。`tools/seed_terms.py` 讀這兩個檔，把譯名填進 `registry/terms.yaml`：
以 `univ.csv` 為主，`hs.csv` 只補 F 冊的基礎詞；同一條列了多個譯名的標為 choose，兩份都沒有的標為 missing，交給作者決定。
