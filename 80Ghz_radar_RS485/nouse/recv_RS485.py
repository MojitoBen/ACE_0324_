import serial

# 設定串口參數
ser = serial.Serial(
    port='/dev/ttyUSB0',  
    baudrate=9600,        
    parity=serial.PARITY_NONE,  
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS 
)

try:
    ser.open()  # 打開串口

    while True:
        # 讀取RS485數據
        rs485_data = ser.readline().decode('utf-8').strip()
        
        if rs485_data:
            print(f"接收到RS485數據: {rs485_data}")
except Exception as e:
    print(f"發生錯誤: {str(e)}")
finally:
    ser.close()  # 關閉串口
