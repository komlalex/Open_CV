import cv2

# Read an image
img = cv2.imread("my_images/apple.jpg")

# Show image
cv2.imshow("Output", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Write image
cv2.imwrite("new_apple.jpg", img)

