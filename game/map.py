# pylint: disable=W0312,W0403
import room
from random import randint


class Map_Sizes():
	@staticmethod
	def get_size(size="default"):
		options = ["default", "small", "medium", "large"]
		if size == options[1]:
			return (20, 20)
		elif size == options[2]:
			return (40, 40)
		elif size == options[3]:
			return (60, 60)
		else:
			return (10, 8)


class Map():
	def __init__(self, size_string):
		size = Map_Sizes.get_size(size_string)
		self.size_x = size[0]
		self.size_y = size[1]
		self.grid = [
			[room.Empty() for y in range(self.size_x)] for x in range(self.size_y)
		]
		self.grid[0][0] = room.Room()
		self.grid[0][1] = room.Room()

	def display_map(self):
		for i in self.grid:
			for j in i:
				print j,
			print ""

	def get_room(self, x, y):
		if x < 0 or y < 0 or x >= self.size_x or y >= self.size_y:
			return room.Empty()
		else:
			return self.grid[y][x]
