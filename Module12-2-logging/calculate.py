import logging

logger = logging.getLogger(__name__)


def add(x, y):
    logger.info(f"adding {x} and {y}")
    return x + y


def divide(x, y):
    try:
        logger.info(f"dividing {x} by {y}")
        return x / y
    except ZeroDivisionError:
        logger.exception("hello")
