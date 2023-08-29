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
image_path = 'C:/Users/Asc-user/Documents/YOLO/Y562_train/steel3/NVR_ch1_main_20230815093954_20230815094030_id.png'
txt_path = 'C:/Users/Asc-user/Documents/YOLO/Y562_train/steel3/NVR_ch1_main_20230815093954_20230815094030_id.txt'

# 呼叫函式進行繪製和顯示
visualize_bbox(image_path, txt_path)
