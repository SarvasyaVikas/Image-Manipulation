import argparse
import cv2
import imutils
from PIL import Image
import numpy as np

# Different Pixels
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

def circle_decide(j,i):
	if j >= cIII:
		return 0
	elif j <= radius_circ:
		return 1
	elif i >= cIV:
		return 2	
	elif i <= radius_circ:
		return 3

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

# Frame Detection
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

	# This part is the usage of the near_white function
for XII in range(0, 300):
	for YII in range(0, 210):
		is_near_white = near_white(YII, XII)
		if is_near_white == True:
			white = (255, 255, 255)
			
# Generating Shapes
def point_arrays(endpoints, speed):
	if endpoints == 3:
		arrI = np.array([[pointsX[-3]+speed,pointsY[-3]+speed],[pointsX[-2]+speed,pointsY[-2]+speed],[pointsX[-1]+speed,pointsY[-1]+speed]])
		return arrI
	elif endpoints == 4:
		arrI = np.array([[pointsX[-4]+speed,pointsY[-4]+speed],[pointsX[-3]+speed,pointsY[-3]+speed],[pointsX[-2]+speed,pointsY[-2]+speed],[pointsX[-1]+speed,pointsY[-1]+speed]])
		return arrI

def random_color():
	blue_intensity = random.randint(0,256)
	green_intensity = random.randint(0,256)
	red_intensity = random.randint(0,256)

	generated_color = (blue_intensity, green_intensity, red_intensity)
	
	return generated_color

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
			DifferenceI.putpixel((YII, XII), white)
			
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
	
# Rotating Images

	# Rotating image using long method, are able to change point of rotation
M = cv2.getRotationMatrix2D( (X, Y), angle, size_change)
rotated = cv2.warpAffine(image1, M, (w, h))
cv2.imshow("Rotated Image", rotated)
cv2.waitKey()

	# Rotating image using imutils convenience function
angle = 0
while True:
  for angle in range(0, 360): 
    final_image = imutils.rotate_bound(image, angle)
    cv2.imshow("Rotated Image 1", final_image)
    cv2.waitKey(time)

# Resizing Images

global scale_percent
scale_percent = start

if change == 1:
	resized = cv2.resize(image, (new_Width, new_Height))
	cv2.imwrite("Final_Image.jpg", resized)
	cv2.imshow("Resized Image", resized)
	cv2.waitKey()

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

# Translating Images

	# Deriving section
Section = image[TLY:BRY, TLX:BRX]

	# Translating section using imutils
Moved = imutils.translate(Section, Right, Down)

# Video Differences

def init_color(value):
	value += 256
	multiplier = value // 256
	modifier = multiplier * 256
	final_value = value - modifier
	return final_value

def modify_image(frame1, frame2, frame3):
	for D2 in range(0, w):
		for D1 in range(0, h):
			(v1) = frame1[D1, D2]
			(v2) = frame2[D1, D2]
			vD = abs(v2 - v1)
			if vD < 20 or vD > 235:
				frame3[D1, D2] = (0)
			else:
				frame3[D1, D2] = (vD)
	return frame3
	
global frame_number
frame_number = 0
	
while(cap.isOpened()):
	ret, frame = cap.read()
	if ret == True:
		frame_number += 1
		if frame_number == start:
			global frame1
			frame1 = frame
		elif frame_number == start + 1:
			global frame2
			frame2 = frame
		elif frame_number == start + 2:
			global frame3
			frame3 = frame
		elif frame_number == start + 3:
			global frame4
			frame4 = frame

# Image Arithmetic

while True:
	factor = 0

	while factor <= 255:
		M = np.ones(image.shape, dtype = "uint8") * factor
		image1 = cv2.add(image, M)
		cv2.imshow("Modified Image", image1)
		cv2.waitKey(1)
		factor += 1
	factor = 255
	while factor >= 0:
		M = np.ones(image.shape, dtype = "uint8") * factor
		image2 = cv2.add(image, M)
		cv2.imshow("Modified Image", image2)
		cv2.waitKey(1)
		factor -= 1
	factor = 0
	while factor <= 255:
		M = np.ones(image.shape, dtype = "uint8") * factor
		image1 = cv2.subtract(image, M)
		cv2.imshow("Modified Image", image1)
		cv2.waitKey(1)
		factor += 1
	factor = 255
	while factor >= 0:
		M = np.ones(image.shape, dtype = "uint8") * factor
		image1 = cv2.subtract(image, M)
		cv2.imshow("Modified Image", image1)
		cv2.waitKey(1)
		factor -= 1

# Masking Images

while True:
	for X in range(radius, distX, tenth_radius):
		for Y in range(radius, distY, speed):
			background = np.zeros(image.shape[:2], dtype = "uint8")
			mask = cv2.circle(background, (X, Y), radius, 255, -1)
			masked = cv2.bitwise_and(image, image, mask=mask)
			cv2.imshow("Modified Image", masked)
			cv2.waitKey(1)

# Manipulating Channels

(b, g, r) = cv2.split(image)

zeros = np.zeros(image.shape[:2], dtype = "uint8")

cv2.imshow("Red", cv2.merge([zeros, zeros, r]))
cv2.imshow("Blue", cv2.merge([b, zeros, zeros]))
cv2.imshow("Green", cv2.merge([zeros, g, zeros]))
cv2.imshow("Magenta", cv2.merge([b, zeros, r]))
cv2.imshow("Yellow", cv2.merge([zeros, g, r]))
cv2.imshow("Cyan", cv2.merge([b, g, zeros]))
cv2.imshow("Merged", cv2.merge([b, g, r]))
cv2.waitKey()

# This program is Image-Manipulation_Methods.py by SarvasyaVikas
