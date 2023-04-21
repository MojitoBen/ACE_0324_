from database import * 
import numpy as np
import cv2
import glob
import os
import sys
import time 
import logging
from yolo import detect
import queue
import threading
import datetime
import copy
sys.path.insert(1,r'C:\Users\Asc-user\Documents\YOLO\darknet')   #導入darknet的path
from darknet import *


def channl_open(cam,ai_id,thresh,channel,area,qu_plate,qu_org):
        List=[]
        incar=''
        temp=''
        timer=0
        temptime = 0
        timestart=0
        clearlist,temp_log=False,False
        while True:
            start=time.time()
            
            status='Plate'   
            img = cv2.imread("C:\\Users\\Asc-user\\Documents\\YOLO\\darknet\\data\\car2.jpg")
            #img = cam.read()            
            w,h,c = img.shape
            org = copy.copy(img)
 
            text,plate = detect(img,area)  #AI辨識  return 車牌號碼/車牌縮圖
            if len(text)>=3:         #車牌號碼大於4
                #print('temptime',temptime,text)
                timestart = timestart+temptime
                if not any(text in s for s in List): #不存在LIST裡的車牌就加入
                    List.append([text,0])
                else:
                    columns = list(zip(*List))      #存在就加次數
                    post = columns[0].index(text)
                    List[post][1]+=1

            List = sorted(List,reverse = True, key = lambda s: s[1])

            if len(List)>0 and List[0][1]>=thresh:  #達到門檻就開始上傳
                incar =List[0][0]

            if temp != incar and len(incar)>4:   #看門檻是否與上筆重覆
                print(List)                   
                temp=incar
                stay_time=0
                clearlist = True
                timer = time.time()

                
                if len(plate)>0:   #上傳縮圖
                    
                        cv2.imwrite(r'C:/Users/Asc-user/Documents/YOLO/darknet/mainpicture/'+incar+'.png',plate)
                        msg = cv2.imencode(".jpg", plate, [cv2.IMWRITE_JPEG_QUALITY, qu_plate])[1]
                        plate = (np.array(msg)).tobytes()
                
                msg = cv2.imencode(".jpg", org, [cv2.IMWRITE_JPEG_QUALITY, qu_org])[1]
                images = (np.array(msg)).tobytes()
                text = incar
                '''
                added_thread = threading.Thread(target = insql,args=(ai_id,channel,status,text,images,plate,))
                added_thread.start()
                '''
                print(timestart)



                if len(List)>0 and List[0][1]>=thresh: #清空LIST與縮圖
                    List,org,img=[],[],[]
                    timestart = 0


                    
            incar,text = '',''
            if  clearlist == True and time.time() - timer >5:   #時間超過5秒也清空
                    timer=0
                    clearlist = False
                    temp = ''
                    List,org,img=[],[],[]



            end = time.time()
            temptime = end- start       
            #img = cv2.resize(img, (h//1, w//1), interpolation=cv2.INTER_CUBIC)               
            #cv2.imshow('car_detect',img)
            if cv2.waitKey(1) == ord('q'):
                    starting = False
                    return starting 
                    break

        cv2.destroyAllWindows()




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
                    raise Exception("Start to show frame..")
                if not self.q.empty():
                    try:
                        self.q.get_nowait()   # discard previous (unprocessed) frame
                    except queue.Empty:
                        pass
                self.q.put(frame)
            except Exception as e:
                print(f"Error: {e}")
                time.sleep(1)  # wait before retrying
                self.cap.open('在此輸入rtsp')  # reopen the connection
    def read(self):
        return self.q.get()

if __name__ == '__main__':
        pid = str(os.getpid())    
        print('A1')
        '''
        print(pid)
        with open(r'C:/Users/uaer/Documents/darknet-master/A1/kill_pid.txt', 'w') as f:
            f.write(pid)
        '''
        logname = r'C:/Users/Asc-user/Documents/YOLO/darknet/log'
        logname = logname+"{:%Y-%m-%d}".format(datetime.datetime.now())+'.log'
        FORMAT = '%(asctime)s %(levelname)s: %(message)s'
        logging.basicConfig(level=logging.DEBUG, filename=logname, filemode='a', format=FORMAT)         
        try:
            AI_ID = '20202020'     #AI的ID參數不能重覆
           
            cam_ip,thresh,channel,area,qu_plate,qu_org = Get_p(AI_ID)   #讀ID相對應的DB參數            
            ai_id = str(AI_ID)
            channel = str(channel)
            print(cam_ip)
            #cam = VideoCapture('https://cctv3.kctmc.nat.gov.tw/77eb2b78')
            cam = VideoCapture(cam_ip)   #load rtsp
            
            print(area)
            starting=True
        except:
            logging.error('camera connecting failed', exc_info=True)
            print('camera connecting failed')     
            starting=False    
                
        while starting==True:
            try:
                starting = channl_open(cam,ai_id,thresh,channel,area,qu_plate,qu_org) #開始跑影象
            except:
                logging.error('camera connecting failed', exc_info=True)
                print('camera connecting failed')

        

               
