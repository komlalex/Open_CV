# The image waitKey() function is used to wait for a keyboard event for a
# specified amount of time.

import cv2

img = cv2.imread("./my_images/apple.jpg")
cv2.imshow("Apple", img)

# Wait for 5 seconds
cv2.waitKey(5000)

# Close all windows
cv2.destroyAllWindows()
