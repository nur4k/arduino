import sys
from loguru import logger

# Configure the logger to include the filename in the log output
logger.add(sys.stdout, format="{time} | {level: <8} | {name}:{function}:{line} - {message}")

# Log a debug message
logger.debug("That's it, beautiful and simple logging!")


service_logger = logger