import socket
import logging
import datetime
from SQL_functions import *
import time
'''
連接繼電器，
回傳state到主程式。
不同繼電器可能有不同訊號數據，
實裝後重測信號數據。
'''

def tcp_server(state, sent_result, ret_result):

    # 建立 TCP Socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))  # 綁定 IP 地址和端口
    server_socket.listen(1)  # 監聽最大連接數量

    print(f"開始監聽 {host}:{port} ...")

    while True:
        client_socket, addr = server_socket.accept()  # 接受客戶端連接
        print(f"與繼電器 {addr[0]}:{addr[1]} 建立連接")

        try:
            while True:
                data = client_socket.recv(1024)  # 接收數據
                if not data:
                    break
                
                #print("data:",data)

                # 解碼數據為16位元的HEX
                decoded_data = data.hex()

                print(f"收到來自客戶端 {addr[0]}:{addr[1]} 的數據: {decoded_data}")

                if decoded_data == "483a01410100000000000000c54544":
                    state = 'in'
                    response = "成功收到訊息: OK"
                    client_socket.sendall(response.encode())
                    return state
                elif decoded_data == "30303030":
                    pass
                
                else:
                    #state = 'waiting'
                    response = "未知訊息: RETRY"  # 回傳未知訊息的訊息
                    client_socket.sendall(response.encode())
                    logging.info(f"無法回應客戶端 {addr[0]}:{addr[1]} 的數據: {decoded_data}")
                    
        except Exception as e:
            print(f"與客戶端 {addr[0]}:{addr[1]} 連接出現錯誤:", str(e))
            logging.error(f"與客戶端 {addr[0]}:{addr[1]} 連接出現錯誤: {str(e)}")
        
        try:
            print("ret_result =====",ret_result)
            print("sent_result =====",sent_result)
            if ret_result == 'OK':
                response = '483a01570100010000000000dc4544' #Y1
                response = bytes.fromhex(response)
                client_socket.send(response)
                time.sleep(3)
                if not sent_result:
                    #client_socket.sendall(response.encode())
                    sent_result = True  # 更新標誌為 True
                    response = '483a01570000010100000000dc4544'

            if ret_result == 'NG':
                response = '483a01570001010000000000dc4544' #Y2
                response = bytes.fromhex(response)
                client_socket.send(response)
                time.sleep(3)
                if not sent_result:
                    #client_socket.sendall(response.encode())
                    sent_result = True
                    response = '483a01570000010100000000dc4544'

            else:
                logging.info(f"無法傳送結果至客戶端 {addr[0]}:{addr[1]} : {ret_result}")

            ret_result = ''

        except Exception as e:
            print(f"與客戶端 {addr[0]}:{addr[1]} 連接出現錯誤:", str(e))
            logging.error(f"與客戶端 {addr[0]}:{addr[1]} 連接出現錯誤: {str(e)}")


if __name__ == '__main__':
    logname = 'log/'
    logname = logname+"{:%Y-%m-%d}".format(datetime.now())+'_IO.log'
    FORMAT = '%(asctime)s %(levelname)s: %(message)s'
    logging.getLogger("requests").setLevel(logging.WARNING)  
    logging.getLogger("urllib3").setLevel(logging.WARNING)  
    logging.basicConfig(level=logging.DEBUG, filename=logname, filemode='a', format=FORMAT)
    
    #host = '192.168.1.126'  # 主機 IP
    #port = 502  # 通訊端口
    host = '192.168.1.185'
    port = 8000
    state = 'waiting'
    sent_result = False
    ret_result = 'OK'

    while True:
        recv = tcp_server(state, sent_result, ret_result)
        print("State:", recv)
    
