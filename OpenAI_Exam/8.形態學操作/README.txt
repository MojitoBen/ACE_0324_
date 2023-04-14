函數語法
#腐蝕操作 將影像的邊界點消除，使影像沿著邊界向內收縮
dst = cv2.erode(src, kernel[, anchor[, iterations[, borderType[, borderValue]]]])
常用形式: dst = cv2.erode(src, kernel)
#膨脹操作 將目前物件接觸到的背景點合併到目前物件內
dst = cv2.dilate(src, kernel[, anchor[, iterations[, borderType[, borderValue]]]])
常用形式: dst = cv2.dilate(src, kernel)
#通用形態學函數
dst = cv2.morphologyEx(src, op, kernel[, anchor[, iterations[, borderType[, borderValue]]]])
'''
dst = 結果影像，與原影像同類型大小
src = 原影像
op = 操作類型
kernel = 採用的結構類型，可以自訂產生，也可以用cv2.getStructuringElement()產生
anchor = 錨點，預設值(-1,-1)(中心點位置)，用預設就好
iterations = 重複操作的次數，預設值為1
borderType = 邊界樣式，用預設就好，有需要再查
'''
==========op==========
cv2.MORPH_ERODE	    腐蝕	    erode(src)
cv2.MORPH_DILATE	膨脹	    dilate(src)
cv2.MORPH_OPEN	    開運算	    dilate(erode(src))
cv2.MORPH_CLOSE	    閉運算	    erode(dilate(src))
cv2.MORPH_GRADIENT	梯度運算	dilate(src)-erode(src)
cv2.MORPH_TOPHAT	禮帽運算	src-open(src)
cv2.MORPH_BLACKHAT	黑帽運算	close(src)-src
cv2.MORPH_HITMISS   擊不擊中    intersection(erode(src),erode(srcI)) #僅支援CV_8UC1二進位影像
======================