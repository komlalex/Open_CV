import cv2

cap = cv2.VideoCapture(0)

# set camera resolution
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Set the brightness to 50 (range: 0 to 100)
cap.set(cv2.CAP_PROP_BRIGHTNESS, 50)

# Print the values
print("Width: ", cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print("Height: ", cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print("Brightness: ", cap.get(cv2.CAP_PROP_BRIGHTNESS))
print("Sharpness: ",  cap.get(cv2.CAP_PROP_SHARPNESS))

# Set the camera contrast to 50 (range: 0 to 100)
cap.set(cv2.CAP_PROP_CONTRAST, 50)

# Loop through all the frame
while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("Frame", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release camera and close the window
cap.release()
cv2.destroyAllWindows()
