#均值濾波
import cv2
o = cv2.imread("C:\\Users\\User\\Desktop\\Ben\\AI\\Cutie.png")
r = cv2.blur(o,(5,5))
cv2.imshow("img", o)
cv2.imshow("blur", r)
cv2.waitKey()
cv2.destroyAllWindows()