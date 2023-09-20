import os
import logging

formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(message)s')


# ---multi logger function to create multiple logs-------
def setup_logger(name, log_file="", level=logging.INFO):
    path = __file__
    a = os.path.realpath(__file__)
    directory = os.path.dirname(os.path.dirname(a)) + "\\logs\\" + name + ".log"
    """To setup as many loggers as you want"""
    handler = logging.FileHandler(directory)
    handler.setFormatter(formatter)
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)
    return logger