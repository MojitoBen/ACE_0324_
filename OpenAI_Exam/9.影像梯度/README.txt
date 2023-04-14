函數語法
#Sobel運算元
dst = cv2.Sobel(src, ddepth, dx, dy[, ksize[, scale[, delta[, borderType]]]])
#取絕對值(實際操作中計算梯度會有負值)
AbsR = cv2.convertScaleAbs(src[, alpha[, beta]])
#將原始影像轉為256色點陣圖
dst = saturate(src * alpha + beta)
#計算x方向邊緣(梯度)dx=1,dy=0
dst = cv2.Sobel(src, ddepth, 1, 0)
#計算y方向邊緣(梯度)dx=0,dy=1
dst = cv2.Sobel(src, ddepth, 0, 1)
#兩方向
dst = cv2.Sobel(src, ddepth, 1, 1)
#Scharr運算元 (較高精度)
dst = cv2.Scharr(src, ddepth, dx, dy[, ksize[, scale[, delta[, borderType]]]])
**dx >=0 && dy >= 0 && dx+dy == 1 所以不能x跟y都是1
#Laplacian運算元
dst = cv2.Laplacian(src, ddepth[, ksize[, scale[, delta[, borderType]]]])
'''
dst = 靶心圖表面
AbsR = 處理結果
src = 原影像
alpha = 調節係數，可選值，預設1
beta = 調節亮度值，預設值，預設0
ddepth = 輸出影像深度
dx = x方向上求導階數
dy = y方向上求導階數
ksize = Sobel核大小，-1時用Scharr運算元進行運算
scale = 縮放因數，1=沒有縮放
(Sobel)(Laplacian)delta = 靶心圖表面dst上值，可選，預設0
(Scharr)delta = 靶心圖上亮度值，可選，預設0
borderType = 邊界樣式，用預設就好，有需要再查
'''
函數語法 <10章>
#Canny函數做邊緣檢測
edges = cv2.Canny(image, threshold1, threshold2[, aperyureSize[, L2gradient]])
'''
edges = 計算後邊緣影像
image = 8位輸入影像
threshold1 = 處理過程中第一設定值
threshold2 = 處理過程中第二設定值
aperyureSize = 表示Sobel運算元的孔徑大小
L2gradient = 計算影像梯度幅度，預設false，ture的話用更精確的L2範數計算
'''
9.3-X方向邊緣完整資訊
9.4-Y方向邊緣完整資訊
9.6-Sobel取邊緣資訊
9.10-Scharr取邊緣資訊
9.13-Sobel和Scharr運算元比較
9.14-Laplacian運算元
10.1-Canny取邊緣