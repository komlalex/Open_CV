import cv2

cap = cv2.VideoCapture("./my_videos/office.mp4")

while True:
    ret, frame = cap.read()

    if not ret:
        break

    ori_frame = frame.copy()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    # Find contours
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Draw Contours on frame
    cv2.drawContours(frame, contours, -1, (0, 255, 0), 2)

    # Display images
    cv2.imshow("Original", ori_frame)
    cv2.imshow("With Contours", frame)

    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()