#用拉普拉斯金字塔和高斯金字塔恢復高斯金字塔內多層影像
import cv2
import numpy as np
o = cv2.imread("C:\\Users\\User\\Desktop\\Ben\\AI\\Cutie_.png")

G0 = o
G1 = cv2.pyrDown(G0)
G2 = cv2.pyrDown(G1)
G3 = cv2.pyrDown(G2)

L0 = G0 - cv2.pyrUp(G1)
L1 = G1 - cv2.pyrUp(G2)
#L2 = G2 - cv2.pyrUp(G3)

RG0 = L0 + cv2.pyrUp(G1)
print("G0.shape=",G0.shape)
print("RG0.shape=",RG0.shape)
result = RG0 - G0
result = abs(result)
print("原始影像G0與恢復影像RG0差值的絕對值和:",np.sum(result))

RG1 = L1 + cv2.pyrUp(G2)
print("G1.shape=",G1.shape)
print("RG1.shape=",RG1.shape)
result = RG1 - G1
result = abs(result)
print("原始影像G1與恢復影像RG1差值的絕對值和:",np.sum(abs(result)))
'''
RG2 = L2 + cv2.pyr(G3)
print("G2.shape=",G2.shape)
print("RG2.shape=",RG2.shape)
result = RG2 - G2
print("原始影像G2與恢復影像RG2差值的絕對值和:",np.sum(abs(result)))
'''
