import os
import subprocess
import time
import requests

def read_address():
    f = open('./host_ip.txt')
    keylist=[]
    for line in f.readlines():
      a = line.split('#')
      keylist.append(a[0])
    f.close
    address = keylist[0]
    
    return address

ip_address = read_address()
while True:
    try:
        time.sleep(5)
        with open('./PID1.txt') as f:
            PID = f.readlines()

        if not PID :  
            subprocess.call(['gnome-terminal','--','./restart.desktop'])
            time.sleep(5)
            continue

        cmd = 'ps -ef | grep '+PID[0]+' | grep -v grep'
        if os.system(cmd)== 0:
            print(PID)
            print('yes')
        else: 
            subprocess.call(['gnome-terminal','--','./restart.desktop'])
            time.sleep(5)
            print('run') 
            
            
    except:
        print('no PID.txt')
        pass



  
