# pylint: disable=W0312,W0403
import requests
import yaml


class Generator(object):

    def __init__(self):
        config = yaml.safe_load(open('config.yml'))
        config_values = [
            'monsters_url',
            'monster_api_key',
            'rooms_url',
            'rooms_api_key'
        ]
        for value in config_values:
            if value not in config:
                raise ValueError(
                    "{} was not found in the config file".format(value))

        self.monster_url = config['monsters_url']
        self.monster_api_key = config['monster_api_key']
        self.room_url = config['rooms_url']
        self.room_api_key = config['rooms_api_key']

    def get_monster(self):
        url = 'https://{}'
        r = requests.get(url)
