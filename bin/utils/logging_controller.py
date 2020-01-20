import logging
import os


def logging_controller(script_dir, log_path, app_name):
    # Get absolute log path
    prefix_dir = os.path.abspath(os.path.join(script_dir))

    logger = logging.getLogger(app_name)
    logger.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s %(levelname)s pid %(process)d - %(module)s : %(message)s")
    log_handler = logging.FileHandler(log_path)
    log_handler.setFormatter(formatter)
    logger.addHandler(log_handler)

    return logger
