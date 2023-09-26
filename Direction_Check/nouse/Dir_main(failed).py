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
from Dir_data import *

#車流辨識用
objIndex=0
ObjList=[] #(index, px, py)
first_points = []
continuous_points = []
count_id = 0
count_up = 0
count_down =0
previous_count_up = 0
previous_count_down = 0
SQL_count_up = 0
SQL_count_down = 0
already_counted = False
leaving_area = True

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
        self.interval = 3600  # 影片生成間隔（30min）
        self.start_time = time.time()  # 記錄開始時間
        self.output_counter = 0  # 影片計數器
        self.output_path = 'D:/YOLO/'
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
        output_filename = f'{self.output_path}output_{self.output_counter}.avi'
        self.out = cv2.VideoWriter(output_filename, self.fourcc, 10.0, (self.width, self.height))

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
class PrintToLog:
    def __init__(self, log_filename):
        self.log = logging.getLogger('print_log')
        self.log.setLevel(logging.INFO)

        self.log_handler = logging.FileHandler(log_filename)
        self.log_handler.setLevel(logging.INFO)

        self.log_formatter = logging.Formatter('%(asctime)s %(message)s')
        self.log_handler.setFormatter(self.log_formatter)

        self.log.addHandler(self.log_handler)

    def write(self, message):
        if message.strip() != '':
            self.log.info(message.strip())

    def flush(self):
        pass
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
def TrackObj(newCenterList,ObjList1,objIndex, leaving_area):
    ObjListTemp=[]
    try:
        for i in range(len(newCenterList)):
            newP=(newCenterList[i][0],newCenterList[i][1])
            Obj,objIndex = MatchObj(newP,ObjList1,objIndex, leaving_area)
            ObjListTemp.append(Obj)

        return ObjListTemp, objIndex
    except Exception as err:
        logging.error('check error', exc_info=True)
        print('check error')
        return ObjListTemp,objIndex

#位置比對程式
def MatchObj(newP, ObjList1, ObjIndex, leaving_area):
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
            if distant < 250:
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
            #
            if dy > 8 and round(movement) > 25:
                direction = "DOWN"
            elif dy < -8 and round(movement) > 25:
                direction = "UP"
            elif -8 <= dy <= 8 or round(movement) < 25:
                direction = "stop"

        if dtlist == []: 
            ObjIndex += 1
            Obj = [ObjIndex, newP[0], newP[1], direction, count_id]
        else:  
            Obj = closest_object
            Obj[1], Obj[2] = newP[0], newP[1]
            Obj[3] = direction
            Obj[4] = leaving_area
        return Obj, ObjIndex

    except:
        logging.error('check error', exc_info=True)
        print('check error')
        return Obj, ObjIndex

def get_first_and_continuous_points(obj_list, obj_index, leaving_area, x1, x2, y1, y2):
    global continuous_points

    for obj in obj_list:
        if obj[0] == obj_index:
            if x1 < obj[1] < x2 and y1 < obj[2] < y2:
                leaving_area = False
                if obj_index not in [o[0] for o in first_points]:
                    first_points.append([obj[0], obj[1], obj[2], obj[3], leaving_area])
                if any(point[0] == obj_index for point in continuous_points):
                    # Update existing object's coordinates and direction
                    for point in continuous_points:
                        if point[0] == obj_index:
                            point[1] = obj[1]
                            point[2] = obj[2]
                            point[3] = obj[3]
                            point[4] = leaving_area
                            break
                else:
                    continuous_points.append([obj[0], obj[1], obj[2], obj[3], leaving_area])
            elif obj_index in [o[0] for o in continuous_points]:
                leaving_area = True
                continuous_points.append([obj[0], obj[1], obj[2], obj[3], leaving_area])

    if len(first_points) > 0:
        return first_points, continuous_points
    else:
        return None, continuous_points




def update_target_list(target, first_points_list, x1, x2, y1, y2):
    global count_up, count_down
    global previous_count_up, previous_count_down
    global continuous_points

    target_id = target[0]
    target_x = target[1]
    target_y = target[2]

    #if not (x1 < target_x < x2 and y1 < target_y < y2):
    for first_point in first_points_list:
        if any(point[0] == target_id and point[4] != first_point[4] for point in continuous_points):
            if first_point[0] == target_id:
                first_point_y = first_point[2]
                if target_y < first_point_y:
                    count_up += 1
                    previous_count_up = target_id
                    print(f'count_up: {count_up} = {target_id} 號車')
                elif target_y > first_point_y:
                    count_down += 1
                    previous_count_down = target_id
                    print(f'count_down: {count_down} = {target_id} 號車')
                first_points_list.remove(first_point)  # 移除已記錄方向的物體
                continuous_points = [point for point in continuous_points if point[0] != target_id]
                break


    return target


sum1=[]
cap = VideoCapture(TARGET)
ObjList=[]

#log
logname = r'C:/Users/Asc-user/Documents/YOLO/direction/log/'
logname = logname+"{:%Y-%m-%d}".format(datetime.datetime.now())+'.log'
FORMAT = '%(asctime)s %(levelname)s: %(message)s'
logging.basicConfig(level=logging.ERROR, filename=logname, filemode='a', format=FORMAT) 
#log_print
print_logname = r'C:/Users/Asc-user/Documents/YOLO/direction/log/print_log/'
print_logname = print_logname + "{:%Y-%m-%d}".format(datetime.datetime.now()) + '.log'
sys.stdout = PrintToLog(print_logname)
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
            newCenterList.append((x,y))
            if x>x1 and x<x2 and y>y1 and y<y2:
                cv2.circle(frame,(x,y), 3, (255,255,0), -1)
            
        ObjList,objIndex =TrackObj(newCenterList,ObjList,objIndex,leaving_area)
        first_points_list,continuous_points = get_first_and_continuous_points(ObjList, objIndex,leaving_area, x1, x2, y1, y2)
        if first_points_list is not None:
            print("first_points_list:",first_points_list)
            print("continuous_points:",continuous_points)
        # 進行記數和區域檢查
        if first_points_list is not None:
            for target in continuous_points:
                if target is not None:
                    target = update_target_list(target,first_points_list,x1,x2,y1,y2)
                    now = time.localtime()
                    timestamp = time.strftime("%m%d%H%M%S", now)
                    # cv2.imwrite(r'C:/Users/Asc-user/Documents/YOLO/direction/cars/'+ str(timestamp) + '_' + str(obj[3]) +'.png', frame)

                    base64_data = img2base64(frame)
                    data = (base64_data, timestamp, target[3])
                    '''
                    if count_up != SQL_count_up or count_down != SQL_count_down:
                        insert_query = "INSERT INTO dir_test (Image, Daytime, Dir) VALUES (%s, %s, %s)"
                        added_thread = threading.Thread(target=upload_SQL, args=(insert_query, data))
                        added_thread.start()
                        SQL_count_up = count_up
                        SQL_count_down = count_down
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
        
        if out is not None :
            success = out.write(frame)  # 將影像寫入影片
        
    except Exception as err:
        logging.error('check error', exc_info=True)
        print('check error')
        break

if cap.out is not None:
    cap.out.release()
cv2.destroyAllWindows()
pass
