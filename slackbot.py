import os
import time
from slackclient import SlackClient
import json
from game.game import Game


# starterbot's ID as an environment variable
BOT_ID = os.environ.get("BOT_ID")

# constants
AT_BOT = "<@" + BOT_ID + ">"

games = {}

# instantiate Slack & Twilio clients
slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))


def handle_command(command, channel, user):
    """
        Receives commands directed at the bot and determines if they
        are valid commands. If so, then acts on the commands. If not,
        returns back what it needs for clarification.
    """

    if command.startswith('start game'):
        print "{} started a game".format(user)
        send_message("Generating map...", channel)
        games[user] = Game()
        send_message("Game started! Type `end game` to stop. Don't forget to use the `help` command!", channel)
        send_message("You wake up in a stone dungeon. It seems like you were "
                     + "chained to the wall but something or someone broke you"
                     + " break from it. Although you don't remember much about"
                     + " how you got hear, you do remember one thing: "
                     + "You need to escape the *Coveo Lab*", channel)
    elif command.startswith('end game'):
        games.pop(user, None)
        send_message("Game stopped. You can now start a new one.", channel)
    elif user in games:
        send_message(games[user].update(command), channel)
    else:
        send_message("Please type the command `start game` to play", channel)


def parse_slack_output(slack_rtm_output):
    """
        The Slack Real Time Messaging API is an events firehose.
        this parsing function returns None unless a message is
        directed at the Bot, based on its ID.
    """
    output_list = slack_rtm_output
    if output_list and len(output_list) > 0:
        for output in output_list:
            if output and 'user' in output and output['user'] != BOT_ID:
                # if output and 'text' in output:
                    # send_message(json.dumps(output), output['channel'])

                if output and 'text' in output and AT_BOT in output['text'] and output['channel'].startswith('C'):
                    # return text after the @ mention, whitespace removed
                    send_message(
                        'Please message me directly to play', output['channel'])

                if output and 'text' in output and output['channel'].startswith('D'):
                    return output['text'].strip().lower(), \
                        output['channel'], output['user']
    return None, None, None


def send_message(message, channel):
    slack_client.api_call(
        "chat.postMessage", channel=channel,
        text=message, as_user=True)


if __name__ == "__main__":
    READ_WEBSOCKET_DELAY = 0.1  # 1 second delay between reading from firehose
    print "Connecting..."
    if slack_client.rtm_connect():
        print "StarterBot connected and running!"
        while True:
            command, channel, user = parse_slack_output(
                slack_client.rtm_read())
            if command and channel:
                handle_command(command, channel, user)
            time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print "Connection failed. Invalid Slack token or bot ID?"
