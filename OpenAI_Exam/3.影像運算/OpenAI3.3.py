import cv2
a = cv2.imread("Cutie.png", 0)
b = a
result1 = a + b
result2 = cv2.add(a,b)
cv2.imshow("1", result1)
cv2.imshow("2", result2)
cv2.waitKey()
cv2.destroyAllWindows()