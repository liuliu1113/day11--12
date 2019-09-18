import logging

fm = "%(asctime)s %(levelname)s [%(name)s] [%(filename)s (%(funcName)s:%(lineno)d] - %(message)s"
logging.basicConfig(level=logging.INFO, filename="./log/file1.log", format=fm)


def get_log():
    return logging
