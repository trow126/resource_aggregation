import os
import re

# フォルダ内の指定されたファイルのフルパスの一覧を取得する関数
def get_file_paths(folder_path, regex_pattern):
    # 正規表現のコンパイル
    file_pattern = re.compile(regex_pattern)
    
    # フォルダ内のファイル名を走査して、正規表現に一致するファイルのフルパスをリストに格納
    file_paths = [os.path.join(folder_path, file_name) for file_name in os.listdir(folder_path) if file_pattern.match(file_name)]

    return file_paths

# 使用例
folder_path = "/path/to/your/folder"  # ここにフォルダパスを指定してください
regex_pattern = r"^.+\.log$"  # ここに取得したいファイル名を正規表現で指定してください
file_paths = get_file_paths(folder_path, regex_pattern)

print(file_paths)
