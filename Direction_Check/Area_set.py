import cv2
import os

def get_coordinates_from_video(video_path):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("cam open failed.")
        return []

    # 獲取原始影片的解析度
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    # 設定顯示視窗的大小
    window_width = 800
    window_height = 600

    scale_x = frame_width / window_width
    scale_y = frame_height / window_height

    cv2.namedWindow("Video", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Video", window_width, window_height)

    coordinates = []  # saved coordinates

    def mouse_handler(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            original_x = int(x * scale_x)
            original_y = int(y * scale_y)
            coordinates.append((original_x, original_y))

    cv2.setMouseCallback("Video", mouse_handler)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.resize(frame, (window_width, window_height))

        for i in range(len(coordinates) // 2):
            x1, y1 = coordinates[2 * i]
            x2, y2 = coordinates[2 * i + 1]
            scaled_x1 = int(x1 / scale_x)
            scaled_y1 = int(y1 / scale_y)
            scaled_x2 = int(x2 / scale_x)
            scaled_y2 = int(y2 / scale_y)
            cv2.rectangle(frame, (scaled_x1, scaled_y1), (scaled_x2, scaled_y2), (0, 255, 0), 2)

        # 在右上角新增說明文字
        text1 = "REDRAW = Backspace"
        text2 = "OK = Enter"
        text_position = (window_width - 250, 30)
        cv2.putText(frame, text1, text_position, cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        cv2.putText(frame, text2, (text_position[0], text_position[1] + 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        
        cv2.imshow("Video", frame)

        key = cv2.waitKey(1)

        if key == 13:  # Quit = Enter
            break
        elif key == 8:  # Delete = Backspace
            if len(coordinates) > 0:
                coordinates = coordinates[:-2]  # Remove the last added rectangle

    cap.release()
    cv2.destroyAllWindows()

    return coordinates


while True:
    video_path = input("Video Path: ")
    if not os.path.isfile(video_path):
        # 檢查輸入的影像位置是否為 RTSP 連接
        if not video_path.startswith("rtsp://"):
            print("無法讀取影像。請檢查影像位置是否正確。")
            continue
    break


coordinates = get_coordinates_from_video(video_path)

if len(coordinates) == 2:
    x1, y1 = coordinates[0]
    x2, y2 = coordinates[1]
    with open("Area.txt", "w") as file:
        file.write("x1: {}\ny1: {}\nx2: {}\ny2: {}".format(x1, y1, x2, y2))
elif len(coordinates) > 2:
    x1, y1 = coordinates[-2]
    x2, y2 = coordinates[-1]
    if not os.path.exists("Area.txt"):
        with open("Area.txt", "w") as file:
            file.write("x1: {}\ny1: {}\nx2: {}\ny2: {}".format(x1, y1, x2, y2))
    with open("Area.txt", "w") as file:
        file.write("x1: {}\ny1: {}\nx2: {}\ny2: {}".format(x1, y1, x2, y2))

print("Coordinates:", coordinates)

