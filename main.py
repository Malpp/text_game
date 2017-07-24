# pylint: disable=W0312,W0403
from game.game import Game

game = Game()

game.run()
game.map.display_map()
print "Done!"
