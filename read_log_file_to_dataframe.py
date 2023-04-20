import pandas as pd

# ログファイルを読み込んでDataFrameに変換する関数
def read_log_file_to_dataframe(file_path):
    with open(file_path, 'r', encoding="utf-8") as file:
        lines = file.readlines()

    data = []
    current_time = None
    for line in lines:
        line = line.strip()
        if "年" in line:
            current_time = line
        else:
            row = process_log_line(line)
            row.insert(0, current_time)
            data.append(row)

    df = pd.DataFrame(data, columns=["時間", "種類", "値1", "値2"])
    return df

# ログファイルの各行を処理してデータを抽出する関数
def process_log_line(line):
    return line.split('\t')

# ファイルパスリストからすべてのログファイルを読み込み、1つのDataFrameに結合する
def read_all_log_files(file_paths):
    all_dataframes = []

    for file_path in file_paths:
        df = read_log_file_to_dataframe(file_path)
        all_dataframes.append(df)

    merged_df = pd.concat(all_dataframes, ignore_index=True)
    return merged_df

# 使用例
merged_df = read_all_log_files(file_paths)
print(merged_df)
