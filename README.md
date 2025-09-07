# CSV 自動集計ツール

このツールは、CSV データを自動的に読み込み、  
「日付別の売上集計」と「カテゴリ別の売上集計」を Excel 形式で出力する Python スクリプトです。  
表は見やすいレイアウトで整形され、ビジネスでの利用を想定しています。

---

## 機能

- CSV ファイルを読み込み、自動で集計  
- 日付別の売上合計を算出  
- カテゴリ別の売上合計を算出  
- 2 種類の集計結果を Excel ファイルとして保存  
- タイトル・罫線・セル幅調整済みで見やすいフォーマットを自動適用

---

## 必要な環境

- Python 3.9 以上推奨
- Windows / macOS / Linux 対応

---

## インストール方法

1. リポジトリをクローン

    ```bash
    git clone https://github.com/ユーザー名/csv_auto_tools.git
    cd csv_auto_tools
    ```

2. 仮想環境を作成して有効化

    **Windows の場合**
    
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

    **macOS / Linux の場合**
    
    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3. 必要なライブラリをインストール

    ```bash
    pip install -r requirements.txt
    ```

---

## 使用方法

1. `examples/` フォルダに CSV ファイルを配置  
   - 例: `sample_data_1.csv`, `sample_data_2.csv`

2. スクリプトを実行

    ```bash
    python csv_auto.py
    ```

3. 出力結果  
   - `daily_total.xlsx` （日付別集計表）  
   - `category_total.xlsx` （カテゴリ別集計表）

---

## フォルダ構成

<pre><code>
csv_auto_tools/
├─ csv_auto.py               # メインスクリプト
├─ README.md                 # このファイル
├─ requirements.txt          # 依存ライブラリ
├─ .gitignore                # Git 無視設定
├─ examples/                 # サンプル CSV を置く（再現用）
│   ├─ sample_data_1.csv
│   └─ sample_data_2.csv
└─ docs/
    └─ screenshots/          # Excel 出力結果のスクリーンショット
        ├─ daily_total.png
        └─ category_total.png
</code></pre>

---

## ライセンス

MIT License
