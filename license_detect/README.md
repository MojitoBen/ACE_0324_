﻿# **車牌辨識系統**

 **需安裝darknet，再把此資料夾移至darknet根目錄下  
 要安裝 pymysql.cursors**

## _A1.py :主程式_

* 要上傳資料庫把71-71註解拿掉(需要的話)
* 14行改darknet位置
* 64行改車牌截圖後要放的位置
* 132行放監視器rtsp位置(不一定要)
* 144行放log位置
_單純跑圖把32行註解，31行放圖片位置
跑影片的網站位置註解掉156行，放在155行_

## database.py  :已改用db讀取AI參數

* 去data\_server.txt改資料庫位置(需要的話)
* 改SQL語法(需要的話)

## yolo\_all.py :AI處理return2main

* 8行改darknet位置
* 13.14行改num\_train跟car\_plate位置(已訓練好的車牌模型)  
下載車牌模組:https://drive.google.com/drive/folders/1L3OBn0Z7cKW1ycVsn2XMRaxyloGkbLot?usp=share_link




