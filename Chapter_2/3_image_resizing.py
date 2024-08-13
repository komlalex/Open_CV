import cv2

img = cv2.imread("./my_images/apple.jpg")

# Resize image
resized_image = cv2.resize(img, (300, 200))

# Displayed resized image
cv2.imshow("Resized Image", resized_image)

# Wait for a key press and close the windows
cv2.waitKey()
cv2.destroyAllWindows()