import cv2

cap = cv2.VideoCapture(0)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter.fourcc(*"XVID")
out = cv2.VideoWriter("with_text.avi", fourcc, 30, (width, height))

while cap.isOpened():
    ret, frame = cap.read()

    if ret:
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, "OpenCV", (10, 50), 1, 1, (230,0 ,100), 3)

        out.write(frame)
        cv2.imshow("With Text", frame)

        if cv2.waitKey(1) == ord("q"):
            break

cap.release()
out.release()
cv2.destroyAllWindows()