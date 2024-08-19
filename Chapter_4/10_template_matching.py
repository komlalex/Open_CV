import cv2
import numpy as np
# Load image and template
image = cv2.imread("./my_images/dog.jpeg")
template = cv2.imread("./my_images/dog_head.jpeg")

# Get the dimensions of the template
template_height, template_width, _ = template.shape

# Apply the template matching using the TM_CCOEFF_NORMED method
result = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)

# Set a threshold to filter out weak matches
threshold = 0.8
locations = np.where(result >= 0.8)
locations = list(zip(*locations[::-1]))

# Draw rectangles around the matching regions

for loc in locations:
    top_left = loc
    bottom_right = (top_left[0] + template_width, top_left[1] + template_height)
    cv2.rectangle(image, top_left, bottom_right, (0, 0, 255), 1)

# Display the result
cv2.imshow("Result", image)
cv2.waitKey(0)
cv2.destroyAllWindows()