# Edge Detection Using the Laplacian of Gaussian
import cv2

img = cv2.imread("./my_images/apple.jpg", cv2.IMREAD_GRAYSCALE)

# Define kernel size and sigma value
kernel_size = 5
sigma = 1.4

# Apply LoG filter
filtered_img = cv2.GaussianBlur(img, (kernel_size, kernel_size), sigma)
filtered_img = cv2.Laplacian(filtered_img, cv2.CV_64F)

# Normalize the filtered images
filtered_img = cv2.normalize(filtered_img, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8U)


# Display the original and filtered images
cv2.imshow("Original Image", img)
cv2.imshow("Filtered Image", filtered_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

