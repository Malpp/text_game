import generation
from random import randint


class Monster(object):
	generator = generation.Generator()

	def __init__(self):
		monster_json = self.generator.get_monster()
		self.name = monster_json['Title']
		self.armor_class = monster_json['raw']['ac']
		self.is_dead = False
		self.hp = int(monster_json['raw']['hp'].split(' ')[0])
		self.saw_player = False
		self.is_boss = False

	def take_damage(self, damage):
		self.hp -= damage
		if self.hp < 1:
			self.is_dead = True

	def roll_attack(self, ac):
		roll = randint(1, 20)
		if roll > ac:
			return randint(1, 4)
		else:
			return 0


class BossMonster(Monster):

	def __init__(self):
		super(BossMonster, self).__init__()
		self.name = "Mad scientist"
		self.armor_class = 10
		self.hp = 10
		self.is_boss = True
