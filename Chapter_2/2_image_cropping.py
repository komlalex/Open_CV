import cv2

img = cv2.imread("./my_images/apple.jpg")

# Crop image
crop_img = img[100:400, 200:500]

#   Display the cropped image
cv2.imshow("Cropped Image", crop_img)

cv2.waitKey(0)
cv2.destroyAllWindows()