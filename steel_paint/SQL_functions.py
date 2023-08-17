import pymysql
from datetime import datetime
import logging
import os

def connected():
    host = "192.168.XX.XXX"
    user = "XXXXXXX"
    password = "XXXXXXX"
    db = "XXXXXXX"
    charset = "utf8"

    connection = pymysql.connect(host=host, user=user, password=password, db=db, charset=charset)
    return connection

def cam1_upload(SN, PaintNum, text, image, org, result):
    connection = connected()
    cursor = connection.cursor()
    if PaintNum == text:
        result = "OK"
    if PaintNum != text:
        result = "NG"
    # 更新 steel_paint_detail 表中的 PaintNum
    update_query = "UPDATE steel_paint_detail SET PaintNum = %s WHERE MasterSN = %s"# AND PaintPos = 'Paint1'"
    update_params = (text, SN)
    cursor.execute(update_query, update_params)

    # 更新 steel_paint_detail 表中的 Image
    update_query = "UPDATE steel_paint_detail SET Image = %s WHERE MasterSN = %s"# AND PaintPos = 'Paint1'"
    update_params = (image, SN)
    cursor.execute(update_query, update_params)

    # 更新 steel_paint_image 表中的 Image
    update_query = "UPDATE steel_paint_image SET Image = %s WHERE MasterSN = %s"# AND ImageType = 'Cam1'"
    update_params = (org, SN)
    cursor.execute(update_query, update_params)

    # 更新 steel_paint_test 表中的 Result
    update_query = "UPDATE steel_paint_test SET Result = %s WHERE SN = %s"
    update_params = (result, SN)
    cursor.execute(update_query, update_params)

    connection.commit()

    cursor.close()
    connection.close()
    
    return result

def get_L1Data(text):
    connection = connected()
    cursor = connection.cursor()

    query = ""
    params = ()

    if text:
        query = "SELECT SN, PaintNum, Result FROM steel_paint_test WHERE PaintNum = %s"
        params = (text,)

    cursor.execute(query, params)
    row = cursor.fetchone()

    Num = None
    result = None
    PaintNum = None

    if row:
        Num = row[0]
        PaintNum = row[1]
        result = row[2]
        match_text = text
    else:  # 如果text為空且未找到相應的資料，則再進行額外的查詢
        cursor.execute("SELECT SN, PaintNum, Result FROM steel_paint_test ORDER BY SN DESC LIMIT 1")
        row = cursor.fetchone()
        if row:
            Num = row[0]
            PaintNum = row[1]
            result = row[2]
            match_text = None

    cursor.close()
    connection.close()

    return Num, result, PaintNum, match_text


def insert_data(decoded_data):

    connection = connected()
    cursor = connection.cursor()

    try:
        # L1資料插入 steel_paint_test 
        insert_query = "INSERT INTO steel_paint_test (PaintNum) VALUES (%s)"
        insert_params = (decoded_data,)
        cursor.execute(insert_query, insert_params)

        sn = cursor.lastrowid

        # 只插入一個 Paint1
        insert_query = "INSERT INTO steel_paint_detail (MasterSN, PaintPos) VALUES (%s, %s)"
        insert_params = (sn, "Paint1")
        cursor.execute(insert_query, insert_params)

        # 只插入一個 Cam1
        insert_query = "INSERT INTO steel_paint_image (MasterSN, ImageType) VALUES (%s, %s)"
        insert_params = (sn, "Cam1")
        cursor.execute(insert_query, insert_params)

        # 紀錄收到L1時間點
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        insert_query = "INSERT INTO steel_paint_time_record (link_SN, L1_data) VALUES (%s, %s)"
        insert_params = (sn, current_time)
        cursor.execute(insert_query, insert_params)

        connection.commit()

    except Exception as e:
        print("插入時發生錯誤:", str(e))
        connection.rollback()

    finally:
        cursor.close()
        connection.close()

def IO_time():
    connection = connected()
    cursor = connection.cursor()

    try:
        select_query = "SELECT MAX(link_SN) FROM steel_paint_time_record"
        cursor.execute(select_query)
        sn = cursor.fetchone()[0]

        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        update_query = f"UPDATE steel_paint_time_record SET IO_signal = '{current_time}' WHERE link_SN = {sn}"
        cursor.execute(update_query)

        connection.commit()

    except Exception as e:
        print("插入時發生錯誤:", str(e))
        connection.rollback()

    finally:
        cursor.close()
        connection.close()

def update_snaptime():

    connection = connected()
    cursor = connection.cursor()

    try:
        # 查詢 steel_paint_test 表中最後一行的 SN 和 SnapTime
        select_query = "SELECT SN, SnapTime FROM steel_paint_test ORDER BY SN DESC LIMIT 1"
        cursor.execute(select_query)
        row = cursor.fetchone()
        if row is not None:  # 檢查是否有資料
            sn = row[0]
            snaptime = row[1]

            # 判斷 SnapTime 是否為 None，如果是就進行更新
            if snaptime is None:
                # 更新 steel_paint_test 表中最後一行的 SnapTime
                update_query = "UPDATE steel_paint_test SET SnapTime = %s WHERE SN = %s"
                current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                update_params = (current_time, sn)
                cursor.execute(update_query, update_params)

                # 提交更改
                connection.commit()

        else:
            logging.info("steel_paint_test 無數據可 UPDATE")
            print("steel_paint_test 無數據可 UPDATE")

    except Exception as e:
        print("更新 SnapTime 時發生錯誤:", str(e))
        connection.rollback()

    finally:
        cursor.close()
        connection.close()

def update_snaptime_and_none(org_img):

    connection = connected()
    cursor = connection.cursor()

    try:
        # 查詢 steel_paint_test 表中最後一行的 SN 和 SnapTime
        select_query = "SELECT SN, SnapTime FROM steel_paint_test ORDER BY SN DESC LIMIT 1"
        cursor.execute(select_query)
        row = cursor.fetchone()
        if row is not None:  # 檢查是否有資料
            SN = row[0]
            snaptime = row[1]

            # 判斷 SnapTime 是否為 None，如果是就進行更新
            if snaptime is None:
                # 更新 steel_paint_test 表中最後一行的 SnapTime
                update_query = "UPDATE steel_paint_test SET SnapTime = %s WHERE SN = %s"
                current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                update_params = (current_time, SN)
                cursor.execute(update_query, update_params)

                result = "NG"
                PaintNum = "None"
                image = "None"
                org = org_img

                update_query = "UPDATE steel_paint_detail SET PaintNum = %s WHERE MasterSN = %s"# AND PaintPos = 'Paint1'"
                update_params = (PaintNum, SN)
                cursor.execute(update_query, update_params)

                # 更新 steel_paint_detail 表中的 Image
                update_query = "UPDATE steel_paint_detail SET Image = %s WHERE MasterSN = %s"# AND PaintPos = 'Paint1'"
                update_params = (image, SN)
                cursor.execute(update_query, update_params)

                # 更新 steel_paint_image 表中的 Image
                update_query = "UPDATE steel_paint_image SET Image = %s WHERE MasterSN = %s"# AND ImageType = 'Cam1'"
                update_params = (org, SN)
                cursor.execute(update_query, update_params)

                # 更新 steel_paint_test 表中的 Result
                update_query = "UPDATE steel_paint_test SET Result = %s WHERE SN = %s"
                update_params = (result, SN)
                cursor.execute(update_query, update_params)
                # 提交更改
                connection.commit()
            else:
                logging.info("無需更新")
                print("無需更新")
        else:
            logging.info("steel_paint_test 無數據可 UPDATE")
            print("steel_paint_test 無數據可 UPDATE")

    except Exception as e:
        print("更新時發生錯誤:", str(e))
        connection.rollback()

    finally:
        cursor.close()
        connection.close()

logname = 'log/'
logname = logname+"{:%Y-%m-%d}".format(datetime.now())+'_SQL_f.log'
log_folder = os.path.dirname(logname)
if not os.path.exists(log_folder):
    os.makedirs(log_folder)
FORMAT = '%(asctime)s %(levelname)s: %(message)s'
logging.getLogger("requests").setLevel(logging.WARNING)  
logging.getLogger("urllib3").setLevel(logging.WARNING)  
logging.basicConfig(level=logging.DEBUG, filename=logname, filemode='a', format=FORMAT)

if __name__ == '__main__':
    decoded_data = '1203485'
    insert_data(decoded_data)
    #update_snaptime()
