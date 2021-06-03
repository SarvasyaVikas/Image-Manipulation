# Import necessary packages
import argparse
import cv2
import numpy as np

ap = argparse.ArgumentParser()

# Command line argument
ap.add_argument("-i", "--image", type=str, default = "Kitty.jpg")

args = vars(ap.parse_args())

# Translating command line argument into variable
image = cv2.imread(args["image"])

# Finding color values of the image
(b, g, r) = cv2.split(image)

# Black background
zeros = np.zeros(image.shape[:2], dtype = "uint8")

# Different filters of the image
cv2.imshow("Red", cv2.merge([zeros, zeros, r]))
cv2.imshow("Blue", cv2.merge([b, zeros, zeros]))
cv2.imshow("Green", cv2.merge([zeros, g, zeros]))
cv2.imshow("Magenta", cv2.merge([b, zeros, r]))
cv2.imshow("Yellow", cv2.merge([zeros, g, r]))
cv2.imshow("Cyan", cv2.merge([b, g, zeros]))
cv2.imshow("Merged", cv2.merge([b, g, r]))
cv2.waitKey()

# This program was Manipulating_Channels_SV_I.py by SarvasyaVikas
