import cv2
img1 = cv2.imread("./my_images/apple.jpg")
img2 = cv2.imread("./my_images/orange.jpg")

# Resize images
img1 = cv2.resize(img1, (320, 280))
img2 = cv2.resize(img2, (320, 280))

# Blend the images with a weight of 0.5
blended_image = cv2.addWeighted(img1, 0.5, img2, 0.5, 0)

# Display the results
cv2.imshow("Image 1", img1)
cv2.imshow("Image 2", img2)
cv2.imshow("Blended Image", blended_image)

cv2.waitKey(0)
cv2.destroyAllWindows()