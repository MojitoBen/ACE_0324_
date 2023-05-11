import sys
sys.path.insert(4, r'C:/Users/Asc-user/Documents/YOLO/darknet')
from darknet import make_image, copy_image_from_bytes, load_network, detect_image, free_image, bbox2points
import time
import cv2
import numpy as np
import threading
import queue
import logging
import datetime

objIndex=0
ObjList=[] #(index, px, py)
count_id = 0

TARGET= 'https://cctv1.kctmc.nat.gov.tw/a63a6101'
WEIGHT="C:\\Users\\Asc-user\\Documents\\YOLO\\darknet\\yolov4.weights"
CFG="C:\\Users\\Asc-user\\Documents\\YOLO\\darknet\\cfg\\yolov4.cfg"
DATA="C:\\Users\\Asc-user\\Documents\\YOLO\\darknet\\cfg\\coco.data"
CONFTH=0.5
(WIDTH,HEIGHT)=(640,480)
network, class_names, class_colors = load_network(
    CFG,
    DATA,
    WEIGHT,
    batch_size=1
)
class VideoCapture:
    def __init__(self, name):
        self.cap = cv2.VideoCapture(name)
        self.q = queue.Queue()
        t = threading.Thread(target=self._reader)
        t.daemon = True
        t.start()

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
                time.sleep(1)  
                self.cap.open(TARGET)  
    def read(self):
        return self.q.get()

def draw_boxes(detections, image, colors):
    for label, confidence, bbox in detections:
        left, top, right, bottom = bbox2points(bbox)
        cv2.rectangle(image, (left, top), (right, bottom), colors[label], 1)
        #cv2.putText(image, "{} [{:.2f}]".format(label, float(confidence)), (left, top - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, colors[label], 2)
    return image

def image_detection(image, network, class_names, class_colors, thresh):
    darknet_image = make_image(WIDTH, HEIGHT, 3)  
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image_resized = cv2.resize(image_rgb, (640, 480), interpolation=cv2.INTER_LINEAR)

    copy_image_from_bytes(darknet_image, image_resized.tobytes())
    detections = detect_image(network, class_names, darknet_image, thresh=thresh)
    free_image(darknet_image)
    valid_classes = ["car", "truck"]

    filtered_detections = []
    for detection in detections:
        label = detection[0]
        if label in valid_classes:
            filtered_detections.append(detection)

    if len(filtered_detections) > 0:
        image = draw_boxes(filtered_detections, image_resized, class_colors)
        return cv2.cvtColor(image, cv2.COLOR_BGR2RGB), filtered_detections
    else:
        return cv2.cvtColor(image_resized, cv2.COLOR_BGR2RGB), detections

def TrackObj(newCenterList,ObjList1,objIndex):
    ObjListTemp=[]
    try:
        for i in range(len(newCenterList)):
            newP=(newCenterList[i][0],newCenterList[i][1])
            Obj,objIndex = MatchObj(newP,ObjList1,objIndex)
            ObjListTemp.append(Obj)


        return ObjListTemp, objIndex
    except Exception as err:
        logging.error('check error', exc_info=True)
        print('check error')
        return ObjListTemp,objIndex

def MatchObj(newP,ObjList1,ObjIndex):
    dtlist=[]
    dtIndex=[]
    direction = "moving"
    global count_id
    try:
        for i in range(len(ObjList1)):
            distant = ((ObjList1[i][1]-newP[0])**2 + (ObjList1[i][2]-newP[1])**2)**0.5
            if distant<20:
                dtIndex.append(i)
                dtlist.append(distant)
        
        if len(ObjList1) > 0:
                    xx1, yy1 = ObjList1[i][1], ObjList1[i][2]
                    xx2, yy2 = newP[0], newP[1]
                    dx, dy = xx2 - xx1, yy2 - yy1  
                    '''            
                    if dx > 0 and abs(dx) > abs(dy):
                        direction = "RIGHT"
                    elif dx < 0 and abs(dx) > abs(dy):
                        direction = "LEFT"
                    ''' 
                    if dy > 0 :
                        direction = "DOWN"
                    elif dy < 0 :
                        direction = "UP"
                    elif dy == 0:
                        direction = "stop"

        if dtlist==[]: 
            ObjIndex+=1
            Obj=[ObjIndex,newP[0],newP[1],direction,count_id]
        else: 
            Obj=list(ObjList1[dtIndex[np.argmin(dtlist)]])
            Obj[1],Obj[2] =newP[0],newP[1]
            Obj[3] = direction
            Obj[4] = int(ObjList1[dtIndex[np.argmin(dtlist)]][4]) + 1
        return Obj,ObjIndex

    except:
        logging.error('check error', exc_info=True)
        print('check error')
        return Obj,ObjIndex

def get_direction(obj_list, obj_index):
    up_count = 0
    down_count = 0
    last_direction = ""
    last_obj = None

    for obj in obj_list:
        if obj[0] == obj_index:
            if obj[3] == "UP":
                up_count += 1
                last_direction = "UP"
                last_obj = obj
            elif obj[3] == "DOWN":
                down_count += 1
                last_direction = "DOWN"
                last_obj = obj

    if up_count > down_count:
        return "UP", last_obj
    elif down_count > up_count:
        return "DOWN", last_obj
    else:
        return None, None

sum1=[]
#cap = cv2.VideoCapture(TARGET)
cap = VideoCapture(TARGET)
ObjList=[]

x1, y1 = 0 , 220
x2, y2 = 480, 230
#log
logname = r'C:/Users/User/Desktop/direction/log/'
logname = logname+"{:%Y-%m-%d}".format(datetime.datetime.now())+'.log'
FORMAT = '%(asctime)s %(levelname)s: %(message)s'
logging.basicConfig(level=logging.DEBUG, filename=logname, filemode='a', format=FORMAT) 

last_center = []

while True:
    try:
        frame = cap.read()       
        stime = time.time()

        frame, detections = image_detection(frame, network, class_names, class_colors, CONFTH)
        # detections[n]=(class,confidence,(x,y,w,h))


        DLine = (y1 + y2) // 2
        d_area = cv2.rectangle(frame, (x1, DLine), (x2, DLine), (255,0,0), 1, cv2.LINE_AA)


        newCenterList=[]

        for i in range(len(detections)):    
            (x,y)=(int(detections[i][2][0]),int(detections[i][2][1]))
            if x>x1 and x<x2 and y>y1 and y<y2:                    
                newCenterList.append((x,y))
                cv2.circle(frame,(x,y), 3, (255,255,0), -1)

        #print("newCenterList",newCenterList)

        ObjList,objIndex =TrackObj(newCenterList,ObjList,objIndex)
        for i in range(len(ObjList)):
            #print("ObjList",ObjList)
            cv2.putText(frame, str(ObjList[i][0]), (ObjList[i][1], ObjList[i][2]), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 1)

        targetlist = get_direction(ObjList,objIndex)
        if targetlist != (None,None):
            print(targetlist)
            now = time.localtime()
            timestamp = time.strftime("%m%d%H%M%S", now)
            for idx, center in enumerate(targetlist):
                cv2.imwrite(r'C:/Users/User/Desktop/direction/cars/'+ str(timestamp) + '_' + str(idx) +'.png', frame)

        cv2.imshow('Inference', frame)
        key =  cv2.waitKey(1)
        if key == ord('q'):
            break
        etime = time.time()
        #fps = round(1/(etime-stime),3)
        #sum1.append(fps)
        #print("FPS: {}".format(fps))
    except Exception as err:
        logging.error('check error', exc_info=True)
        print('check error')
        break

pass