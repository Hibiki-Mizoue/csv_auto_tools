# CSV 自動集計ツール

![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)

## 概要
複数の CSV データを自動で集計し、Excel に出力する Python ツールです。  
日付別・カテゴリ別の集計を自動で行い、見やすい表を生成します。

---

## フォルダ構成

``` 
csv_auto_tools/
├─ csv_auto.py # メインスクリプト
├─ README.md # このファイル
├─ requirements.txt # 依存ライブラリ
├─ .gitignore # Git 無視設定
├─ examples/ # サンプル CSV を置く
│ ├─ sample_data_1.csv
│ └─ sample_data_2.csv
└─ docs/
└─ screenshots/ # Excel 出力結果のスクリーンショット
├─ daily_total.png
└─ category_total.png

``` 

## 使い方

1. 仮想環境を作成・有効化  

   **Windows の場合**
   ```bash
   python -m venv venv
   venv\Scripts\activate

   mac / Linux の場合

   python -m venv venv
source venv/bin/activate

2. 必要なライブラリをインストール

pip install -r requirements.txt

3. サンプル CSV を準備（examples/ 内に置く）
4. スクリプトを実行

python csv_auto.py

5. Excel ファイルが生成されます（出力ファイルは .gitignore により GitHub に上がりません）

出力イメージ
日付別集計

カテゴリ別集計

注意事項

仮想環境 (venv/) や生成 Excel ファイル (*.xlsx) は .gitignore により GitHub には上がりません

サンプル CSV は examples/ フォルダに置くこと

他の開発環境でも同じ手順で再現可能です

ライセンス

このプロジェクトは MIT ライセンスのもとで公開されています。