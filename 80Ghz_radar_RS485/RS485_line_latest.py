import serial
import time
import requests
import datetime
import logging
import tkinter as tk
from tkinter import ttk, font
import threading
import cv2
import os

alarm_counter = 0

def Get_data():
    try:
        with open('Setting.txt', 'r') as f:
            Data_list = []
            for line in f.readlines():
                a = line.split('=', 1)
                if len(a) > 1:
                    Data_list.append(a[1].strip())
                else:
                    logging.warning(f"No data found after '=' in line: {line.strip()}")
            return Data_list
    except Exception as e:
        logging.error(f'Error occurred: {e}')
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
    

# Line Notify
url = 'https://notify-api.line.me/api/notify'
token = 'OoPCuvvUYYq8nyV5AXexAMabJ51HR8zo92iew44x6AS'
headers = {
    'Authorization': 'Bearer ' + token
}

# RS485串口
ser = serial.Serial(
    port='/dev/ttyUSB0',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
)

def startrun():
    Setting_list = Get_data()
    notify_value = int(Setting_list[0])
    frequency = int(Setting_list[1])
    time_lag = (frequency // 3) * 1000
    rtsp_url = Setting_list[2]
    total_height = int(Setting_list[3])
    
    try:

        command = '010300000001840A'  # 主機端向雷達詢問空距(cm)
        ser.write(bytes.fromhex(command))
        time.sleep(0.1)
        rs485_data = ser.readline().decode().strip()
        if rs485_data:
            rs485_data = rs485_data.replace(" ", "")

        if rs485_data and len(rs485_data) == 14 and rs485_data.isalnum():
            distance_hex = rs485_data[6:10]
            distance_decimal = int(distance_hex, 16)

            distance_show = total_height - distance_decimal
            distance_label.config(text="累積水量: {}".format(distance_show))

            if distance_show > notify_value:  # 當大於警示水量標準時
                global alarm_counter
                alarm_message = "已達警示水量標準: {}".format(notify_value)
                alarm_label.config(text=alarm_message, foreground="red")  # 將文字設為紅色
                distance_label.config(foreground="red")  # 將當前文字設為紅色

                # 如果達到3次警示標準，發送訊息並重設計數器
                if alarm_counter >= 2:
                    captured_frame = capture_frame_from_rtsp(rtsp_url)
                    if captured_frame is not None:
                        if not os.path.exists('images'):
                            os.makedirs('images')

                        current_time = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
                        image_filename = os.path.join('images', 'warning_frame_{}.jpg'.format(current_time))

                        # 將影像存為檔案
                        cv2.imwrite(image_filename, captured_frame)
                        print("Captured frame saved")
                    
                        alarm_message = "🚱🚱累積水量: {}，已連續達到警示水量標準三次: {}，請檢查🚱🚱".format(distance_show, notify_value)
                        notify = {'message': alarm_message}
                        files = {'imageFile': open(image_filename, 'rb')}
                        send = requests.post(url, headers=headers, data=notify, files=files)
                        print("Upload to line group! status = ", send.status_code)
                        logging.debug(f"累積水量: {distance_show}，已達到警示水量標準: {notify_value}")
                        alarm_counter = 0
                    else:
                        print("Failed to capture frame from RTSP stream.")
                else:
                    alarm_counter += 1
                    time.sleep(0.1)
                print("警示記數 : ", alarm_counter)
            else:
                alarm_label.config(text="警示水量: {}".format(notify_value), foreground="black")
                distance_label.config(foreground="black") 
                alarm_counter = 0 

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

    distance_label = ttk.Label(root, text="累積水量:", font=font_style)
    distance_label.pack(pady=10)
    
    initial_alarm_text = Setting_list[0]
    alarm_label = ttk.Label(root, text="警示水量: {}".format(initial_alarm_text), font=font_style)
    alarm_label.pack(pady=10)
    
    frequency = Setting_list[1]
    frequency_label = ttk.Label(root, text="警示回傳頻率:", font=font_style)
    frequency_label.pack(pady=10)
    frequency_label.config(text="回傳頻率: {} 秒".format(frequency))

    startrun()

    root.mainloop()
