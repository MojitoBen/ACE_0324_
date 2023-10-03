import requests

url = 'https://notify-api.line.me/api/notify'
token = 'OoPCuvvUYYq8nyV5AXexAMabJ51HR8zo92iew44x6AS'
headers = {
    'Authorization': 'Bearer ' + token    # 設定權杖
}
notify = {
    'message':'測試兩下！'     # 設定要發送的訊息
}
send = requests.post(url, headers=headers, data=notify)   # 使用 POST 方法 #成功時 send = <Response [200]>
