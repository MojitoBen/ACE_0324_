from flask import Flask, request, render_template,Response
import base64
import cv2
import requests
import numpy as np
import logging
import datetime
import time


def apiget_img(url):
    response = requests.get('http://'+url+'')
                #auth = HTTPBasicAuth('admin', '123456'))

    image = np.asarray(bytearray(response.content), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    retval, buffer = cv2.imencode('.png', image)
    image = base64.b64encode(buffer)
    image=  image.decode('utf-8')

    return image

sn1={"TagSN": 1,
 "TagNumber": "",
 "TagImage": ""
 }
 


app = Flask(__name__)
@app.route('/ai_json',methods=['GET','POST']) #get from 旭亨
def response_json():
    try:
        image_1 = apiget_img('192.168.1.185')
        print("image_1",image_1)
    except:
        logging.error('api read org_error', exc_info=True)
        image_1 = '' 
        
    target = request.args.get('value')    
    if target not in  sn1['TagNumber']:
       if len(sn1['TagNumber'])>0:
          sn1['TagNumber'] = sn1['TagNumber'][0]
       else:
          sn1['TagNumber'] =''
    else:
       sn1['TagNumber'] = target
     
       
        
    data = {
     "Master":[{
      "camSN":1,
      "OriImage":image_1
     }
     ],
     "Detail":[sn1]}
    
    result = data
    print("sn1['TagNumber']",sn1['TagNumber'])
    resp = Response(response=result,status=200,content_type='text/html;charset=utf-8')
    resp.headers.add('Access-Control-Allow-Origin', '*')

    return result

@app.route('/send_json_sn1',methods=['GET','POST'])
def send_json_sn1():
    global sn1   
    sn1  = request.get_json()
    result = 'yes'
    resp = Response(response=result,status=200,content_type='text/html;charset=utf-8')
    resp.headers.add('Access-Control-Allow-Origin', '*')
    return result


if __name__ == '__main__':
     logname = 'log/'
     logname = logname+"{:%Y-%m-%d}".format(datetime.datetime.now())+'.log'
     FORMAT = '%(asctime)s %(levelname)s: %(message)s'
     logging.getLogger("requests").setLevel(logging.WARNING)  
     logging.getLogger("urllib3").setLevel(logging.WARNING)  
     #logging.basicConfig(level=logging.ERROR, filename=logname, filemode='a', format=FORMAT) 
 

     while True:
       try:
           app.run('192.168.1.126',8000)
       except:        
         logging.error('camera connecting failed', exc_info=True)
         print('error')
       time.sleep(3)         
