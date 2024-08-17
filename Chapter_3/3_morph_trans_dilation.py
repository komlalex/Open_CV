import cv2
import numpy as np

img = cv2.imread("./my_images/apple.jpg", 0)

kernel = np.ones((4, 2), np.uint8)

# Apply dilation
dilated = cv2.dilate(img, kernel, iterations=1)

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Dilated Image", dilated)

cv2.waitKey(0)
cv2.destroyAllWindows()