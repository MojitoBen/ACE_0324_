import os

def rename_files(folder_path, target_name):
    for filename in os.listdir(folder_path):
        if filename.endswith(".png") and " - 複製" in filename:
            old_path = os.path.join(folder_path, filename)
            new_filename = filename.replace(" - 複製", target_name)
            new_path = os.path.join(folder_path, new_filename)
            os.rename(old_path, new_path)
            print(f"Renamed: {filename} -> {new_filename}")

if __name__ == "__main__":
    folder_path = "C:/Users/Asc-user/Documents/YOLO/Y562_train/shid_num_temp/hid"  # 替換成你的資料夾路徑
    target_name = "_2"  # 替換成你想要的新名稱
    rename_files(folder_path, target_name)
