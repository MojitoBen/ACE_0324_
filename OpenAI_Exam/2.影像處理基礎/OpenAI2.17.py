import cv2
cutie = cv2.imread("Cutie.png")
b,g,r = cv2.split(cutie)
cv2.imshow("B",b)
cv2.imshow("G",g)
cv2.imshow("R",r)
cv2.waitKey()
cv2.destroyAllWindows()