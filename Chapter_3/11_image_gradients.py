import cv2

# Load image
img = cv2.imread("./my_images/apple.jpg")

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Calculate the horizontal and vertical Sobel gradients
grad_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
grad_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

# Calculate the absolute value of the gradients
abs_gray_x = cv2.convertScaleAbs(grad_x)
abs_gray_y = cv2.convertScaleAbs(grad_y)

# Combine the gradients using the magnitude and direction
grad_mag = cv2.addWeighted(abs_gray_x, 0.5, abs_gray_y, 0.5, 0)
grad_dir = cv2.phase(grad_x, grad_y, angleInDegrees=True)

# Display the results
cv2.imshow("Original", img)
cv2.imshow("Horizontal Gradient", abs_gray_x)
cv2.imshow("Vertical Gradient", abs_gray_y)
cv2.imshow("Combined Gradient (Magnitude)", grad_mag)
cv2.imshow("Gradient Direction", grad_dir)

cv2.waitKey(0)
cv2.destroyAllWindows()
