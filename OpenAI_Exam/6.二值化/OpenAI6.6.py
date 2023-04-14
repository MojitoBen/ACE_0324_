#截斷設定值:大於設定值像素=設定值，小於設定值的值不變
import cv2
img = cv2.imread("C:\\Users\\User\\Desktop\\Ben\\AI\\Cutie.png")
t, rst = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
cv2.imshow("img", img)
cv2.imshow("rst", rst)
cv2.waitKey()
cv2.destroyAllWindows()