# Import necessary packages
import argparse
import imutils
import cv2
import numpy as np

ap = argparse.ArgumentParser()

# Command line arguments
ap.add_argument("-i", "--image", type=str, default = "Rogue.jpg")
ap.add_argument("-i1", "--image1", type=str, default = "Rogue.jpg")
ap.add_argument("-a", "--angle", type=str, default = "0")
ap.add_argument("-t", "--time", type=str, default = "1")
ap.add_argument("-x", "--x_c", type=str, default = "0")
ap.add_argument("-y", "--y_c", type=str, default = "0")
ap.add_argument("-s", "--size_change", type=str, default = "1")

args = vars(ap.parse_args())


# Translating arguments into variables
image = cv2.imread(args["image"])
image1 = cv2.imread(args["image1"])

[h, w] = image1.shape[:2]

time = int(args["time"])
angle = int(args["angle"])
X = int(args["x_c"])
Y = int(args["y_c"])
size_change = int(args["size_change"])

# Rotating image using long method, are able to change point of rotation
M = cv2.getRotationMatrix2D( (X, Y), angle, size_change)
rotated = cv2.warpAffine(image1, M, (w, h))
cv2.imshow("Rotated Image", rotated)
cv2.waitKey()

# Rotating image using imutils convenience function
angle = 0
while True:
  for angle in range(0, 360): 
    final_image = imutils.rotate_bound(image, angle)
    cv2.imshow("Rotated Image 1", final_image)
    cv2.waitKey(time)

# This program was Rotating_Images_SV_XII.py by SarvasyaVikas
