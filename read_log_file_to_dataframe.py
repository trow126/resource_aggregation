import pandas as pd
import datetime

# ログファイルの各行を処理してデータを抽出する関数
def process_log_line(line):
    return line.strip().split('\t')

# ログファイルを読み込んでDataFrameに変換する関数
def read_log_file_to_dataframe(file_path):
    # ログファイルを読み込む
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # ログファイルの各行を処理し、データを抽出する
    data = []
    for line in lines:
        row = process_log_line(line)
        data.append(row)

    # データを整形してDataFrameに変換する
    df = pd.DataFrame(data)
    df = df.pivot_table(index=0, columns=1, aggfunc=lambda x: x)

    # カラム名をリネーム
    df.columns = [f"{col[0]}_{idx + 1}" for idx, col in enumerate(df.columns)]

    # インデックスをdatetime型に変換
    df.index = pd.to_datetime(df.index, format="%Y年%m月%d日\t%H時%M分%S秒")

    return df

# file_pathsのファイルを1件ずつ処理する
dfs = []
for file_path in file_paths:
    df = read_log_file_to_dataframe(file_path)
    dfs.append(df)

# 各DataFrameを結合する
combined_df = pd.concat(dfs)

print(combined_df)
