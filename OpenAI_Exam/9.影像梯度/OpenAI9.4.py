#Y方向邊緣完整資訊
import cv2
o = cv2.imread("C:\\Users\\User\\Desktop\\Ben\\AI\\Cutie.png", cv2.IMREAD_GRAYSCALE)
Sobely = cv2.Sobel(o, cv2.CV_64F, 0, 1)
Sobely = cv2.convertScaleAbs(Sobely)
cv2.imshow("o", o)
cv2.imshow("x", Sobely)
cv2.waitKey()
cv2.destroyAllWindows()