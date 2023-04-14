#X方向邊緣完整資訊
import cv2
o = cv2.imread("C:\\Users\\User\\Desktop\\Ben\\AI\\Cutie.png", cv2.IMREAD_GRAYSCALE)
Sobelx = cv2.Sobel(o, cv2.CV_64F, 1, 0)
Sobelx = cv2.convertScaleAbs(Sobelx)
cv2.imshow("o", o)
cv2.imshow("x", Sobelx)
cv2.waitKey()
cv2.destroyAllWindows()