# Detect Simple Geometric Shapes Using OpenCV
import cv2
import numpy as np

# Load image and convert it to grayscale
img = cv2.imread("./my_images/shapes.jpg")
img = cv2.resize(img, (720, 600))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply edge detection to detect edges in the image
edges = cv2.Canny(gray, 50, 150, apertureSize=3)

# Find Contours
contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# Loop through each contour and check if it matches a circle, triangle or square

for cnt in contours:
    # Calculate perimeter of contour
    perimeter = cv2.arcLength(cnt, True)

    # Approximate the shape of the contour
    approx = cv2.approxPolyDP(cnt, 0.04 * perimeter, True)

    # Calculate the number of vertices of the approximated shape
    num_vertices = len(approx)
    # If the shape has 3 vertices, it's a triangle
    if num_vertices == 3:
        cv2.drawContours(img, [approx], 0, (0, 255, 0), 2)
        cv2.putText(img, "Triangle", tuple(approx[0][0]), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # If the shape has 4 vertices, it should be a square or a rectangle
    elif num_vertices == 4:
        x, y, w, h = cv2.boundingRect(cnt)
        aspect_ratio = float(w) / h

        # If aspect ratio is close to 1, it's a square
        if 0.95 <= aspect_ratio <= 1.05:
            cv2.drawContours(img, [approx], 0, (0, 0, 255), 2)
            cv2.putText(img, "Square", tuple(approx[0][0]), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
        else:
            cv2.drawContours(img, [approx], 0, (0, 255, 255), 2)
            cv2.putText(img, "Rectangle", tuple(approx[0][0]), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)

    # If the shape has more than 4 vertices, we assume its aa circle
    else:
        cv2.drawContours(img, [approx], 0, (255, 0, 0), 2)
        cv2.putText(img, "Circle", tuple(approx[0][0]), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

# Display the image with the detected contours
cv2.imshow("Detected", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

