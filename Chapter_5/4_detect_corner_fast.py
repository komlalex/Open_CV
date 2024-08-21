import cv2

img = cv2.imread("./my_images/blox.jpeg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Set parameters for FAST corner detection
fast = cv2.FastFeatureDetector.create(threshold=25)

# Detect corners using FAST algorithm
kp = fast.detect(gray, None)

# Draw detected corners on the original image
img2 = cv2.drawKeypoints(img, kp, None, color=(0, 255, 0))

# Display the original image with detected corners
cv2.imshow("Image", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
