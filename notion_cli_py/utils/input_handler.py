import sys
from ..utils import logger
from getpass import getpass


def input_handler(message):
    lg = logger.init_logger(__name__)
    try:
        m = input(message)
        return m
    except KeyboardInterrupt:
        lg.error("\n==> Aborted.")
        sys.exit(1)

def getpass_handler(message):
    lg = logger.init_logger(__name__)
    try:
        m = getpass(message)
        return m
    except KeyboardInterrupt:
        lg.error("\n==> Aborted.")
        sys.exit(1)
