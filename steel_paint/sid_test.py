import sys
sys.path.insert(4, r'C:/Users/Asc-user/Documents/YOLO/darknet')
from darknet import *
import cv2
import math

network, class_names, class_colors = load_network(r"C:/Users/Asc-user/Documents/YOLO/Y562_2PLCM/CS_ID/yolov4-tiny.cfg", 
                                                  r"C:/Users/Asc-user/Documents/YOLO/Y562_2PLCM/CS_ID/obj.data", 
                                                  r"C:/Users/Asc-user/Documents/YOLO/Y562_2PLCM/cs_id_v12.weights")

text = ''

def darknet_helper(image, width, height):
    darknet_image = make_image(width, height, 3)
    img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    img_resized = cv2.resize(img_rgb, (width, height), interpolation=cv2.INTER_LINEAR)
    img_height, img_width, _ = image.shape
    width_ratio = img_width / width
    height_ratio = img_height / height
    copy_image_from_bytes(darknet_image, img_resized.tobytes())
    detections = detect_image(network, class_names, darknet_image, thresh=0.3)
    free_image(darknet_image)

    return detections, width_ratio, height_ratio

def sid_detect(image):
    global text
    detections, width_ratio, height_ratio = darknet_helper(image, 352, 160)
    detections = sorted(detections, reverse=False, key=lambda s: s[2])

    for label, confidence, bbox in detections:
        left, top, right, bottom = bbox2points(bbox)
        left, top, right, bottom = int(left * width_ratio), int(top * height_ratio), int(right * width_ratio), int(bottom * height_ratio)
        top, bottom, left, right = abs(top), abs(bottom), abs(left), abs(right)
        cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 255), 2) #加框測試用################
        #cv2.putText(image, text, (left-20, top-20), cv2.FONT_HERSHEY_SIMPLEX,5, (0, 255, 255), 10, cv2.LINE_AA)
        text += label

    return text


frame = cv2.imread(r'C:/Users/Asc-user/Desktop/1234.png')
w, h, c = frame.shape

while True:

    text = sid_detect(frame)
    print(text)

    resized_frame = cv2.resize(frame, (h, w), interpolation=cv2.INTER_CUBIC)
    cv2.imshow('test', resized_frame)
    if cv2.waitKey(1) == ord('q'):
        break