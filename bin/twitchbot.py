import sys
import irc.bot
import requests
import threading
from bin.utils.timer_controller import start_timers


class TwitchBot(irc.bot.SingleServerIRCBot):
    def __init__(self, username, client_id, token, channel, server, port, logger, db_path):
        self.client_id = client_id
        self.token = token
        self.channel = '#' + channel
        self.logger = logger
        self.db_path = db_path

        # Get the channel id, we will need this for v5 API calls
        url = 'https://api.twitch.tv/kraken/users?login={}'.format(channel)
        headers = {'Client-ID': client_id, 'Accept': 'application/vnd.twitchtv.v5+json'}
        r = requests.get(url, headers=headers).json()
        self.channel_id = r['users'][0]['_id']

        print("Starting Connection")
        # Create IRC bot connection
        logger.info('Connecting to {} on port {}...'.format(server, int(port)))
        irc.bot.SingleServerIRCBot.__init__(self, [(server, int(port), 'oauth:' + token)], username, username)
        logger.info('Connected to {} on port {}...'.format(server, int(port)))

    def on_welcome(self, c, e):
        self.logger.info('Joining {}'.format(self.channel))

        # You must request specific capabilities before you can use them
        c.cap('REQ', ':twitch.tv/membership')
        c.cap('REQ', ':twitch.tv/tags')
        c.cap('REQ', ':twitch.tv/commands')
        c.join(self.channel)
        start_timers(self.connection, self.channel, self.logger, self.db_path)

    def on_pubmsg(self, c, e):
        self.logger.info('Listening {}'.format(self.channel))

        # If a chat message starts with an exclamation point, try to run it as a command
        if e.arguments[0][:1] == '!':
            cmd = e.arguments[0].split(' ')[0][1:]
            self.logger.info('Received command: {}'.format(cmd))
            self.do_command(e, cmd)
        return

    def do_command(self, e, cmd):
        c = self.connection

        url = 'https://api.twitch.tv/kraken/channels/' + self.channel_id
        headers = {'Client-ID': self.client_id, 'Accept': 'application/vnd.twitchtv.v5+json'}
        r = requests.get(url, headers=headers).json()

        list = {}
        list['game'] = '{} is currently playing {}'.format(r['display_name'], r['game'])
        list['title'] = '{} channel title is currently {}'.format(r['display_name'], r['status'])
        list['raffle'] = 'Thanks for interest in our raffle!'
        list['love_me'] = 'I love you with all my heart!'

        if cmd in list:
            c.privmsg(self.channel, list[cmd])
        else:
            c.privmsg(self.channel, "Did not understand command: {}".format(cmd))