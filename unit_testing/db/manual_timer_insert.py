import sqlite3


def insert_timer(db_path, timer_id, short_desc, msg, timer, is_diabled):
    conn = sqlite3.connect(db_path)
    command = "INSERT INTO TIMERS (TIMER_ID, SHORT_DESC, MESSAGE, TIMER, IS_DISABLED) \
            VALUES('{}', '{}','{}', {}, {})".format(timer_id, short_desc, msg, timer, is_diabled)
    conn.execute(command)
    conn.commit()
    conn.close()


db_path = input("Database filepath: ")
timer_id = input("Input timer id: ")
short_desc = input("Short Description: ")
msg = input("Timer Message: ")
timer = int(input("Time by Minutes: "))

insert_timer(db_path, timer_id, short_desc, msg, timer, 0)