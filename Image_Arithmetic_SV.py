# Import necessary packages
import argparse
import cv2
import numpy as np

ap = argparse.ArgumentParser()

# Command line argument
ap.add_argument("-i", "--image", type=str, default = "Kitty.jpg")

args = vars(ap.parse_args())

# Translates command line argument into variable
global image
image = cv2.imread(args["image"])

# Infinite loop
while True:
	# Resetting
  factor = 0
  # Lightening
	while factor <= 255:
		M = np.ones(image.shape, dtype = "uint8") * factor
		image1 = cv2.add(image, M)
		cv2.imshow("Modified Image", image1)
		cv2.waitKey(1)
		factor += 1
	factor = 255
  # Darkening
	while factor >= 0:
		M = np.ones(image.shape, dtype = "uint8") * factor
		image2 = cv2.add(image, M)
		cv2.imshow("Modified Image", image2)
		cv2.waitKey(1)
		factor -= 1
	factor = 0
  # Darkening
	while factor <= 255:
		M = np.ones(image.shape, dtype = "uint8") * factor
		image1 = cv2.subtract(image, M)
		cv2.imshow("Modified Image", image1)
		cv2.waitKey(1)
		factor += 1
	factor = 255
  # Lightening
	while factor >= 0:
		M = np.ones(image.shape, dtype = "uint8") * factor
		image1 = cv2.subtract(image, M)
		cv2.imshow("Modified Image", image1)
		cv2.waitKey(1)
		factor -= 1
    
# This program was Image_Arithmetic_SV_V.py by SarvasyaVikas
