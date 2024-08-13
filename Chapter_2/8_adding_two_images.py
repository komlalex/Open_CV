import cv2

img1 = cv2.imread("./my_images/apple.jpg")
img2 = cv2.imread("./my_images/orange.jpg")

# Add 2 images
img2 = cv2.resize(img2, img1.shape[:2])

add = cv2.add(img1, img2)

cv2.imshow("Added Images", add)

cv2.waitKey(0)
cv2.destroyAllWindows()