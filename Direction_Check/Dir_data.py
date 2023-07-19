import logging
import datetime

def Get_area():
    try:
        f = open('Area.txt')
        Coordinate_list=[]
        for line in f.readlines():
            a = line.split(':')
            Coordinate_list.append(a[1].strip())
        f.close()
        return Coordinate_list
    except:
        logging.error('get coordinate failed')
        print('get coordinate failed')

def Get_data():
    try:
        f = open('Data.txt')
        Data_list=[]
        for line in f.readlines():
            a = line.split('=')
            Data_list.append(a[1].strip())
        f.close()
        return Data_list
    except:
        logging.error('get data failed')
        print('get data failed')

#log
logname = r'C:/Users/Asc-user/Documents/YOLO/direction/log/'
logname = logname+"{:%Y-%m-%d}".format(datetime.datetime.now())+'.log'
FORMAT = '%(asctime)s %(levelname)s: %(message)s'
logging.basicConfig(level=logging.DEBUG, filename=logname, filemode='a', format=FORMAT)