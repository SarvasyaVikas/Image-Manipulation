# Importing necessary packages
import argparse
import cv2
import numpy as np
import random

ap = argparse.ArgumentParser()

# Command line arguments
ap.add_argument("-i", "--image", type=str, default="Quicksilver.jpg",
	help="path to the input image")
	
ap.add_argument("-e","--endpoints",type=str,default="3")
ap.add_argument("-sp","--speed",type=str,default="1")
ap.add_argument("-th","--thickness",type=str,default="1")

args = vars(ap.parse_args())

# Find dimensions of image
image = cv2.imread(args["image"])
(h, w) = image.shape[:2]

# Converting user inputs into variables
endpoints = int(args["endpoints"])
speed = int(args["speed"])
thickness = int(args["thickness"])

# Defining two empty lists
pointsX0 = []
pointsY0 = []

# This function will append the coordinates into a list for the shape
def point_arrays(endpoints, speed):
	if endpoints == 3:
		arrI = np.array([[pointsX[-3]+speed,pointsY[-3]+speed],[pointsX[-2]+speed,pointsY[-2]+speed],[pointsX[-1]+speed,pointsY[-1]+speed]])
		return arrI
	elif endpoints == 4:
		arrI = np.array([[pointsX[-4]+speed,pointsY[-4]+speed],[pointsX[-3]+speed,pointsY[-3]+speed],[pointsX[-2]+speed,pointsY[-2]+speed],[pointsX[-1]+speed,pointsY[-1]+speed]])
		return arrI

# Generates a random color
def random_color():
	blue_intensity = random.randint(0,256)
	green_intensity = random.randint(0,256)
	red_intensity = random.randint(0,256)

	generated_color = (blue_intensity, green_intensity, red_intensity)
	
	return generated_color

# The movement portion only applies for the triangle

# Decide which vertex of the triangle is touching which edge of the picture to inform future movements
def tri_decide(arrIII):

	vIV = w - speed
	vV = h - speed
	vVI = speed
	if arrIII[0,0] >= vIV:
		return 0
	elif arrIII[0,0] <= vVI:
		return 1
	elif arrIII[1,0] >= vIV:
		return 2
	elif arrIII[1,0] <= vVI:
		return 3
	elif arrIII[2,0] >= vIV:
		return 4
	elif arrIII[2,0] <= vVI:
		return 5
	elif arrIII[0,1] >= vV:
		return 6
	elif arrIII[0,1] <= vVI:
		return 7
	elif arrIII[1,1] >= vV:
		return 8
	elif arrIII[1,1] <= vVI:
		return 9
	elif arrIII[2,1] >= vV:
		return 10
	elif arrIII[2,1] <= vVI:
		return 11

# This function initializes the triangle location
def tri_initialize(arrIII):

	vIV = w - speed
	vV = h - speed
	vVI = speed
	if arrIII[0,0] >= vIV:
		add = vIV - arrIII[0,0]
		arrIII[0,0] += add
		arrIII[1,0] += add
		arrIII[2,0] += add
		return arrIII
	elif arrIII[0,0] <= vVI:
		add = vVI - arrIII[0,0]
		arrIII[0,0] += add
		arrIII[1,0] += add
		arrIII[2,0] += add
		return arrIII
	elif arrIII[1,0] >= vIV:
		add = vIV - arrIII[1,0]
		arrIII[0,0] += add
		arrIII[1,0] += add
		arrIII[2,0] += add
		return arrIII
	elif arrIII[1,0] <= vVI:
		add = vVI - arrIII[1,0]
		arrIII[0,0] += add
		arrIII[1,0] += add
		arrIII[2,0] += add
		return arrIII
	elif arrIII[2,0] >= vIV:
		add = vIV - arrIII[2,0]
		arrIII[0,0] += add
		arrIII[1,0] += add
		arrIII[2,0] += add
		return arrIII
	elif arrIII[2,0] <= vVI:
		add = vVI - arrIII[2,0]
		arrIII[0,0] += add
		arrIII[1,0] += add
		arrIII[2,0] += add
		return arrIII
	elif arrIII[0,1] >= vV:
		add = vV - arrIII[0,1]
		arrIII[0,1] += add
		arrIII[1,1] += add
		arrIII[2,1] += add
		return arrIII
	elif arrIII[0,1] <= vVI:
		add = vVI - arrIII[0,1]
		arrIII[0,1] += add
		arrIII[1,1] += add
		arrIII[2,1] += add
		return arrIII
	elif arrIII[1,1] >= vV:
		add = vV - arrIII[1,1]
		arrIII[0,1] += add
		arrIII[1,1] += add
		arrIII[2,1] += add
		return arrIII
	elif arrIII[1,1] <= vVI:
		add = vVI - arrIII[1,1]
		arrIII[0,1] += add
		arrIII[1,1] += add
		arrIII[2,1] += add
		return arrIII
	elif arrIII[2,1] >= vV:
		add = vV - arrIII[2,1]
		arrIII[0,1] += add
		arrIII[1,1] += add
		arrIII[2,1] += add
		return arrIII
	elif arrIII[2,1] <= vVI:
		add = vVI - arrIII[2,1]
		arrIII[0,1] += add
		arrIII[1,1] += add
		arrIII[2,1] += add
		return arrIII

a = 0
b = 0
c = 0

pointsX = pointsX0.copy()
pointsY = pointsY0.copy()

# This randomly generates the coordinates of the shape
for a in range(0, endpoints):
	rX = random.randint(0, w-1)
	pointsX.append(rX)
for b in range(0, endpoints):
	rY = random.randint(0, h-1)
	pointsY.append(rY)

lowest_point_Y = max(pointsY)
distanceI = h - lowest_point_Y

right_point_X = max(pointsX)
distanceII = w - right_point_X

# This function is used to move the triangle from its original location and set up the movement with the rest of the program
def original_move():
	global c
	global distanceI
	global distanceII
	global thickness
		
	while c < distanceI and c < distanceII:
		global arrIII
		imageI = image.copy()
		arrII = point_arrays(endpoints, c)
		arrIII = arrII.copy()
		final_image = cv2.polylines(imageI,[arrIII],True,random_color(),thickness)

		cv2.imshow("Modified_Image",final_image)
		cv2.waitKey(2)
		c += speed
		global arrIV
		arrIV = arrIII.copy()
	return arrIV
		
arrV = original_move()

# Makes the triangle bounce around the edges of the image
if endpoints == 3:	
	while True:
		
		global d
		d = tri_decide(arrV)
		arrIII = tri_initialize(arrV)
		r = random.randint(0,1)
		
		vI = w + speed
		vII = h + speed
		vIII = speed
		thickness += 1
		
		while bool(bool(bool(arrV[0,0] <= vI and arrV[0,0] >= vIII) and bool(arrV[1,0] <= vI and arrV[1,0] >= vIII)) and bool(bool(arrV[2,0] <= vI and arrV[2,0] >= vIII) and bool(arrV[0,1] <= vII and arrV[0,1] >= vIII)) and bool(bool(arrV[1,1] <= vII and arrV[1,1] >= vIII) and bool(arrV[2,1] <= vII and arrV[2,1] >= vIII))) == True:

			imageII = image.copy()
			
			if d == 0 or d == 2 or d == 4:
				arrIII[0,0] -= speed
				arrIII[1,0] -= speed
				arrIII[2,0] -= speed
				if r == 0:
					arrIII[0,1] -= speed
					arrIII[1,1] -= speed
					arrIII[2,1] -= speed
				elif r == 1:
					arrIII[0,1] += speed
					arrIII[1,1] += speed
					arrIII[2,1] += speed
			
				final_image = cv2.polylines(imageII,[arrIII],True,random_color(),thickness)
				cv2.imshow("Modified_Image",final_image)
				cv2.waitKey(2)
			elif d == 1 or d == 3 or d == 5:
				arrIII[0,0] += speed
				arrIII[1,0] += speed
				arrIII[2,0] += speed
				if r == 0:
					arrIII[0,1] += speed
					arrIII[1,1] += speed
					arrIII[2,1] += speed
				elif r == 1:
					arrIII[0,1] -= speed
					arrIII[1,1] -= speed
					arrIII[2,1] -= speed
			
				final_image = cv2.polylines(imageII,[arrIII],True,random_color(),thickness)
				cv2.imshow("Modified_Image",final_image)
				cv2.waitKey(2)
			elif d == 6 or d == 8 or d == 10:
				arrIII[0,1] -= speed
				arrIII[1,1] -= speed
				arrIII[2,1] -= speed
				if r == 0:
					arrIII[0,0] += speed
					arrIII[1,0] += speed
					arrIII[2,0] += speed
				elif r == 1:
					arrIII[0,0] -= speed
					arrIII[1,0] -= speed
					arrIII[2,0] -= speed
				
				final_image = cv2.polylines(imageII,[arrIII],True,random_color(),thickness)
				cv2.imshow("Modified_Image",final_image)
				cv2.waitKey(2)
			elif d == 7 or d == 9 or d == 11:
				arrIII[0,1] += speed
				arrIII[1,1] += speed
				arrIII[2,1] += speed
				if r == 0:
					arrIII[0,0] -= speed
					arrIII[1,0] -= speed
					arrIII[2,0] -= speed
				elif r == 1:
					arrIII[0,0] += speed
					arrIII[1,0] += speed
					arrIII[2,0] += speed
				
				final_image = cv2.polylines(imageII,[arrIII],True,random_color(),thickness)
				cv2.imshow("Modified_Image",final_image)
				cv2.waitKey(2)

# This program was Generating_Shapes_SV_XXXII.py by SarvasyaVikas
