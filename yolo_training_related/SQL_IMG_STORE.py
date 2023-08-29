import pymysql
import numpy as np
import cv2
import base64

# 連接 MySQL 資料庫
conn = pymysql.connect(
    host='192.168.1.185',
    user='qadmin',
    password='3753890',
    database='asc_ai'
)

# 建立資料庫游標
cursor = conn.cursor()

# 執行 SQL 查詢，取得所有圖片及其名稱
query = "SELECT * FROM steel_paint_image"
cursor.execute(query)

# 取得所有查詢結果
results = cursor.fetchall()

# 逐一處理每個結果
idx = 0  # 用於追蹤當前顯示的圖片索引
total_images = len(results)  # 總圖片數量

while True:
    # 取得圖片和名稱
    result = results[idx]
    image_name = result[0]
    image_data = result[3]
    #image_Daytime = str(result[2])
    #image_Dir = str(result[3])
    #info = f"{image_name}_{image_Daytime}_{image_Dir}"
    info = image_name

    decoded_data = base64.b64decode(image_data)

    # 將解碼後的資料轉換為 NumPy 陣列
    nparr = np.frombuffer(decoded_data, np.uint8)

    # 使用 OpenCV 解碼圖片資料
    image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # 顯示圖片，以名稱作為視窗標題
    #cv2.namedWindow(str(info), cv2.WINDOW_NORMAL)  # Convert image_name to string
    #cv2.resizeWindow(str(info), 800, 600)  # Convert image_name to string
    #cv2.imshow(str(info), image)  # Convert image_name to string

    # 儲存圖片成 PNG
    save_path = f"./708_1043/{info}.png"
    cv2.imwrite(save_path, image)
    idx += 1
    '''
    # 等待按鍵輸入
    key = cv2.waitKey(0)

    if key == ord('q') or idx == total_images - 1:  # Press 'q' or last image reached
        break
    elif key == ord('n'):  # Press 'n' for next image
        idx += 1

    # 關閉當前視窗
    cv2.destroyWindow(str(info))
    '''

# 關閉所有視窗
cv2.destroyAllWindows()

# 關閉資料庫游標
cursor.close()
# 關閉資料庫連接
conn.close()
