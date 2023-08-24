import logging

# Define a log format to be used in logging messages. This format includes:
# - The current timestamp (asctime)
# - The severity level of the message (e.g., INFO, ERROR) (levelname)
# - The actual log message (message)
log_format = '%(asctime)s [%(levelname)s] %(message)s'

# Configure the basic settings for logging.
# This sets up the log format as defined above and sets the logging level to "INFO",
# meaning messages with level INFO and above (like WARNING, ERROR, etc.) will be logged.
logging.basicConfig(format=log_format, level=logging.INFO)

# Get a logger instance for the current module.
# This allows us to create log messages specific to this part of the application.
logger = logging.getLogger(__name__)
