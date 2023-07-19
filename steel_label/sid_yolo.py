import numpy as np
import sys
sys.path.insert(0, r'C:\Users\user\Documents\darknet-master')
from darknet import *
import cv2
import glob
import time 

network, class_names, class_colors = load_network(r"C:\Users\user\Documents\darknet-master\train\CS_label\yolov4-tiny.cfg", r"C:\Users\user\Documents\darknet-master\train\CS_label\obj.data", r"C:\Users\user\Documents\darknet-master\weights\cs_label_v6.weights")

def darknet_helper(image, width, height):
    darknet_image = make_image(width, height, 3)
    img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    img_resized = cv2.resize(img_rgb, (width, height),interpolation=cv2.INTER_LINEAR)
    img_height, img_width, _ = image.shape
    width_ratio = img_width/width
    height_ratio = img_height/height
    copy_image_from_bytes(darknet_image, img_resized.tobytes())
    detections = detect_image(network, class_names, darknet_image, thresh=0.3)
    free_image(darknet_image)

    return detections, width_ratio, height_ratio
       

def sid_detect(image):
        text=''
        
        size = [image.shape[1],image.shape[0]]
        detections, width_ratio, height_ratio = darknet_helper(image, 352, 160)
        detections = sorted(detections,reverse = False, key = lambda s: s[2])
        
        for label,confidence, bbox in detections:
            left, top, right, bottom = bbox2points(bbox)
            left, top, right, bottom = int(left * width_ratio), int(top * height_ratio), int(right * width_ratio), int(bottom * height_ratio)
            top,bottom,left,right = abs(top),abs(bottom),abs(left),abs(right)
            text = text+label
        #cv2.imshow(text,image)
        return text
