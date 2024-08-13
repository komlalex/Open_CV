import cv2

img1 = cv2.imread("./my_images/apple.jpg")
img2 = cv2.imread("./my_images/orange.jpg")

# Resize images
img2 = cv2.resize(img2, img1.shape[0:2])

# Blend images with different weight
add = cv2.addWeighted(img1, 0.1, img2, 0.8, 0)

# Show
cv2.imshow("Blended with Weight", add)


cv2.waitKey(0)
cv2.destroyAllWindows()