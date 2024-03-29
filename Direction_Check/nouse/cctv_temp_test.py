import sys
import time
import cv2
import numpy as np
import threading
import queue
import logging
import datetime
import base64
import time
from MySQL import *
from CCTV_data import *
import copy

#車流辨識用
objIndex=0
ObjList=[] #(index, px, py)
target_list = []
count_id = 0
count_up = 0
count_down =0
previous_count_up = 0
previous_count_down = 0
already_counted = False

Data_list = Get_data()
TARGET= Data_list[0]
WEIGHT= Data_list[1]
CFG= Data_list[2]
DATA= Data_list[3]

sys.path.insert(4, r'C:/Users/Asc-user/Documents/YOLO/darknet')
from darknet import make_image, copy_image_from_bytes, load_network, detect_image, free_image, bbox2points

CONFTH=0.5
(WIDTH,HEIGHT)=(1920,1080)
network, class_names, class_colors = load_network(
    CFG,
    DATA,
    WEIGHT,
    batch_size=1
)
#判斷區域
Coordinate_list = Get_area()
x1, y1 = int(Coordinate_list[0]) , int(Coordinate_list[1])
x2, y2 = int(Coordinate_list[2]) , int(Coordinate_list[3])

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
    org = image.copy()
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
    valid_classes = Data_list[4]

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
            print("ObjListTemp",ObjListTemp)


        return ObjListTemp, objIndex
    except Exception as err:
        logging.error('check error', exc_info=True)
        print('check error')
        return ObjListTemp,objIndex

#位置比對程式
def MatchObj(newP, ObjList1, ObjIndex):
    dtlist = []
    dtIndex = []
    direction = " "
    global count_id

    try:
        # 只考慮前幾個畫面的物件進行比對
        num_frames_to_compare = 2
        start_index = max(0, len(ObjList1) - num_frames_to_compare)

        # 計算物件與前幾個畫面物件的距離
        for i in range(start_index, len(ObjList1)):
            distant = ((ObjList1[i][1] - newP[0]) ** 2 + (ObjList1[i][2] - newP[1]) ** 2) ** 0.5
            if distant < 300:
                dtIndex.append(i)
                dtlist.append(distant)

        if len(dtlist) > 0:
            # 找出最小距離對應的物件
            min_distance_index = dtIndex[np.argmin(dtlist)]
            closest_object = ObjList1[min_distance_index]

            xx1, yy1 = closest_object[1], closest_object[2]
            xx2, yy2 = newP[0], newP[1]
            dx, dy = xx2 - xx1, yy2 - yy1
            movement = abs(((closest_object[1] - newP[0]) ** 2 + (closest_object[2] - newP[1]) ** 2) ** 0.5)

            if dy > 10 and round(movement) > 20:
                direction = "DOWN"
            elif dy < -10 and round(movement) > 20:
                direction = "UP"
            elif -10 <= dy <= 10 or round(movement) < 20:
                direction = "stop"

        # 設定回傳
        if dtlist == []:  # 新物件
            ObjIndex += 1
            Obj = [ObjIndex, newP[0], newP[1], direction, count_id]
        else:  
            closest_object_copy = copy.copy(closest_object)
            closest_object_copy[1], closest_object_copy[2] = newP[0], newP[1]
            closest_object_copy[3] = direction
            closest_object_copy[4] = int(closest_object_copy[4]) + 1
            Obj = closest_object_copy

        return Obj, ObjIndex
    except:
        logging.error('check error', exc_info=True)
        print('check error')
        return Obj, ObjIndex

def get_direction(obj_list, obj_index):
    up_count = 0
    down_count = 0
    stop_count = 0
    last_objs = []

    for obj in obj_list:
        if obj[0] == obj_index:
            if obj[3] == "UP":
                up_count += 1
                last_objs.append(obj)
            elif obj[3] == "DOWN":
                down_count += 1
                last_objs.append(obj)
            elif obj[3] == "stop":
                stop_count += 1
                last_objs.append(obj)
    
    if up_count > down_count and up_count > stop_count:
        return last_objs
    elif down_count > up_count and  down_count > stop_count:
        return last_objs
    elif stop_count > up_count and stop_count > down_count:
        return None
    else:
        return None
    
def update_target_list(target):
    global count_up, count_down
    global previous_count_up, previous_count_down
    global target_list
    
    for t in target:
        if len(t) >= 4 and t[0] == target[0] and t[3] == target[3] and t[3] != "stop":
            return
    
    target_list.append(target)
    print("target_list:", target_list)
    
    for targets in target_list:
        if targets[0][3] == "UP":
            count_up += 1
            print("count_up", count_up)
        elif targets[0][3] == "DOWN":
            count_down += 1
            print("count_down", count_down)
    
    if len(target_list) > 10:
        target_list = target_list[-10:]



    
sum1=[]
cap = VideoCapture(TARGET)
ObjList=[]

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
def img2base64(image):
    retval, buffer = cv2.imencode('.png', image)
    image = base64.b64encode(buffer)
    image = image.decode('utf-8')
    
    return image


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
        target = get_direction(ObjList, objIndex)
        if target is not None:
            update_target_list(target)
            now = time.localtime()
            timestamp = time.strftime("%m%d%H%M%S", now)
            print("target",target)

            # cv2.imwrite(r'C:/Users/Asc-user/Documents/YOLO/direction/cars/'+ str(timestamp) + '_' + str(obj[3]) +'.png', frame)

            #base64_data = img2base64(frame)
            #data = (base64_data, timestamp, obj[3])
            '''
            if count_up != previous_count_up or count_down != previous_count_down:
                insert_query = "INSERT INTO dir_test (Image, Daytime, Dir) VALUES (%s, %s, %s)"
                added_thread = threading.Thread(target = upload_SQL,args=(insert_query, data))
                added_thread.start()
            previous_count_up = count_up
            previous_count_down = count_down
            '''
        '''
        for o in ObjList:
            if o[3] == 'stop':
                cv2.rectangle(frame, (o[1]-100,o[2]-100), (o[1]+100,o[2]+100), (255, 255, 255), -1)
        '''
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