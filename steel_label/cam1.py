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
                self.cap.open('rtsp://192.168.1.201:554/profile1')  # reopen the connection
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
    List2 = []
    temp1,temp2='',''

    timesetA, timesetB =0,0
    ip_address = '192.168.1.111'
    cap = VideoCapture('rtsp://admin:djs123456@192.168.1.108:554/cam/realmonitor?channel=1&subtype=0')
    while True:
        start = time.time()
        frame = cap.read()



        #frame = cv2.imread(r'D:\back\00060_2023-03-20_3_org.png')
        w,h,c  = frame.shape
        try:
           raw_list,image_list = steel_detect_1(frame)
        except:
           logging.error('camera connecting failed', exc_info=True)
           print('error')
           pass
        clear_dataA , clear_dataB = True,True
        listnum = 0
        print(raw_list)
        for text_list in raw_list:
                for text in text_list:
                     if len(text)>5 and listnum==0:
                        clear_dataA == False
                        timesetA = 0
                        if not any(text in s for s in List1):
                                List1.append([text,1])
                        else:
                            columns = list(zip(*List1))
                            post = columns[0].index(text)
                            List1[post][1]+=1

                        List1 = sorted(List1,reverse = True, key = lambda s: s[1])
                        upload1 = []
                        if len(List1)>0:
                                for tmp in List1:
                                    upload1.append(tmp[0])
                                
                                print('upload1',upload1)
                                image = img2base64(image_list[listnum])                    
                                data = {'TagSN': 1,
                                        'TagNumber': upload1,
                                        'TagImage': image
                                        }
                                try:
                                   requests.post('http://'+ip_address+':8000/send_json_sn1', json=data , timeout=2)
                                except:
                                   logging.error('camera connecting failed', exc_info=True)
                                   pass
                                #List1=[]
                                if len(List1)>=5:
                                   List1.pop(0)


                     if len(text)>5 and listnum==1:
                        clear_dataB == False
                        timesetB = 0            
                        if not any(text in s for s in List2):
                            List2.append([text,1])
                        else:
                            columns = list(zip(*List2))
                            post = columns[0].index(text)
                            List2[post][1]+=1

                        List2 = sorted(List2,reverse = True, key = lambda s: s[1])
                        upload2 = []
                        if len(List2)>0:               
                                for tmp in List2:
                                    #print('tmp',tmp[0])
                                    upload2.append(tmp[0])
                           
                                print('upload2',upload2)  
                                 
                                image = img2base64(image_list[listnum])
                                data = {'TagSN': 2,
                                        'TagNumber': upload2,
                                        'TagImage': image
                                        }
                                try:
                                   requests.post('http://'+ip_address+':8000/send_json_sn2', json=data, timeout=2)
                                except:
                                   logging.error('camera connecting failed', exc_info=True)
                                   pass
                                if len(List1)>=5:
                                   List1.pop(0)


                     listnum+=1

        

        if clear_dataA == 5:
            if timesetA > 5:
                List1=[]
                data = {'TagSN': 1,
                        'TagNumber': '',
                        'TagImage': ''  }
                
                try:
                    requests.post('http://'+ip_address+':8000/send_json_sn1', json=data, timeout=2) 
                except:
                    logging.error('camera connecting failed', exc_info=True)
                    pass         
                #print(data)         
                timesetA = 0
            else: 
                timesetA = timesetA+time.time()-start

        if clear_dataB == 5:
            if timesetB > 5:            
                List2=[]
                data = {'TagSN': 2,
                        'TagNumber': '',
                        'TagImage': ''  }

                try:
                    requests.post('http://'+ip_address+':8000/send_json_sn2', json=data, timeout=2)
                except:
                    logging.error('camera connecting failed', exc_info=True)
                    pass
                #print(data)            
                timesetB = 0            
            else:
                timesetB = timesetB+time.time()-start


        #frame = cv2.resize(frame, (h//3, w//3), interpolation=cv2.INTER_CUBIC)
        #cv2.imshow('www',frame)            
        #if cv2.waitKey(1) == ord('q'):
           #break


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
