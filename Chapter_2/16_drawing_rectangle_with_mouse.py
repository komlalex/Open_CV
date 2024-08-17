import numpy as np
import cv2

drawing = False
mode = True  # if True, draw a rectangle. Press m to toggle curve

ix, iy = -1, -1


# mouse callback function
def draw_curve(event, x, y, flags, param):
    global ix, iy, drawing, mode

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            if mode:
                cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
            else:
                cv2.circle(img, (x, y), 3, (0, 0, 255), -1)
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode:
            cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), -1)
        else:
            cv2.circle(img, (ix, iy), 5, (0, 0, 255), -1)


img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow("image")
cv2.setMouseCallback("image", draw_curve)

while True:
    cv2.imshow("image", img)

    k = cv2.waitKey(1)
    if k == ord("m"):
        mode = not mode
    elif k == ord("q"):
        break

cv2.destroyAllWindows()
