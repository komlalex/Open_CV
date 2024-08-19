import cv2
import numpy as np

img = cv2.imread("./my_images/circles.png")
output = img.copy()

# Apply median blur
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 5)

# Apply Hough Circles Transform
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 20, param1=100, param2=30, minRadius=1, maxRadius=30)

detected_circles = np.uint16(np.around(circles))

# Draw detected circles on original image
for (x, y, r) in detected_circles[0, :]:
    cv2.circle(output, (x, y), r, (0, 255, 0), 3)
    cv2.circle(output, (x, y), 2, (0, 255, 255), 3)

# Display result
cv2.imshow("Output", output)
cv2.waitKey(0)
cv2.destroyAllWindows()