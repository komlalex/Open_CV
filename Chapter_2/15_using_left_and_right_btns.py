import cv2


def click_event(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"Left button clicked at {x, y}")

        # Add text to the image displaying the coordinates of the click
        font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
        text = f"{x}, {y}"
        cv2.putText(img, text, (x,y), font, 1, (255, 255, 0), 2)
        cv2.imshow("image", img)

    if event == cv2.EVENT_RBUTTONDOWN:
        blue = img[x, y, 0]
        green = img[x, y, 1]
        red = img[x, y, 2]
        font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
        text = f"{blue}, {green}, {red}"
        cv2.putText(img, text, (x, y), font, 1, (0, 255, 255), 2)
        cv2.imshow("image", img)


img = cv2.imread("./my_images/apple.jpg")
cv2.imshow("image", img)
cv2.setMouseCallback("image", click_event)

cv2.waitKey(0)

cv2.destroyAllWindows()
