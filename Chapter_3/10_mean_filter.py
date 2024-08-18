import cv2
import numpy as np
img = cv2.imread("./my_images/apple.jpg")

# Define kernel size
kernel_size = 25

# Define the kernel
kernel = np.ones((kernel_size, kernel_size), np.float32) / (kernel_size**2)

# Apply the mean filter
filtered = cv2.filter2D(img, -1, kernel)

cv2.imshow("Original", img)
cv2.imshow("Filtered", filtered)

cv2.waitKey(0)
cv2.destroyAllWindows()