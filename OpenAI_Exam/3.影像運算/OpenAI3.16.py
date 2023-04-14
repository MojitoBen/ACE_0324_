import cv2
import numpy as np
cutie = cv2.imread("Cutie.png", 0)
r,c = cutie.shape
mask = np.zeros((r,c), dtype = np.uint8)
mask[100:230, 170:320] = 1
#KEY
key = np.random.randint(0,256,size = [r,c], dtype = np.uint8)
#========打碼=========
#對原始影像加密
cutie_Xorkey = cv2.bitwise_xor(cutie, key)
#取得加密影像的臉部資訊encryptFace
encryptFace = cv2.bitwise_and(cutie_Xorkey, mask * 255)
#將影像臉部值設定為0，獲得noFace1
noFace1 = cv2.bitwise_and(cutie, (1-mask) * 255)
#打碼後影像
maskFace = encryptFace + noFace1
#========解碼=========
#獲得臉部原始資訊
extractOriginal = cv2.bitwise_xor(maskFace,key)
#將解碼的臉部資訊分析出來
extractFace = cv2.bitwise_and(extractOriginal, mask * 255)
#分析沒有臉部資訊的原影像
noFace2 = cv2.bitwise_and(maskFace,(1-mask) * 255)
#解碼影像
extractCutie = noFace2 + extractFace

cv2.imshow("mask", mask * 255)
cv2.imshow("1-mask", (1-mask) * 255)
cv2.imshow("key", key)
cv2.imshow("cutieNorKey", cutie_Xorkey)
cv2.imshow("encryptFace", encryptFace)
cv2.imshow("noFace1", noFace1)
cv2.imshow("maskFace", maskFace)
cv2.imshow("extractOriginal", extractOriginal)
cv2.imshow("extractFace", extractFace)
cv2.imshow("noFace2", noFace2)
cv2.imshow("extractCutie", extractCutie)
cv2.waitKey()
cv2.destroyAllWindows()