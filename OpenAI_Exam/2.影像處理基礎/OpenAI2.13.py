import cv2
a = cv2.imread("Cutie.png", cv2.IMREAD_UNCHANGED)
face = a[100:230, 170:320]
cv2.imshow("original",a)
cv2.imshow("face",face)
cv2.waitKey()
cv2.destroyAllWindows()