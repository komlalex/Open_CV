import cv2
# Load image as grayscale

img = cv2.imread("./my_images/apple.jpg", cv2.IMREAD_GRAYSCALE)

# Apply adaptive thresholding
max_value = 255
adaptive_method = cv2.ADAPTIVE_THRESH_GAUSSIAN_C
threshold_type = cv2.THRESH_BINARY_INV
block_size = 11
c = 2
thresh = cv2.adaptiveThreshold(img, max_value, adaptive_method, threshold_type, block_size, c)

# Show result
cv2.imshow("Original", img)
cv2.imshow("Thresh", thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()
