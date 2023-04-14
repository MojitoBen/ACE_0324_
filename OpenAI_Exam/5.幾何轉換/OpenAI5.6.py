#旋轉 retval = cv2.getRotationMatrix2D(center, angle, scale)
#M = cv2.getRotationMatrix2D((height/2,width/2), 45, 0.8) 中心點在正中心，轉45度，縮小成0.8倍
import cv2
img = cv2.imread("Cutie.png")
height,width = img.shape[:2]
M = cv2.getRotationMatrix2D((height/2,width/2), 45, 0.8)
rotate = cv2.warpAffine(img, M, (width,height))
cv2.imshow("original", img)
cv2.imshow("rotation", rotate)
cv2.waitKey()
cv2.destroyAllWindows()