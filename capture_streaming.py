import cv2
import time
import pytesseract
from ocr_utils import extract_text_from_rectangles, draw_rectangles

# Configure tesseract executable path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update this path as needed

# RTSP stream URL
rtsp_url = 'rtsp://100.96.227.62:8554/mystream'

# Open a connection to the RTSP stream
cap = cv2.VideoCapture(rtsp_url)

if not cap.isOpened():
    print("Error: Could not open RTSP stream.")
    exit()

# Define the rectangles for OCR (example: [(x, y, width, height)])
rectangles = [
    #(294, 348, 400, 170), 
    #(438, 540, 48, 25)
    (262, 346, 400,17 )
    ]  # Update these coordinates as needed

def save_frame(frame, frame_id):
    filename = f"frame_{frame_id}.jpg"
    cv2.imwrite(filename, frame)
    print(f"Saved: {filename}")

frame_id = 0
start_time = time.time()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Could not read frame.")
        break

    # Get the current time
    current_time = time.time()

    # Save and process a frame every 60 seconds
    if (current_time - start_time) >= 60:
        save_frame(frame, frame_id)

        # Draw rectangles on the frame
        frame_with_rectangles = draw_rectangles(frame.copy(), rectangles)

        # Extract text from the rectangles
        extracted_texts = extract_text_from_rectangles(frame, rectangles)
        for i, text in enumerate(extracted_texts):
            print(f"Text from rectangle {i}: {text}")

        frame_id += 1
        start_time = current_time

    # Display the frame with rectangles (optional)
    frame_with_rectangles = draw_rectangles(frame.copy(), rectangles)
    cv2.imshow('RTSP Stream with OCR Rectangles', frame_with_rectangles)

    # Exit on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close OpenCV windows
cap.release()
cv2.destroyAllWindows()
