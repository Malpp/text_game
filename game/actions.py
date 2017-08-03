# pylint: disable=W0312,W0403
class Action(object):

    def __init__(self, name, actions, help_text):
        self.help_text = help_text
        self.actions = actions
        self.name = name

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
            ["north", "east", "south", "west", "options"],
            "You can move North, East, South or West using `move command`"
        )


class Help(Action):

    def __init__(self):
        super(Help, self).__init__(
            "help",
            [],
            "The help function. Use `help command` to learn more about a command"
        )


class Attack(Action):

    def __init__(self):
        super(Attack, self).__init__(
            "attack",
            ["monster"],
            "Attack a monster. Use `attack monster`"
        )


class Loot(Action):

    def __init__(self):
        super(Loot, self).__init__(
            "loot",
            ["room"],
            "Loot a room. Use `loot room`"
        )


class Examine(Action):

    def __init__(self):
        super(Examine, self).__init__(
            "examine",
            ["room", "weapon", "armor", "loot"],
            "Examine an item. See full list of things to examine using `help examine`"
        )
