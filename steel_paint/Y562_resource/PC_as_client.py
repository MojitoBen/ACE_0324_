import socket
import binascii

# 繼電器的IP和端口
relay_ip = "192.168.1.78"
relay_port = 1030

# 要發送的資料，已轉換為二進位格式
data = bytes.fromhex('48 3a 01 57 00 01 01 00 00 00 00 00 dc 45 44')

# 建立socket對象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 連接到繼電器
s.connect((relay_ip, relay_port))

# 發送資料
s.sendall(data)

# 接收回應
response = s.recv(1024)  # 1024是接收的最大字節數，您可以根據需要調整

# 將接收到的數據轉換為十六進制格式
hex_response = binascii.hexlify(response)

# 將bytes型別的數據轉換為str型別，並將每兩個字符之間插入一個空格
formatted_response = ' '.join(hex_response[i : i+2].decode() for i in range(0, len(hex_response), 2))

print("Received:", formatted_response)

# 確認x1 x2狀態: '48 3a 01 52 00 00 00 00 00 00 00 00 d5 45 44'
# x2 on : 48 3a 01 41 00 01 01 01 00 00 00 00 c7 45 44
# x1 on : 48 3a 01 41 01 00 01 01 00 00 00 00 c7 45 44
# x1 off x2 off: 48 3a 01 41 00 00 01 01 00 00 00 00 c6 45 44
# 要x1變on, x2變off: '48 3a 01 57 01 00 01 00 00 00 00 00 dc 45 44'  # 第六組還要一個01是要符合校驗
# 要x2變on, x1變off: '48 3a 01 57 00 01 01 00 00 00 00 00 dc 45 44'

# 關閉連接
s.close()
