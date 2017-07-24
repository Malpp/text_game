# pylint: disable=W0312,W0403
from random import randint


class MapObject(object):
	def __init__(self, height, width, accessible=False):
		self.accessible = accessible
		self.width = width
		self.height = height

	def is_accessible(self):
		return self.accessible

	def get_height(self):
		return self.height

	def get_width(self):
		return self.width

	def get_dimensions(self):
		return "{}x{}".format(self.width, self.height)

	def __str__(self):
		return self.get_dimensions()


class Room(MapObject):
	min_size = 3
	max_size = 6

	def __init__(self):
		super(Room, self).__init__(
			randint(self.min_size, self.max_size),
			randint(self.min_size, self.max_size),
			True
		)


class Empty(MapObject):
	def __init__(self):
		super(Empty, self).__init__(0, 0)
