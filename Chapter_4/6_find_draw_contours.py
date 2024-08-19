import cv2
import numpy as np

# Load image
img = cv2.imread("./my_images/opencv.png")
img2 = img.copy()

# Convert the image to grayscale

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply threshold to the image
_, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

# Find the contours
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Draw contours on the image
cv2.drawContours(img, contours, -1, (0, 255, 0), 2)

# Display the image
cv2.imshow("Original Image", img2)
cv2.imshow("Image with Contours", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
