import socket
from SQL_functions import *

'''
持續接收L1資料
接收到L1資料後寫進資料庫並建立相對應欄位
'''
def data_server(host, port):
    while True:
        try:
            # 建立 TCP Socket
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP宣告
            # server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #UDP宣告
            server_socket.bind((host, port))  # 綁定 IP 地址和端口
            server_socket.listen(1)  # 用於伺服器端最多可接受多少socket串接

            print(f"開始監聽 {host}:{port} ...")

            client_socket, addr = server_socket.accept()  # 接受客戶端連接
            print(f"與客戶端 {addr[0]}:{addr[1]} 建立連接")

            while True:
                data = client_socket.recv(1024)  # 接收客戶端發送的數據
                if not data:
                    break

                # 解碼數據為10bytes的ASCII
                decoded_data = data[:10].decode('ascii')

                #print(f"收到來自客戶端 {addr[0]}:{addr[1]} 的數據: {decoded_data}")

                insert_data(decoded_data)

        except Exception as e:
            print(f"發生錯誤:", str(e))
        finally:
            client_socket.close()  # 關閉客戶端連接
            print(f"與客戶端 {addr[0]}:{addr[1]} 的連接已關閉")
            server_socket.close()  # 關閉伺服器端Socket，以便重新綁定

if __name__ == '__main__':
    host = '192.168.1.185'  # 主機 IP
    port = 19000  # 通訊端口，這裡我們使用整數而不是字串
    data_server(host, port)
