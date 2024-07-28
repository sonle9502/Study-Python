# # utils/dataPath.py
import os

data_root = f'C:\\Users\\s-le\\Desktop\\study-private\\Python\\Study-Python\\Project\\Project_file\\datatest'
def create_filepath(position, name):
    # 正しいパス結合方法を使用 
    base_dir = os.path.join(data_root, position)
    # フォルダーの存在を確認し、存在しない場合は作成
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)
        print(f"{base_dir} フォルダーを作成しました。")
    else:
        print(f"{base_dir} フォルダーは既に存在します。")
    file_path = os.path.join(base_dir, name)
    return file_path

def create_folderpath(position):
    # 正しいパス結合方法を使用 
    folderpath = os.path.join(data_root, position)
    # フォルダーの存在を確認し、存在しない場合は作成
    if not os.path.exists(folderpath):
        os.makedirs(folderpath)
        print(f"{folderpath} フォルダーを作成しました。")
    else:
        print(f"{folderpath} フォルダーは既に存在します。")
    return folderpath

def count_files_in_folder(position):
    folder_path = create_folderpath(position)
    # フォルダーの存在を確認
    if not os.path.exists(folder_path):
        print(f"{folder_path} フォルダーが存在しません。")
        return 0

    # フォルダー内のファイル数をカウント
    file_count = len([f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))])
    return file_count