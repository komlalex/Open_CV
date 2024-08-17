import cv2
import numpy as np

# Load images
img1 = cv2.imread("./my_images/apple.jpg")
img2 = cv2.imread("./my_images/orange.jpg")

# Resize images
img2 = cv2.resize(img2, img1.shape[0:2])

# Create a mask by thresholding the first image
gray_img1 = cv2.cvtColor(img1, cv2.COLOR_BGRA2GRAY)
ret, mask = cv2.threshold(gray_img1, 100, 255, cv2.THRESH_BINARY)
mask = cv2.bitwise_not(mask)

# Perform a bitwise AND operation on the images
bitwise_and = cv2.bitwise_and(img1, img2, mask=mask)
# Perform a bitwise OR operation on the images
bitwise_or = cv2.bitwise_or(img1, img2, mask=mask)
# Perform a bitwise XOR operation on the images
bitwise_xor = cv2.bitwise_xor(img1, img2, mask=mask)
# Perform a bitwise NOT operation on the images
bitwise_not = cv2.bitwise_not(img1, img2, mask=mask)

cv2.imshow("Image 1", img1)
cv2.imshow("Image 2", img2)
cv2.imshow("Mask", mask)
cv2.imshow("Bitwise AND", bitwise_and)
cv2.imshow("Bitwise OR", bitwise_or)
cv2.imshow("Bitwise XOR", bitwise_xor)
cv2.imshow("Bitwise NOT", bitwise_not)


cv2.waitKey(0)
cv2.destroyAllWindows()