import argparse
import cv2

ap = argparse.ArgumentParser()

ap.add_argument("-i", "--image", type=str, default = "Kitty.jpg")
ap.add_argument("-wi", "--width", type=str, default = "200")
ap.add_argument("-he", "--height", type=str, default = "200")

args = vars(ap.parse_args())

image = cv2.imread(args["image"])
(h, w) = image.shape[:2]
width = int(args["width"])
height = int(args["height"])
cX = width
cY = height

section = image[:, 150:400]
cv2.imshow("Section", section)
cv2.waitKey()

while True:
	for cX in range(width, w, 20):
		for cY in range(height, h):
			sY = cY - height
			sX = cX - width
			section = image[sY:cY, sX:cX]
			cv2.imshow("Cropped Image", section)
			cv2.waitKey(1)
		print("Next Column")
	print("Next Round")
