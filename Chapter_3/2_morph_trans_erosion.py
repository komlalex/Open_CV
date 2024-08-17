import cv2
import numpy as np

img = cv2.imread("./my_images/apple.jpg")

# Define kernel
kernel = np.ones((5, 5), np.uint8)

# Apply erosion
erosion = cv2.erode(img, kernel, iterations=2)

# Display the results
cv2.imshow('Original Image', img)
cv2.imshow("Eroded Image", erosion)

cv2.waitKey(0)
cv2.destroyAllWindows()