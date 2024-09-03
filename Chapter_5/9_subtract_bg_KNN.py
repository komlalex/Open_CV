import cv2

cap = cv2.VideoCapture(0)

# Create a BackgroundSubtractorKNN object
bg_subtractor = cv2.createBackgroundSubtractorKNN()

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Apply background subtractor
    fg_mask = bg_subtractor.apply(frame)

    # Display the original and the foreground mask
    cv2.imshow("Original", frame)
    cv2.imshow("Foreground", fg_mask)

    if cv2.waitKey(1) == ord("q"):
        break


cap.release()
cv2.destroyAllWindows()
