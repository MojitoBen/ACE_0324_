import numpy as np
import cv2
from threading import Thread
from queue import Queue
import time
import sys
sys.path.insert(4, r'C:/Users/Asc-user/Documents/YOLO/darknet')
from darknet import *


#模型參數載入
#network2, class_names2, class_colors2 = load_network(r"C:/Users\Asc-user/Documents/YOLO/darknet/train/num_train/yolov4-tiny.cfg", r"C:/Users\Asc-user/Documents/YOLO/darknet/train/num_train/obj.data", r"C:/Users/Asc-user/Documents/YOLO/darknet/weights/num_tv1_gray.weights")
#network, class_names, class_colors = load_network(r"C:/Users\Asc-user/Documents/YOLO/darknet/train/car_plate/yolov4-tiny.cfg", r"C:/Users\Asc-user/Documents/YOLO/darknet/train/car_plate/obj.data", r"C:/Users/Asc-user/Documents/YOLO/darknet/weights/plate_tv5.weights")

yolo_weights = 'C:\\Users\\Asc-user\\Documents\\YOLO\\darknet\\yolov4.weights'
yolo_cfg = 'C:\\Users\\Asc-user\\Documents\\YOLO\\darknet\\cfg\\yolov4.cfg'
data = 'C:\\Users\\Asc-user\\Documents\\YOLO\\darknet\\cfg\\coco.data'
net, class_name , colors  = load_network(yolo_cfg, data, yolo_weights)

confThreshold = 0.5  #Confidence threshold
nmsThreshold = 0.4   #Non-maximum suppression threshold，機率門檻，0.4以下不顯示在畫面

def darknet_helper(image, width, height):     #AI的模型運算
    darknet_image = make_image(width, height, 3)
    img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    img_resized = cv2.resize(img_rgb, (width, height),interpolation=cv2.INTER_LINEAR)
    img_height, img_width, _ = image.shape
    width_ratio = img_width/width
    height_ratio = img_height/height
    copy_image_from_bytes(darknet_image, img_resized.tobytes())
    detections = detect_image(net,class_name, darknet_image, thresh=0.5)
    free_image(darknet_image)

    return detections, width_ratio, height_ratio


def detect(img, area):
    car_centers = []  # 儲存所有車子中心點座標的列表
    images_list = []

    classesFile = "C:\\Users\\Asc-user\\Documents\\YOLO\\darknet\\cfg\\coco.names"
    classes = None
    with open(classesFile, 'rt') as f:
        classes = f.read().rstrip('\n').split('\n')
    #只取coco列表中2汽車3機車7卡車，有需要再加
    valid_classes = [classes[2], classes[3], classes[7]]
    #只取coco列表中2汽車5公車7卡車，有需要再加
    #valid_classes = [classes[2], classes[5], classes[7]]
    
    # 將之前的設定範圍功能先註解掉，如果需要可以再加上去
    im = np.zeros(img.shape[:2], dtype="uint8")  # 設計辨識範圍
    cv2.polylines(im, area, 1, 255)
    cv2.fillPoly(im, area, 255)
    img = cv2.bitwise_and(img, img, mask=im)

    detections, width_ratio, height_ratio = darknet_helper(img, 416, 416)

    detections = sorted(detections, reverse=False, key=lambda s: s[2])
    if len(detections) > 0:
        for label, confidence, bbox in detections: #每一個被偵測到的物件
            if label in valid_classes:
                class_index = valid_classes.index(label)
                left, top, right, bottom = bbox2points(bbox)
                left, top, right, bottom = (
                    int(left * width_ratio),
                    int(top * height_ratio),
                    int(right * width_ratio),
                    int(bottom * height_ratio),
                )
                center_x = (left + right) // 2  # 計算車子中心點的 x 座標
                center_y = (top + bottom) // 2  # 計算車子中心點的 y 座標

                #check_stopped(center_x, center_y) 要排除非移動車，失敗

                car_centers.append((center_x, center_y))  # 將座標加入列表
                top, bottom, left, right = abs(top), abs(bottom), abs(left), abs(right)
                cv2.rectangle(img, (left, top), (right, bottom), (0, 0, 255), 2)
                # 修改以下三行，將框選到的車裁剪下來再進行後續處理
                car_img = img[max(0, top):min(bottom, img.shape[0]), max(0, left):min(right, img.shape[1])]
                gray = cv2.cvtColor(car_img, cv2.COLOR_BGR2GRAY)
                gray = cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB)

                images_list.append(car_img)

    # 畫出所有車子中心點
    if len(car_centers) > 0:
        for center in car_centers:
            center_x, center_y = center
            cv2.circle(img, (center_x, center_y), 5, (0, 0, 255), -1)
    
        
    # 修改以下部分，如果偵測到的車數量為0，則直接回傳空的列表
    num_car = len(images_list)
    if num_car == 0:
        return images_list, img, car_centers

    # 否則回傳結果
    return images_list, img, car_centers

def draw_text(img, text, pos, font_scale=1, thickness=3, color=(255, 0, 255)):
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_thickness = int(thickness)
    text_size, _ = cv2.getTextSize(text, font, font_scale, font_thickness)
    text_x = pos[0] - text_size[0] // 2
    text_y = pos[1] + text_size[1] // 2
    cv2.putText(img, text, (text_x, text_y), font, font_scale, color, font_thickness, cv2.LINE_AA)

'''
def check_stopped(center_x, center_y):
    # 記錄前一次的座標
    prev_x = center_x
    prev_y = center_y
    # 設定連續判斷的次數
    num_checks = 10
    # 建立一個Queue來存放每次判斷結果
    result_queue = Queue()
    
    # 定義子執行緒的函數，進行連續判斷
    def check_loop():
        nonlocal prev_x, prev_y
        for i in range(num_checks):
            time.sleep(0.1)  # 等待0.1秒，避免過快地進行連續判斷
            curr_x, curr_y = center_x, center_y  # 取得目前的座標
            print("curr_x",curr_x)
            print("curr_y", curr_y)
            #判斷目前的座標是否和前一次相同
            print("prev_x",prev_x)
            print("prev_y",prev_y)
            if abs(curr_x - prev_x) < 10 and abs(curr_y - prev_y) < 10:
                result_queue.put(True)  # 如果是，則放入True
            else:
                result_queue.put(False)  # 如果不是，則放入False
            
            # 更新前一次的座標
            prev_x = curr_x
            prev_y = curr_y
            print()
    
    # 建立子執行緒，進行連續判斷
    thread = Thread(target=check_loop)
    thread.start()
    
    # 等待所有判斷結果都被放入Queue中
    thread.join()
    
    # 檢查所有判斷結果是否都為True
    for i in range(num_checks):
        if not result_queue.get():
            # 如果有任何一次判斷結果為False，則代表車子沒有停下來，回傳座標值
            return center_x, center_y
'''