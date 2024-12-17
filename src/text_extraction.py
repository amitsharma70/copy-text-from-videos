import pytesseract
from pytesseract import Output
from PIL import Image
import cv2

# Set up pytesseract path if not set in environment variables
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update with your path

def extract_text_from_frame(frame):
    pil_img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    text = pytesseract.image_to_string(pil_img, output_type=Output.STRING)
    return text
