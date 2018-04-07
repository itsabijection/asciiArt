from __future__ import print_function
from PIL import Image
import math
import sys
import codecs
def mean(vals):
	m=0
	for i in vals:
		m+=i
	return(m/len(vals))

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
with codecs.open("blockImage.txt", "w", "utf-8") as ti:
	for i in range(0, height, 2):
		for j in range(0, width, 2):
			if mean((brightness[i][j], brightness[i+1][j], brightness[i][j+1], brightness[i+1][j+1], brightness[i+2][j]))>128:
				ti.write(u'\u25A0')
				#ti.write(".")
			else:
				ti.write(' ')
		ti.write("\n")