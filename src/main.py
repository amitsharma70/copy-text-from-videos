# src/main.py
import cv2
from video_capture import capture_video_stream
from text_extraction import extract_text_from_frame
from gui import create_text_window

def main():
    video_url = r'D:\New folder\ecommerce.mp4'
    print("Starting video capture...")
    for frame in capture_video_stream(video_url):
        print("Captured a frame")
        text = extract_text_from_frame(frame)
        print(f"Extracted text: {text}")
        create_text_window(text)

if __name__ == "__main__":
    print("Running main.py")
    main()
