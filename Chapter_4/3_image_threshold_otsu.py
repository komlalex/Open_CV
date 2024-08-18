import cv2

# read image in grayscale
img = cv2.imread("./my_images/apple.jpg", 0)

# apply Otsu's thresholding

ret, thresh = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Display result
cv2.imshow("Original", img)
cv2.imshow("Thresh", thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()
