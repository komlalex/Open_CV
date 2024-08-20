import cv2
import numpy as np


# Define region of interest
def roi_mask(img, vertices):
    mask = np.zeros_like(img)
    cv2.fillPoly(mask, vertices, (255, 0, 0))
    masked_img = cv2.bitwise_and(img, mask)
    return masked_img


# Apply Hough Line Transform
def hough_lines(img, rho, theta, threshold, min_line_len, max_line_gap):
    lines = cv2.HoughLinesP(img, rho, theta, threshold, np.array([]), minLineLength=min_line_len,
                            maxLineGap=max_line_gap)
    return lines


# Draw detected lines on the original image

def draw_lines(img, lines, color=(255, 0, 0), thickness=5):
    for line in lines:

        for x1, y1, x2, y2 in line:
            cv2.line(img, (x1, y1), (x2, y2), color, thickness)


# Road Lane Detection video stream

cap = cv2.VideoCapture("./my_videos/test_video.mp4")

while True:
    ret, frame = cap.read()

    if ret:
        try:
            # Convert to grayscale
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY, dst=frame.shape)

            # Apply Gaussian blur
            blur = cv2.GaussianBlur(gray, (5, 5), 0)

            # Apply Canny edge detection
            edges = cv2.Canny(blur, 50, 150)

            # Define region of interest
            roi_vertices = np.array([[(0, frame.shape[0]), (frame.shape[1] // 2, frame.shape[0] // 2 + 50),
                                      (frame.shape[1], frame.shape[0])]], dtype=np.int32)

            roi = roi_mask(edges, roi_vertices)

            # Apply Hough Lines Transform
            lines = hough_lines(roi, rho=2, theta=np.pi / 180, threshold=50, min_line_len=100, max_line_gap=50)

            # Draw detected lines on original image
            line_img = np.zeros((frame.shape[0], frame.shape[1]), dtype=np.uint8)
            draw_lines(line_img, lines)

            # Convert Grayscale back to bgr to get the third dimension back
            line_img = cv2.cvtColor(line_img, cv2.COLOR_GRAY2RGB)

            # Overlay detected lane lines on original image
            result = cv2.addWeighted(frame, 0.8, line_img, 1, 0)

            # Display the result
            cv2.imshow("Result", result)

            # exit on 'q' press
            if cv2.waitKey(1) == ord("q"):
                break
        except ValueError:
            print("Failed")
            pass
    else:
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
