import os
import glob

def write_png_file_names(path, output_file):
    # 取得指定路徑下的所有.png檔案
    file_names = glob.glob(os.path.join(path, '*.png'))
    
    with open(output_file, 'w') as f:
        for file_name in file_names:
            # 寫入檔案名稱（包含路徑）至txt檔案
            f.write(file_name + '\n')

# 指定要搜尋的路徑和輸出的檔案名稱
folder_path = 'C:/Users/Asc-user/Documents/YOLO/Y562_train/shid_paint_2'
output_file_path = 'C:/Users/Asc-user/Documents/YOLO/Y562_train/shid_paint_2/train.txt'

# 呼叫函式將檔案名稱寫進txt檔案
write_png_file_names(folder_path, output_file_path)
