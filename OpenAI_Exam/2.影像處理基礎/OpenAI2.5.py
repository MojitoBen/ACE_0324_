import numpy as np

img = np.zeros((2,4,3), dtype = np.uint8)
print ("img=\n", img)
print("讀取像素點img[0,3] = ", img[0,3])
print("讀取像素點img[1,2,2] = ", img[1,2,2])
img[0,3] = 255
img[0,0] = [66,77,88]
img[1,1,1] = 3
img[1,2,2] = 4
img[0,2,0] = 5
print("修改後img\n", img)
print("讀取修改後像素點img[1,2,2] = ", img[1,2,2])
