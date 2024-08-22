# Scale-invariant feature transform

import cv2
img = cv2.imread("./my_images/blox.jpeg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Create a SIFT detector object
sift = cv2.SIFT.create()

# Detect keypoints on the original image
keypoints = sift.detect(gray, None)

# Draw detected keypoints on the original image
img_with_keypoints = cv2.drawKeypoints(img, keypoints, None)

# Display the original image with the detected keypoints
cv2.imshow("Image", img_with_keypoints)
cv2.waitKey(0)
cv2.destroyAllWindows()