import cv2

# Global variable to store the clicked points
clicked_points = []
start_x, start_y = 0, 0

def Capture_Event(event, x, y, flags, params):
    global clicked_points, start_x, start_y
    # If the left mouse button is pressed
    if event == cv2.EVENT_LBUTTONDOWN:
        # Calculate the actual coordinates on the full image
        actual_x = start_x + x
        actual_y = start_y + y
        # Print the coordinate of the clicked point
        print(f"Clicked point: ({actual_x}, {actual_y})")
        # Add the clicked point to the list
        clicked_points.append((actual_x, actual_y))

def display_image(window_name, img, start_x, start_y, window_size):
    """
    Display a portion of the image defined by start_x and start_y as the top-left corner
    and window_size as the size of the view window.
    """
    h, w = img.shape[:2]
    end_x = min(start_x + window_size[0], w)
    end_y = min(start_y + window_size[1], h)
    
    cv2.imshow(window_name, img[start_y:end_y, start_x:end_x])

if __name__ == "__main__":
    # Read the image
    img = cv2.imread('./frame_0.jpg', 1)
    img_height, img_width = img.shape[:2]

    # Define the window size and starting coordinates for the viewport
    window_size = (800, 600)  # Adjust this to your preferred window size

    window_name = 'image'
    cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
    cv2.setMouseCallback(window_name, Capture_Event)

    while True:
        display_image(window_name, img, start_x, start_y, window_size)
        key = cv2.waitKey(0) & 0xFF
        
        # Key bindings for navigation
        if key == 27:  # Escape key
            break
        elif key == ord('w'):  # Move up
            start_y = max(start_y - 50, 0)
        elif key == ord('s'):  # Move down
            start_y = min(start_y + 50, img_height - window_size[1])
        elif key == ord('a'):  # Move left
            start_x = max(start_x - 50, 0)
        elif key == ord('d'):  # Move right
            start_x = min(start_x + 50, img_width - window_size[0])

    cv2.destroyAllWindows()

    # Print all the clicked points
    print("Clicked points:")
    for point in clicked_points:
        print(point)