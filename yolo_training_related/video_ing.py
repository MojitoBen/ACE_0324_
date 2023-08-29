# autolabel steel 放影片自動產生鋼捲+標籤圖


import numpy as np
import sys
sys.path.insert(4, r'C:/Users/Asc-user/Documents/YOLO/darknet')
from darknet_noWinmode import *
import cv2
from datetime import datetime

def darknet_helper(image, width, height):
    darknet_image = make_image(width, height, 3)
    img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    img_resized = cv2.resize(img_rgb, (width, height),interpolation=cv2.INTER_LINEAR)
    img_height, img_width, _ = image.shape
    width_ratio = img_width/width
    height_ratio = img_height/height
    copy_image_from_bytes(darknet_image, img_resized.tobytes())
    detections = detect_image(network, class_names, darknet_image, thresh=0.6)
    free_image(darknet_image)

    return detections, width_ratio, height_ratio

network, class_names, class_colors = load_network(r"C:/Users/Asc-user/Documents/YOLO/Y562_2PLCM/AI_CS/yolov4-tiny.cfg", 
                                                  r"C:/Users/Asc-user/Documents/YOLO/Y562_2PLCM/AI_CS/obj.data", 
                                                  r"C:/Users/Asc-user/Documents/YOLO/Y562_2PLCM/steel_shidv3.weights")
count=0
total=-1
pos_tmp = 0
pos2_tmp = 0

cap = cv2.VideoCapture('C:/Users/Asc-user/Documents/YOLO/Y562_train/no_sid/5145113.mp4')

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        cap.release()
        break
    
    

    count += 1 

    #if count%300 == 0:   
    if count%100 == 0: 
        count = 0
        detections, width_ratio, height_ratio = darknet_helper(frame, 416, 416)
        detections = sorted(detections,reverse = False, key = lambda s: s[2][1])
        idtotal = len(detections) 
        total+=1
        timestamp = datetime.now().strftime("%H-%M-%S")
        for label,confidence, bbox in detections:
                left, top, right, bottom = bbox2points(bbox)
                left, top, right, bottom = int(left * width_ratio), int(top * height_ratio), int(right * width_ratio), int(bottom * height_ratio)
                top,bottom,left,right = abs(top),abs(bottom),abs(left),abs(right)
                if label == 'steel': 
                    if abs(left - pos_tmp) > 10 or abs(left - pos_tmp) < 10:
                        pos_tmp = left
                        cv2.imwrite('C:/Users/Asc-user/Documents/YOLO/Y562_train/sid2/%05d_%s_org.png' % (total, timestamp), frame)
                '''
                if label == 'sid':
                    if abs(left - pos2_tmp) > 10 or abs(left - pos2_tmp) < 10:
                        pos2_tmp = left
                        capture = frame[top:bottom, left:right]
                        cv2.imwrite('C:/Users/Asc-user/Documents/YOLO/Y562_train/sid/%06d_%s_id.png' % (total, timestamp), capture)
                idtotal -= 1
                '''
                                           
        if total == 99999:
           total = 0