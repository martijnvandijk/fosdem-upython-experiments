import pyb
import time

class State:
	def __init__(self):
		self.b=True
	def set(self, val):
		self.b = val
	def toggle(self):
		self.b = not self.b
	def get(self):
		return self.b

status = State()
sw = pyb.Switch()
sw.callback(lambda:status.toggle())

led = pyb.LED(1)

while True:
	if status.get():
		led.toggle()
		time.sleep_ms(500)
	else:
		led.off()