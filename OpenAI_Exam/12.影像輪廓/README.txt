函數語法 
#尋找影像輪廓 findContours函數
(image,) contours, hierarchy = cv2.findContours(image, mode, method)
'''
contours = 傳回的輪廓，list類型 常用:len(), .shape
hierarchy = 影像的輪廓層次，每個輪廓contours[i]對應[Next, Previous, First_Child, Parent]，沒對應關係:值= -1
mode = 輪廓的分析方式
method = 如何表達輪廓
'''
==========mode==========
cv2.RETR_EXTERNAL    只檢測外輪廓
cv2.RETR_LIST        對檢測到的輪廓不建立等級關係
cv2.RETR_CCOMP       檢測所有輪廓組織成兩級層次結構，最內層邊界 && 其他都是頂層
cv2.RETR_TREE        建立等級樹結構輪廓
==========method========
cv2.CHAIN_APPROX_NONE        儲存所有輪廓點，相鄰兩點像素位置差不超過1
cv2.CHAIN_APPROX_SIMPLE      壓縮水平垂直對角線方向只保留該方向終點座標
cv2.CHAIN_APPROX_TC89_L1     近似演算法
cv2.CHAIN_APPROX_TC89_KCOS   近似演算法
========================
#繪製影像輪廓 drawContours函數
(image =) cv2.drawContours(image, contours, contourIdx, color[, thickness[, lineType[, hierarchy[, maxLevel[, offset]]]]]) 
'''
image = 原影像
contours = 需要繪製的輪廓
contourIdx = 參數>=0繪製對應索引號輪廓，參數<0繪製全部輪廓
color = BGR格式。例如紅色(0, 0, 255)
thickness = 畫筆粗細
lineType = 輪廓線型
hierarchy = 對應函數cv2.findContours()輸出的層次資訊
maxLevel = 0=第0層輪廓，>0繪製最高層及以下相同數量層級輪廓
offset = 偏移參數，展示輪廓偏移到不同位置
'''
==========lineType==========
cv2.FILLED     x
cv2.LINE_4     相鄰2點間4個方向
cv2.LINE_8     相鄰2點間8個方向
cv2.LINE_AA    反鋸齒，讓線條更平滑
============================
#矩特徵 moments函數
retval = cv2.moments(array[, binaryImage])
'''
retval = 傳回的矩特徵，包括:空間矩(['m00']為面積)、中心矩、歸一化中心矩
array = 點集、灰階影像、二值影像
binaryImage = True時array內所有非0值處理為1
'''
12.1-繪製影像輪廓
12.2-抓取個別輪廓
12.3-分析前景物件
12.4-分析影像特徵