import cv2
import numpy as np
cutie = cv2.imread("Cutie.png", 0)
r,c = cutie.shape
key = np.random.randint(0,256,size=[r,c],dtype = np.uint8)
encryption = cv2.bitwise_xor(cutie, key)
decryption = cv2.bitwise_xor(encryption,key)
cv2.imshow("key",key) #金鑰影像
cv2.imshow("encryption", encryption) #加密影像
cv2.imshow("decryption", decryption) #解密影像
cv2.waitKey()
cv2.destroyAllWindows()