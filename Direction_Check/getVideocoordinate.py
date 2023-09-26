import cv2

def get_coordinates_from_video(video_path):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("cam open failed.")
        return []

    cv2.namedWindow("Video") #windows name

    coordinates = [] #saved coordinates

    def mouse_handler(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            print("coordinates (x, y) = ({}, {})".format(x, y))
            coordinates.append((x, y))

    cv2.setMouseCallback("Video", mouse_handler)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imshow("Video", frame)

        # Quit = ESC
        if cv2.waitKey(1) == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

    return coordinates

video_path = input("Video Path：")

coordinates = get_coordinates_from_video(video_path)
print("coordinates",coordinates)
