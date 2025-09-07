# CSV 自動集計ツール

## 概要
複数の CSV データを自動で集計し、Excel に出力する Python ツールです。  
日付別・カテゴリ別の集計を自動で行い、見やすい表を生成します。

## フォルダ構成
csv_auto_tools/
├─ csv_auto.py # メインスクリプト
├─ README.md # このファイル
├─ requirements.txt # 依存ライブラリ
├─ examples/ # サンプル CSV を置く（再現用）
│ ├─ sample_data_1.csv
│ └─ sample_data_2.csv
└─ docs/
└─ screenshots/ # Excel 出力結果のスクリーンショット
├─ daily_total.png
└─ category_total.png

markdown
コードをコピーする

## 使い方

1. 仮想環境を作成・有効化  

   **Windows の場合**
python -m venv venv
venv\Scripts\activate

markdown
コードをコピーする

**mac / Linux の場合**
python -m venv venv
source venv/bin/activate

markdown
コードをコピーする

2. 必要なライブラリをインストール  

pip install -r requirements.txt

markdown
コードをコピーする

3. サンプル CSV を準備（`examples/` 内に置く）

4. スクリプトを実行  

python csv_auto.py

yaml
コードをコピーする

5. Excel ファイルが生成されます（出力は Git で無視されます）

---

## 出力イメージ

### 日付別集計
![日付別集計](docs/screenshots/daily_total.png)

### カテゴリ別集計
![カテゴリ別集計](docs/screenshots/category_total.png)

---

## 注意事項

- 仮想環境 (`venv/`) や生成 Excel ファイル (`*.xlsx`) は `.gitignore` により GitHub には上がりません  
- サンプル CSV は `examples/` フォルダに置くこと  
- 他の開発環境でも同じ手順で再現可能です