import cv2
from rembg import remove

img = cv2.imread("./my_images/orange.jpg")
"""
# Convert the image to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 1. Remove the background using a threshold
# Median filter is applied to the grayscale image using a threshold
gray_img = cv2.medianBlur(gray_img, 5)

# A binary threshold is applied to the grayscale image using a threshold
ret, thresh = cv2.threshold(gray_img, 150, 255, cv2.THRESH_BINARY_INV)

# The binary image is eroded to remove small objects and fill in small gaps using erode
mask = cv2.erode(thresh, None, iterations=2)

# The binary image is dilated to expand the remaining foreground objects and fill in small gaps
mask = cv2.dilate(mask, None, iterations=2)

# The original input is combined with the binary mask using bitwise_and
background_removed_img= cv2.bitwise_and(img, img, mask=mask)

# Display the processed images
cv2.imshow("Background Removed Image", background_removed_img)


cv2.waitKey(0)
cv2.destroyAllWindows()
"""
# Using rembg library


ori_img = cv2.imread("./my_images/orange.jpg")
removed_bg = remove(ori_img)

# Save
cv2.imwrite("output.png", removed_bg)

# Display
cv2.imshow("Removed Background", removed_bg)

cv2.waitKey()
cv2.destroyAllWindows()
