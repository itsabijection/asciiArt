from __future__ import print_function
from PIL import Image
import math
import sys
import codecs
def mean(vals):
	m=0
	for i in vals:
		if i:
			m+=i
	return(m/len(vals))

dark="."
light=" "
#use unicode block (u25a0) instead of period
if len(sys.argv)>3 and sys.argv[3]=="unicode":
	dark=u'\u25a0'
#use specified unicode char instead of block (integer must be entered). heart is u2764
if len(sys.argv)>4:
	dark=unichr(int(sys.argv[4], 16))
#reverse colors
if len(sys.argv)>2 and int(sys.argv[2])==1:
	temp=light
	light=dark
	dark=temp


im=Image.open(sys.argv[1])
width, height=im.size
pixel=list(im.getdata())
brightness=[[None for x in range(width)] for y in range(height)]
for i in range(height):
	for j in range(width):
		#current pixel
		cpix=pixel[i*width+j]
		#magic numbers found online
		brightness[i][j]=(0.299*cpix[0]**2+0.587*cpix[1]**2+0.114*cpix[2]**2)**0.5
with codecs.open("blockImage.txt", "w", "utf-16") as ti:
	for i in range(0, height-2, 2):
		for j in range(0, width-2, 2):
			if mean((brightness[i][j], brightness[i+1][j], brightness[i][j+1], brightness[i+1][j+1], brightness[i+2][j]))<128:
				ti.write(dark)
			else:
				ti.write(light)
		ti.write("\n")