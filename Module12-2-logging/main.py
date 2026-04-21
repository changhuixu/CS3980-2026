import logging

from calculate import add, divide

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)

logger.info("this is an info message")
logger.debug("this is a debug message")
logger.warning("this is a warning message")
logger.error("this is an error message")

result = add(6, 7)
logger.info(f"the result is {result}")

divide(1, 0)
