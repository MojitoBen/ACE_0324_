import sys
sys.path.insert(4, r'C:/Users/Asc-user/Documents/YOLO/darknet')
from darknet import *
import cv2
from sid_cam1 import sid_detect

network, class_names, class_colors = load_network(r"C:/Users/Asc-user/Documents/YOLO/Y562_2PLCM/AI_CS/yolov4-tiny.cfg", 
                                                  r"C:/Users/Asc-user/Documents/YOLO/Y562_2PLCM/AI_CS/obj.data", 
                                                  r"C:/Users/Asc-user/Documents/YOLO/Y562_2PLCM/steel_paint_v4.weights")
#/home/asc/darknet/weights/steel_v14.weights
#/home/asc/darknet/backup/yolov4-tiny_best.weights
raw_list = []
found_text = False
saved_sid_image = None

def darknet_helper(image, width, height):
    darknet_image = make_image(width, height, 3)
    img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    img_resized = cv2.resize(img_rgb, (width, height), interpolation=cv2.INTER_LINEAR)
    img_height, img_width, _ = image.shape
    width_ratio = img_width / width
    height_ratio = img_height / height
    copy_image_from_bytes(darknet_image, img_resized.tobytes())
    detections = detect_image(network, class_names, darknet_image, thresh=0.5)
    free_image(darknet_image)

    return detections, width_ratio, height_ratio

def steel_detect_1(frame):
    image = frame.copy()
    text = ''
    global raw_list
    global saved_sid_image
    raw_list = []
    text_list = []
    sid_image = None
    image_list = [frame, image]
    outimage = frame
    w, h, c = image.shape

    detections, width_ratio, height_ratio = darknet_helper(image, 608, 352)
    detections = sorted(detections, reverse=False, key=lambda s: s[2])

    for label, confidence, bbox in detections:
        left, top, right, bottom = bbox2points(bbox)
        left, top, right, bottom = int(left * width_ratio), int(top * height_ratio), int(right * width_ratio), int(bottom * height_ratio)
        top, bottom, left, right = abs(top), abs(bottom), abs(left), abs(right)
        cv2.rectangle(frame, (left-40, top-20), (right+40, bottom+20), (0, 255, 0), 2) #加框測試用################
        if label == 'sid':    #sid 印刷   hid 手寫
            try:
                sid_image = image[top-20:bottom+20, left-40:right+40]
            except:
                sid_image = image[top:bottom, left:right]
            
            saved_sid_image = sid_image
            image_list[0] = sid_image

            h, w, c = sid_image.shape
            if h > w:
                ro90 = cv2.rotate(sid_image, cv2.ROTATE_90_CLOCKWISE)
                text, image_ = sid_detect(ro90)
                if len(text) >= 6 and text not in text_list:
                    text_list.append(text)
                    outimage = image_

                ro270 = cv2.rotate(sid_image, cv2.ROTATE_90_COUNTERCLOCKWISE)
                text, image_ = sid_detect(ro270)
                if len(text) >= 6 and text not in text_list:
                    text_list.append(text)
                    outimage = image_
            else:
                text, image_ = sid_detect(sid_image)
                if text not in text_list:
                    text_list.append(text)
                    outimage = image_

            if any(text in n for n in raw_list):
                continue
            else:
                raw_list.extend(text_list)
                #image_list[0] = outimage

    if sid_image is not None:
        saved_sid_image = sid_image
    if saved_sid_image is not None:
        image_list[0] = saved_sid_image

    return raw_list, image_list
