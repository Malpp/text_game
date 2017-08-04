from random import randint

class Armor(object):
	def __init__(self, name, armor_class, description):
		self.name = name
		self.armor_class = armor_class
		self.description = description

	def roll_hit(self, to_hit):
		return to_hit > self.armor_class


class Cloth(Armor):
	def __init__(self):
		super(Cloth, self).__init__(
			"cloth",
			10,
			"Cloth armor, doesn't seem to give much protection"
		)


class Leather(Armor):
	def __init__(self):
		super(Leather, self).__init__(
			"leather",
			12,
			"This armor seems to be light and sturdy"
		)


class Mail(Armor):
	def __init__(self):
		super(Mail, self).__init__(
			"mail",
			15,
			"Nice heavy armor that can fend off most blows."
		)
