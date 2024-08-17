import cv2
import time

# create a video object
cap = cv2.VideoCapture(0)

# loop over frames from the video capture

while True:
    ret, frame = cap.read()

    if not ret:
        break
    cv2.imshow("Pause Frame", frame)

    # pause for 5 seconds

    time.sleep(5)

    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()