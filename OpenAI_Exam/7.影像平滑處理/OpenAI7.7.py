#中值濾波
import cv2
o = cv2.imread("C:\\Users\\User\\Desktop\\Ben\\AI\\Cutie.png")
r = cv2.medianBlur(o, 3)
cv2.imshow("img", o)
cv2.imshow("median", r)
cv2.waitKey()
cv2.destroyAllWindows()