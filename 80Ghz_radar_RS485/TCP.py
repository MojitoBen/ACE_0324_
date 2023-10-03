'''
用TCP方式模擬信號交換
調整預設空距值達到目標效果
'''
import socket
import random

# 預設回應
default_response = '01 03 02 01 30 B9 C0'

# 設定伺服器的IP和埠號
server_ip = '127.0.0.1'
server_port = 12345

# 建立TCP伺服器
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((server_ip, server_port))
server_socket.listen(5)

print(f"等待連接在 {server_ip}:{server_port} 的設備...")

while True:
    # 等待客戶端連接
    client_socket, addr = server_socket.accept()
    print(f"已連接到來自 {addr} 的設備")

    # 接收來自客戶端的訊息
    data = client_socket.recv(1024).decode('utf-8').strip()

    # 如果收到特定訊息，則回傳預設回應
    if data == '010300000001840A':
        print(f"收到訊息: {data}")
        # 生成A到B之間的隨機數字
        random_value = random.randint(295, 305)
        # 將隨機數字轉換為十六進位字串，並補零到四位數
        hex_value = '{:04X}'.format(random_value)
        # 組合回應字串
        default_response = f'01 03 02 {hex_value} B9 C0'
        print(f"回應: {default_response}")
        client_socket.sendall(default_response.encode('utf-8'))
    else:
        print(f"收到未知訊息: {data}")

    # 關閉與客戶端的連接
    client_socket.close()
