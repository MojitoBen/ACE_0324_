# **80GHz雷達量測累積水量警示系統**

需準備:    
以現有python下安裝所需模組 (conda)    
* pip install pyserial : import serial 作為接收rs485訊息的橋接器    
* pip install requests : line notify推播所需    
* pip install opencv-python 擷取串流影像所需    
3.7版本的python用3.4.2.16的opencv    
pip install -i https://mirrors.aliyun.com/pypi/simple/opencv-python==3.4.2.16    
* pip install tk 介面

![image](https://github.com/MojitoBen/ACE_0324_/blob/main/80Ghz_radar_RS485/readimg/merge.jpg)

程式功能:       
透過RS485與設備詢問訊息    
<介面>    
* 顯示目前累積水量：(總高度-空距)    
* 顯示設定警示累積水量(cm)：使用者設定    
* 顯示警示頻率(秒)    
<功能>    
* 當空距小於警示設定時，推播消息至line群組，顯示目前累積水量(總高度-空距)和警示累積水量，並傳回當前影像    
* 當空距小於警示設定時，轉成醒目”紅字”    
* 向RS485詢問頻率為”警示頻率(秒) // 3” 例:設定60秒發一次警報等於20秒問一次空距

## RS485_line_latest.py : 主程式(需有設備，與RS485互動)

* 修改Setting.txt內容
* 修改RS485串口配置
* 修改Line Notify配置

![image](https://github.com/MojitoBen/ACE_0324_/blob/main/80Ghz_radar_RS485/readimg/parameter.png)

## RS485_line_simulation.py  : 主程式(模擬與RS485互動，需先開啟TCP)

* 是使用TCP，與RS485不同模式交流
* 修改Setting.txt內容
* 修改Line Notify配置
* 以本機作為TCP伺服器，不同設備請修改server_ip跟server_port

## TCP.py :用來傳接訊號

* 4個IMG框分別是廠商、現場畫面、鋼捲原圖、噴字圖
* 要在UI_functions調整資料庫的connected

![image](https://github.com/MojitoBen/ACE_0324_/blob/main/80Ghz_radar_RS485/readimg/TCP.png)

## 流程圖

* 流程圖還沒畫



