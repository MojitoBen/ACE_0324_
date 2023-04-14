#Laplacian運算元
import cv2
o = cv2.imread("C:\\Users\\User\\Desktop\\Ben\\AI\\Cutie.png", cv2.IMREAD_GRAYSCALE)
Laplacian = cv2.Laplacian(o, cv2.CV_64F)
Laplacian = cv2.convertScaleAbs(Laplacian)
cv2.imshow("o", o)
cv2.imshow("Laplacian", Laplacian)
cv2.waitKey()
cv2.destroyAllWindows()