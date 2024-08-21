# Shit Tomasi Corner Detector

import cv2
import numpy as np

img = cv2.imread("./my_images/blox.jpeg")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Set parameters for Shi-Tomasi Corner detector

max_corners = 100
quality_level = 0.3
min_distance = 7
block_size = 7


# Apply Shi-Tomasi Corner Detector
corners = cv2.goodFeaturesToTrack(gray, max_corners, quality_level, min_distance, blockSize=block_size)

# Draw detected corners on the original image
corners = np.int8(corners)

for i in corners:
    x, y = i.ravel()
    cv2.circle(img, (x, y), 5, (0, 255, 0), -1)

# Display the original image with detected corners
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()