# Import necessary packages
import argparse
import cv2

ap = argparse.ArgumentParser()

# Command line arguments
ap.add_argument("-i", "--image", type=str, default = "Kitty.jpg")
ap.add_argument("-wi", "--width", type=str, default = "200")
ap.add_argument("-he", "--height", type=str, default = "200")

args = vars(ap.parse_args())

# Translating command line arguments into variables
image = cv2.imread(args["image"])
(h, w) = image.shape[:2]
width = int(args["width"])
height = int(args["height"])
cX = width
cY = height

section = image[:, 150:400]
cv2.imshow("Section", section)
cv2.waitKey()

# Infinite loop to continually move the cropped section
while True:
	for cX in range(width, w, 20):
		for cY in range(height, h):
			sY = cY - height
			sX = cX - width
			section = image[sY:cY, sX:cX]
			cv2.imshow("Cropped Image", section)
			cv2.waitKey(1)
	# Notifications to the user
		print("Next Column")
	print("Next Round")

# This program was Cropped_Images_SV_VI.py by SarvasyaVikas
