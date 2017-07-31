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
        return self.player.update(self.map, action)
