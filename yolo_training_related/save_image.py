import pymysql
import base64

# 讀取 .jfif 圖片並轉換為二進位數據
with open('su.jfif', 'rb') as file:
    image_data = file.read()
    base64_data = base64.b64encode(image_data)

conn = pymysql.connect(
            host='192.168.1.185',
            user='ben',
            password=',./kl;iop890',
            database='summon',
            port = 3305
        )
#conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# 插入圖片資料
cursor.execute('INSERT INTO hero_area_img (Map) VALUES (%s)', (base64_data,))

# 提交更改並關閉資料庫連接
conn.commit()
conn.close()