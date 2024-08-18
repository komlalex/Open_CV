# Smoothing and Blurring Images
import cv2

img = cv2.imread("./my_images/apple.jpg")
blur = cv2.GaussianBlur(img, (25,25), 0)

cv2.imshow("Original Image", img)
cv2.imshow("Blurred Image", blur)

cv2.waitKey(0)
cv2.destroyAllWindows()