import cv2
import numpy as np
img = cv2.imread("Cutie.png", 1)
cv2.imshow("before", img)

for i in range(0,50):
    for j in range(0,100):
        for k in range(0,3):
            img.itemset((i,j,k), 255) #白色
cv2.imshow("after",img)
cv2.waitKey(3000)
cv2.destroyAllWindows()