#先向下再向上，觀察差異
import cv2
o = cv2.imread("C:\\Users\\User\\Desktop\\Ben\\AI\\Cutie_.png", cv2.IMREAD_GRAYSCALE)
down = cv2.pyrDown(o)
up = cv2.pyrUp(down)
diff = up-o
cv2.imshow("o", o)
cv2.imshow("up", up)
cv2.imshow("difference", diff)
cv2.waitKey()
cv2.destroyAllWindows()