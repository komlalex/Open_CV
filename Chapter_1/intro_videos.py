import cv2

# cap = cv2.VideoCapture("./my_videos/office.mp4")
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow("Video", frame)

    # break the loop Press Q button

    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
