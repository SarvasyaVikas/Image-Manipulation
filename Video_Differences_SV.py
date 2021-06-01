# Import necessary packages
import argparse
import cv2
import imutils
import numpy as np
from PIL import Image

ap = argparse.ArgumentParser()

# Command line arguments
ap.add_argument("-v", "--video", type=str, default = "X2-Pyro.mp4")
ap.add_argument("-s", "--start", type=str, default = "1336")

args = vars(ap.parse_args())

# Define video in a variable
cap = cv2.VideoCapture('X2-Pyro.mp4')

start = int(args["start"])

global frame_number
frame_number = 0

# Take four frames out of the video
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
	else:
		break


(h, w) = frame1.shape[:2]

D1 = 0
D2 = 0

# Turn all images into grayscale
frame5 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
frame6 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
frame7 = cv2.cvtColor(frame3, cv2.COLOR_BGR2GRAY)
frame8 = cv2.cvtColor(frame4, cv2.COLOR_BGR2GRAY)
frame9 = frame6.copy()
frame10 = frame7.copy()
frame11 = frame8.copy()

# Function to ensure that no values are exceeding 256 or below 0
def init_color(value):
	value += 256
	multiplier = value // 256
	modifier = multiplier * 256
	final_value = value - modifier
	return final_value

# Function to find differences between frames given different inputs
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

# Creating frame differences
frame12 = modify_image(frame5, frame6, frame9)
frame13 = modify_image(frame6, frame7, frame10)
frame14 = modify_image(frame7, frame8, frame11)
cv2.imshow("Original", frame5)
cv2.waitKey()

frame16 = frame13.copy()
frame17 = frame14.copy()

# First tier- differences between frames
cv2.imshow("DifferenceA1", frame12)
cv2.imshow("DifferenceA2", frame13)
cv2.imshow("DifferenceA3", frame14)
cv2.waitKey()

frame18 = modify_image(frame12, frame13, frame16)
frame19 = modify_image(frame13, frame14, frame17)

frame20 = frame19.copy()

# Second tier- differences between A level frames
cv2.imshow("DifferenceB1", frame18)
cv2.imshow("DifferenceB2", frame19)
cv2.waitKey()

frame21 = modify_image(frame18, frame19, frame20)

# Third tier- differences between C level frames
cv2.imshow("DifferenceC1", frame21)
cv2.waitKey()

# This program was Video_Differences_SV_XXVII.py by SarvasyaVikas
