class State:
	def __init__(self):
		self.b=True
	def set(self, val):
		self.b = val
	def toggle(self):
		self.b = not self.b
	def get(self):
		return self.b