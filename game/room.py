# pylint: disable=W0312,W0403
from random import randint
import weapon
import armor
import monster

class MapObject(object):

    def __init__(self, name, chance_loot, chance_monster, accessible=False):
        self.accessible = accessible
        self.name = name
        self.loot = None
        self.monster = None
        self.chance_loot = chance_loot
        self.chance_monster = chance_monster
        self.saw_loot = False

    def roll_loot(self):
        roll = randint(1,100)
        if roll < self.chance_loot:
            spawnable = [weapon.Axe(), weapon.Dagger(), weapon.Weapon(), armor.Cloth(), armor.Leather(), armor.Mail()]
            self.loot = spawnable[randint(0, len(spawnable) - 1)]

    def __str__(self):
        return self.name


class Room(MapObject):

    def __init__(self, should_spawn = True):
        super(Room, self).__init__("Room", 10, 15, True)
        if should_spawn:
            roll = randint(1,100)
            if roll < self.chance_monster:
                self.monster = monster.Monster()


class Empty(MapObject):

    def __init__(self):
        super(Empty, self).__init__(" ", 0, 0)


class Hallway(MapObject):

    def __init__(self):
        super(Hallway, self).__init__("Hallway", 5, 5, True)
