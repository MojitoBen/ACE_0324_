*需安裝darknet，再把此資料夾移至darknet根目錄下
*import pymysql.cursors

A1.py 主程式 
*要上傳資料庫把71-71註解拿掉(需要的話)
*14行改darknet位置
*64行改車牌截圖後要放的位置
*132行放監視器rtsp位置(不一定要)
*144行放log位置
單純跑圖把32行註解，31行放圖片位置
跑影片的網站位置註解掉156行，放在155行

database.py  已改用db讀取AI參數
*去data_server.txt改資料庫位置(需要的話)
*改SQL語法(需要的話)

yolo_all.py  AI處理return2main
*8行改darknet位置
*13.14行改num_train跟car_plate位置(已訓練好的車牌模型)





