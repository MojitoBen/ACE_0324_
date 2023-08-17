import sys
sys.path.insert(4, r'C:/Users/Asc-user/Documents/YOLO/darknet')
from darknet import *
import cv2
import math

network, class_names, class_colors = load_network(r"C:/Users/Asc-user/Documents/YOLO/Y562_2PLCM/CS_ID/yolov4-tiny.cfg", 
                                                  r"C:/Users/Asc-user/Documents/YOLO/Y562_2PLCM/CS_ID/obj.data", 
                                                  r"C:/Users/Asc-user/Documents/YOLO/Y562_2PLCM/cs_id_v12.weights")

def darknet_helper(image, width, height):
    if image is None or image.size == 0:  # 檢查圖像是否為空
        return [], 0, 0

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


    return detections, width_ratio, height_ratio
def calculate_angle(left, top, right, bottom):
    width = right - left
    height = bottom - top

    if width != 0:
        slope = height / width
        angle = math.degrees(math.atan(slope))
        if angle < 0:
            angle += 180
        return angle
    else:
        if height >= 0:
            return 90
        else:
            return 270
        
def sid_detect(image):
    text = ''
    size = [image.shape[1], image.shape[0]]
    detections, width_ratio, height_ratio = darknet_helper(image, 352, 160)
    detections = sorted(detections, reverse=False, key=lambda s: s[2])
    
    confidence_sum = 0
    num_confidences = 0
    avg_confidence = None  # 提前初始化avg_confidence為None

    try:
        for label, confidence, bbox in detections:
            left, top, right, bottom = bbox2points(bbox)
            left, top, right, bottom = int(left * width_ratio), int(top * height_ratio), int(right * width_ratio), int(bottom * height_ratio)
            top, bottom, left, right = abs(top), abs(bottom), abs(left), abs(right)
            #cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 255), 2) #加框測試用################
            text += label
            if label.isdigit():
                confidence_sum += float(confidence)
                num_confidences += 1

        if num_confidences > 0:
            avg_confidence = confidence_sum / num_confidences
    except Exception as e:
        print(f"Error during detection: {e}")
        avg_confidence = 0  # 預設值為0

    if avg_confidence is not None and round(avg_confidence) < 90:
        text = ''
        image = cv2.rotate(image, cv2.ROTATE_180)
        detections, _, _ = darknet_helper(image, 352, 160)
        detections = sorted(detections, reverse=False, key=lambda s: s[2])
        for label,confidence, bbox in detections:
            left, top, right, bottom = bbox2points(bbox)
            left, top, right, bottom = int(left * width_ratio), int(top * height_ratio), int(right * width_ratio), int(bottom * height_ratio)
            top,bottom,left,right = abs(top),abs(bottom),abs(left),abs(right)
            text += label

    return text


#可以考慮不用list的方式，偵測目標只有一個
#round(avg_confidence) < 90 可能得依照訓練後的噴字權重還有手寫權重做調整
