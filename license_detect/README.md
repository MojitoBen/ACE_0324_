\# \*需安裝darknet，再把此資料夾移至darknet根目錄下

#\*import pymysql.cursors

##\_\_A1.py 主程式\_\_

* 要上傳資料庫把71-71註解拿掉(需要的話)
* 14行改darknet位置
* 64行改車牌截圖後要放的位置
* 132行放監視器rtsp位置(不一定要)
* 144行放log位置

\_單純跑圖把32行註解，31行放圖片位置\_

\_跑影片的網站位置註解掉156行，放在155行\_

##\_\_database.py\_\_  已改用db讀取AI參數

* 去data\_server.txt改資料庫位置(需要的話)
* 改SQL語法(需要的話)

##\_\_yolo\_all.py\_\_  AI處理return2main

* 8行改darknet位置
* 13.14行改num\_train跟car\_plate位置(已訓練好的車牌模型)





