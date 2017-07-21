from room import Room
from random import randint

class Map_Sizes():
	@staticmethod
	def get_size(size="default"):
		options = ["default", "small", "medium", "large"]
		if size == options[1]:
			return (20,20)
		elif size == options[2]:
			return (40,40)
		elif size == options[3]:
			return (60,60)
		else:
			return (10,8)

class Map():
	def __init__(self, size_string):
		size = Map_Sizes.get_size(size_string)
		self.x = size[0]
		self.y = size[1]
		self.grid = [[0 for y in range(self.x)] for x in range(self.y)]
		self.grid[0][0] = Room()
	
	def display_map(self):
		for i in self.grid:
			for j in i:
				print j,            
			print ""
