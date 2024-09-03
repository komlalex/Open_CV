import cv2
import numpy as np

# Load images
img1 = cv2.imread("./my_images/dog.jpg")
img2 = cv2.imread("./my_images/dog-head.jpg")

# Initiate SIFT detector
sift = cv2.SIFT.create()

# Find keypoints and descriptors for both images
kp1, des1 = sift.detectAndCompute(img1, None)
kp2, des2 = sift.detectAndCompute(img2, None)

# FLANN Parameters
FLANN_INDEX_KDTREE = 1
index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
search_params = dict(checks=50)

# Create FLANN matcher
flann = cv2.FlannBasedMatcher(index_params, search_params)

# Match descriptors
matches = flann.knnMatch(des1, des2, k=2)

# Ratio test as per Lowe's paper
good_matches = []

for m, n, in matches:
    """
    m:  This variable represents the first best match between a
    feature descriptor in des1 and the feature descriptors in
    des2.
    n: This variable represents the second-best match between a
    feature descriptor in des1 and the feature descriptors in des2.
    """
    if m.distance < 0.7 * n.distance:
        good_matches.append(m)

    # Draw matches
img3 = cv2.drawMatches(img1, kp1, img2, kp2, good_matches, None,
                       flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

# Display image
cv2.imshow("Matches", img3)
cv2.waitKey(0)
cv2.destroyAllWindows()
