# main.py -- put your code here!
# This code has been adapted from http://docs.micropython.org/en/latest/pyboard/pyboard/tutorial/leds.html

import pyb

from State import State

#create an leds array with 4 LED objects
leds = [pyb.LED(i) for i in range(1,5)]

#turn off all 4 LEDs
for l in leds:
    l.off()

accel = pyb.Accel()

enabled = State()
sw = pyb.Switch()

sw.callback(lambda:enabled.toggle())

while True:
	if enabled.get():
		angle = accel.y()
		if angle < 2 and angle > -2:
			leds[0].off()
			leds[1].on()
			leds[2].on()
			leds[3].off()
		if angle > 2 and angle < 5:
			leds[0].off()
			leds[1].off()
			leds[2].on()
			leds[3].off()
		if angle > 10 and angle < 15:
			leds[0].off()
			leds[1].off()
			leds[2].on()
			leds[3].on()
		if angle > 15:
			leds[0].off()
			leds[1].off()
			leds[2].off()
			leds[3].on()

		if angle < -15:
			leds[0].on()
			leds[1].off()
			leds[2].off()
			leds[3].off()
		if angle > -15 and angle < -10:
			leds[0].on()
			leds[1].on()
			leds[2].off()
			leds[3].off()
		if angle > -10 and angle < -5:
			leds[0].off()
			leds[1].on()
			leds[2].off()
			leds[3].off()
	else:
		for l in leds:
			l.off()

