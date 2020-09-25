#!/usr/bin/env python3

# written 2020-09-07 by mza
# last updated 2020-09-25 by mza

# https://learn.pimoroni.com/tutorial/sandyj/getting-started-with-inky-phat
from inky import InkyWHAT
#inky_display = InkyWHAT("red")
inky_display = InkyWHAT("black")
inky_display.set_border(inky_display.WHITE)
#inky_display.show()

#img = Image.open("x.png")
#img = Image.open("time.png")

import make_clock
import PythonMagick # sudo apt install -y python3-pythonmagick
from PIL import Image, ImageFont, ImageDraw
resolution = PythonMagick.Geometry(400, 300)
import time
import datetime
#composite -size 400x300 -resize 400x300 -gravity center time.svg canvas:white time.png

#while /bin/true; do ./clock.py ; sleep 60; done

def once():
	make_clock.generate_clock() # generates an svg file with a clockface of the current time
	image = PythonMagick.Image()
	image.size(resolution)
	image.read("canvas:white")
	gravity_center = PythonMagick.GravityType(PythonMagick.GravityType.CenterGravity)
	clockface = PythonMagick.Image("time.svg")
	image.composite(clockface, gravity_center)
	image.pixelColor(200, 150, "red")
	#convert time.png -map palette.png output.png
	palette = PythonMagick.Image("palette.png")
	image.map(palette)
	image.write("output.png")
	img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
	img = Image.open("output.png")
	inky_display.set_image(img)
	inky_display.show()

def run():
	while True:
		sleeptime = 60 - datetime.datetime.utcnow().second
		#print(str(sleeptime))
		time.sleep(sleeptime)
		once()

#once()
run()
