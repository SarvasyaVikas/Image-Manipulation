# Importing necessary packages
import argparse
import cv2

ap = argparse.ArgumentParser()

# Command line arguments
ap.add_argument("-i", "--image", type=str, default = "Rogue.jpg")
ap.add_argument("-s", "--start", type=str, default = "75")
ap.add_argument("-e", "--end", type=str, default = "125")
ap.add_argument("-t", "--time", type=str, default = "1")
ap.add_argument("-c", "--change", type=str, default = "0")
ap.add_argument("-nH", "--new_Height", type=str, default = "960")
ap.add_argument("-nW", "--new_Width", type=str, default = "745")
ap.add_argument("-m", "--move", type=str, default = "1")

args = vars(ap.parse_args())

image = cv2.imread(args["image"])

# Start size and end size
start = int(args["start"])
end = int(args["end"])

# Time between switching frames
time = int(args["time"])

# Choose between which section to run
move = int(args["move"])
change = int(args["change"])

# New Height and Width for the change section
new_Height = int(args["new_Height"])
new_Width = int(args["new_Width"])

(h, w) = image.shape[:2]

scale_percent = 25

# Create an image with set pixel values as width and height
if change == 1:
	resized = cv2.resize(image, (new_Width, new_Height))
	cv2.imshow("Resized Image", resized)
	cv2.waitKey()

# Make the image get bigger and smaller in an animation
if move == 1:
	while True:
		for scale_percent in range(start, end + 1):
			new_height = h * scale_percent // 100	
			new_width = w * scale_percent // 100
		
			resized = cv2.resize(image, (new_width, new_height))

			cv2.imshow("Resized Image", resized)
			cv2.waitKey(time)
		
		scale_percent = scale_percent * -1
		
		for scale_percent in range(-end - 1, -start):
			scale_percent = scale_percent * -1
			new_height = h * scale_percent // 100	
			new_width = w * scale_percent // 100
		
			resized = cv2.resize(image, (new_width, new_height))

			cv2.imshow("Resized Image", resized)
			cv2.waitKey(time)
		
		scale_percent = scale_percent * -1
    
# This program was Resizing_Images_SV_VIII.py by SarvasyaVikas
