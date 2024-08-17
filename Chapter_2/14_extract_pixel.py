import cv2


# Define the callback function

def get_pixel_color(event, x, y, flags, param):
    """
    Callback function to extract the color of a pixel in an image using mouse events.
    Parameters
    event (int): The type of mouse event that occurred
    x (int): The x-coordinate  of mouse cursor
    y (int): The y-coordinate of the mouse cursor
    flags (int): Any special flags associated with the mouse
    param (object): Optional parameters passed to the mouse callback
    Returns: None
    Side Effects: Prints the BGR and RGB values of the pixel at the
    given coordinates in the image.
    """

    if event == cv2.EVENT_LBUTTONDOWN:
        bgr_color = img[y, x]
        rgb_color = tuple(reversed(bgr_color))
        print("RGB color: ", rgb_color)


img = cv2.imread("./my_images/apple.jpg")
cv2.namedWindow("image")

# Set the mouse callback function
cv2.setMouseCallback("image", get_pixel_color)

# Display the image and wait for keypress
while True:
    cv2.imshow("image", img)

    if cv2.waitKey(1) == ord("q"):
        break

cv2.destroyAllWindows()

