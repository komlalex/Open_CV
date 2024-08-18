import cv2

# Load the image in grayscale mode
img = cv2.imread("./my_images/apple.jpg", cv2.IMREAD_GRAYSCALE)

# Apply simple thresholding
threshold_value = 127
max_value = 255

ret, thresh = cv2.threshold(img, threshold_value, max_value, cv2.THRESH_BINARY)

# Display the original and thresholded images
cv2.imshow("Original", img)

cv2.imshow("Thresholded Image", thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()
