import cv2
a = cv2.imread("C:\\Users\\User\\Desktop\\Ben\\Cutie_.png", -1)
b = cv2.imread("C:\\Users\\User\\Desktop\\Ben\\BG_.png", -1)
if b is None:
    print("Failed to read image")
result = cv2.addWeighted(a,0.8,b,0.2,0)
cv2.imshow("result", result)
cv2.waitKey()
cv2.destroyAllWindows()