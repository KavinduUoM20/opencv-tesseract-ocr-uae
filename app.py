import cv2
from ocr_utils import extract_text_from_rectangles, draw_rectangles

# video file
video_path = './data/file.mp4'

# Open the video file
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print(f"Error: Could not open video file {video_path}.")
    exit()

# Define rectangles for OCR (x, y, width, height)
rectangles = [
    #(830, 330,330, 217)
    #(430, 330,330, 217),
    #(184, 138, 133, 82)  # rectangle-1
    #(400, 500, 300, 100)   # rectangle-2
]

# Get the frame rate of the video
fps = cap.get(cv2.CAP_PROP_FPS)
print(f"Video FPS: {fps}")

# Calculate the frame interval to get 1 frame per second
frame_interval = int(fps)

frame_count = 0

# Get the screen size for window resizing
screen_width = 1080  # Change to your screen width
screen_height = 720  # Change to your screen height

def save_frame_as_png(frame, filename):
    """
    Saves a frame as a PNG image.
    
    Parameters:
        frame (numpy.ndarray): The frame to save.
        filename (str): The filename for the PNG image.
    """
    cv2.imwrite(filename, frame, [cv2.IMWRITE_PNG_COMPRESSION, 0])

while True:
    # Set the frame position
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_count * frame_interval)
    frame_count += 1
    
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    if not ret:
        print("End of video file reached or error occurred.")
        break
    
    # Print full frame dimensions
    print(f"Frame dimensions: {frame.shape}")

    # Extract text from specified rectangles in the frame
    texts = extract_text_from_rectangles(frame, rectangles)
    for i, text in enumerate(texts):
        print(f"Text from rectangle {i}: {text}")
    
    # Draw rectangles on the frame
    frame_with_rectangles = draw_rectangles(frame, rectangles)
    
    # Resize the frame to fit within the screen size while maintaining aspect ratio
    frame_height, frame_width = frame_with_rectangles.shape[:2]
    aspect_ratio = frame_width / frame_height

    if frame_width > screen_width or frame_height > screen_height:
        if aspect_ratio > 1:  # Wide frame
            new_width = screen_width
            new_height = int(screen_width / aspect_ratio)
        else:  # Tall frame
            new_height = screen_height
            new_width = int(screen_height * aspect_ratio)
        frame_with_rectangles = cv2.resize(frame_with_rectangles, (new_width, new_height))
    
    # Save one frame as a PNG image
    #save_frame_as_png(frame_with_rectangles, f"frame_{frame_count}.png")

    # Display the resulting frame
    cv2.imshow('Frame', frame_with_rectangles)
    
    # Wait for a while and check if 'q' is pressed to exit
    if cv2.waitKey(1000) & 0xFF == ord('q'):
        break

# When everything is done, release the capture device and close windows
cap.release()
cv2.destroyAllWindows()