import serial
import time
import requests
import datetime
import logging
import tkinter as tk
from tkinter import ttk, font
import threading
import cv2

alarm_counter = 0

def Get_data():
    try:
        f = open('Setting.txt')
        Data_list=[]
        for line in f.readlines():
            a = line.split('=')
            Data_list.append(a[1].strip())
        f.close()
        return Data_list
    except:
        logging.error('get data failed')
        print('get data failed')

def capture_frame_from_rtsp(rtsp_url):
    cap = cv2.VideoCapture(rtsp_url)
    if not cap.isOpened():
        print("Error: Could not open RTSP stream.")
        return None

    ret, frame = cap.read()
    cap.release()

    if ret:
        return frame
    else:
        print("Error: Could not read frame from RTSP stream.")
        return None
    

# 配置Line Notify
url = 'https://notify-api.line.me/api/notify'
token = 'OoPCuvvUYYq8nyV5AXexAMabJ51HR8zo92iew44x6AS'
headers = {
    'Authorization': 'Bearer ' + token
}
'''
# 配置RS485串口
ser = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
)
'''
def startrun():
    Setting_list = Get_data()
    notify_value = int(Setting_list[0])
    frequency = int(Setting_list[1])
    time_lag = (frequency // 3) * 1000
    rtsp = Setting_list[2]
    
    try:
        #command = '010300000001840A'  # 主機詢問空距(cm)
        #ser.write(bytes.fromhex(command))
        #time.sleep(0.1)

        # rs485_data = ser.readline().decode().strip()
        rs485_data = '01 03 02 01 30 B9 C0'  # 模擬回傳信號 304cm
        rs485_data = rs485_data.replace(" ", "")

        #print("警示空距測試: ", notify_value)
        if len(rs485_data) == 14 and rs485_data.isalnum():
            distance_hex = rs485_data[6:10]
            distance_decimal = int(distance_hex, 16)

            distance_show = distance_decimal  # 顯示在介面第一欄位
            distance_label.config(text="當前空距: {}".format(distance_show))

            if distance_decimal < notify_value:  # 當小於警示空距時
                global alarm_counter
                alarm_message = "已達警示空距標準: {}".format(notify_value)
                alarm_label.config(text=alarm_message, foreground="red")  # 將文字設為紅色

                # 如果達到3次警示標準，發送訊息並重設計數器
                if alarm_counter > 2:
                    alarm_message = "🚱🚱當前空距: {}，已連續達到警示空距標準三次: {}，請檢查🚱🚱".format(distance_show, notify_value)
                    notify = {'message': alarm_message}
                    send = requests.post(url, headers=headers, data=notify)
                    print(send.status_code, send.text)
                    logging.debug(f"當前空距: {distance_show}，已達到警示空距標準: {notify_value}")
                    alarm_counter = 0
                else:
                    alarm_counter += 1
                    time.sleep(0.1)

            frequency_label.config(text="回傳頻率: {} 秒".format(frequency))
        
        root.update_idletasks()
        root.after(time_lag, startrun)

    except Exception as e:
        print(f"connected failed:", str(e))
        logging.error(f"connected failed: {str(e)}")

if __name__ == '__main__':
    logname = 'log/'
    logname = logname + "{:%Y-%m-%d}".format(datetime.datetime.now()) + '_rs485.log'
    FORMAT = '%(asctime)s %(levelname)s: %(message)s'
    logging.getLogger("requests").setLevel(logging.WARNING)
    logging.getLogger("urllib3").setLevel(logging.WARNING)
    logging.basicConfig(level=logging.DEBUG, filename=logname, filemode='a', format=FORMAT)

    Setting_list = Get_data()

    root = tk.Tk()
    root.title("RS485信息")
    root.geometry("640x360")
    
    font_style = font.Font(size=40)

    distance_label = ttk.Label(root, text="當前空距:", font=font_style)
    distance_label.pack(pady=10)
    
    initial_alarm_text = Setting_list[0]
    alarm_label = ttk.Label(root, text="警示空距: {}".format(initial_alarm_text), font=font_style)
    alarm_label.pack(pady=10)
    
    frequency_label = ttk.Label(root, text="回傳頻率:", font=font_style)
    frequency_label.pack(pady=10)

    startrun()

    root.mainloop()
