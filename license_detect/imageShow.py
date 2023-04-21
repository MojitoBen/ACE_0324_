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
    sql_fetch_blob_query = "SELECT * from `ai_log_image`"
    cursor.execute(sql_fetch_blob_query)
    records = cursor.fetchall()

    for i in range(len(records)):
            print("Reading record:", i+1)

            record = records[i]
            print("Id = ", record[0])
            print("Name = ", record[1])
            image = record[2]
            print("Storing image on disk...")
            write_file(image, f'photo_{i+1}.png')

 
except mdb.Error as error:
        print("Failed to read BLOB data from MySQL table {}".format(error))
 
finally:
        cursor.close()
        conn.close()
        print("MySQL connection is closed")
 
 
