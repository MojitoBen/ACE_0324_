import numpy as np
import cv2
o = cv2.imread("C:\\Users\\User\\Desktop\\Ben\\AI\\Cutie.png")
kernel = np.ones((9,9), np.float32)/81
r2D = cv2.filter2D(o, -1, kernel)
blur= cv2.blur(o,(5,5))
box = cv2.boxFilter(o, -1, (5,5))
Gaus = cv2.GaussianBlur(o,(5,5), 0, 0)
median = cv2.medianBlur(o, 3)
bilateral = cv2.bilateralFilter(o, 25, 100, 100)
cv2.imshow("img", o)
cv2.imshow("blur", blur)
cv2.imshow("box", box)
cv2.imshow("Gaus", Gaus)
cv2.imshow("median", median)
cv2.imshow("bilateral", bilateral)
cv2.imshow("filter2D", r2D)
cv2.waitKey()
cv2.destroyAllWindows()