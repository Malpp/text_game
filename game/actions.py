# pylint: disable=W0312,W0403
class Action(object):

    def __init__(self, name, actions, help_text):
        self.help_text = help_text
        self.actions = actions
        self.name = name

    def get_help(self):
        return self.help_text

    def is_action(self, action_input):
        return action_input.split(" ")[0].lower() == self.name.lower()

    def parse_action(self, sub_action_input):
        if sub_action_input not in self.actions:
            return -1
        else:
            return self.actions.index(sub_action_input)


class Move(Action):

    def __init__(self):
        super(Move, self).__init__(
            "move",
            ["north", "east", "south", "west"],
            "You can move North, East, South or West using 'move direction'"
        )

class Spawn(Action):

    def __init__(self):
        super(Spawn, self).__init__(
            "spawn",
            ["monster"],
            "Test function"
        )
