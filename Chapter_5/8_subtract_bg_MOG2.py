import cv2

# Create background subtraction object
bg_sub = cv2.createBackgroundSubtractorKNN()

# Open video file or stream
cap = cv2.VideoCapture(0)

while True:
    # Read frame
    ret, frame = cap.read()
    if ret:
        # Apply background subtraction
        fg_mask = bg_sub.apply(frame)

        # Apply morphological operations to clean up mask
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))

        fg_mask = cv2.morphologyEx(fg_mask, cv2.MORPH_OPEN, kernel)

        # Display result
        cv2.imshow("Foreground Mask", fg_mask)
        cv2.imshow("Original Frame", frame)

    if cv2.waitKey(25) & 0xFF == ord("q"):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()

