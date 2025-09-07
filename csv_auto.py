import pandas as pd
from openpyxl import load_workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
import shutil
import os

# --- 元CSVをコピーして作業用ファイルにする ---
ORIGINAL_CSV = "sample_data.csv"
WORK_CSV = "sample_data_work.csv"

if os.path.exists(WORK_CSV):
    os.remove(WORK_CSV)
shutil.copy(ORIGINAL_CSV, WORK_CSV)

# --- CSV読み込み（文字化け対策） ---
try:
    df = pd.read_csv(WORK_CSV, encoding="utf-8-sig")
except UnicodeDecodeError:
    df = pd.read_csv(WORK_CSV, encoding="cp932")

# 列名の前後スペースを削除
df.columns = df.columns.str.strip()

# --- 必須列チェック ---
required_columns = ["日付", "商品", "売上"]
for col in required_columns:
    if col not in df.columns:
        raise ValueError(f"列 '{col}' が CSV に存在しません。列名を確認してください。")

# --- 日付別集計 ---
daily_total = df.groupby("日付")["売上"].sum()
daily_total_df = daily_total.reset_index()

# --- 商品別集計 ---
category_total = df.groupby("商品")["売上"].sum()
category_total_df = category_total.reset_index()

# --- Excel出力関数 ---
def save_excel(df, filename, title="集計表"):
    # データをB3から出力
    df.to_excel(filename, index=False, startrow=2, startcol=1)

    wb = load_workbook(filename)
    ws = wb.active

    # --- タイトルをB2:C2結合（初期） ---
    start_col = 2
    end_col = min(3, 1 + len(df.columns))  # B2:C2 または列数に応じて
    ws.merge_cells(start_row=2, start_column=start_col, end_row=2, end_column=end_col)
    ws["B2"] = title
    ws["B2"].font = Font(bold=True, size=14)
    ws["B2"].alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)

    # --- タイトルが長い場合は横幅全体まで拡張 ---
    if len(title) > 15 and len(df.columns) > 2:
        ws.unmerge_cells(start_row=2, start_column=start_col, end_row=2, end_column=end_col)
        end_col = 1 + len(df.columns)  # 表の右端まで結合
        ws.merge_cells(start_row=2, start_column=start_col, end_row=2, end_column=end_col)

    # --- タイトル下太線 ---
    thick_line = Border(bottom=Side(style='thick'))
    for col in range(start_col, end_col + 1):
        ws.cell(row=2, column=col).border = thick_line

    # --- ヘッダー装飾（B3から） ---
    for col in range(2, 2 + len(df.columns)):
        cell = ws.cell(row=3, column=col)
        cell.font = Font(bold=True, color="FFFFFF")
        cell.fill = PatternFill("solid", fgColor="4F81BD")
        cell.alignment = Alignment(horizontal="center")
        # ヘッダー下二重線
        double_line = Border(bottom=Side(style='double'))
        cell.border = double_line

    # --- 数値列書式（C列想定） ---
    for row in ws.iter_rows(min_row=4, max_row=3 + len(df), min_col=3, max_col=3):
        for cell in row:
            cell.number_format = '#,##0'

    # --- 外枠 ---
    thick_border = Border(
        left=Side(style='thick'),
        right=Side(style='thick'),
        top=Side(style='thick'),
        bottom=Side(style='thick')
    )
    for r in range(3, 4 + len(df)):
        for c in range(2, 2 + len(df.columns)):
            ws.cell(row=r, column=c).border = thick_border

    # --- 列幅自動調整 ---
    for c in range(2, 2 + len(df.columns)):
        real_cells = [ws.cell(row=r, column=c) for r in range(3, 4 + len(df))]
        max_length = max(len(str(cell.value)) for cell in real_cells if cell.value is not None)
        ws.column_dimensions[ws.cell(row=3, column=c).column_letter].width = max_length + 2

    wb.save(filename)

# --- 保存（タイトルはカテゴリートータル表記なし） ---
save_excel(daily_total_df, "daily_total.xlsx", title="日付別売上集計")
save_excel(category_total_df, "category_total.xlsx", title="商品別売上集計")

# --- 結果表示 ---
print("日付別合計:")
print(daily_total)
print("\n商品別合計:")
print(category_total)
