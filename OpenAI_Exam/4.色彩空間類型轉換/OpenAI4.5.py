import cv2
cutie = cv2.imread("Cutie.png")
rgb = cv2.cvtColor(cutie, cv2.COLOR_BGR2RGB)
cv2.imshow("Cutie", cutie)
cv2.imshow("rgb", rgb)
cv2.waitKey()
cv2.destroyAllWindows()