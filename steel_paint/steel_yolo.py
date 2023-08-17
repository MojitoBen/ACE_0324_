import sys
sys.path.insert(4, r'C:/Users/Asc-user/Documents/YOLO/darknet')
from darknet import *
import cv2
from sid_yolo import sid_detect

network, class_names, class_colors = load_network(r"C:/Users/Asc-user/Documents/YOLO/Y562_2PLCM/AI_CS/yolov4-tiny.cfg", 
                                                  r"C:/Users/Asc-user/Documents/YOLO/Y562_2PLCM/AI_CS/obj.data", 
                                                  r"C:/Users/Asc-user/Documents/YOLO/Y562_2PLCM/steel_shidv3.weights")
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
    image = frame.copy()
    text = ''
    raw_list = []
    text_list = []
    image_list=[]
    detections, width_ratio, height_ratio = darknet_helper(image, 608, 352)
    detections = sorted(detections,reverse = False, key = lambda s: s[2])
    #print(detections)
    
    for label,confidence, bbox in detections:
            left, top, right, bottom = bbox2points(bbox)
            left, top, right, bottom = int(left * width_ratio), int(top * height_ratio), int(right * width_ratio), int(bottom * height_ratio)
            top,bottom,left,right = abs(top),abs(bottom),abs(left),abs(right)
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2) #加框測試用################
            if label == 'sid' or label == 'hid':    #sid 印刷   hid 手寫
            
                try:
                    frame = frame[top-20:bottom+20,left-20:right+20]
                except:
                    frame = image[top:bottom,left:right]
                    pass           	
                h,w,c = frame.shape
                
                if  h>w:
                        ro90 = cv2.rotate(frame,cv2.ROTATE_90_CLOCKWISE)
                        text = sid_detect(ro90)
                        if len(text)>2:
                            text_list.append(text)
                            outimage = ro90
                        
                        ro270 = cv2.rotate(frame,cv2.ROTATE_90_COUNTERCLOCKWISE)
                        text = sid_detect(ro270)
                        if len(text)>2:
                            text_list.append(text)
                            outimage = ro270
                else:   
                    text = sid_detect(frame)
                    text_list.append(text)
                    outimage = frame
                    
                if text_list not in raw_list:
                    raw_list.append(text_list)
                    image_list.append(outimage)
                
    return raw_list,image_list
