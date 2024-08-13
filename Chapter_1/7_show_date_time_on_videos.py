# Show the date and time on videos using OpencCV
import cv2

import datetime
cap = cv2.VideoCapture(0)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Define the codec and create the VideoWriter object
fourcc = cv2.VideoWriter.fourcc(*"XVID")
out = cv2.VideoWriter("with_dt.avi", fourcc, 30, (width, height))

while cap.isOpened():
    # Read the current frame
    ret, frame = cap.read()
    # if the frame was read successfully
    if ret:
        # Get current date and time
        now = datetime.datetime.now()
        date_time = now.strftime("%d-%m-%Y %H:%M:%S")

        # Put the date and time on the frame
        font = cv2.FONT_ITALIC
        cv2.putText(frame, date_time,(10, 50), font, 1, (0, 255, 255), 2, cv2.LINE_AA)

        # Write the frame to the output
        out.write(frame)

        # Display the resulting frame
        cv2.imshow("Frame", frame)

        if cv2.waitKey(1) == ord("q"):
            break

cap.release()
out.release()
cv2.destroyAllWindows()