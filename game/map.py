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


class Map(object):

    def __init__(self, size_string):
        size = Map_Sizes.get_size(size_string)
        self.size_x = size[0]
        self.size_y = size[1]
        self.grid = [
            [
                room.Empty() for y in range(self.size_x)
            ] for x in range(self.size_y)
        ]
        self.grid[0][0] = room.Room()
        self.grid[self.size_y - 1][self.size_x - 1] = room.Room()
        self.rooms = [(0, 0)]
        self.generate_rooms()
        self.rooms.append((self.size_x - 1, self.size_y - 1))
        self.generate_hallways()

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

    def generate_rooms(self):
        remaining = int(self.size_x * self.size_y * 0.1)

        while remaining > 0:
            x = randint(0, self.size_x - 1)
            y = randint(0, self.size_y - 1)
            if str(self.grid[y][x]) == str(room.Empty()):
                self.grid[y][x] = room.Room()
                self.rooms.append((x, y))
                remaining -= 1

    def add_x_hallways(self, start, end, y, is_negative):
        mod = -1 if is_negative else 1
        for i in range(abs(end - start)):
            tile = self.grid[y][start + i * mod]
            if str(tile) == str(room.Empty()):
                self.grid[y][start + i * mod] = room.Hallway()

    def add_y_hallways(self, start, end, x, is_negative):
        mod = -1 if is_negative else 1
        for i in range(abs(end - start)):
            tile = self.grid[start + i * mod][x]
            if str(tile) == str(room.Empty()):
                self.grid[start + i * mod][x] = room.Hallway()

    def add_hallways(self, start_x, start_y, end_x, end_y):
        is_x_negative = (end_x - start_x < 0)
        is_y_negative = (end_y - start_y < 0)
        x_or_y_first = randint(1, 2)
        if x_or_y_first == 1:
            self.add_x_hallways(start_x, end_x, start_y, is_x_negative)
            self.add_y_hallways(start_y, end_y, end_x, is_y_negative)
        else:
            self.add_y_hallways(start_y, end_y, start_x, is_y_negative)
            self.add_x_hallways(start_x, end_x, end_y, is_x_negative)

    def generate_hallways(self):
        for room in range(len(self.rooms) - 1):
            from_room = self.rooms[room]
            to_room = self.rooms[room + 1]

            self.add_hallways(
                from_room[0], from_room[1], to_room[0], to_room[1])
