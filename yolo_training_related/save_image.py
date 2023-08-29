'''
將圖片資料寫進資料庫
'''
import pymysql
import base64

# 讀取 .jfif 圖片並轉換為二進位數據
with open('su.jfif', 'rb') as file:
    image_data = file.read()
    base64_data = base64.b64encode(image_data)

conn = pymysql.connect(
            host='192.168.XX.XXX',
            user='XXXXXX',
            password='XXXXXX',
            database='XXXXXX',
            port = XXXXX
        )
#conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute('INSERT INTO hero_area_img (Map) VALUES (%s)', (base64_data,)) #選擇插入圖片資料位置

conn.commit()
conn.close()
