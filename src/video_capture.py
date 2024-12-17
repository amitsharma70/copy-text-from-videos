import cv2

def capture_video_stream(video_url):
    print(video_url)
    cap = cv2.VideoCapture(video_url)
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        yield frame
    cap.release()
    cv2.destroyAllWindows()
