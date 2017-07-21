import actions

class Player():
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.actions = {
				"move": [actions.Move(), self.handle_move]
			}

	def update(self, map, action_text):
		split_text = action_text.strip().split(" ")

		if len(split_text) != 2:
			print "Invalid input"
		else:
			main_action = split_text[0].lower()
			action_option = split_text[1].lower()
			if main_action in self.actions:
				self.actions[main_action][1](self.actions[main_action][0].parse_action(action_option))
			else:
				print "No actions"

	def handle_move(self, direction):
		if direction == -1:
			print "Failed to move"
		elif direction == 0:
			print "Moved north"
		elif direction == 1:
			print "Moved east"
		elif direction == 2:
			print "Moved south"
		elif direction == 3:
			print "Moved west"
	