import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        break
    resized = cv2.resize(frame, (400, 400))

    cv2.imshow("Original Frame", frame)
    cv2.imshow("Resized Frame", resized)

    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()