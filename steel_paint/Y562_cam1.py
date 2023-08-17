import cv2
from steel_rotate180 import *
from IO_check import *
from SQL_functions import *
import base64
import time
import datetime
import logging
import queue
import threading
import requests

prev_raw_list = []
state = 'waiting'
timeset = 0

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

def img2base64(image):
    retval, buffer = cv2.imencode('.png', image)
    image = base64.b64encode(buffer)
    image = image.decode('utf-8')
    
    return image
def run_tcp_server():
    global state
    while True:
        state = tcp_server(state)
def startrun():
    #cap = VideoCapture(r'C:/Users/Asc-user/Documents/YOLO/Y562_train/tall.mp4') # 測試用#########
    #cap = VideoCapture(r'C:/Users/Asc-user/Documents/YOLO/Y562_train/test.mp4') # 測試用#########
    cap = VideoCapture(r'C:/Users/Asc-user/Desktop/123.mp4') # 測試用#########
    List1 = []
    raw_list = [[]]
    global prev_raw_list
    global state
    global timeset
    detected = False

    while True:
        frame = cap.read()

        w, h, c = frame.shape
        #tcp_thread = threading.Thread(target=run_tcp_server, daemon=True)
        #tcp_thread.start()
        state = 'in'
        if state == 'in':
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
            if raw_list and raw_list[0]:
                text_to_display = str(raw_list[0])
                if text_to_display:
                    cv2.putText(frame, text_to_display, (180, 200), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 255), 2, cv2.LINE_AA)
            
            # 顯示影像
            resized_frame = cv2.resize(frame, (h // 2, w // 2), interpolation=cv2.INTER_CUBIC)
            cv2.imshow('test', resized_frame)
            if cv2.waitKey(1) == ord('q'):
                break
            
            timeset = timeset+0.3

            if timeset >= 15 and detected:
                raw_list = [[]]
                prev_raw_list = []
                state = 'waiting'
                List1 = []
                timeset = 0
                detected = False
            if timeset >= 15 and not detected:

                raw_list = [[]]
                prev_raw_list = []
                List1 = []
                state = 'waiting'
                timeset = 0
        
        else:
            # 如果state不是'in'，仍然顯示影像
            resized_frame = cv2.resize(frame, (h // 2, w // 2), interpolation=cv2.INTER_CUBIC)
            cv2.imshow('test', resized_frame)
            if cv2.waitKey(1) == ord('q'):
                break
            timeset = 0
        
if __name__ == '__main__':

    logname = 'C:/Users/Asc-user/Documents/YOLO/Y562_2PLCM/log/'
    logname = logname+"{:%Y-%m-%d}".format(datetime.datetime.now())+'_cam1.log'
    FORMAT = '%(asctime)s %(levelname)s: %(message)s'
    logging.getLogger("requests").setLevel(logging.WARNING)  
    logging.getLogger("urllib3").setLevel(logging.WARNING)  
    logging.basicConfig(level=logging.DEBUG, filename=logname, filemode='a', format=FORMAT)

    while True:
        try:
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