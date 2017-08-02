from random import randint

class Weapon(object):
    def __init__(self, name, damage, to_hit, description):
        self.name = name
        self.damage = damage
        self.to_hit = to_hit
        self.description = description

    def roll_hit(self):
        roll = randint(1,20)
        if roll > self.to_hit:
            return randint(1, self.damage)
        else:
            return 0


class Dagger(Weapon):
    def __init__(self):
        super(Dagger, self).__init__(
            "dagger",
            3,
            10,
            "Small blunt dagger. It works I guess."
        )


class Axe(Weapon):
    def __init__(self):
        super(Axe, self).__init__(
            "axe",
            6,
            13,
            "This looks like it hard to swing, but it's mighty sharp"
        )


class Sword(Weapon):
    def __init__(self):
        super(SwordAxe, self).__init__(
            "sword",
            5,
            15,
            "This sword feels good and light in your hand."
        )
