import numpy as np
import cv2
img = np.random.randint(0,256,size = [256,256], dtype = np.uint8)
cv2.imshow("demo", img)
cv2.waitKey(3000)
cv2.destroyAllWindows()