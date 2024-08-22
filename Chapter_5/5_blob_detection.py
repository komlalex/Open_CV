import cv2
import numpy as np

# Load image
img = cv2.imread("./my_images/blox.jpeg")

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Set parameters for blob detection
params = cv2.SimpleBlobDetector.Params()

# Filter by color and size
params.filterByColor = True
params.blobColor = 0
params.filterByArea = True
params.minArea = 100

# Create a blob detector object
detector = cv2.SimpleBlobDetector.create(params)

# Detect blobs using the blob detector
keypoints = detector.detect(gray)

# Draw detected blobs on the original image
img_with_keypoints = cv2.drawKeypoints(img, keypoints, np.array([]), (0, 0, 255),
                                       cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# Display the original image with detected blobs
cv2.imshow("Image", img_with_keypoints)
cv2.waitKey(0)
cv2.destroyAllWindows()
