#Scharr取邊緣資訊
import cv2
o = cv2.imread("C:\\Users\\User\\Desktop\\Ben\\AI\\Cutie.png", cv2.IMREAD_GRAYSCALE)
scharrx = cv2.Sobel(o, cv2.CV_64F, 1, 0)
scharry = cv2.Sobel(o, cv2.CV_64F, 0, 1)
scharrx = cv2.convertScaleAbs(scharrx)
scharry = cv2.convertScaleAbs(scharry)
scharrxy = cv2.addWeighted(scharrx, 0.5, scharry, 0.5, 0)
cv2.imshow("o", o)
cv2.imshow("xy", scharrxy)
cv2.waitKey()
cv2.destroyAllWindows()