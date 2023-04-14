import cv2
img = cv2.imread("Cutie.png")
x = cv2.flip(img, 0) #上下顛倒
y = cv2.flip(img, 1) #左右顛倒
xy = cv2.flip(img, -1) #上下左右顛倒
cv2.imshow("x", x)
cv2.imshow("y", y)
cv2.imshow("xy", xy)
cv2.waitKey()
cv2.destroyAllWindows()