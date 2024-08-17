import cv2
import numpy as np

img = cv2.imread("./my_images/apple.jpg", 0)

kernel = np.ones((5, 5), np.uint8)

# Apply Kernel
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

# Display Images
cv2.imshow('Original Image', img)
cv2.imshow("Closed Image", closing)

cv2.waitKey(0)
cv2.destroyAllWindows()