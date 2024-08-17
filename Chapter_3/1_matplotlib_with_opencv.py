import cv2
import matplotlib.pyplot as plt

# Load two images
img1 = cv2.imread("./my_images/apple.jpg")
img2 = cv2.imread("./my_images/orange.jpg")
print(img1.shape)

#   Reshape image 2
img2 = cv2.resize(img2, img1.shape[0:2])
# Convert the images to RGB color
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)

# Create a figure and two subplots

fig, (ax1, ax2) = plt.subplots(1, 2)

# Display the images on the subplot
ax1.imshow(img1)
ax1.set_title("Image 1")
ax2.imshow(img2)
ax2.set_title("Image 2")

plt.show()

# PLOTTING A HISTOGRAM OF AN IMAGE
img = cv2.imread("./my_images/apple.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Calculate and plot the histogram
hist = cv2.calcHist([gray], [0], None, [256], [0, 256])
plt.plot(hist)
plt.xlim([0, 256])
plt.show()