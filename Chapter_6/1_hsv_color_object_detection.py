import cv2
import numpy as np

# Define the callback  function for the trackbar
def nothing(x):
    pass

# Create a named window for the trackbars
cv2.namedWindow("Trackbars")

# Create trackbars for hue, saturation and value
cv2.createTrackbar("Hue_Low", "Trackbars", 0, 179, nothing)
cv2.createTrackbar("Hue_High", "Trackbars", 179, 179, nothing)

cv2.createTrackbar("Saturation_Low", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("Saturation_High", "Trackbars", 255, 255, nothing)

cv2.createTrackbar("Value_Low", "Trackbars", 0, 255, nothing)
cv2.createTrackbar("Value_High", "Trackbars", 255, 255, nothing)

# Load image
img = cv2.imread("./my_images/colors.jpeg")

# Convert to HSV color space
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

while True:
    # Get the current trackbar positions
    h_low = cv2.getTrackbarPos("Hue_Low", "Trackbars")
    h_high = cv2.getTrackbarPos("Hue_High", "Trackbars")

    s_low = cv2.getTrackbarPos("Saturation_Low", "Trackbars")
    s_high = cv2.getTrackbarPos("Saturation_High", "Trackbars")

    v_low = cv2.getTrackbarPos("Value_Low", "Trackbars")
    v_high = cv2.getTrackbarPos("Value_High", "Trackbars")
    
    # Define the lower and upper bounds of the color to detect 
    lower_bound = np.array([h_low, s_low, v_low]) 
    upper_bound = np.array([h_high, s_high, v_high])

    # Create a mask using the lower and upper bounds
    mask = cv2.inRange(hsv, lower_bound, upper_bound)

    # Apply the mask to the original image
    result = cv2.bitwise_and(img, img, mask=mask)

    # Show the original image and the result
    cv2.imshow("Original", img)
    cv2.imshow("Result", result)

    if cv2.waitKey(1) == ord("q"):
        break

cv2.destroyAllWindows()