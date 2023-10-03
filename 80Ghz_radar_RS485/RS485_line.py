import serial
import time
import requests
import datetime
import logging

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

# 配置Line Notify
url = 'https://notify-api.line.me/api/notify'
token = 'OoPCuvvUYYq8nyV5AXexAMabJ51HR8zo92iew44x6AS'
headers = {
    'Authorization': 'Bearer ' + token
}

#配置RS485串口
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
    time_lag = frequency // 3
    rtsp = Setting_list[2]
    distance_message = '目前空距: {}'
    alarm_message = '已達警示空距標準: {}'
    try:
        while True:
            command = '010300000001840A' #主機詢問空距(cm)
            ser.write(bytes.fromhex(command))
            time.sleep(0.1)

            #rs485_data = ser.readline().decode().strip()
            rs485_data = '01 03 02 01 30 B9 C0' #模擬回傳信號 304cm
            rs485_data = rs485_data.replace(" ", "")
            
            if len(rs485_data) == 14 and rs485_data.isalnum():
                distance_hex = rs485_data[6:10]
                distance_decimal = int(distance_hex, 16)
                
                distance_show = distance_message.format(distance_decimal) #顯示在介面第一欄位

                if distance_decimal < notify_value: #當小於警示空距時
                    alarm_message = alarm_message.format(distance_decimal)
                    notify = {'message': alarm_message}
                    send = requests.post(url, headers=headers, data=notify)
                    
                    print(send.status_code, send.text)
                    logging.info(f"record: {send.text}")
            
            time.sleep(time_lag)

    except Exception as e:
            print(f"connected failed:", str(e))
            logging.error(f"connected failed: {str(e)}")

if __name__ == '__main__':

    logname = 'log/'
    logname = logname+"{:%Y-%m-%d}".format(datetime.datetime.now())+'_rs485.log'
    FORMAT = '%(asctime)s %(levelname)s: %(message)s'
    logging.getLogger("requests").setLevel(logging.WARNING)  
    logging.getLogger("urllib3").setLevel(logging.WARNING)  
    logging.basicConfig(level=logging.DEBUG, filename=logname, filemode='a', format=FORMAT)

    while True:
        try:
            startrun()
        except:
            logging.error('RS485 connecting failed', exc_info=True)
            print('error')
            time.sleep(1)
