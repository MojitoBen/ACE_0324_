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
            ret, frame = self.cap.read()
            if not ret:
                break
            if not self.q.empty():
                try:
                    self.q.get_nowait()   # discard previous (unprocessed) frame
                except queue.Empty:
                    pass
            self.q.put(frame)

    def read(self):
        return self.q.get()


def startrun():
    text=''
    cap = VideoCapture('rtsp://admin:djs123456@192.168.1.108:554/cam/realmonitor?channel=2&subtype=0')
    while True:
        frame = cap.read()
        w,h,c  = frame.shape
        try:
           text, image = steel_detect_2(frame)
        except:
           logging.error('camera connecting failed', exc_info=True)
           print('error')
        print(text)
        frame = cv2.resize(frame, (h//4, w//4), interpolation=cv2.INTER_CUBIC)
        cv2.imshow('www',frame)            
        if cv2.waitKey(1) == ord('q'):
            break


    cv2.destroyAllWindows()
    cap.release()     

    
if __name__ == '__main__':

     logname = 'log/'
     logname = logname+"{:%Y-%m-%d}".format(datetime.datetime.now())+'.log'
     FORMAT = '%(asctime)s %(levelname)s: %(message)s'
     logging.basicConfig(level=logging.DEBUG, filename=logname, filemode='a', format=FORMAT)      
     while True:
       try:
         startrun()
       except:
         logging.error('camera connecting failed', exc_info=True)
         print('error')
       time.sleep(3)
