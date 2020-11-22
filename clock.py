#!/usr/bin/env python3

# written 2020-09-07 by mza
# last updated 2020-11-21 by mza

# https://learn.pimoroni.com/tutorial/sandyj/getting-started-with-inky-phat
from inky import InkyWHAT
#inky_display = InkyWHAT("red")
inky_display = InkyWHAT("black")
inky_display.set_border(inky_display.WHITE)
#inky_display.show()
width = 400
height = 300

#img = Image.open("x.png")
#img = Image.open("time.png")

import make_clock
import PythonMagick # sudo apt install -y python3-pythonmagick
import PIL
resolution = PythonMagick.Geometry(width, height)
import time
import datetime
#composite -size 400x300 -resize 400x300 -gravity center time.svg canvas:white time.png
# from https://stackoverflow.com/a/6209894/5728815
import inspect
import os
filename = inspect.getframeinfo(inspect.currentframe()).filename
path = os.path.dirname(os.path.abspath(filename))
#print(path)

#while /bin/true; do ./clock.py ; sleep 60; done
make_clock.set_width(width)
make_clock.set_height(height)
palette = PythonMagick.Image(path + "/palette.png")

def setup(time = datetime.datetime.now()):
	#print("")
	#print(str(datetime.datetime.now()) + " setup(" + str(time) + ")")
	make_clock.generate_clock(time) # generates an svg file with a clockface of the given time
	image = PythonMagick.Image(path + "/time.svg")
	image.size(resolution)
	image.pixelColor(width//2, height//2, "red")
	image.map(palette)
	image.write(path + "/output.png")
	img = PIL.Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
	img = PIL.Image.open(path + "/output.png")
	inky_display.set_image(img)
	#print(str(datetime.datetime.now()) + " setup() complete")

def show():
	#print(str(datetime.datetime.now()) + " show()")
	inky_display.show() # this takes about 7 seconds for B&W mode
	#print(str(datetime.datetime.now()) + " show() complete")

def once():
	setup()
	show()

def run():
	while True:
		setup(datetime.datetime.now() + datetime.timedelta(minutes=1))
		sleeptime = 60 - datetime.datetime.utcnow().second
		#print(str(sleeptime))
		time.sleep(sleeptime)
		show()

once()
run()

