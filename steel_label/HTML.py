from flask import Flask, request, render_template, Response
from base64_1 import *
import logging

host = '192.168.1.126'
port = 8000

app = Flask(__name__)

@app.route('/send_json_sn1', methods=['GET', 'POST'])
def send_json_sn1():
    data = request.get_json()
    print("sn1:",list(data.items())[:2])  
    resp = Response(response="yes", status=200, content_type='application/json')
    resp.headers.add('Access-Control-Allow-Origin', '*')
    return render_template('json.html', data=data)
@app.route('/send_json_sn2', methods=['GET', 'POST'])

def send_json_sn2():
    data = request.get_json()
    print("sn2:",list(data.items())[:2])
    resp = Response(response="yes", status=200, content_type='application/json')
    resp.headers.add('Access-Control-Allow-Origin', '*')
    return render_template('json.html', data=data)
    
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)  # 設定日誌級別
    app.run(host, port)
