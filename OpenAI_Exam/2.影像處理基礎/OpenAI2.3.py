import numpy as np
import cv2

blue = np.zeros((300, 300, 3), dtype = np.uint8)
blue[:,:,0] = 255
print("blue=\n", blue)
cv2.imshow("blue", blue)

green = np.zeros((300, 300, 3), dtype = np.uint8)
green[:,:,1] = 255
print("green=\n", green)
cv2.imshow("green", green)

red = np.zeros((300, 300, 3), dtype = np.uint8)
red[:,:,2] = 255
print("red=\n", red)
cv2.imshow("red", red)

cv2.waitKey()
cv2.destroyAllWindows()