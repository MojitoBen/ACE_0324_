#計算輪廓面積
retval = cv2.contourArea(contour[, oriented])
'''
contours = 輪廓
oriented = True時，傳回的值正/負號表示輪廓是順/逆時針；False時，傳回的retval是絕對值
'''
#計算輪廓長度
retval = cv2.arcLength(curve, closed)
'''
curve = 輪廓
closed = 輪廓是否封閉，True = 封閉
'''
#Hu矩:歸一化中心矩的線性組合，在影像旋轉縮放平移等操作後仍能保持矩的不變性
hu = cv2.HuMoments( m )
'''
m = 由函數cv2.moments()計算獲得的矩特徵值
'''
#形狀比對 cv2.matchShapes()
retval = cv2.matchShapes(contour1, contour2, method, parameter)
'''
method = 比較2個物件的Hu矩的方法
parameter = 擴充參數，先預設0
'''
#繪製矩形包圍框 cv2.boundingRect()
retval = cv2.boundingRect( array )
'''
retval or x,y,w,h = 傳回左上角頂點座標值 &&矩形邊界寬度和高度
array = 灰階影像或輪廓
'''
#最小包圍矩形 cv2.minAreaRect()
retval = cv2.minAreaRect( points )
points = cv2.boxPoints( box )
#最小包圍圓形 cv2.minEnclosingCircle
center, radius = cv2.minEnclosingCircle( points )
==========method==========
cv2.CONTOURS_MATCH_I1
cv2.CONTOURS_MATCH_I2
cv2.CONTOURS_MATCH_I3
==========================
12.6-計算各輪廓面積並篩選
12.7-計算輪廓長度
12.10-形狀比對
12.12-
12.13-
12.14-