# Smoothing and Blurring Images

import cv2
img = cv2.imread("./my_images/apple.jpg")

blur = cv2.medianBlur(img, 5)

cv2.imshow("Original", img)
cv2.imshow("Blurred", blur)

cv2.waitKey(0)
cv2.destroyAllWindows()