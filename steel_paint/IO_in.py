import socket
'''
模擬繼電器傳送信號，
使主程式state轉為in。
'''
def simulate_relay_trigger(host, port, data):
    # 建立 TCP Socket
    client_socket2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        # 連接到伺服器
        client_socket2.connect((host, port))
        
        # 將數據轉換為bytes並傳送給伺服器
        client_socket2.sendall(bytes.fromhex(data))
        print(f"已傳送數據: {data}")
        
        # 接收伺服器回傳的狀態
        response = client_socket2.recv(1024)
        print(f"伺服器回傳的狀態: {response.decode()}")
        
    except Exception as e:
        print("與伺服器連接出現錯誤:", str(e))
    
    finally:
        client_socket2.close()  # 關閉連接

if __name__ == '__main__':
    host = '192.168.1.185'  # 主機 IP
    port = 8000  # 通訊端口
    data_to_send = "483a01410100000000000000c54544"  # 要傳送的數據

    simulate_relay_trigger(host, port, data_to_send)
