import sys
sys.path.insert(4, r'C:/Users/Asc-user/Documents/YOLO/darknet')
from darknet import *
import cv2
import time
import logging
import queue
import threading

network, class_names, class_colors = load_network(r"C:/Users/Asc-user/Documents/YOLO/Y562_2PLCM/AI_CS/yolov4-tiny.cfg", 
                                                  r"C:/Users/Asc-user/Documents/YOLO/Y562_2PLCM/AI_CS/obj.data", 
                                                  r"C:/Users/Asc-user/Documents/YOLO/Y562_2PLCM/steel_paint_v3.weights")
def darknet_helper(image, width, height):
    darknet_image = make_image(width, height, 3)
    img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    img_resized = cv2.resize(img_rgb, (width, height), interpolation=cv2.INTER_LINEAR)
    img_height, img_width, _ = image.shape
    width_ratio = img_width / width
    height_ratio = img_height / height
    copy_image_from_bytes(darknet_image, img_resized.tobytes())
    detections = detect_image(network, class_names, darknet_image, thresh=0.6)
    free_image(darknet_image)

    return detections, width_ratio, height_ratio

def steel_detect_1(frame):
    image = frame.copy()
    text = ''
    w, h, c = image.shape

    detections, width_ratio, height_ratio = darknet_helper(image, 608, 352)
    detections = sorted(detections, reverse=False, key=lambda s: s[2])

    for label, confidence, bbox in detections:
        left, top, right, bottom = bbox2points(bbox)
        left, top, right, bottom = int(left * width_ratio), int(top * height_ratio), int(right * width_ratio), int(bottom * height_ratio)
        top, bottom, left, right = abs(top), abs(bottom), abs(left), abs(right)
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2) #加框測試用################


frame_img = cv2.imread(r'C:/Users/Asc-user/Desktop/12345.png')

cap = cv2.VideoCapture(r'C:/Users/Asc-user/Desktop/123.mp4')
ret, frame = cap.read()



h, w, c = frame.shape
frame = cv2.resize(frame, (1600, 900), interpolation=cv2.INTER_CUBIC)
# print(frame.shape)
# cv2.imshow("test", frame)
# cv2.waitKey(0)

#------
frame = cv2.imread(r'C:/Users/Asc-user/Desktop/frame_img.jpg')
frame2 = cv2.imread(r'C:/Users/Asc-user/Desktop/frame_video.jpg')


while True:

    # cv2.imwrite(r'C:/Users/Asc-user/Desktop/frame_img.jpg', frame_img)
    # cv2.imwrite(r'C:/Users/Asc-user/Desktop/frame_video.jpg', frame)
    # exit()

    steel_detect_1(frame)
    steel_detect_1(frame2)

    resized_frame = cv2.resize(frame, (w //2, h//2), interpolation=cv2.INTER_CUBIC)
    cv2.imshow('test', resized_frame)
    # if cv2.waitKey(1) == ord('q'):
    #     break
    cv2.waitKey(0)

    resized_frame = cv2.resize(frame2, (w //2, h//2), interpolation=cv2.INTER_CUBIC)
    cv2.imshow('test', resized_frame)
    # if cv2.waitKey(1) == ord('q'):
    #     break
    cv2.waitKey(0)