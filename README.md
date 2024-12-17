# 🎥 YouTube Video Text Extractor with Image Support

## 🚀 Project Overview

This project allows you to **extract text** from:
1. **YouTube Videos**: Extract text frame-by-frame dynamically from running video files.
2. **Static Images**: Upload an image file and extract text using OCR (Optical Character Recognition).

The project utilizes:
- **Tesseract OCR** for text recognition.
- **OpenCV** for video processing.
- **Pillow (PIL)** for image handling.
- **Pyperclip** for copying extracted text.

---

## 📊 Features and Statistics

### Features:
- **Real-time Text Extraction**: Process video files frame-by-frame.
- **Static Image Support**: Extract text from image files.
- **Clipboard Integration**: Copy the extracted text instantly for easy usage.
- **User-Friendly Interface**: Console-based interface for video/image input selection.

### Performance Stats:
| Feature                | Average Processing Time |
|------------------------|-------------------------|
| Text Extraction (Video)| ~20ms per frame         |
| Text Extraction (Image)| ~200ms for an image     |

- **Accuracy**: ~80%-95% on clean and high-resolution text.
- **Frame Optimization**: Video frames are preprocessed (grayscale) for improved OCR speed and accuracy.

---

## ⚙️ How It Works

### Mathematical/Optimization Insight:
1. **Grayscale Conversion**:
   - Frames are converted to **grayscale** to simplify data for OCR and reduce computational load.
   - Formula for grayscale:
     ```
     Grayscale = 0.299 * R + 0.587 * G + 0.114 * B
     ```
2. **OCR Processing**:
   - Each frame/image is passed to **Tesseract OCR** for text detection and extraction.
3. **Frame Rate Management**:
   - Real-time processing is optimized to skip redundant frames if no text is detected.
4. **Image Processing**:
   - Static images are directly read and processed using Pillow.

---

## 🛠️ Installation

### Prerequisites:
1. Python 3.8+ installed.
2. Tesseract OCR installed:
   - Download: [Tesseract GitHub](https://github.com/tesseract-ocr/tesseract)
   - Add Tesseract to your PATH variable.

### Steps to Run:

1. **Clone the Project**:
   ```bash
   git clone https://github.com/your-username/youtube-text-extractor.git
   cd youtube-text-extractor
