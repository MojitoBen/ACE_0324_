'''
鋼捲噴字的'無SQL'、'無繼電器'版本
用來完善整個流程跟測試權重狀況
搭配IO_in使用
'''
import cv2
from steel_rotate180 import *
from SQL_functions import *
import base64
import time
import datetime
import logging
import queue
import threading
import socket
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
host = '192.168.1.XXXXXXX'
port = 8000
decoded_data = None
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(1) #max_listen_num
recognition_event = threading.Event()

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
                    self.cap.open(r'--------->rtsp或影片路徑<-----------')
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
                self.cap.open(r'--------->rtsp或影片路徑<-----------')  # reopen the connection
                logging.error('camera connecting failed', exc_info=True)

    def read(self):
        return self.q.get()

def img2base64(image, quality=30):

    retval, buffer = cv2.imencode('.jpg', image, [cv2.IMWRITE_JPEG_QUALITY, quality])
    image_data = base64.b64encode(buffer)
    image_data = image_data.decode('utf-8')

    return image_data

def startrun():
    cap = VideoCapture(r'--------->rtsp或影片路徑<-----------')
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
    global recognition_event
    
    tcp_thread = threading.Thread(target=tcp_server, daemon=True)
    tcp_thread.start()
    while True:
        frame = cap.read()
        
        w, h, c = frame.shape
        #tcp_thread = threading.Thread(target=tcp_server, daemon=True)
        #tcp_thread.start()
        #state = 'in'
        if state == 'in':
            if not update_IO_time:
                IO_time()
                update_IO_time = True
                if update_IO_time == True:
                    print("IO : OK")
            start= time.time()
            try:
                raw_list, image_list, shid, position= steel_detect_1(frame)
            except Exception as e:
                logging.error(f"Error: {e}", exc_info=True)
                print(f"Error: {e}")
                pass
            if raw_list and raw_list != prev_raw_list:
                if len(raw_list[0]) >= 5:
                    prev_raw_list = raw_list
                    print("prev_raw_list", prev_raw_list)
                    detected = True
            for text in prev_raw_list:
                if len(text)>= 5:
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
                                #SN_num,result, PaintNum, match_text= get_L1Data(tmp[0])
                                SN_num = '999'
                                result = 'OK'
                                PaintNum = '5821219' #根據測試影片調整 --------->rtsp或影片路徑的鋼捲號碼<-----------
                                match_text = '5821219' #根據測試影片調整 --------->rtsp或影片路徑的鋼捲號碼<-----------
                            if match_text:
                                upload1 = match_text
                        
                        print("upload1:", upload1)
                        print("SN:", SN_num)
                        print("PaintNum:",PaintNum)

            #image1 = img2base64(image_list[0])
            #org1 = img2base64(image_list[1])

            end= time.time()
            timeset = end-start+timeset+0.3
            if timeset >= 15 and detected:
                if not upload1:
                    upload1 = prev_raw_list[0]
                #update_snaptime()
                print("shid : ", shid)
                #result = cam1_upload(SN_num, PaintNum, upload1, image1, org1, result, shid)
                result = "OK"
                ret_result = result
                resY = True
                recognition_event.set()
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
            if timeset >= 15 and not detected:
                print("shid : ", shid)
                org_img = img2base64(image_list[1])
                #update_snaptime_and_none(org_img, shid)
                if shid == 'hid':
                    ret_result = 'OK'
                else:
                    ret_result = 'OK' #改成沒辨識到也直接OK
                resY = True
                recognition_event.set()
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
    global decoded_data
    global recognition_event

    while True:
        client_socket, addr = server_socket.accept()
        print(f"connected with : {addr[0]}:{addr[1]}")

        try:
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                
                decoded_data = data.hex()

                print(f"get data from {addr[0]}:{addr[1]} : {decoded_data}")

                if decoded_data == '483a01410100000000000000c54544':
                    state = 'in'
                    print('辨識中')
                if decoded_data == '30303030':
                    print("Reg package")
                if decoded_data == '483a01540000010100000000d94544':
                    print('.')
                if decoded_data == '483a01410100000000000000c54544':
                    print('out')
                if decoded_data == '483a01410100000000000000c44544':
                    print('.')
                if decoded_data == '483a01540000010100000000d94544':
                    print('.')
                
                else:
                    #state = 'waiting'
                    logging.info(f"cannot respond {addr[0]}:{addr[1]} data : {decoded_data}")

                #time.sleep(12) #9/8新增，這樣才能順利讓result回傳，不然thread會卡住等到下次訊號進來才回傳
                recognition_event.wait()

                if resY:
                    try:
                        print("ret_result",ret_result)
                        if ret_result == 'OK':
                            response = '483a01570100010000000000dc4544' #Y1
                            response = bytes.fromhex(response)
                            client_socket.send(response)
                            time.sleep(3)
                            if not sent_result:
                                #client_socket.sendall(response.encode())
                                sent_result = True  
                                response = '483a01570000010100000000dc4544'
                                response = bytes.fromhex(response)
                                client_socket.send(response)
                                resY = False

                        if ret_result == 'NG' or ret_result == 'null' or not ret_result or ret_result == '':
                            response = '483a01570001010000000000dc4544' #Y2
                            response = bytes.fromhex(response)
                            client_socket.send(response)
                            time.sleep(3)
                            if not sent_result:
                                #client_socket.sendall(response.encode())
                                sent_result = True
                                response = '483a01570000010100000000dc4544'
                                response = bytes.fromhex(response)
                                client_socket.send(response)
                                resY = False

                        else:
                            logging.info(f"cannot sent to {addr[0]}:{addr[1]} : {ret_result}")

                        ret_result = ''

                    except Exception as e:
                        print(f"respond error {addr[0]}:{addr[1]} :", str(e))
                        logging.error(f"respond error {addr[0]}:{addr[1]} : {str(e)}")
                
                recognition_event.clear()

        except Exception as e:
            print(f"connected with {addr[0]}:{addr[1]} failed:", str(e))
            logging.error(f"connected with {addr[0]}:{addr[1]} failed: {str(e)}")


if __name__ == '__main__':

    logname = 'log/'
    logname = logname+"{:%Y-%m-%d}".format(datetime.datetime.now())+'_cam1.log'
    FORMAT = '%(asctime)s %(levelname)s: %(message)s'
    logging.getLogger("requests").setLevel(logging.WARNING)  
    logging.getLogger("urllib3").setLevel(logging.WARNING)  
    logging.basicConfig(level=logging.DEBUG, filename=logname, filemode='a', format=FORMAT)
    recognition_event.clear()
    while True:
        try:
            startrun()

        except:
            logging.error('camera connecting failed', exc_info=True)
            print('error')
            time.sleep(1)
