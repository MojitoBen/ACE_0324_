import pymysql.cursors
import cv2
import numpy as np
import logging

def connect():
    try:
        f = open(r'C:/Users/Asc-user/Documents/YOLO/darknet/main/data_server.txt')
        keylist=[]
        for line in f.readlines():
            a = line.split('#')
            keylist.append(a[0])
        f.close
        print(keylist)
        connection=pymysql.connect(host=keylist[0],
                       user=keylist[1],
                       password=keylist[2],
                       db=keylist[3],
                       charset='',
                       cursorclass=pymysql.cursors.DictCursor)
        return connection 	         
    except:
        logging.error('database connecting failed')
        print('database connecting failed')

        
        
def Get_p(AI_ID):
    connection = connect()
    cursor = connection.cursor()
    sql = "SELECT * FROM ai_paremeters WHERE ID="+AI_ID
    cursor.execute(sql)
    results = cursor.fetchall()
    b=[]
    for j in range(1,5):
        for i in results:
            cam_ip = i['RTSP']
            channel = i['Channel']
            thresh = i['Thresh']
            point = i['Point_'+str(j)].split("x", 1)
            qu_plate = i['Qu_plate']
            qu_org = i['Qu_org']
        b.append(point)
    area = np.array([b],dtype = np.int32)
    
    return cam_ip,thresh,channel,area,qu_plate,qu_org       
            
        
        
def Get_ip(AI_ID):
    connection = connect()
    cursor = connection.cursor()
    sql = "SELECT * FROM ai_paremeters WHERE ID="+AI_ID
    cursor.execute(sql)
    results = cursor.fetchall()


    for i in results:
        ip = i['IP']
        cam_ip = i['RTSP']

    return ip,cam_ip     
                
        
        
        
        
def insql(ai_id,channel,status,text,images,plate):
    try:
        connection = connect()
        with connection.cursor() as cursor:
            sql = "INSERT INTO `ai_log`(`AI_ID`,`AI_Channel`,`EventType`,`Message`) VALUES ('"+str(ai_id)+"','"+str(channel)+"','"+status+"','"+text+"')"
            cursor=connection.cursor()
            cursor.execute(sql)
            connection.commit()
            result = cursor.lastrowid

        sql = "INSERT INTO `ai_log_image`(`LogID`,`ImageType`,`Image`) VALUES ('"+str(result)+"','Scene',%s)"
        args = images
        cursor=connection.cursor()
        cursor.execute(sql,args)
        connection.commit()
        print('in uploaded')

        if  len(plate)>0:
            sql = "INSERT INTO `ai_log_image`(`LogID`,`ImageType`,`Image`) VALUES ('"+str(result)+"','Plate',%s)"
            args = plate
            cursor=connection.cursor()
            cursor.execute(sql,args)
            connection.commit()
    except:
        logging.error('failed to upload', exc_info=True)
        print('failed to upload')
        pass         
            
            
