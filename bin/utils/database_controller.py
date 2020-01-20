import os
import sqlite3


def health_check(logger, script_dir, db_path):
    logger.info("Health Check for Database")
    prefix_dir = os.path.abspath(os.path.join(script_dir))
    db_path = os.path.abspath(os.path.join(prefix_dir, db_path))

    logger.debug("Database location {}".format(db_path))
    if not os.path.isfile(db_path):
        logger.info("Database not found under path {}".format(db_path))
        f = open(db_path, "w+")
        f.close()
        logger.info("Created new Database")
        create_table(logger, db_path)
    else:
        logger.info("Database exists!~")


def create_table(logger, db_path):
    conn = sqlite3.connect(db_path)
    logger.info("Creating Tables")
    try:
        conn.execute('''CREATE TABLE TIMERS
                 (TIMER_ID TEXT PRIMARY KEY     NOT NULL,
                 SHORT_DESC            TEXT     NOT NULL,
                 MESSAGE            TEXT     NOT NULL,
                 TIMER            INT     NOT NULL,
                 IS_DISABLED           INT    NOT NULL);''')
        logger.info("Created Tables Successfully")
    except Exception as e:
        logger.error("Couldn't create table! {}".format(str(e)))
    conn.close()