# pylint: disable=W0312,W0403
from map import Map
from player import Player


class Game(object):

	def __init__(self):
		self.map = Map("default")
		self.player = Player(0, 0)

	def run(self):
		while True:
			action = raw_input("Action: ").rstrip().lower()
			if action == "stop":
				break
			self.update(action)

	def update(self, action):
		to_return = ""
		if self.player.is_dead:
			to_return += "You are dead"
		elif self.player.won:
			to_return += "You won!"
		else:
			to_return += self.player.update(self.map, action) + "\n"
			to_return += self.map.update(self.player)
		return to_return
