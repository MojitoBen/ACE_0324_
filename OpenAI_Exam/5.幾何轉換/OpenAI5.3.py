import cv2
img = cv2.imread("Cutie.png")
rst = cv2.resize(img, None, fx = 0.5, fy = 0.5)
print("img.shape = ", img.shape)
print("rst.shape = ", rst.shape)

#cv2.imshow("img", img)
cv2.imshow("rst", rst)
cv2.waitKey()
cv2.destroyAllWindows()

#cv2.imwrite("rst.png", rst) #儲存縮放後影像