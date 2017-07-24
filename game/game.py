from map import Map
from player import Player

class Game():
	def __init__(self):
		self.map = Map("small")
		self.player = Player(0,0)
		self.text_handler = ""

	def run(self):
		while True:
			action = raw_input("Action: ").rstrip().lower()
			if action == "stop":
				break
			self.update(action)

	def update(self, action):
		self.player.update(self.map, action)
