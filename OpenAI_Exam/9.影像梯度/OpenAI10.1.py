#Canny取邊緣
import cv2
o = cv2.imread("C:\\Users\\User\\Desktop\\Ben\\AI\\Cutie.png", cv2.IMREAD_GRAYSCALE)
r1 = cv2.Canny(o, 128, 200)
r2 = cv2.Canny(o, 32, 128)
r3 = cv2.Canny(o, 4, 32)
cv2.imshow("o", o)
cv2.imshow("r1", r1)
cv2.imshow("r2", r2)
cv2.imshow("r3", r3)
cv2.waitKey()
cv2.destroyAllWindows()