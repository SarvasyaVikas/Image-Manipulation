# Importing necessary packages
import argparse
import cv2
import numpy as np
import PIL
from PIL import Image

ap = argparse.ArgumentParser()

# Frames
ap.add_argument("-iI", "--imageI", type=str, default="Pyro_Iceman_Part_I.png")
ap.add_argument("-iII", "--imageII", type=str, default="Pyro_Iceman_Part_II.png")

args = vars(ap.parse_args())

imageI = cv2.imread(args["imageI"])
imageII = cv2.imread(args["imageII"])

(hI, wI) = imageI.shape[:2]
(hII, wII) = imageII.shape[:2]

X = 0
Y = 0

# Create new image to find difference
DifferenceI = Image.new(mode = "RGB", size = (210, 300), color = (255, 255, 255))

# Compiles images and fills up DifferenceI
for X in range(0, wI):
	for Y in range(0, hI):
		(bI, gI, rI) = imageI[Y, X]
		(bII, gII, rII) = imageII[Y, X]
		if Y > 440 and X > 811 and Y < 650 and X < 1111:
			if bI != bII or gI != gII or rI != rII:
				YI = Y - 440
				XI = X - 811
				if YI < 210 and XI < 300:
					bIII = abs(bII - bI)
					gIII = abs(gII - gI)
					rIII = abs(rII - rI)
					value = (bIII, gIII, rIII)
					DifferenceI.putpixel((YI, XI), value)
			else:
				if YI < 210 and XI < 300:
					YI = Y - 440
					XI = X - 811
					white = (255, 255, 255)
					DifferenceI.putpixel((YI, XI), white)

YII = 0
XII = 0

def init_Y(YIV):
	if YIV < 0:
		return 0
	elif YIV > 209:
		return 209
	else:
		return YIV
		
def init_X(XIV):
	if XIV < 0:
		return 0
	elif XIV > 299:
		return 299
	else:
		return XIV

# Eliminates small sections of different pixels
def near_white(Y, X):
	for rangeI in range(1, 7):
		total_near = 0
		YIII = -rangeI
		XIII = -rangeI
		for XIII in range(-rangeI, rangeI + 1):
			for YIII in range(-rangeI, rangeI + 1):
				global YIV
				global XIV
				YIV = Y + YIII
				XIV = X + XIII
				YV = init_Y(YIV)
				XV = init_Y(XIV)
				(bIV, gIV, rIV) = DifferenceI.getpixel((XV, YV))
				if bIV == 255 and gIV == 255 and rIV == 255:
					total_near += 1
				elif bIV < 20 and gIV < 20 and rIV < 20:
					total_near += 1
					
		rangeII = rangeI * 2
		rangeII += 1
		rangeIII = rangeII ** 2
		rangeIII -= 1
		rangeIV = rangeIII // 2
		if total_near >= rangeIV:
			return True
	return False

for XII in range(0, 300):
	for YII in range(0, 210):
		is_near_white = near_white(YII, XII)
		if is_near_white == True:
			white = (255, 255, 255)
			DifferenceI.putpixel((YII, XII), white)

# Shows image
DifferenceII = DifferenceI.rotate(270, expand= True)
DifferenceIII = DifferenceII.transpose(PIL.Image.FLIP_LEFT_RIGHT)
DifferenceIV = DifferenceIII.resize((1200, 840))
Difference = DifferenceIV.copy()
Difference.show()

# This program was Frame_Detection_SV_XXII.py by Vikas Sarvasya
