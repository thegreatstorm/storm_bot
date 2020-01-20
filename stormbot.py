import os

from bin.utils.configuration_controller import config_controller
from bin.utils.logging_controller import logging_controller
from bin.twitchbot import TwitchBot
from bin.utils.database_controller import health_check

# ================ Configuration Piece ===================
script_dir = os.path.dirname(os.path.abspath(__file__))
config_settings = config_controller(script_dir, 'confs/default.conf', 'confs/local.conf')
# ================ Configuration Piece ===================

app_usage = config_settings.get('general', 'app_usage')


def main():
    # if Twitch
    if 'twitch' == app_usage:
        client_id = config_settings.get('twitch', 'client_id')
        oauth_token = config_settings.get('twitch', 'oauth_token')
        channel = config_settings.get('twitch', 'channel')
        host = config_settings.get('twitch', 'host')
        port = config_settings.get('twitch', 'port')
        bot = TwitchBot(channel, client_id, oauth_token, channel, host, port, logger, db_path)
        bot.start()


if __name__ == "__main__":
    # ================ Retrieve Logging info =================
    log_path = config_settings.get('general', 'log_path')
    app_name = config_settings.get('general', 'app_name')
    logger = logging_controller(script_dir, log_path, app_name)
    # ================ Retrieve Logging info =================

    # ================ Database info =================
    db_path = config_settings.get('database', 'db_path')
    health_check(logger, script_dir, db_path)
    # ================ Database info =================
    main()
