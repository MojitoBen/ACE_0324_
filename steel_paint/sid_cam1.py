import sys
sys.path.insert(0, r"/home/asc/Desktop/darknet-master")
from darknet import *
import cv2
import math

network, class_names, class_colors = load_network(r"/home/asc/Desktop/Y562_0815/weight/sid_train/yolov4-tiny.cfg", 
                                                  r"/home/asc/Desktop/Y562_0815/weight/sid_train/obj.data", 
                                                  r"/home/asc/Desktop/Y562_0815/weight/shid_num_v3.weights")

def darknet_helper(image, width, height):
    darknet_image = make_image(width, height, 3)
    img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    img_resized = cv2.resize(img_rgb, (width, height), interpolation=cv2.INTER_LINEAR)
    img_height, img_width, _ = image.shape
    width_ratio = img_width / width
    height_ratio = img_height / height
    copy_image_from_bytes(darknet_image, img_resized.tobytes())
    detections = detect_image(network, class_names, darknet_image, thresh=0.4)
    free_image(darknet_image)

    return detections, width_ratio, height_ratio

def rotate_image(image, angle):
    h, w = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated_image = cv2.warpAffine(image, M, (w, h))      
    return rotated_image

def sid_detect(image):
    text = ''
    #size = [image.shape[1], image.shape[0]]
    # 原始圖片辨識
    def calculate_avg_confidence(detections):
        confidence_sum = 0
        num_confidences = 0

        for label, confidence, bbox in detections:
            confidence_sum += float(confidence)
            num_confidences += 1

        if num_confidences > 0:
            avg_confidence = confidence_sum / num_confidences
        else:
            avg_confidence = 0.0

        return avg_confidence


    # 原始圖片辨識
    detections, width_ratio, height_ratio = darknet_helper(image, 352, 160)
    detections = sorted(detections, reverse=False, key=lambda s: s[2])
    avg_confidence_original = calculate_avg_confidence(detections)  # 計算原始圖片的平均信心指數

    # 左轉30度辨識
    image_rotated_left = rotate_image(image, 30)
    detections_left, _, _ = darknet_helper(image_rotated_left, 352, 160)
    detections_left = sorted(detections_left, reverse=False, key=lambda s: s[2])
    avg_confidence_left = calculate_avg_confidence(detections_left)  # 計算左轉30度的平均信心指數

    # 右轉30度辨識
    image_rotated_right = rotate_image(image, -30)
    detections_right, _, _ = darknet_helper(image_rotated_right, 352, 160)
    detections_right = sorted(detections_right, reverse=False, key=lambda s: s[2])
    avg_confidence_right = calculate_avg_confidence(detections_right)  # 計算右轉30度的平均信心指數

    # 選擇最佳方向的辨識結果
    if avg_confidence_left >= avg_confidence_original and avg_confidence_left >= avg_confidence_right:
        best_detections = detections_left

    elif avg_confidence_right >= avg_confidence_original and avg_confidence_right >= avg_confidence_left:
        best_detections = detections_right

    else:
        best_detections = detections

    confidence_sum = 0
    num_confidences = 0
    avg_confidence = 0
    
    for label, confidence, bbox in best_detections:
        left, top, right, bottom = bbox2points(bbox)
        left, top, right, bottom = int(left * width_ratio), int(top * height_ratio), int(right * width_ratio), int(bottom * height_ratio)
        top, bottom, left, right = abs(top), abs(bottom), abs(left), abs(right)
        #cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 255), 2) #加框測試用################
        #cv2.putText(image, text, (left-20, top-20), cv2.FONT_HERSHEY_SIMPLEX,5, (0, 255, 255), 10, cv2.LINE_AA)
        text += label
        if label.isdigit():
            confidence_sum += float(confidence)
            num_confidences += 1

        if num_confidences > 0:
            avg_confidence = confidence_sum / num_confidences
        else:
            avg_confidence = 0.0
    
    if avg_confidence is not None and round(avg_confidence) < 60:
        text = ''
        image = cv2.rotate(image, cv2.ROTATE_180)
        detections, _, _ = darknet_helper(image, 352, 160)
        detections = sorted(detections, reverse=False, key=lambda s: s[2])
        for label,confidence, bbox in detections:
            left, top, right, bottom = bbox2points(bbox)
            left, top, right, bottom = int(left * width_ratio), int(top * height_ratio), int(right * width_ratio), int(bottom * height_ratio)
            top,bottom,left,right = abs(top),abs(bottom),abs(left),abs(right)
            text += label
            
    return text, image



'''
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
            '''
