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
from MySQL import *
import pickle
import time


#車流辨識用
objIndex=0
ObjList=[] #(index, px, py)
target_list = []
count_id = 0
count_up = 0
count_down =0


TARGET= 'rtsp://admin:Admin1234@192.168.1.151:554/Streaming/Channels/101'
#TARGET= r'C:/Users/Asc-user/Documents/YOLO/direction/avi/0526-01.mp4'
WEIGHT="C:\\Users\\Asc-user\\Documents\\YOLO\\darknet\\yolov4.weights"
CFG="C:\\Users\\Asc-user\\Documents\\YOLO\\darknet\\cfg\\yolov4.cfg"
DATA="C:\\Users\\Asc-user\\Documents\\YOLO\\darknet\\cfg\\coco.data"
CONFTH=0.5
(WIDTH,HEIGHT)=(1920,1080)
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
        self.width = WIDTH    # 取得影像寬度
        self.height = HEIGHT  # 取得影像高度
        self.fourcc = cv2.VideoWriter_fourcc(*'MJPG')               # 設定影片的格式為 MJPG(x)XVID
        self.out = None  # 初始化影片寫入器
        self.interval = 1500  # 影片生成間隔（30秒）
        self.start_time = time.time()  # 記錄開始時間
        self.output_counter = 0  # 影片計數器
        self.initialize_writer()  # 初始化影片寫入器
        self.read_thread = threading.Thread(target=self._reader)  # 影像讀取執行緒
        self.read_thread.daemon = True
        self.read_thread.start()

    def _reader(self):
        while True:
            try:
                ret, frame = self.cap.read()
                if not ret:
                    raise Exception("Failed to read frame")
                if not self.q.empty():
                    try:
                        self.q.get_nowait()
                    except queue.Empty:
                        pass
                self.q.put(frame)
            except Exception as e:
                print(f"Error: {e}")
                time.sleep(1)
                self.cap.open(TARGET)

    def initialize_writer(self):
        self.out = cv2.VideoWriter(f'output_{self.output_counter}.avi', self.fourcc, 10.0, (self.width, self.height))

    def generate_video(self):
        elapsed_time = time.time() - self.start_time
        if elapsed_time >= self.interval:
            if self.out is not None:
                self.out.release()
            self.output_counter += 1
            self.initialize_writer()
            self.start_time = time.time()

    def read(self):
        self.generate_video()
        return self.q.get(), self.out

def draw_boxes(detections, image, colors):
    images_list = []
    org = image.copy() #同時也需要沒畫線的圖時可以用copy的乾淨原圖
    for label, confidence, bbox in detections:
        left, top, right, bottom = bbox2points(bbox)
        cv2.rectangle(image, (left, top), (right, bottom), colors[label], 1)
        #cv2.putText(image, "{} [{:.2f}]".format(label, float(confidence)), (left, top - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, colors[label], 2)

        car_img = org[max(0, top):min(bottom, image.shape[0]), max(0, left):min(right, image.shape[1])]
        gray = cv2.cvtColor(car_img, cv2.COLOR_BGR2GRAY)
        gray = cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB)
        images_list.append(car_img)

    return image,images_list

def image_detection(image, network, class_names, class_colors, thresh):
    darknet_image = make_image(WIDTH, HEIGHT, 3)  
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image_resized = cv2.resize(image_rgb, (1920, 1080), interpolation=cv2.INTER_LINEAR)

    copy_image_from_bytes(darknet_image, image_resized.tobytes())
    detections = detect_image(network, class_names, darknet_image, thresh=thresh)
    free_image(darknet_image)
    valid_classes = ["car", "truck","motorbike"]

    filtered_detections = []
    for detection in detections:
        label = detection[0]
        if label in valid_classes:
            filtered_detections.append(detection)

    if len(filtered_detections) > 0:
        image, car_image = draw_boxes(filtered_detections, image_resized, class_colors)
        return cv2.cvtColor(image, cv2.COLOR_BGR2RGB), filtered_detections, car_image
    else:
        return cv2.cvtColor(image_resized, cv2.COLOR_BGR2RGB), detections, None

#物件追蹤程式
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

#位置比對程式
def MatchObj(newP,ObjList1,ObjIndex):
    dtlist=[]
    dtIndex=[]
    direction = " "
    global count_id
    try:
    #計算物件與所有前一畫面物件的距離
        for i in range(len(ObjList1)):
            distant = ((ObjList1[i][1]-newP[0])**2 + (ObjList1[i][2]-newP[1])**2)**0.5
            if distant<300:
                #print("distant",distant)
                dtIndex.append(i)
                dtlist.append(distant)
        
        if len(ObjList1) > 0:
                    xx1, yy1 = ObjList1[i][1], ObjList1[i][2]
                    xx2, yy2 = newP[0], newP[1]
                    dx, dy = xx2 - xx1, yy2 - yy1  
                    movement = abs(((ObjList1[i][1]-newP[0])**2 + (ObjList1[i][2]-newP[1])**2)**0.5)
                    '''            
                    if dx > 0 and abs(dx) > abs(dy):
                        direction = "RIGHT"
                    elif dx < 0 and abs(dx) > abs(dy):
                        direction = "LEFT"
                    ''' 
                    print("round(movement)",round(movement))
                    if dy > 0 and round(movement) > 12:
                        direction = "DOWN"
                    elif dy < 0 and round(movement) > 12:
                        direction = "UP"
                    elif dy == 0 or round(movement) < 12:
                        direction = "stop"
                        
        #設定回傳
        if dtlist==[]: #新物件
            ObjIndex+=1
            Obj=[ObjIndex,newP[0],newP[1],direction,count_id]
        else: #舊物件
            #找出最小距離
            Obj=list(ObjList1[dtIndex[np.argmin(dtlist)]])
            Obj[1],Obj[2] =newP[0],newP[1]
            Obj[3] = direction
            Obj[4] = int(ObjList1[dtIndex[np.argmin(dtlist)]][4]) + 1
        '''
        for i in range(len(ObjList1)):
            if ObjList1[i][0] == Obj[0] and ObjList1[i][3] != "moving" and ObjList1[i][3] != "stop":
                Obj[3] = "moving"
                break
        '''
        return Obj, ObjIndex


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
        return last_obj
    elif down_count > up_count:
        return last_obj
    else:
        return None, None
    
def update_target_list(target):
    global count_up, count_down
    
    for t in target_list:
        if t[0] == target[0] and t[3] == target[3]:
            return
    target_list.append(target)

    if len(target_list) > 10:
        target_list.pop(0)

    # 更新計數器
    if target[3] == 'UP':
        count_up += 1
        print("count_up",count_up)
    elif target[3] == 'DOWN':
        count_down += 1
        print("count_down",count_down)

sum1=[]
#cap = cv2.VideoCapture(TARGET)
cap = VideoCapture(TARGET)
ObjList=[]

#判斷區域
x1, y1 = 534 , 670
x2, y2 = 1373 , 820
#log
logname = r'C:/Users/Asc-user/Documents/YOLO/direction/log/'
logname = logname+"{:%Y-%m-%d}".format(datetime.datetime.now())+'.log'
FORMAT = '%(asctime)s %(levelname)s: %(message)s'
logging.basicConfig(level=logging.DEBUG, filename=logname, filemode='a', format=FORMAT) 
#SQL
def upload_SQL(insert_query, data):
    try:
        cnx = connect()
        cursor = cnx.cursor()
        cursor.execute(insert_query, data)
        cnx.commit()
    except:
        logging.error('failed to upload', exc_info=True)
        print('failed to upload')
        pass



while True:
    try:
        frame, out = cap.read()     
        stime = time.time()

        #                                                  影像   神經網路   物件名稱      顏色         信任度
        frame, detections, car_imagelist = image_detection(frame, network, class_names, class_colors, CONFTH)
        # detections[n]=(class,信任度,(x,y,w,h))

        DLine = (y1 + y2) // 2 #偵測區域的中線
        d_area = cv2.rectangle(frame, (x1, DLine), (x2, DLine), (0,0,255), 1, cv2.LINE_AA)

        #新畫面中所有物件中心點        
        newCenterList=[]
        for i in range(len(detections)):    
            #進判斷區域加中心點
            (x,y)=(int(detections[i][2][0]),int(detections[i][2][1]))
            if x>x1 and x<x2 and y>y1 and y<y2:
                newCenterList.append((x,y))
                cv2.circle(frame,(x,y), 3, (255,255,0), -1)

        ObjList,objIndex =TrackObj(newCenterList,ObjList,objIndex)
        #for i in range(len(ObjList)): #標註編號
            #print("ObjList",ObjList)
            #cv2.putText(frame, str(ObjList[i][0]), (ObjList[i][1], ObjList[i][2]), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 1)
        #print("ObjList",ObjList)
        target = get_direction(ObjList,objIndex)
        if target != (None,None):
            now = time.localtime()
            timestamp = time.strftime("%m%d%H%M%S", now)
            #print(target)
            update_target_list(target)
            #print("target_list",target_list)

            #cv2.imwrite(r'C:/Users/Asc-user/Documents/YOLO/direction/cars/'+ str(timestamp) + '_' + str(target[3]) +'.png', frame)
            '''
            car_img = np.array(car_imagelist, dtype=np.uint8)
            for car_img in enumerate(car_imagelist):
                cv2.imwrite(r'C:/Users/Asc-user/Documents/YOLO/direction/car_closeup/'+ str(timestamp) + '_' + str(target[3]) +'.png', car_img)
            '''
            img_bytes = pickle.dumps(frame)
            
            data = (img_bytes, timestamp, target[3])

            insert_query = "INSERT INTO dir_test (Image, Daytime, Dir) VALUES (%s, %s, %s)"
            #added_thread = threading.Thread(target = upload_SQL,args=(insert_query, data))
            #added_thread.start()

        UP = cv2.putText(frame, "UP: {}".format(count_up), (20, 920), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 255, 0),thickness=4)
        DOWN = cv2.putText(frame, "DOWN: {}".format(count_down), (20, 1010), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 255, 0),thickness=4)


        cv2.namedWindow("Inference", 0)
        cv2.resizeWindow("Inference", 800, 600)
        cv2.imshow('Inference', frame)
        key =  cv2.waitKey(1)
        if key == ord('q'):
            break
        etime = time.time()
        #fps = round(1/(etime-stime),3)
        #sum1.append(fps)
        #print("FPS: {}".format(fps))
        '''
        if out is not None :
            success = out.write(frame)  # 將影像寫入影片
        '''
    except Exception as err:
        logging.error('check error', exc_info=True)
        print('check error')
        break

if cap.out is not None:
    cap.out.release()
cv2.destroyAllWindows()
pass