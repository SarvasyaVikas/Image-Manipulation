# Import necessary packages
import argparse
import cv2
import numpy as np

ap = argparse.ArgumentParser()

# Command line arguments
ap.add_argument("-i", "--image", type=str, default = "Kitty.jpg")
ap.add_argument("-r", "--radius", type=str, default = "100")
ap.add_argument("-s", "--speed", type=str, default = "1")

args = vars(ap.parse_args())

# Translating command line arguments into variables
image = cv2.imread(args["image"])
radius = int(args["radius"])
speed = int(args["speed"])

# Dimensions of the image
(h, w) = image.shape[:2]

# Variables used in animating mask
X = radius
Y = radius
distX = w - radius
distY = h - radius
tenth_radius = radius // 10

# Infinite loop that is moving the mask
while True:
	for X in range(radius, distX, tenth_radius):
		for Y in range(radius, distY, speed):
			background = np.zeros(image.shape[:2], dtype = "uint8")
			mask = cv2.circle(background, (X, Y), radius, 255, -1)
			masked = cv2.bitwise_and(image, image, mask=mask)
			cv2.imshow("Modified Image", masked)
			cv2.waitKey(1)
      
# This program was Masking_Images_SV_II.py by SarvasyaVikas
