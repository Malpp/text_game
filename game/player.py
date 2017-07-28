# pylint: disable=W0312,W0403
import actions
import generation
from map import Map


class Player(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.actions = {
            "move": [actions.Move(), self.handle_move],
            "spawn": [actions.Spawn(), self.handle_spawn]
        }
        self.generator = generation.Generator()

    def update(self, map_obj, action_text):
        split_text = action_text.strip().split(" ")

        if len(split_text) != 2:
            print "Invalid input"
        else:
            main_action = split_text[0].lower()
            action_option = split_text[1].lower()
            if main_action in self.actions:
                self.actions[main_action][1](
                    self.actions[main_action][
                        0].parse_action(action_option),
                    map_obj
                )
            else:
                print "No actions"

    def handle_move(self, direction, map_obj):
        new_x = self.x
        new_y = self.y

        if direction == -1:
            print "Invalid direction"
            return
        elif direction == 0:
            new_y -= 1
        elif direction == 1:
            new_x += 1
        elif direction == 2:
            new_y += 1
        elif direction == 3:
            new_x -= 1

        room = map_obj.get_room(new_x, new_y)

        if room.accessible:
            self.x = new_x
            self.y = new_y
            print "Moved into {}".format(room)
        else:
            print "You can't move there"

    def handle_spawn(self, result, map_obj):
        if result == 0:
            self.generator.get_monster()
        elif result == 1:
            new_map = Map("small")
            new_map.display_map()
