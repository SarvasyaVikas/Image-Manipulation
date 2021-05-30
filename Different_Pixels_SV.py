# Import needed packages
import argparse
import cv2
import time
import random

# Receive original image
ap = argparse.ArgumentParser()

# The user will have to load an image to disk that will be supplied to the program to be manipulated
ap.add_argument("-i", "--image", type=str, default="Quicksilver.jpg",
	help="path to the input image")

# Generating endpoints of Rectangle
ap.add_argument("-sI","--start_Y", type=str, default="0")
ap.add_argument("-eI","--end_Y", type=str, default="0")
ap.add_argument("-sII","--start_X", type=str, default="0")
ap.add_argument("-eII","--end_X", type=str, default="0")

# Color of rectangle
ap.add_argument("-b","--blue",type=str, default="0")
ap.add_argument("-g","--green",type=str, default="0")
ap.add_argument("-r","--red",type=str, default="0")

# Name of Images
ap.add_argument("-NI","--start_N",type=str, default="Original_Image")
ap.add_argument("-NII","--end_N",type=str, default="Modified_Image")

# Generating beginning point and leg length of 45-45-90 triangle
ap.add_argument("-RT_I","--RightTri_Y",type=str,default="0")
ap.add_argument("-RT_II","--RightTri_X",type=str,default="0") 
ap.add_argument("-TL","--Tri_Length",type=str,default="0")

# Color of 45-45-90 triangle
ap.add_argument("-bT","--blue_tri",type=str, default="0")
ap.add_argument("-gT","--green_tri",type=str, default="0")
ap.add_argument("-rT","--red_tri",type=str, default="0")

# Generating circle parameters
ap.add_argument("-cCY","--center_circ_Y",type=str, default="225")
ap.add_argument("-cCX","--center_circ_X",type=str, default="300")
ap.add_argument("-radC","--radius_circ",type=str, default="0")

# Color of circle
ap.add_argument("-bC","--blue_circ",type=str, default="0")
ap.add_argument("-gC","--green_circ",type=str, default="0")
ap.add_argument("-rC","--red_circ",type=str, default="0")

# Speed of the circle movement
ap.add_argument("-sp","--speed",type=str,default="0")

# Display original image
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
(h, w) = image.shape[:2]

#cv2.imshow(args["start_N"], image)
# If the user wants to show the original image, they can uncomment the previous line

# Translation of variables for rectangle endpoints
varI = 0
varII = 0
start_Y = int(args["start_Y"])
end_Y = int(args["end_Y"])
start_X = int(args["start_X"])
end_X = int(args["end_X"])

# Translation of variables for rectangle color
blue = int(args["blue"])
green = int(args["green"])
red = int(args["red"])

# Translation of variables for 45-45-90 triangle endpoints
varIII = 1
varIV = 1
Tri_Length = int(args["Tri_Length"])
RightTri_Y = int(args["RightTri_Y"])
RightTri_X = int(args["RightTri_X"])

# Translation of variables for 45-45-90 triangle color
blue_tri = int(args["blue_tri"])
green_tri = int(args["green_tri"])
red_tri = int(args["red_tri"])

# Translation of variables for circle parameters
center_circ_Y = int(args["center_circ_Y"])
center_circ_X = int(args["center_circ_X"])
radius_circ = int(args["radius_circ"])

# Translation of variables for circle color
blue_circ = int(args["blue_circ"])
green_circ = int(args["green_circ"])
red_circ = int(args["red_circ"])

# Define speed of moving circle
speed = int(args["speed"])

# Nestled for loop to generate rectangle
for varII in range(start_X, end_X):
	for varI in range(start_Y, end_Y):
		imageI = image
		imageI[varI,varII] = (blue,green,red)
    
# Nestled for loop to generate triangle
for varIV in range(1,Tri_Length):
	varVI = varIV + RightTri_X
	for varIII in range(RightTri_Y,varVI):
		varV = varIII + RightTri_Y
		imageI = image
		imageI[varV,varVI] = (blue_tri,green_tri,red_tri)
		
# Nestled for loop to generate circle
def circle(center_circ_Y,center_circ_X,radius_circ, image):
	# Arbitrary points
  arb_Y = 0
	arb_X = 0
	cI = h - 1
	cII = w - 1
	sq_radius = radius_circ * radius_circ
	imageI = image.copy()
	for arb_X in range(0,cII):
		for arb_Y in range(0,cI):
      
			# Distance between arbitrary point coordinates and center coordinates
			dist_Y = abs(arb_Y - center_circ_Y)
			dist_X = abs(arb_X - center_circ_X)
      
			# Square of the distances
			sqdist_Y = dist_Y * dist_Y
			sqdist_X = dist_X * dist_X
      
			# Distance theorem- square of the distance between point and center
			sqdist_T = sqdist_Y + sqdist_X
      
			# If the point is within the locus of points that make up the circle
			if sqdist_T <= sq_radius:
				imageI[arb_Y,arb_X] = (blue_circ,green_circ,red_circ)
	
  # Drawing the circle itself
	return imageI

# Defining new variables for simplicity of the code
cIII = h - radius_circ
cIV = w - radius_circ

def circle_decide(j,i):
	if j >= cIII:
		return 0
	elif j <= radius_circ:
		return 1
	elif i >= cIV:
		return 2	
	elif i <= radius_circ:
		return 3

# More variables for simplicity
i = radius_circ
j = h // 2

while j <= cIII and i <= cIV and j >= radius_circ and i >= radius_circ: 
	imageII = circle(j,i,radius_circ,image)
	
  # Output final image
	cv2.imshow(args["end_N"], imageII)
	cv2.waitKey(1)
	i += speed	
	j += speed

# Infinite loop
while True:
	
	# Initializing
	if j > cIII:
		j = cIII
	elif i > cIV:
		i = cIV
	elif j < radius_circ:
		j = radius_circ
	elif i < radius_circ:
		i = radius_circ
	
  # Determine path of the circle	
	r = random.randint(0,1)
	d = circle_decide(j,i)

	while j <= cIII and i <= cIV and j >= radius_circ and i >= radius_circ:
		imageII = circle(j,i,radius_circ,image)
		
    # Output final image
		cv2.imshow(args["end_N"], imageII)
		cv2.waitKey(1)
		
    # Execute circle movement	
		if d == 0:
			j -= speed
			if r == 0:
				i += speed
			elif r == 1:
				i -= speed
		elif d == 1:
			j += speed
			if r == 0:
				i += speed
			elif r == 1:
				i -= speed
		elif d == 2:
			i -= speed
			if r == 0:
				j -= speed
			elif r == 1:
				j += speed
		elif d == 3:
			i += speed
			if r == 0:
				j -= speed
			elif r == 1:
				j += speed
				
# This program was Different_Pixels_SV_LXIV.py by SarvasyaVikas
