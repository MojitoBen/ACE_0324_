import cv2

def get_resolution(rtsp_url):
    cap = cv2.VideoCapture(rtsp_url)
    if not cap.isOpened():
        print("無法連接到攝影機")
        return

    # 從攝影機讀取第一個影格
    ret, frame = cap.read()
    if not ret:
        print("無法讀取影格")
        cap.release()
        return

    # 獲取影格的解析度
    height, width, _ = frame.shape
    print("解析度：{}x{}".format(width, height))

    # 釋放攝影機資源
    cap.release()

# 測試程式碼
#rtsp_url = "rtsp://admin:Admin1234@192.168.1.145:554/cam/realmonitor?channel=1&subtype=0"
rtsp_url = "rtsp://admin:Admin1234@192.168.1.151:554/Streaming/Channels/101"
#rtsp_url = "https://cctv1.kctmc.nat.gov.tw/a63a6101"
get_resolution(rtsp_url)
