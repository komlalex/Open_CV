import cv2

# Load image
img = cv2.imread("./my_images/apple.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Calculate the horizontal and vertical sobel gradients
grad_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
grad_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

# Combine the gradients using the magnitude and direction
grad_mag = cv2.addWeighted(grad_x, 0.5, grad_y, 0.5, 0)

# Threshold the gradient magnitude to produce binary edge map
edges = cv2.threshold(grad_mag, 50, 255, cv2.THRESH_BINARY)[1]

# Display the results

cv2.imshow("Original Image", img)
cv2.imshow("Sobel Edges", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
