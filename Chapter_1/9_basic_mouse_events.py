import cv2
import numpy as np


# Define the callback function

def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"Left button clicked at ({x}, {y})")
    elif event == cv2.EVENT_RBUTTONDOWN:
        print(f"Right button clicked at {x}, {y}")
    elif event == cv2.EVENT_MOUSEMOVE:
        print(f"Mouse moved at {x}, {y}")


# Create a window and set the callback

cv2.namedWindow("Image")
cv2.setMouseCallback("Image", mouse_callback)


# Create a blank image
img = np.zeros([512, 512, 3], np.uint8)
img = cv2.imread("Image", img)

# Wait for a key press and exit

cv2.waitKey(0)
cv2.destroyAllWindows()
