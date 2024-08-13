import cv2

img = cv2.imread("./my_images/apple.jpg")

# Display the image and select a ROI
x, y, w, h = cv2.selectROI(img)

# crop the image to select ROI
roi = img[y:y+h, x:x+w]

# display the cropped ROI
cv2.imshow('ROI', roi)

# wait for a key and close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()