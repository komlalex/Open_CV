import cv2
import numpy as np


def nothing(x):
    pass


# Load the video file
cap = cv2.VideoCapture("./my_videos/dog.mp4")

# Create a window and trackbars to adjust the color thresholds
cv2.namedWindow("Object Detection")

cv2.createTrackbar("Low H", "Object Detection", 0, 179, nothing)
cv2.createTrackbar("High H", "Object Detection", 179, 179, nothing)

cv2.createTrackbar("Low S", "Object Detection", 0, 255, nothing)
cv2.createTrackbar("High S", "Object Detection", 255, 255, nothing)

cv2.createTrackbar("Low V", "Object Detection", 0, 255, nothing)
cv2.createTrackbar("High V", "Object Detection", 255, 255, nothing)

while True:
    # Read the video frame
    ret, frame = cap.read()

    if not ret:
        break

    # Convert to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Get the color thresholds from the trackbars
    low_h = cv2.getTrackbarPos("Low H", "Object Detection")
    high_h = cv2.getTrackbarPos("High H", "Object Detection")

    low_s = cv2.getTrackbarPos("Low S", "Object Detection")
    high_s = cv2.getTrackbarPos("High S", "Object Detection")

    low_v = cv2.getTrackbarPos("Low V", "Object Detection")
    high_v = cv2.getTrackbarPos("High V", "Object Detection")

    # Define the color thresholds
    lower_color = np.array([low_h, low_s, low_v])
    upper_color = np.array([high_s, high_s, high_v])

    # Threshold the HSV image to get only the object in the color range
    mask = cv2.inRange(hsv, lower_color, upper_color)

    # Apply morphological operations
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.erode(mask, kernel)
    mask = cv2.dilate(mask, kernel)

    # Find contours of the object in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Draw the contours on the original image
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 100:
            cv2.drawContours(frame, contour, -1, (0, 255, 0), 3)

    # Display the frames
    cv2.imshow("Object Detection", frame)
    cv2.imshow("Mask", mask)

    # Press "q" to exit the program
    if cv2.waitKey(1) == ord("q"):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()

