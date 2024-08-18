import cv2

img = cv2.imread("./my_images/apple.jpg", 0)

# Apply binary thresholding
thresh_value, thresh = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)

# Display images
cv2.imshow("Original", img)
cv2.imshow("Thresh", thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()