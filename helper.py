import logging
logger = logging.getLogger(__name__)
logger.propagate = False
logger.info("Logging from helper module")


def do_something():
    logger.info("Helper function executed.")
