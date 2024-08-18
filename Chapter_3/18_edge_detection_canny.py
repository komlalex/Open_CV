import cv2

img = cv2.imread("./my_images/apple.jpg")
img = cv2.resize(img, (320, 280))

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply the Canny edge detection algorithm
edges = cv2.Canny(gray, 100, 200)

# Display the results
cv2.imshow("Original Image", img)
cv2.imshow("Canny Edges", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
