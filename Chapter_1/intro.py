import cv2

# Read an image
img = cv2.imread("./my_files/apple.jpg")

# Show image
cv2.imshow("Output", img)
cv2.waitKey(0)

