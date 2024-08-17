import cv2
import numpy as np

cv2.namedWindow("image")
def nothing(x):
    print(x)

# create trackbar
cv2.createTrackbar("cp", "image", 10, 400, nothing)

switch = "color/gray"
cv2.createTrackbar(switch, "image", 0, 1, nothing)

while True:
    img = cv2.imread("./my_images/apple.jpg")
    pos = cv2.getTrackbarPos("cp", "image")
    font = cv2.FONT_HERSHEY_SIMPLEX

    # Put text in the frame
    cv2.putText(img, str(pos), (50, 150), font, 4, (0, 0, 255))

    p = cv2.getTrackbarPos(switch, "image")
    if p == 0:
        cv2.imshow("image", img)
    else:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.imshow("image", img)

    if cv2.waitKey(1) == ord("q"):
        break

cv2.destroyAllWindows()
