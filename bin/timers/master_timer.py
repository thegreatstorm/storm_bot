import time


def sub_timer(connect, channel, logger, timer_id, short_desc, message, timer, is_disabled):
    if is_disabled == 0:
        logger.info("Starting {0}:{1} - Timer Time: Every {2}min".format(timer_id, short_desc, str(timer)))
        while True:
            time.sleep(60 * timer)
            logger.info("I'm telling people about {}!".format(timer_id))
            connect.privmsg(channel, message)
    else:
        logger.info("{0}:{1} Timer Disabled".format(timer_id, short_desc))





