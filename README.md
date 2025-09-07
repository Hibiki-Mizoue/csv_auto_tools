# CSV 自動集計ツール

## 概要
複数の CSV データを自動で集計し、Excel に出力する Python ツールです。  
日付別・カテゴリ別の集計を自動で行い、見やすい表を生成します。

## フォルダ構成
csv_auto_tools/
├─ csv_auto.py
├─ README.md
├─ requirements.txt
├─ examples/
└─ docs/screenshots/

bash
コードをコピーする

## 使い方
1. 仮想環境を作成・有効化
```bash
python -m venv venv
source venv/bin/activate  # mac/linux
venv\Scripts\activate     # Windows
必要なライブラリをインストール

bash
コードをコピーする
pip install -r requirements.txt
サンプル CSV を準備（examples/ 内に置く）

スクリプトを実行

bash
コードをコピーする
python csv_auto.py
Excel ファイルが生成されます（出力は無視される設定）

出力イメージ
日付別集計

カテゴリ別集計

注意
仮想環境や生成 Excel ファイルは Git に上がらないよう .gitignore で管理しています

サンプル CSV は examples/ フォルダに置いてください

yaml
コードをコピーする
