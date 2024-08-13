import cv2

img = cv2.imread("./my_images/apple.jpg")

(b, g, r) = cv2.split(img)
# Merge image
merged_img = cv2.merge((r, g, g))

cv2.imshow("Merged Image", merged_img)

cv2.waitKey(0)
cv2.destroyAllWindows()