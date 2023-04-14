函數語法 
#pyrDown 高斯金字塔向下取樣
dst = cv2.pyrDown(src[, dstsize[, borderType]])
#pyrDown 高斯金字塔向上取樣
dst = cv2.pyrUp(src[, dstsize[, borderType]])
'''
dst = 靶心圖表面
src = 原始影像
dstsize = 靶心圖表面大小
borderType = 邊界樣式，僅支援BORDER_DEFAULT
'''
11.1-pyrDown
11.2-pyrUp
11.3-先向下再向上，觀察差異
11.7-用拉普拉斯金字塔和高斯金字塔恢復高斯金字塔內多層影像