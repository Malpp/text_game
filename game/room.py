# pylint: disable=W0312,W0403


class MapObject(object):

    def __init__(self, name, accessible=False):
        self.accessible = accessible
        self.name = name

    def __str__(self):
        return self.name


class Room(MapObject):

    def __init__(self):
        super(Room, self).__init__("R", True)


class Empty(MapObject):

    def __init__(self):
        super(Empty, self).__init__(" ")


class Hallway(MapObject):

    def __init__(self):
        super(Hallway, self).__init__("H", True)
