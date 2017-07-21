from math import floor
from random import randint

class Room():

	min_size = 3
	max_size = 6

	def __init__(self):
		self.width = randint(self.min_size, self.max_size)
		self.height = randint(self.min_size, self.max_size)

	def __str__(self):
		return "{} x {}".format(self.width, self.height)