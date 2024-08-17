import cv2
import numpy as np

# Create a black image
img = np.zeros((512, 512, 3), np.int8)


# Create a function to handle trackbar changes
def trackbar_callback(x):
    pass


# Create trackbars for each color channel
cv2.namedWindow("image")
cv2.createTrackbar("R", "image", 0, 255, trackbar_callback)
cv2.createTrackbar("G", "image", 0, 255, trackbar_callback)
cv2.createTrackbar("B", "image", 0, 255, trackbar_callback)

while True:
    cv2.imshow("image", img)

    # Get the current position of the trackbars
    r = cv2.getTrackbarPos("R", "image")
    g = cv2.getTrackbarPos("G", "image")
    b = cv2.getTrackbarPos("B", "image")

    # Set the color of the image based on the trackbar position
    img[:] = np.array([b, g, r]).astype(np.int8)

    if cv2.waitKey(1) == ord("q"):
        break

cv2.destroyAllWindows()

