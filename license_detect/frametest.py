import cv2
from yolo_all import detect
import numpy as np



img =  cv2.imread('C:\\Users\\Asc-user\\Documents\\YOLO\\darknet\\data\\car2.jpg')
area = [np.array([(0, 0), (1067, 0), (1067, 800), (0, 800)])]

text_list,plate_list, img_r = detect(img,area)
#print(text_list)
#print(plate_list)


cv2.imshow('license_detect',img_r)
cv2.waitKey()
cv2.destroyAllWindows()

