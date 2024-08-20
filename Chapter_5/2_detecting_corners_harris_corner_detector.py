# Harris Corner Detection
import cv2
import numpy as np

# Load image
img = cv2.imread("./my_images/blox.jpeg")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Harris Corner Detector
dst = cv2.cornerHarris(gray, 2, 3, 0.04)

# Threshold for an optimal value
thresh = 0.01 * dst.max()

# Create a back image to display the corners
corner_img = np.zeros_like(img)

# Draw detected corners on the black image
for row_index in range(dst.shape[0]):
    for column_index in range(dst.shape[1]):
        if dst[row_index, column_index] > thresh:
            cv2.circle(corner_img, (column_index, row_index), 3, (0, 255, 0), 1)
            cv2.circle(img, (column_index, row_index), 3, (0, 255, 0), 1)

# Display the original image and the detected corners
cv2.imshow("Image", img)
cv2.imshow("Corners", corner_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
