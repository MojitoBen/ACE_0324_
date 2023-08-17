import cv2
from steel_rotate180 import *
from SQL_functions import *
import base64
import time
import datetime
import logging
import queue
import threading
from IO_in import *
import requests

raw_list = [[]]
prev_raw_list = []
List1 = []
upload1 = ''
match_text = ''
ret_result = ''
state = 'waiting'
sent_result = False
detected = False
update_IO_time = False
resY = False
timeset = 0
host = '192.168.1.185'
port = 8000
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))  # 綁定 IP 地址和端口
server_socket.listen(1)  # 監聽最大連接數量

class VideoCapture:
    def __init__(self, name):
        self.cap = cv2.VideoCapture(name)
        self.q = queue.Queue()
        t = threading.Thread(target=self._reader)
        t.daemon = True
        t.start()

  # read frames as soon as they are available, keeping only most recent one
    def _reader(self):
        while True:
            try:
                ret, frame = self.cap.read()
                if not ret:
                    self.cap.open(r'C:/Users/Asc-user/Desktop/123.mp4')
                    #raise Exception("Could not read frame, VideoCapture _error")
                    #logging.error('Could not read frame', exc_info=True)
                    continue
                if not self.q.empty():
                    try:
                        self.q.get_nowait()   # discard previous (unprocessed) frame
                    except queue.Empty:
                        pass
                self.q.put(frame)
            except Exception as e:
                print(f"Error: {e}")
                time.sleep(1)  # wait before retrying
                self.cap.open(r'C:/Users/Asc-user/Desktop/123.mp4')  # reopen the connection
                logging.error('camera connecting failed', exc_info=True)

    def read(self):
        return self.q.get()

def img2base64(image, quality=30):
    # 將圖片轉換為壓縮格式（JPEG）
    retval, buffer = cv2.imencode('.jpg', image, [cv2.IMWRITE_JPEG_QUALITY, quality])

    # 將壓縮後的數據轉換為base64編碼
    image_data = base64.b64encode(buffer)
    image_data = image_data.decode('utf-8')

    return image_data

'''
def run_tcp_server():
    global state
    while True:
        state = tcp_server(state, sent_result, ret_result)
    '''
def startrun():
    cap = VideoCapture(r'C:/Users/Asc-user/Desktop/123.mp4') # 測試用#########
    global List1 
    global raw_list
    global prev_raw_list
    global state
    global timeset
    global match_text
    global upload1
    global sent_result
    global detected
    global ret_result
    global update_IO_time
    global server_socket
    global resY

    while True:
        frame = cap.read()
        
        w, h, c = frame.shape
        tcp_thread = threading.Thread(target=tcp_server, daemon=True)
        tcp_thread.start()
        #state = 'in'
        if state == 'in':
            if not update_IO_time:
                IO_time()
                update_IO_time = True
            start= time.time()
            try:
                raw_list, image_list = steel_detect_1(frame)
            except Exception as e:
                logging.error(f"Error: {e}", exc_info=True)
                print(f"Error: {e}")
                pass
            if raw_list and raw_list != prev_raw_list:
                if len(raw_list[0]) >= 7:
                    prev_raw_list = raw_list
                    print("prev_raw_list", prev_raw_list)
                    detected = True
            for text in prev_raw_list:
                if len(text)>= 7:
                    if not any(text in n for n in List1):
                        List1.append([text, 1])
                    else:
                        columns = list(zip(*List1))
                        post = columns[0].index(text)
                        List1[post][1]+=1

                    List1 = sorted(List1,reverse = True, key = lambda s: s[1])
                    if len(List1)>0:
                        for tmp in List1:
                            for i in range(len(List1)):
                                SN_num,result, PaintNum, match_text= get_L1Data(tmp[0])
                            if match_text:
                                upload1 = match_text
                        
                        print("upload1:", upload1)
                        print("SN:", SN_num)
                        print("PaintNum:",PaintNum)

            image1 = img2base64(image_list[0])
            org1 = img2base64(image_list[1])

            end= time.time()
            timeset = end-start+timeset+0.3
            print("timeset:",timeset)
            if timeset >= 12 and detected: #辨識完成，回傳資料進資料庫
                if not upload1:
                    upload1 = prev_raw_list[0] #有辨識到SID且有數字但數字是錯的
                update_snaptime()
                result = cam1_upload(SN_num, PaintNum, upload1, image1, org1, result)
                ret_result = result
                resY = True
                raw_list = [[]]
                prev_raw_list = []
                List1 = []
                match_text = ''
                upload1 = ''
                state = 'waiting'
                sent_result = False
                timeset = 0
                detected = False
                update_IO_time = False
            if timeset >= 12 and not detected:
                org_img = img2base64(image_list[1])
                update_snaptime_and_none(org_img)
                ret_result = 'NG'
                resY = True
                raw_list = [[]]
                prev_raw_list = []
                List1 = []
                match_text = ''
                upload1 = ''
                state = 'waiting'
                sent_result = False
                update_IO_time = False
                timeset = 0

def tcp_server():
    global state
    global sent_result
    global ret_result
    global timeset
    global resY

    while True:
        client_socket, addr = server_socket.accept()  # 接受客戶端連接
        print(f"與繼電器 {addr[0]}:{addr[1]} 建立連接")

        try:
            while True:
                data = client_socket.recv(1024)  # 接收數據
                if not data:
                    break
                
                print("data:",data)

                # 解碼數據為16位元的HEX
                decoded_data = data.hex()

                print(f"收到來自客戶端 {addr[0]}:{addr[1]} 的數據: {decoded_data}")

                if decoded_data == '483a01410100000000000000c54544':
                    state = 'in'
                elif decoded_data == '30303030':
                    print("Reg package")
                
                else:
                    #state = 'waiting'
                    logging.info(f"無法回應客戶端 {addr[0]}:{addr[1]} 的數據: {decoded_data}")

                if resY:
                    try:
                        print("ret_result =====",ret_result)
                        print("sent_result =====",sent_result)
                        if ret_result == 'OK':
                            response = '483a01570100010000000000dc4544' #Y1
                            response = bytes.fromhex(response)
                            client_socket.send(response)
                            print("Y1亮")
                            time.sleep(3)
                            if not sent_result:
                                #client_socket.sendall(response.encode())
                                sent_result = True  # 更新標誌為 True
                                response = '483a01570000010100000000dc4544'
                                response = bytes.fromhex(response)
                                client_socket.send(response)
                                print("全暗")
                                resY = False

                        if ret_result == 'NG':
                            response = '483a01570001010000000000dc4544' #Y2
                            response = bytes.fromhex(response)
                            client_socket.send(response)
                            print("Y2亮")
                            time.sleep(3)
                            if not sent_result:
                                #client_socket.sendall(response.encode())
                                sent_result = True
                                response = '483a01570000010100000000dc4544'
                                response = bytes.fromhex(response)
                                client_socket.send(response)
                                print("全暗")
                                resY = False

                        else:
                            logging.info(f"無法傳送結果至客戶端 {addr[0]}:{addr[1]} : {ret_result}")

                        ret_result = ''

                    except Exception as e:
                        print(f"回應客戶端 {addr[0]}:{addr[1]} 出現錯誤:", str(e))
                        logging.error(f"回應客戶端 {addr[0]}:{addr[1]} 出現錯誤: {str(e)}")

        except Exception as e:
            print(f"與客戶端 {addr[0]}:{addr[1]} 連接出現錯誤:", str(e))
            logging.error(f"與客戶端 {addr[0]}:{addr[1]} 連接出現錯誤: {str(e)}")


if __name__ == '__main__':

    logname = 'C:/Users/Asc-user/Documents/YOLO/Y562_2PLCM/噴字測試_0809/log/'
    logname = logname+"{:%Y-%m-%d}".format(datetime.datetime.now())+'_cam1.log'
    FORMAT = '%(asctime)s %(levelname)s: %(message)s'
    logging.getLogger("requests").setLevel(logging.WARNING)  
    logging.getLogger("urllib3").setLevel(logging.WARNING)  
    logging.basicConfig(level=logging.DEBUG, filename=logname, filemode='a', format=FORMAT)

    while True:
        try:
            decoded_data = '5145088'

            insert_data(decoded_data)
            time.sleep(2)
            startrun()

        except:
            logging.error('camera connecting failed', exc_info=True)
            print('error')
            time.sleep(1)

'''
#有需要將資料上傳給L1的話，插進程式碼:
ip_address = '上傳ip'
data = {'Cam_SN': cam1,
        'Steel_Number': upload1,
        'Number_Image': image1,
        'Steel_Image' : org1
        }
try:
    requests.post('http://'+ip_address+':8000/send_json_sn1', json=data, timeout=2) 
except:
    logging.error('upload data failed', exc_info=True)
    pass     
''' 