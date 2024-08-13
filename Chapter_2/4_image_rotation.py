import cv2

img = cv2.imread("./my_images/apple.jpg")

(rows, cols) = img.shape[:2]

# Rotate Image
M = cv2.getRotationMatrix2D((cols/2, rows/2), 45, 0.6)

rotated_image = cv2.warpAffine(img, M, (cols, rows))

# Display processed image
cv2.imshow("Rotated Image", rotated_image)

# Wait for a key and close all the windows
cv2.waitKey(0)
cv2.destroyAllWindows()