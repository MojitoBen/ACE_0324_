#高斯濾波
import cv2
o = cv2.imread("C:\\Users\\User\\Desktop\\Ben\\AI\\Cutie.png")
r = cv2.GaussianBlur(o,(5,5), 0, 0)
cv2.imshow("img", o)
cv2.imshow("Gaus", r)
cv2.waitKey()
cv2.destroyAllWindows()