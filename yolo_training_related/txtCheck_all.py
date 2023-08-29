
import cv2
import os

def visualize_bboxes_in_folder(folder_path):
    # 取得指定資料夾內的所有圖片和對應的txt檔案
    image_files = [file for file in os.listdir(folder_path) if file.endswith('.png')]
    txt_files = [file[:-4] + '.txt' for file in image_files]
    #txt_files = [file for file in os.listdir(folder_path) if file.endswith('.txt')]

    for image_file, txt_file in zip(image_files, txt_files):
        # 圖片路徑和對應的txt檔案路徑
        image_path = os.path.join(folder_path, image_file)
        txt_path = os.path.join(folder_path, txt_file)

        # 開啟圖片
        image = cv2.imread(image_path)

        # 讀取 txt 檔案內容
        with open(txt_path, 'r') as f:
            lines = f.readlines()

        # 繪製框
        for line in lines:
            line = line.strip().split(' ')
            cls_id = str(line[0])
            x, y, w, h = [float(coord) for coord in line[1:]]
            image_height, image_width = image.shape[:2]

            # 將相對座標轉換為圖片上的絕對座標
            x1 = int((x - w / 2) * image_width)
            y1 = int((y - h / 2) * image_height)
            x2 = int((x + w / 2) * image_width)
            y2 = int((y + h / 2) * image_height)

            # 繪製矩形框
            cv2.rectangle(image, (x1 , y1 ), (x2 , y2 ), (0, 255, 0), 2)
            cv2.putText(image, str(cls_id), (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 2)

        # 顯示圖片
        w, h, c = image.shape
        image = cv2.resize(image, (h //3, w //3), interpolation=cv2.INTER_CUBIC)
        cv2.imshow('Image with Bounding Boxes', image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

# 指定資料夾路徑
folder_path = 'C:/Users/Asc-user/Documents/YOLO/Y562_train/steel'
#folder_path = 'C:/Users/Asc-user/Desktop/steel'

# 呼叫函式進行繪製和顯示
visualize_bboxes_in_folder(folder_path)


'''
import cv2

def visualize_bbox(image_path, txt_path):
    # 開啟圖片
    image = cv2.imread(image_path)

    # 讀取 txt 檔案內容
    with open(txt_path, 'r') as f:
        lines = f.readlines()

    # 繪製框
    for line in lines:
        line = line.strip().split(' ')
        cls_id = str(line[0])
        x, y, w, h = [float(coord) for coord in line[1:]]
        image_height, image_width = image.shape[:2]

        # 將相對座標轉換為圖片上的絕對座標
        x1 = int((x - w / 2) * image_width)
        y1 = int((y - h / 2) * image_height)
        x2 = int((x + w / 2) * image_width)
        y2 = int((y + h / 2) * image_height)

        # 繪製矩形框
        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(image, str(cls_id), (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # 顯示圖片
    w,h,c  = image.shape
    image = cv2.resize(image, (h//3, w//3), interpolation=cv2.INTER_CUBIC)
    cv2.imshow('Image with Bounding Boxes', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 原始圖片路徑和對應的 txt 檔案路徑
image_path = 'C:/Users/Asc-user/Documents/YOLO/Y562_train/steel/00000_14-41-23_org.png'
txt_path = 'C:/Users/Asc-user/Documents/YOLO/Y562_train/steel/00000_14-41-23_org.txt'

# 呼叫函式進行繪製和顯示
visualize_bbox(image_path, txt_path)
'''

