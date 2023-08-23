# **鋼捲噴字辨識系統**

 **需安裝darknet，再把此資料夾移至darknet根目錄下  
 要安裝 pymysql.cursors    
 opencv - 最新就好、 logging、threading、queue、time、datetime     
 **

## Y562_cam1.py :主程式(不上傳進資料庫單純辨識)

![image](https://github.com/MojitoBen/ACE_0324_/blob/main/steel_paint/Y562_resource/0717_test.png)

## L1_check.py  :接收前站鋼捲資料

* 有上傳資料庫才需要
* 作為TCP_SERVER持續監聽CLIENT傳來的資料(僅限1CLIENT)

## UI.py & UI(match_window) :介面，用來看歷史資料

* 4個IMG框分別是廠商、現場畫面、鋼捲原圖、噴字圖
* 要在UI_functions調整資料庫的connected

![image](https://github.com/MojitoBen/ACE_0324_/blob/main/steel_paint/Y562_resource/UI_screenshot_deal.png)

## steel_rotate180.py & sid_cam1.py : 辨識用

* steel_rotate180.py跟sid_cam1.py裡面的darknet跟load_network部分要改成自己檔案位置的路徑


