#雙邊濾波
import cv2
o = cv2.imread("C:\\Users\\User\\Desktop\\Ben\\AI\\Cutie.png")
r = cv2.bilateralFilter(o, 25, 100, 100)
cv2.imshow("img", o)
cv2.imshow("bilateral", r)
cv2.waitKey()
cv2.destroyAllWindows()