import json
import os
import numpy as np
import cv2

json_root = 'C:/Users/Asc-user/Documents/YOLO/Y562_train/steel_json/'
txt_root = 'C:/Users/Asc-user/Documents/YOLO/Y562_train/steel_txt/'
files = os.listdir(json_root)
obj_names = 'C:/Users/Asc-user/Documents/YOLO/Y562_train/obj.names.txt'
f_names = open(obj_names, 'a')
names = []

print(len(files))
for i in range(len(files)):
    name = files[i].split('.')[0]
    json_name = os.path.join(json_root, files[i])
    txt_name = os.path.join(txt_root, name+'.txt')
    f_json = open(json_name, 'r', encoding='utf-8')
    f_txt = open(txt_name, 'w')
    data = json.load(f_json)
    shapes = data['shapes']
    ww = float(data['imageWidth'])
    hh = float(data['imageHeight'])

    for j in range(len(shapes)):
        # 將 JSON 中 'group_id'=255 的轉換為 6
        if shapes[j]['label'] == 255:
            shapes[j]['label'] = 6
        # 製作 obj.names 檔案
        if shapes[j]['label'] in names:
            continue
        else:
            f_names.write(str(shapes[j]['label']) + '\n')
            names.append(shapes[j]['label'])
        # 將 JSON 轉換為 txt
        points = shapes[j]['points']
        points = np.array(points)
        xs = points[:, 0].astype('float')
        ys = points[:, 1].astype('float')
        x_max = xs.max()
        x_min = xs.min()
        y_max = ys.max()
        y_min = ys.min()
        x_center = (x_min + x_max)/2
        y_center = (y_min + y_max)/2
        w = x_max - x_min
        h = y_max - y_min
        f_txt.write(str(shapes[j]['label']) + ' ')
        f_txt.write(str(x_center / ww) + ' ')
        f_txt.write(str(y_center / hh) + ' ')
        f_txt.write(str(w / ww) + ' ')
        f_txt.write(str(h / hh) + '\n')

    f_txt.close()
    f_json.close()
f_names.close()