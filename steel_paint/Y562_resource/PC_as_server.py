# 提供者: Ben謝

import socket
'''
連接繼電器，
回傳state到主程式。
不同繼電器可能有不同訊號數據，
實裝後重測信號數據。
'''
def tcp_server(state):
    # 建立 TCP Socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))  # 綁定 IP 地址和端口
    server_socket.listen(1)  # 監聽最大連接數量

    print(f"開始監聽 {host}:{port} ...")

    while True:
        client_socket, addr = server_socket.accept()  # 接受客戶端連接
        print(f"與客戶端 {addr[0]}:{addr[1]} 建立連接")

        try:
            while True:
                data = client_socket.recv(1024)  # 接收客戶端發送的數據
                if not data:
                    break

                # 解碼數據為16位元的HEX
                decoded_data = data.hex()

                print(f"收到來自客戶端 {addr[0]}:{addr[1]} 的數據: {decoded_data}")

                if decoded_data == "48 3a 01 41 01 00 00 00 00 00 00 00 c5 45 44":
                    state = 'in'
                elif decoded_data == "48 3a 01 41 00 00 00 00 00 00 00 00 c4 45 44":
                    state = 'out'
                else:
                    state = 'waiting'
                
                print(state)
                #return state


        except Exception as e:
            print(f"與客戶端 {addr[0]}:{addr[1]} 連接出現錯誤:", str(e))

        finally:
            client_socket.close()  # 關閉客戶端連接
            print(f"與客戶端 {addr[0]}:{addr[1]} 的連接已關閉")

if __name__ == '__main__':
    # 先進到 http://192.168.1.78/ (internet_relay的IP) 進行設定, 將其設定為client, 並且RemoteIP與Port設定為此電腦的IP
    # 然後重啟 internet relay
    host = '192.168.1.126'  # 主機 IP  , 自己電腦的
    port = 8000  # 通訊端口
    state = 'waiting'
    tcp_server(state)
