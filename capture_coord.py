import cv2

# Global variable to store the clicked points
clicked_points = []

def Capture_Event(event, x, y, flags, params):
    global clicked_points
    # If the left mouse button is pressed
    if event == cv2.EVENT_LBUTTONDOWN:
        # Print the coordinate of the clicked point
        print(f"Clicked point: ({x}, {y})")
        # Add the clicked point to the list
        clicked_points.append((x, y))

if __name__ == "__main__":
    # Read the image
    img = cv2.imread('./frame_0.jpg', 1)
    
    # Show the image
    cv2.imshow('image', img)
    
    # Set the Mouse Callback function
    cv2.setMouseCallback('image', Capture_Event)
    
    # Wait for any key to be pressed
    cv2.waitKey(0)
    
    # Destroy all the windows
    cv2.destroyAllWindows()

    # Print all the clicked points
    print("Clicked points:")
    for point in clicked_points:
        print(point)
