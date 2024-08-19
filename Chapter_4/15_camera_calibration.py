# import required modules
import numpy as np
import cv2
import glob

# Define the dimensions of the checkerboard pattern
CHECKERBOARD = (6, 9)

# Define the object points (3D coordinates of the checkerboard corners)
objp = np.zeros((CHECKERBOARD[0] * CHECKERBOARD[1], 3), np.float32)

objp[:, :2] = np.mgrid[0:CHECKERBOARD[0], 0:CHECKERBOARD[1]].T.reshape(-1, 2)

# Create arrays to store the object points and image points from all images

objpoints = []
imgpoints = []

# Get a list of all calibration images
images = glob.glob('./my_images/checkerboard*.jpeg')

# Loop through each image and detect checkerboard corners
for fname in images:
    img = cv2.imread(fname)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, corners = cv2.findChessboardCorners(gray, CHECKERBOARD, None)

    # If corners are detected, add object points and image points to the respective lists
    if ret:
        objpoints.append(objp)
        imgpoints.append(corners)

    # Draw and display the corners
        img = cv2.drawChessboardCorners(img, CHECKERBOARD, corners, ret)
        cv2.imshow("img", img)
        cv2.waitKey(0)

    cv2.destroyAllWindows()

    # Calibrate the camera using the object points and image points
    ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

    # Displaying the required output
    print("Camera matrix:")
    print(mtx)

    print("\n Distortion coefficient:")
    print(dist)

    print("\n Rotation Vectors:")
    print(rvecs)

    print("\n Translation Vectors:")
    print(tvecs)


