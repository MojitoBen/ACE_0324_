import cv2
import json
from steel_yolo import*
import base64
import requests
import time
import datetime
import logging
import queue
import threading
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
                    raise Exception("Could not read frame")
                    logging.error('camera connecting failed', exc_info=True)
                if not self.q.empty():
                    try:
                        self.q.get_nowait()   # discard previous (unprocessed) frame
                    except queue.Empty:
                        pass
                self.q.put(frame)
            except Exception as e:
                print(f"Error: {e}")
                time.sleep(1)  # wait before retrying
                self.cap.open('rtsp://192.168.1.202:554/profile1')  # reopen the connection
                logging.error('camera connecting failed', exc_info=True)

    def read(self):
        return self.q.get()

def img2base64(image):
    retval, buffer = cv2.imencode('.png', image)
    image = base64.b64encode(buffer)
    image = image.decode('utf-8')
    
    return image


def startrun():
    List1 = []
    temp1=''
    timeset = 0
    ip_address = '192.168.1.111'
    cap = VideoCapture('rtsp://admin:djs123456@192.168.1.108:554/cam/realmonitor?channel=2&subtype=0')
    
    try:
    
        while True:
            start = time.time()
            frame = cap.read()
            print(start)
            #frame = cv2.imread(r'D:\head\01274_2023-02-10_2_org.png')
            w,h,c  = frame.shape
            try:
                raw_list, image = steel_detect_2(frame)
            except:
                logging.error('steel_detect failed', exc_info=True)
                text = ''
                print('error')
                pass
            clear_data = True
            try:
                image = img2base64(image)
            except:
                text=''
                logging.error('img2base64 failed', exc_info=True)
            for text in raw_list:
                if len(text)>5:
                    if not any(text in s for s in List1):
                            #List1.append([text,1])
                            List1 = [[text, 1]]
                    else:
                        '''
                        columns = list(zip(*List1))
                        post = columns[0].index(text)
                        List1[post][1]+=1
                        '''
                        pass

                    List1 = sorted(List1,reverse = True, key = lambda s: s[1])
                    upload1 = []
                    if len(List1)>0:
                        for tmp in List1:
                            upload1.append(tmp[0])

                        print('upload1',upload1)                 
                        data = {'TagSN': 3,
                                'TagNumber': upload1,
                                'TagImage': image
                                }
                        try:
                            requests.post('http://'+ip_address+':8000/send_json_sn3', json=data, timeout=2)
                        except:
                            logging.error('camera connecting failed', exc_info=True)
                            pass
                        if len(List1)>=5:
                            List1.pop(0)
                else:
                    List1=[]
                    data = {'TagSN': 3,
                            'TagNumber': '',
                            'TagImage': ''  }
                    clear_data == False

            if clear_data == False:
                    if timeset > 5:            
                        List1=[]
                        data = {'TagSN': 3,
                                'TagNumber': '',
                                'TagImage': ''  }
                        try:
                            requests.post('http://'+ip_address+':8000/send_json_sn3', json=data, timeout=2)  
                        except:
                            logging.error('camera connecting failed', exc_info=True)
                            pass         
                        timeset = 0            
                    else:
                        timeset = timeset+time.time()-start


            #frame = cv2.resize(frame, (h//3, w//3), interpolation=cv2.INTER_CUBIC)
            #cv2.imshow('www',frame)            
            #if cv2.waitKey(1) == ord('q'):
                #break

    except:
        logging.error('camera connecting failed', exc_info=True)  
        cv2.destroyAllWindows()
        cap.release()     
    
if __name__ == '__main__':

    logname = 'log/'
    logname = logname+"{:%Y-%m-%d}".format(datetime.datetime.now())+'.log'
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
        time.sleep(3)
