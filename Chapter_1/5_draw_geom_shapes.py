# DRAWING Geometric Shapes On Images
"""
1. Line ---> cv2.line()
2. Arrowed Line --> cv2.arrowedLine()
3. Rectangle --> cv2.rectangle()
4. Circle ---> cv2.circle()
5. Ellipse ---> cv2.ellipse()
6. Polylines --> cv2.polylines()
7. Text ---> cv2.putText()
"""
import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
# cv2.rectangle(img, (100, 100), (400, 400), (0, 255, 0), 3)
# cv2.circle(img, (256, 256), 100, (0, 0, 255), 2)
# cv2.ellipse(img, (256, 256), (100, 50), 0, 0, 360, (255, 0, 0), 2)
# pts = np.array([[100, 100], [200, 300], [400, 200], [300, 100]], np.int32)
# cv2.polylines(img, [pts], True, (0, 255, 0), 3)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, "OpenCV", (200, 200), font, 2, (255, 255, 255), 2, cv2.LINE_AA)
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
