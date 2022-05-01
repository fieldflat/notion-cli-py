from logging import getLogger, StreamHandler, INFO, DEBUG


def init_logger(name):
    logger = getLogger(name)
    logger.setLevel(INFO)
    if not logger.hasHandlers():
        handler = StreamHandler()
        handler.setLevel(DEBUG)
        logger.addHandler(handler)
        logger.propagate = False

    return logger
