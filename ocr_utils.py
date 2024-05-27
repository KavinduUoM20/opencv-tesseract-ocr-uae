import cv2
import pytesseract

# Configure tesseract executable path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Update this path as needed

def extract_text_from_rectangles(frame, rectangles):
    """
    Extracts text from specified rectangles in a video frame using OCR.
    
    Parameters:
        frame (numpy.ndarray): The video frame from which to extract text.
        rectangles (list of tuples): List of rectangles specified as (x, y, width, height).
    
    Returns:
        list of str: List of extracted text strings.
    """
    extracted_texts = []
    for rect in rectangles:
        x, y, w, h = rect
        roi = frame[y:y+h, x:x+w]
        text = pytesseract.image_to_string(roi)
        extracted_texts.append(text)
    return extracted_texts

def draw_rectangles(frame, rectangles):
    """
    Draws rectangles on the video frame.
    
    Parameters:
        frame (numpy.ndarray): The video frame on which to draw rectangles.
        rectangles (list of tuples): List of rectangles specified as (x, y, width, height).
    
    Returns:
        numpy.ndarray: The video frame with rectangles drawn.
    """
    for rect in rectangles:
        x, y, w, h = rect
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    return frame
