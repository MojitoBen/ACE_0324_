import collections
import numpy as np
import copy
import cv2
import glob
import time 
import sys
sys.path.insert(1,r'C:\Users\Asc-user\Documents\YOLO\darknet')   #導入darknet的path
from darknet import load_network, make_image, copy_image_from_bytes,detect_image, free_image, bbox2points


#模型參數載入
network2, class_names2, class_colors2 = load_network(r"C:/Users\Asc-user/Documents/YOLO/darknet/train/num_train/yolov4-tiny.cfg", r"C:/Users\Asc-user/Documents/YOLO/darknet/train/num_train/obj.data", r"C:/Users/Asc-user/Documents/YOLO/darknet/weights/num_tv1_gray.weights")
network, class_names, class_colors = load_network(r"C:/Users\Asc-user/Documents/YOLO/darknet/train/car_plate/yolov4-tiny.cfg", r"C:/Users\Asc-user/Documents/YOLO/darknet/train/car_plate/obj.data", r"C:/Users/Asc-user/Documents/YOLO/darknet/weights/plate_tv5.weights")


def ID2text(images,text):    #辨識縮圖
  
    def darknet_helper(images, width, height):
        darknet_image = make_image(width, height, 3)
        img_rgb = cv2.cvtColor(images, cv2.COLOR_BGR2RGB)
        img_resized = cv2.resize(img_rgb, (width, height),interpolation=cv2.INTER_LINEAR)

        # get image ratios to convert bounding boxes to proper size
        img_height, img_width, _ = images.shape
        width_ratio = img_width/width
        height_ratio = img_height/height

        # run model on darknet style image to get detections
        copy_image_from_bytes(darknet_image, img_resized.tobytes())
        detections = detect_image(network2, class_names2, darknet_image, thresh=0.7)
        free_image(darknet_image)
        return detections, width_ratio, height_ratio    

    detections, width_ratio, height_ratio = darknet_helper(images, 608, 608)
    table = []
    text = ''
    dist = 0
    temp=0
    lenght=0
    detections = sorted(detections, key = lambda s: s[2])  #排序車牌字從左到右
 
    for label, confidence, bbox in detections:
        left, top, right, bottom = bbox2points(bbox)
        left, top, right, bottom = int(left * width_ratio), int(top * height_ratio), int(right * width_ratio), int(bottom * height_ratio)
        #label, confidence, list(bbox)
        table.append(label)
        table.append(confidence)
        table.append(int(bbox[0]))
    

    table = np.array(table)    #重組號碼╴分數高的位罝不差10px內就取最高分的
    lenght = int(len(table)/3)

    table = table.reshape(lenght, 3)

    for i in range(len(table)):
        dist = int(table[i][2]) - temp
        if dist > 10:
            temp = int(table[i][2])
            text = text+str(table[i][0])
        else:
            if table[i][1] > table[i-1][1]:
                text = text.replace(table[i-1][0],table[i][0])

    return text





def darknet_helper(image, width, height):     #AI的模型運算
    darknet_image = make_image(width, height, 3)
    img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    img_resized = cv2.resize(img_rgb, (width, height),interpolation=cv2.INTER_LINEAR)
    img_height, img_width, _ = image.shape
    width_ratio = img_width/width
    height_ratio = img_height/height
    copy_image_from_bytes(darknet_image, img_resized.tobytes())
    detections = detect_image(network, class_names, darknet_image, thresh=0.5)
    free_image(darknet_image)

    return detections, width_ratio, height_ratio



#def detect(img,area):
def detect(img, area):
    text_list = []
    images_list = []
    num_plates = 0 #框住的車牌

    # 將之前的設定範圍功能先註解掉，如果需要可以再加上去
    im = np.zeros(img.shape[:2], dtype="uint8")  # 設計辨識範圍
    cv2.polylines(im, area, 1, 255)
    cv2.fillPoly(im, area, 255)
    img = cv2.bitwise_and(img, img, mask=im)
    
    # 修改以下兩行，改成使用較小的縮圖進行辨識
    detections, width_ratio, height_ratio = darknet_helper(img, 416, 416)
    # detections, width_ratio, height_ratio = darknet_helper(img, 832, 832)

    detections = sorted(detections, reverse=False, key=lambda s: s[2])
    #print("license : ", len(detections))
    if len(detections) > 0:
        for label, confidence, bbox in detections:
            left, top, right, bottom = bbox2points(bbox)
            left, top, right, bottom = (
                int(left * width_ratio),
                int(top * height_ratio),
                int(right * width_ratio),
                int(bottom * height_ratio),
            )
            top, bottom, left, right = abs(top), abs(bottom), abs(left), abs(right)
            cv2.rectangle(img, (left, top), (right, bottom), (255, 0, 0), 2)
            # 修改以下三行，將框選到的車牌裁剪下來再進行後續處理
            plate_img = img[max(0, top):min(bottom, img.shape[0]), max(0, left):min(right, img.shape[1])]
            gray = cv2.cvtColor(plate_img, cv2.COLOR_BGR2GRAY)
            gray = cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB)

            # 以下部分保留原本的程式碼，用來判斷是否需要將黑白圖片反轉顏色
            text = ID2text(gray, "")
            if len(text) < 5:
                gray = 255 - gray
                text = ID2text(gray, "")

            # 將處理後的結果存入相應的列表中
            text_list.append(text)
            images_list.append(plate_img)
            
            # 每處理到一張車牌就將計數器加1
            num_plates += 1

    # 修改以下部分，如果偵測到的車牌數量為0，則直接回傳空的列表
    if num_plates == 0:
        return text_list, images_list, img

    # 否則回傳結果
    return text_list, images_list, img


