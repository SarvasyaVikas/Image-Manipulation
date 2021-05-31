# Importing necessary packages
# Install imutils
import argparse
import cv2
import numpy as np
import imutils

ap = argparse.ArgumentParser()

# Provided arguments
ap.add_argument("-i", "--image", type=str, default = "Quicksilver.jpg")
ap.add_argument("-s_TL_Y", "--section_Top_Left_Y", type=str, default = "0")
ap.add_argument("-s_TL_X", "--section_Top_Left_X", type=str, default = "0")
ap.add_argument("-s_BR_Y", "--section_Bottom_Right_Y", type=str, default = "0")
ap.add_argument("-s_BR_X", "--section_Bottom_Right_X", type=str, default = "0")

ap.add_argument("-r", "--right", type=str, default = "0")
ap.add_argument("-d", "--down", type=str, default = "0")

args = vars(ap.parse_args())

# Showing the original image
image = cv2.imread(args["image"])
cv2.imshow("Original", image)

# Finding corners of translated section
TLY = int(args["section_Top_Left_Y"])
TLX = int(args["section_Top_Left_X"])
BLY = int(args["section_Bottom_Right_Y"])
BLX = int(args["section_Bottom_Right_X"])

# Values for translating section, in pixels
Right = int(args["right"])
Down = int(args["down"])

# Deriving section
Section = image[TLY:BRY, TLX:BRX]

# Translating section using imutils
Moved = imutils.translate(Section, Right, Down)

# Showing image
cv2.imshow("Translated_Image", Moved)
cv2.waitKey() 

# This program was Translating_Images_SV_VII.py by SarvasyaVikas
