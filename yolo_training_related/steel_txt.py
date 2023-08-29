# autolabel steel


import numpy as np
import sys
sys.path.insert(0, r'C:/Users/Asc-user/Documents/YOLO/darknet')
from darknet_noWinmode import *
import cv2
import glob
import time 
import copy
import os
import signal

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


path = 'C:/Users/Asc-user/Documents/YOLO/Y562_train/steel3/'
for level_1 in os.listdir(path):
    image = cv2.imread(path+level_1)
    size = [image.shape[1],image.shape[0]]
    detections, width_ratio, height_ratio = darknet_helper(image, 416, 416)
    detections = sorted(detections,reverse = False, key = lambda s: s[2][1])
    print(detections)
    for label,confidence, bbox in detections:
            left, top, right, bottom = bbox2points(bbox)
            left, top, right, bottom = int(left * width_ratio), int(top * height_ratio), int(right * width_ratio), int(bottom * height_ratio)
            top,bottom,left,right = abs(top),abs(bottom),abs(left),abs(right)
            if label == 'steel':
                label = '2'
            elif label == 'sid':
                label = '0'
            else:
                 label = '1'
                
            dw = 1./size[0]
            dh = 1./size[1]
            #print(dw,dh)
            x = (left + right)/2.0
            y = (top + bottom)/2.0
            w = right - left
            h = bottom - top
            x = x*dw
            w = w*dw
            y = y*dh
            h = h*dh
            id_path = path+level_1[:-4]
            write = open(id_path+'.txt', 'a')
            print(label ,x,y,w,h,file=write)

            write.close() 
print('done')
