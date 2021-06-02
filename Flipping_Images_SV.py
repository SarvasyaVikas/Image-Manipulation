# Import necessary packages
import argparse
import cv2

ap = argparse.ArgumentParser()

# Command line arguments
ap.add_argument("-i", "--image", type=str, default = "Rogue.jpg")
ap.add_argument("-t", "--time", type=str, default = "500")

args = vars(ap.parse_args())

# Translating command line arguments into variables
image = cv2.imread(args["image"])
time = int(args["time"])

cv2.imshow("Original Image", image)
cv2.waitKey(time)

# Start infinite loop
while True:
  # Flip vertically
	first = cv2.flip(image, 1)
	cv2.imshow("Modified Image", first)
	cv2.waitKey(time)
  # Flip horizontally
	second = cv2.flip(first, 0)
	cv2.imshow("Modified Image", second)
	cv2.waitKey(time)
	# Flip vertically
  third = cv2.flip(second, 1)
	cv2.imshow("Modified Image", third)
	cv2.waitKey(time)
  # Flip horizontally
	fourth = cv2.flip(third, 0)
	cv2.imshow("Modified Image", fourth)
	cv2.waitKey(time)
  
# This program was Flipping_Images_SV_III.py by SarvasyaVikas
