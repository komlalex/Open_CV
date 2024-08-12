import cv2

# cap = cv2.VideoCapture("./my_videos/office.mp4")

"""
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

"""

# Write Videos
cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter.fourcc(*"XVID")
out = cv2.VideoWriter("output.avi", fourcc, 25, (640, 480))

while True:
    ret, frame = cap.read()
    if not ret:
        break

    out.write(frame)
    cv2.imshow("Video", frame)
    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
