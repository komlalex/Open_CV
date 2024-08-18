import cv2
import cv2
import numpy as np

# Load Image
img = cv2.imread("./my_images/apple.jpg")

# Create a Gaussian pyramid
gaussian = img.copy()
gaussian_pyramid = [gaussian]
for i in range(4):
    gaussian = cv2.pyrDown(gaussian)
    gaussian_pyramid.append(gaussian)


# Create a laplacian pyramid
laplacian_pyramid = []
for i in range(3, 0, -1):
    gaussian_expanded = cv2.pyrUp(gaussian_pyramid[i])
    laplacian = cv2.subtract(gaussian_pyramid[i-1], gaussian_expanded)
    laplacian_pyramid.append(laplacian)


# Display the results
cv2.imshow("Original", img)

for i in range (4):
    cv2.imshow(f"Gaussian Pyramid {i}", gaussian_pyramid[i])

for i in range(3):
    cv2.imshow(f"Laplacian Pyramid {i}", laplacian_pyramid[i])

cv2.waitKey(0)
cv2.destroyAllWindows()