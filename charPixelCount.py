from PIL import Image, ImageFont, ImageDraw
from string import ascii_lowercase
with open("map.txt", "w") as f:
	for i in range(33, 126):
		count=0
		img=Image.new('RGB', (200,200))
		d=ImageDraw.Draw(img)
		d.text((20,20), chr(i), fill=(255,255,255))
		for pixel in img.getdata():
			if pixel==(255, 255, 255):
				count+=1
		f.write(str(count)+", ")