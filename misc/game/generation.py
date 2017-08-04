# pylint: disable=W0312,W0403
import requests
import yaml
from random import randint
import json


class Generator(object):

	def __init__(self):
		config = yaml.safe_load(open('config.yml'))
		config_values = [
			'monsters_url',
			'monster_api_key'
		]
		for value in config_values:
			if value not in config:
				raise ValueError(
					"{} was not found in the config file".format(value))

		self.monster_url = config['monsters_url']
		self.monster_api_key = config['monster_api_key']

	def get_monster(self):
		url = "https://{}/rest/search/?numberOfResults=1&rankingFunctions=%5B%7B%22expression%22%3A%22(%40magic%2B{})%251000000%20%2B%201%22%2C%22normalizeWeight%22%3Afalse%7D%5D&maximumAge=-1&q=%40source%3D%22Monsters%22&format=json&access_token={}".format(self.monster_url, randint(1000000, 10000000), self.monster_api_key)
		r = requests.get(url)
		monster_json = json.loads(r.text)
		return monster_json['results'][0]
