'''
資料庫blob檔案轉存成圖片
'''
import pymysql
import numpy as np
import cv2
import base64

conn = pymysql.connect(
    host='192.168.xx.xxx',
    user='qadmin',
    password='3753890',
    database='asc_ai'
)

cursor = conn.cursor()

query = "SELECT * FROM steel_paint_image" #blob位置
cursor.execute(query)

results = cursor.fetchall()

idx = 0 
total_images = len(results)

while True:
    result = results[idx]
    image_name = result[0]
    image_data = result[3]
    #image_Daytime = str(result[2])
    #image_Dir = str(result[3])
    #info = f"{image_name}_{image_Daytime}_{image_Dir}"
    info = image_name

    decoded_data = base64.b64decode(image_data)
    nparr = np.frombuffer(decoded_data, np.uint8)
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    #cv2.namedWindow(str(info), cv2.WINDOW_NORMAL)  # Convert image_name to string
    #cv2.resizeWindow(str(info), 800, 600)  # Convert image_name to string
    #cv2.imshow(str(info), image)  # Convert image_name to string

    save_path = f"./708_1043/{info}.png" #png或jpg或其他
    cv2.imwrite(save_path, image)
    idx += 1
    '''
    key = cv2.waitKey(0)
    if key == ord('q') or idx == total_images - 1:  # Press 'q' or last image reached
        break
    elif key == ord('n'):  # Press 'n' for next image
        idx += 1

    cv2.destroyWindow(str(info))
    '''
cv2.destroyAllWindows()
cursor.close()
conn.close()
