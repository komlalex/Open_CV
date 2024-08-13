import cv2
import numpy as np

img = cv2.imread("./my_images/apple.jpg")

# Split the image into its color channels
b, g, r = cv2.split(img)
cv2.imshow("Blue Channel", b)
cv2.imshow("Green Channel", g)
cv2.imshow("Red Channel", r)


cv2.waitKey(0)
cv2.destroyAllWindows()