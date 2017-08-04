# Coveo Text Game
This is a text based game powered by a slack bot and the Coveo Cloud V2 platform

## Description
This project was to combine all my previous projects together and make one in my field of study. I used 
my last projects to quickly created a web source and parse a website full of mosnters. The website
contained random monsters from DnD 5e. Then when generating the map of the game, I do a randomized
call to the source to get a random monster. It works pretty well.

## How to build
This is a pretty long setup. Running a "Local setup" might be a pain, but here goes.

### Setup for the slack app
1. Create a new app in your team
2. Add a bot user in the app
3. Install the app in your team, keep the `Bot User OAuth Access Token` for later


### Setup for the python file
1. Download the following requirements
    1. `pip install pyyaml`
    2. `pip install slackclient`
2. Rename `example-config.yml` to `config.yml`
    1. Inside the new `config.yml`, change the values of the variables
    2. `monsters_url` to the url of where your org lives
    3. `monster_api_key` to a new API key with the following enabled
        1. `Search > Execute queries`
3. Next we need to get the ID of the bot
    1. Go [here](https://www.fullstackpython.com/blog/build-first-slack-bot-python.html) and navigate to the `Obtaining Our Bot’s ID` section
    2. Change the line `os.environ.get('SLACK_BOT_TOKEN')` to just put your bot's token
    3. Save the output for later
4. Now we need to setup the enviroment variables. This step maybe be different depending on how you run your script. Since I ran mine off VSCode, I'll do those steps
    1. Go to your `launch.json`
    2. Find the python instance type that you run, usually `Python`
    3. Under the `env` variable, add the following keys and values:
        1. `"SLACK_BOT_TOKEN": "Bot User OAuth Access Token FROM EARLIER"`
        2. `"BOT_ID": "Bot ID FROM EARLIER"`
    4. After changing to the right values, your bot should be up and running

### Setup for the web source
1. Create a Web Source called `Monsters`
    1. Under site url, put `http://chisaipete.github.io/bestiary/`
    2. Under advanced settings, put `Maximum crawling depth` to `1`
    3. Under Web Scraping, add the following config
```json
[
  {
    "for": {
      "urls": [
        ".*"
      ]
    },
    "exclude": [
      {
        "type": "CSS",
        "path": ".tag-list"
      },
      {
        "type": "CSS",
        "path": ".site-footer"
      },
      {
        "type": "CSS",
        "path": ".rss-subscribe"
      },
      {
        "type": "XPATH",
        "path": "//a[@href=\"#top\"]"
      },
      {
        "type": "XPATH",
        "path": "//*[@id=\"sortBy\"]"
      },
      {
        "type": "XPATH",
        "path": "//*[@id=\"creatureSearch\"]"
      },
      {
        "type": "CSS",
        "path": ".site-header"
      }
    ],
    "metadata": {
      "ac": {
        "type": "XPATH",
        "path": "//p[contains(., 'Armor Class')]/text()"
      },
      "hp": {
        "type": "XPATH",
        "path": "//p[contains(., 'Hit Points')]/text()"
      },
      "challenge": {
        "type": "XPATH",
        "path": "//p[contains(., 'Challenge')]/text()"
      },
      "name": {
        "type": "CSS",
        "path": ".post-title"
      }
    }
  }
]
```

    4. After adding the config, save but don't rebuild