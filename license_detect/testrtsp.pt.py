import cv2
import queue
import threading
import time
import gc
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
                if not self.q.empty():
                    try:
                        self.q.get_nowait()   # discard previous (unprocessed) frame
                    except queue.Empty:
                        pass
                self.q.put(frame)
            except Exception as e:
                print(f"Error: {e}")
                time.sleep(1)  # wait before retrying
                self.cap.open(self.name)  # reopen the connection

cap = cv2.VideoCapture('rtsp://admin:Admin1234@192.168.1.152:554/cam/realmonitor?channel=1&subtype=0')

count=0
while True:
    start = time.time()
    _,frame =  cap.read()
    count+=1
    w,h, _ = frame.shape
    end = time.time()
    if count ==30:   #clear
        gc.collect()
        count=0
    tmp = end-start
    print(1/tmp)
    
    #print(w,h)
    frame = cv2.resize(frame, (h//2, w//2), interpolation=cv2.INTER_AREA)
    cv2.imshow('frME',frame)
    if  cv2.waitKey(1) & 0xFF == ord('q'):
       break


    
cap.release()
cv2.destroyAllWindows()    
