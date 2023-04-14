import cv2
import numpy as np
a = cv2.imread("Cutie.png", cv2.IMREAD_UNCHANGED)
#face = a[100:230, 170:320]
cv2.imshow("original",a)
face = np.random.randint(0,256,(130,150,3))
a[100:230, 170:320] = face
cv2.imshow("result",a)
cv2.waitKey()
cv2.destroyAllWindows()