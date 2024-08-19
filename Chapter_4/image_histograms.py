import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load image in grayscale
img = cv2.imread("./my_images/apple.jpg", cv2.IMREAD_GRAYSCALE)

# Calculate the histogram of the image
hist = cv2.calcHist([img], [0], None, [256], [0, 256])

# Plot the histogram using matplotlib
plt.plot(hist)
plt.xlim([0, 256])


# Display the image
cv2.imshow("Image", img)
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()