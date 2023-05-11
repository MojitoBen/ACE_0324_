import pymysql
import logging

def connect():
    try:
        f = open('C:/Users/Asc-user/Documents/YOLO/direction/SQL_server.txt')
        keylist=[]
        for line in f.readlines():
            a = line.split('#')
            keylist.append(a[0])
        f.close
        connection=pymysql.connect(host=keylist[0],
                       user=keylist[1],
                       password=keylist[2],
                       db=keylist[3],
                       charset=keylist[4],
                       cursorclass=pymysql.cursors.DictCursor)
        return connection
    except:
        logging.error('database connecting failed')
        print('database connecting failed')

def Get_time():
    connection = connect()
    with connection.cursor() as cursor:
        sql = "select now() AS dbTime"
        cursor = connection.cursor()
        cursor.execute(sql)
        result = cursor.fetchall()
        for timeler in result:
            time_start = timeler['dbTime']
        
        return time_start