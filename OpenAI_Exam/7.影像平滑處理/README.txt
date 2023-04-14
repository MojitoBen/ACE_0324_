函數語法
#均值濾波 用目前像素點周圍像素值的均值代替目前像素點
dst = cv2.blur(src, ksize, anchor, borderType) 
常用形式:dst = cv2.blur(src, ksize)
#方框濾波 normalize=1表示要歸一化，用鄰域像素值的和除以面積；normalize=0表示不歸一化，直接使用鄰域像素值的和 *濾波核建議小不然圖會變全白
dst = cv2.boxFilter(src, ddepth, ksize, anchor, normalize, borderType) 
常用形式:dst = cv2.boxFilter(src, ddepth, ksize)
#高斯濾波 將中心點加權值加強；遠離中心點加權值減小
dst = cv2.GaussianBlur(src, ksize, sigmaX, sigmaY, borderType)
常用形式:dst =cv2.GaussianBlur(src, ksize, 0, 0)
#中值濾波 鄰域內所有像素值的中間值替代目前像素點的像素值
dst = cv2.medianBlur(src, ksize)
#雙邊濾波 
dst = cv2.bilateralFilter(src, d, sigmaColor, sigmaSpace, borderType)
#自訂旋積
dst = cv2.Filter2D(src, ddepth, kernel, anchor, delta, borderType) 
常用形式:dst = cv2.Filter2D(src, ddepth, kernel)
'''
dst = 回傳值
src = 原影像
d = 空間距離參數，以目前像素點為中心點的直徑，濾波空間較大則速度較慢，推薦d=5，雜訊較大者用d=9
ddepth = 影像深度(-1 = 原影像深度)(CV_8U、CV_16U、CV_16S、CV_32F、CV_64F)
ksize = 濾波核大小(影響鄰域的高度寬度)
kernel = 卷積核，單通道陣列(使用numpy)，處理彩色影像時讓每個通道使用不同的核，分解彩色影像後使用不同核
sigmaX = 卷積核在水平方向上的標準差，其控制的是加權比例，必選參數，可預設0
sigmaY = 卷積核在垂直方向上的標準差，非必選參數，實際處理中也是預設0，建議預設
sigmaColor = 選取的顏色差值範圍，決定周圍那些像素點可以參與運算，0=沒意義；255=指定直徑內所有點都能參與
sigmaSpace = 值越大，越多點可以參與到計算中，一般數值與sigmaColor設相同
delta = 修正值，如果有值，會在基礎濾波結果上加該值作為最後結果
anchor = 錨點，預設值(-1,-1)(中心點位置)，用預設就好
normalize = 濾波時是否進行歸一化(將計算結果規範化為目前像素範圍內值) 1=要 0=不要
borderType = 邊界樣式，用預設就好，有需要再查
'''
7.1-均值濾波
7.3-方框濾波
7.6-高斯濾波
7.7-中值濾波
7.8-雙邊濾波
7.10-2D旋積