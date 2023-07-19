import numpy as np
import sys
sys.path.insert(0, r'C:\Users\user\Documents\darknet-master')
from darknet import *
import cv2
import glob
import time 
from sid_yolo import sid_detect

network, class_names, class_colors = load_network(r"C:\Users\user\Documents\darknet-master\train\AI_label\yolov4-tiny.cfg", r"C:\Users\user\Documents\darknet-master\train\AI_label\obj.data", r"C:\Users\user\Documents\darknet-master\weights\AI_label_v3.weights")
#/home/asc/darknet/weights/steel_v14.weights
#/home/asc/darknet/backup/yolov4-tiny_best.weights

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
                print("confidence",confidence)
                if  left <850:
                        h,w,c = inimage.shape

                        if  h>w:
                            ro90 = cv2.rotate(inimage,cv2.ROTATE_90_CLOCKWISE)
                            text = sid_detect(ro90)
                            if len(text)>2:
                                text_list.append(text)
                                outimage = ro90
                            
                            ro270 = cv2.rotate(inimage,cv2.ROTATE_90_COUNTERCLOCKWISE)
                            text = sid_detect(ro270)
                            if len(text)>2:
                                text_list.append(text)
                                outimage = ro270
                        else:   
                                # Check confidence threshold here
                            if confidence < 0.7:  
                                image = cv2.rotate(inimage, cv2.ROTATE_180)
                                text = sid_detect(image)
                                text_list.append(text)
                                outimage = image
                            else:
                                text = sid_detect(inimage)
                                text_list.append(text)
                                outimage = inimage
                                
                        raw_list[0] = text_list
                        image_list[0]= outimage
                
        
                else:
                        h,w,c = inimage.shape

                        if  h>w:
                            ro90 = cv2.rotate(inimage,cv2.ROTATE_90_CLOCKWISE)
                            text = sid_detect(ro90)
                            if len(text)>2:
                                text_list.append(text)
                                outimage = ro90
                            
                            ro270 = cv2.rotate(inimage,cv2.ROTATE_90_COUNTERCLOCKWISE)
                            text = sid_detect(ro270)
                            if len(text)>2:
                                text_list.append(text)
                                outimage = ro270
                        else:   
                            if confidence < 0.7:  
                                image = cv2.rotate(inimage, cv2.ROTATE_180)
                                text = sid_detect(image)
                                text_list.append(text)
                                outimage = image
                            else:
                                #加入if_confidence_180 : image = cv2.rotate(inimage, cv2.ROTATE_180)
                                text = sid_detect(inimage)
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
            #cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            if label == 'id':
                try:
                   inimage = image[top-10:bottom+10,left-10:right+10]
                except:
                   inimage = image[top:bottom,left:right]
                h,w,c = inimage.shape

                if  h>w:
                    ro90 = cv2.rotate(inimage,cv2.ROTATE_90_CLOCKWISE)
                    text = sid_detect(ro90)
                    if len(text)>2:
                        raw_list.append(text)
                        outimage = ro90
                    
                    ro270 = cv2.rotate(inimage,cv2.ROTATE_90_COUNTERCLOCKWISE)
                    text = sid_detect(ro270)
                    if len(text)>2:
                        raw_list.append(text)
                        outimage = ro270
                    
                else:
                    text = sid_detect(inimage)
                    raw_list.append(text)
                    outimage = inimage
                
             
 
    return raw_list,outimage