# pylint: disable=W0312,W0403
import actions
import generation
from map import Map
import weapon
import armor


class Player(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.actions = {
            "help": [actions.Help(), self.handle_help],
            "move": [actions.Move(), self.handle_move],
            "attack": [actions.Attack(), self.handle_attack]
        }
        self.generator = generation.Generator()
        self.armor = armor.Cloth()
        self.weapon = weapon.Dagger()
        self.hp = 10
        self.is_dead = False

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 1:
            self.is_dead = True

    def update(self, map_obj, action_text):
        split_text = action_text.strip().split(" ")

        if self.is_dead:
            return "You are dead"

        if len(split_text) == 1:
            split_text.append("")

        main_action = split_text[0].lower()
        action_option = split_text[1].lower()
        if main_action in self.actions:
            return self.actions[main_action][1](
                    self.actions[main_action][
                    0].parse_action(action_option),
                action_option,
                map_obj
            )
        else:
            return "No actions"

    def handle_move(self, direction, command, map_obj):
        room_monster = map_obj.get_room(self.x, self.y).monster
        if room_monster is not None and not room_monster.is_dead:
            return "You cannot run away from a monster!"

        new_x = self.x
        new_y = self.y

        if direction == -1:
            return "Invalid direction"
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
            return "Moved into {}".format(room)
        else:
            return "You can't move there"

    def handle_help(self, result, command, map_obj):
        to_return = ""
        if command in self.actions and command != "help":
            to_return += self.actions[command][0].help_text + "\n"
            to_return += "Avaible commands: \n"
            to_return += ", ".join(self.actions[command][0].actions)
        else:
            to_return += self.actions['help'][0].help_text + "\n"
            to_return += "Avaible commands: \n"
            to_return += ", ".join(list(self.actions.keys()))

        return to_return

    def handle_attack(self, result, command, map_obj):
        room_monster = map_obj.get_room(self.x, self.y).monster
        damage = self.weapon.roll_hit()
        if room_monster is not None:
            if not room_monster.is_dead:
                if damage == 0:
                    return "You missed your attack"
                else:
                    to_return = ""
                    to_return += "You hit the monster for {} damage \n".format(damage)
                    room_monster.take_damage(damage)
                    if room_monster.is_dead:
                        to_return += "You have killed the monster!"
                    return to_return
            else:
                return "Woah, chill, the monster is already dead..."
        else:
            return "There is nothing to attack..."
