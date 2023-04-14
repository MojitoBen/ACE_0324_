#影像透視，將矩形對映為任意四邊形
import cv2
import numpy as np
img = cv2.imread("Cutie.png")
rows,cols = img.shape[:2]

#4個頂點位子
pts1 = np.float32([[150,50],[400,50],[60,450],[310,450]])
pts2 = np.float32([[50,50],[rows-50,50],[50,cols-50],[rows-50,cols-50]])

M = cv2.getPerspectiveTransform(pts1, pts2)
dst = cv2.warpPerspective(img,M,(cols,rows))
cv2.imshow("original", img)
cv2.imshow("result", dst)
cv2.waitKey()
cv2.destroyAllWindows()