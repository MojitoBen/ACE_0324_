import numpy as np
import sys
sys.path.insert(4, r'C:/Users/Asc-user/Documents/YOLO/darknet')
from darknet import *
import cv2
import glob
import time 
from sid_yolo import sid_detect

#network, class_names, class_colors = load_network(r"C:\Users\user\Documents\darknet-master\train\AI_label\yolov4-tiny.cfg", r"C:\Users\user\Documents\darknet-master\train\AI_label\obj.data", r"C:\Users\user\Documents\darknet-master\weights\AI_label_v3.weights")
#/home/asc/darknet/weights/steel_v14.weights
#/home/asc/darknet/backup/yolov4-tiny_best.weights
network, class_names, class_colors = load_network(r"C:/Users/Asc-user/Documents/YOLO/steel_label/AI_label/yolov4-tiny.cfg", r"C:/Users/Asc-user/Documents/YOLO/steel_label/AI_label/obj.data", r"C:/Users/Asc-user/Documents/YOLO/steel_label/weights/AI_label_v3.weights")

def darknet_helper(image, width, height):
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

def rotate(image, angle, center=None, scale=1.0):

    (h, w) = image.shape[:2]
 
    if center is None:
        center = (w / 2, h / 2)

    M = cv2.getRotationMatrix2D(center, angle, scale)
    rotated = cv2.warpAffine(image, M, (w, h))
 
    return rotated


def steel_detect_1(frame):
    count_steel=0
    image = frame.copy()
    text = ''
    tmpmid = 0
    raw_list = ['','']
    image_list=[frame,frame]
    detections, width_ratio, height_ratio = darknet_helper(image, 608, 352)
    detections = sorted(detections,reverse = False, key = lambda s: s[2])
    #print(detections)
    
    for label,confidence, bbox in detections:
            left, top, right, bottom = bbox2points(bbox)
            left, top, right, bottom = int(left * width_ratio), int(top * height_ratio), int(right * width_ratio), int(bottom * height_ratio)
            top,bottom,left,right = abs(top),abs(bottom),abs(left),abs(right)
            #cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            if label == 'id':
                try:
                       inimage = image[top-10:bottom+10,left-10:right+10]
                except:
                       inimage = image[top:bottom,left:right]
                       
                text_list= []
                jg = inimage.copy()
                
                if  left <850:
                        h,w,c = inimage.shape
                        
                        if  h>w:
                            ro90 = cv2.rotate(inimage,cv2.ROTATE_90_CLOCKWISE)
                            ro60 = rotate(jg, 60)
                            text = sid_detect(ro60)
                            if len(text)>2:
                                text_list.append(text)
                                outimage = ro90
                            
                            ro270 = cv2.rotate(inimage,cv2.ROTATE_90_COUNTERCLOCKWISE)
                            ro240 = rotate(jg, 240)
                            text = sid_detect(ro240)
                            if len(text)>2:
                                text_list.append(text)
                                outimage = ro270
                        else:   
                                ro330 = rotate(jg, -30)
                                text = sid_detect(ro330)
                                text_list.append(text)
                                outimage = inimage
                                
                        raw_list[0] = text_list
                        image_list[0]= outimage
                
        
                else:
                        h,w,c = inimage.shape

                        if  h>w:
                            ro90 = cv2.rotate(inimage,cv2.ROTATE_90_CLOCKWISE)
                            ro60 = rotate(jg, 60)
                            text = sid_detect(ro60)
                            if len(text)>2:
                                text_list.append(text)
                                outimage = ro90
                            
                            ro270 = cv2.rotate(inimage,cv2.ROTATE_90_COUNTERCLOCKWISE)
                            ro240 = rotate(jg, 240)
                            text = sid_detect(ro240)
                            if len(text)>2:
                                text_list.append(text)
                                outimage = ro270
                        else:   
                                ro330 = rotate(jg, -30)
                                text = sid_detect(ro330)
                                text_list.append(text)
                                outimage = inimage
                                
                        raw_list[1] = text_list
                        image_list[1]= outimage
                        
    return raw_list,image_list




def steel_detect_2(frame):
    count_steel=0
    image = frame.copy()
    text = ''
    tmpmid = 0
    outimage=[]
    raw_list=[]
    image_list=[frame,frame]
    detections, width_ratio, height_ratio = darknet_helper(image, 608, 352)
    detections = sorted(detections,reverse = False, key = lambda s: s[2])
    #print(detections)
    
    for label,confidence, bbox in detections:
            left, top, right, bottom = bbox2points(bbox)
            left, top, right, bottom = int(left * width_ratio), int(top * height_ratio), int(right * width_ratio), int(bottom * height_ratio)
            top,bottom,left,right = abs(top),abs(bottom),abs(left),abs(right)
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            if label == 'id':
                try:
                   inimage = image[top-10:bottom+10,left-10:right+10]
                except:
                   inimage = image[top:bottom,left:right]
                h,w,c = inimage.shape
                jg2 = inimage.copy()
                if  h>w:
                    ro90 = cv2.rotate(inimage,cv2.ROTATE_90_CLOCKWISE)
                    ro100 = rotate(jg2, 100)
                    text = sid_detect(ro100)
                    if len(text)>2:
                        raw_list.append(text)
                        outimage = ro90
                    
                    ro270 = cv2.rotate(inimage,cv2.ROTATE_90_COUNTERCLOCKWISE)
                    ro280 = rotate(jg2, 280)
                    text = sid_detect(ro280)
                    if len(text)>2:
                        raw_list.append(text)
                        outimage = ro270
                    
                else:
                    ro10 = rotate(jg2, 10)
                    text = sid_detect(ro10)
                    raw_list.append(text)
                    outimage = inimage
                
             
 
    return raw_list,outimage