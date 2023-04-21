import MySQLdb as mdb 
import sys

def write_file(data, filename):
    # Convert binary data to proper format and write it on Hard Disk
    with open(filename, 'wb') as file:
        file.write(data)

try:

    conn = mdb.connect(host='192.168.1.185',user='qadmin', 
        passwd='3753890', db='asc_pms_tai')
    cursor = conn.cursor()
    sql_fetch_blob_query = "SELECT * from `ai_log_image` where `LogID` = %s"
 
    cursor.execute(sql_fetch_blob_query, '4')
    record = cursor.fetchall()
    for row in record:
        print("Id = ", row[0], )
        print("Name = ", row[1])
        image = row[2]
        print("Storing employee image and bio-data on disk \n")
        write_file(image, 'photo4.png')

 
except mdb.Error as error:
        print("Failed to read BLOB data from MySQL table {}".format(error))
 
finally:
        cursor.close()
        conn.close()
        print("MySQL connection is closed")
 
 
