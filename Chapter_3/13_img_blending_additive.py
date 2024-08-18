import cv2

# Load images
img1 = cv2.imread("./my_images/apple.jpg")
img2 = cv2.imread("./my_images/orange.jpg")

# Resize the images to be the same
img1 = cv2.resize(img1, (320, 280))
img2 = cv2.resize(img2, (320, 280))

# Blend the images
blended_img = cv2.add(img1, img2)

# Display results
cv2.imshow("Image 1", img1)
cv2.imshow("Image 2", img2)
cv2.imshow("Blended Image", blended_img)

cv2.waitKey(0)
cv2.destroyAllWindows()