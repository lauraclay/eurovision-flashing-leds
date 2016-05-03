#!/usr/bin/python
# Simple demo of of the WS2801/SPI-like addressable RGB LED lights.
# Will color all the lights different primary colors.
# Author: Tony DiCola
# License: Public Domain
from __future__ import division
import time
import random

# Import the WS2801 module.
import Adafruit_WS2801
import Adafruit_GPIO.SPI as SPI


# Configure the count of pixels:
PIXEL_COUNT = 160

# Alternatively specify a hardware SPI connection on /dev/spidev0.0:
SPI_PORT   = 0
SPI_DEVICE = 0
pixels = Adafruit_WS2801.WS2801Pixels(PIXEL_COUNT, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

FACTOR = 0.03
SPARKLE = 0.02
#FACTOR = 1.0
#SPARKLE = 1.0
NUM_STARS = 10
CYCLE_DELAY = 0.1
CYCLE_COUNT = 30
STAR_BRIGHTNESS = 100

FRANCE = ((0,0,255),(100,100,100),(200,0,0))
ITALY = ((255,0,0),(100,100,100),(0,255,0))
GERMANY = ((0,0,0),(255,0,0),(255,255,0))

def pixels_from_tuple(i, n, t, factor, sparkle):
 for j in range(i,i+n):
  if j >= PIXEL_COUNT:
   return j
  (r,g,b) = t
  f = random.uniform(factor, factor-sparkle)
  pixels.set_pixel_rgb(j,int(r*f),int(b*f),int(g*f))
 return i+n

def tricolor(x,tt): 
 (first,second,third) = tt
 x = pixels_from_tuple(x,10,first,FACTOR,SPARKLE)
 x = pixels_from_tuple(x,10,second,FACTOR,SPARKLE)
 x = pixels_from_tuple(x,10,third,FACTOR,SPARKLE)
 return x
 

def do_tricolor_once(tt):
 x = 0
 while (x<PIXEL_COUNT):
  x = tricolor(x,tt)
 for p in range(0,NUM_STARS):
  pixels.set_pixel_rgb(random.randint(0,PIXEL_COUNT-1),STAR_BRIGHTNESS,STAR_BRIGHTNESS,STAR_BRIGHTNESS)
 pixels.show()
 x = 0
 while (x<PIXEL_COUNT):
  x = tricolor(x,tt)
 pixels.show()
 time.sleep(CYCLE_DELAY)

def do_tricolor_for_a_bit(tt,howlong):
 for i in range(0,howlong):
  do_tricolor_once(tt)

#################################

# Clear all the pixels to turn them off.
pixels.clear()
pixels.show()  # Make sure to call show() after changing any pixels!

while True:
 do_tricolor_for_a_bit(FRANCE,CYCLE_COUNT)
 do_tricolor_for_a_bit(ITALY,CYCLE_COUNT)
 do_tricolor_for_a_bit(GERMANY,CYCLE_COUNT)

# for brightness in range(0,128):
#  for i in range(PIXEL_COUNT):
#    pixels.set_pixel_rgb(0,0,i, brightness)  # Set the RGB color (0-255) of pixel i.  
#  pixels.show()
# for brightness in range(127,0,-1):
#  for i in range(PIXEL_COUNT):
#    pixels.set_pixel_rgb(i, 0, i, brightness)  # Set the RGB color (0-255) of pixel i.  
#  pixels.show()

    


# Now make sure to call show() to update the pixels with the colors set above!
pixels.show()

# Not used but you can also read pixel colors with the get_pixel_rgb function:
#r, g, b = pixels.get_pixel_rgb(0)  # Read pixel 0 red, green, blue value.
