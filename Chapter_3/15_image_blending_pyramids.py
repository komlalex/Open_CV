import cv2
import numpy as np

#  Load the images
img1 = cv2.imread("./my_images/apple.jpg")
img2 = cv2.imread("./my_images/orange.jpg")

# Create a gaussian pyramid for each
G1 = img1.copy()
G2 = img2.copy()
gp1 = [G1]
gp2 = [G2]

for i in range(6):
    G1 = cv2.pyrDown(G1)
    G2 = cv2.pyrDown(G2)
    gp1.append(G1)
    gp2.append(G2)


# Create the Laplacian Image for each image
lp1 = [gp1[5]]
lp2 = [gp2[5]]

for i in range(5, 0, -1):
    GE1 = cv2.pyrUp(gp1[i])
    GE2 = cv2.pyrUp(gp2[i])

    L1 = cv2.subtract(gp1[i-1], GE1)
    L2 = cv2.subtract(gp2[i-1], GE2)

    lp1.append(L1)
    lp2.append(L2)

# Merge the Laplacian Pyramids
LS = []
for l1, l2 in zip(lp1, lp2):
    rows, cols, dpt = l1.shape
    ls = np.hstack((l1[:, 0:cols//2], l2[:, cols//2:]))
    LS.append(ls)

# Reconstruct the blended image
blended_img = LS[0]
for i in range(1, 6):
    blended_img = cv2.pyrUp(blended_img)
    blended_img = cv2.add(blended_img, LS[i])

# Display the blended image
cv2.imshow("Blended Image", blended_img)

cv2.waitKey(0)
cv2.destroyAllWindows()