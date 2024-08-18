import cv2
# Load the image
img = cv2.imread("./my_images/apple.jpg", 0)

# Apply threshold
_, thresh = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY_INV)

# Show the results
cv2.imshow("Original", img)
cv2.imshow("Thresh", thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()
