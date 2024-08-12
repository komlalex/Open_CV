import cv2

img = cv2.imread("my_images/apple.jpg")

img_rgb = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
cv2.imshow("Image", img_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()