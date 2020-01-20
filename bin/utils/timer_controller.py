import sqlite3
from bin.timers.master_timer import sub_timer
import threading


def start_timers(connect, channel, logger, db_path):
    logger.info("Reading database!")
    conn = sqlite3.connect(db_path)
    command = "SELECT TIMER_ID, SHORT_DESC, MESSAGE, TIMER,IS_DISABLED FROM TIMERS"
    cursor = conn.execute(command)
    desc = cursor.description
    for row in cursor:
        timer_id = row[0]
        short_desc = row[1]
        message = row[2]
        timer = row[3]
        is_disabled = row[4]
        thread = threading.Thread(
            target=sub_timer,
            args=(connect,
                  channel,
                  logger,
                  timer_id,
                  short_desc,
                  message,
                  timer,
                  is_disabled))
        thread.start()