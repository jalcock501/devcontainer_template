"""Module contains the logger configuration for the application."""

import logging
import sys

from pythonjsonlogger import jsonlogger

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# Create Handlers for logging stdout and err
stdout_handler = logging.StreamHandler(stream=sys.stdout)
err_handler = logging.FileHandler("error.log")

# Set the log level for each handler
stdout_handler.setLevel(logging.DEBUG)
err_handler.setLevel(logging.ERROR)

fmt = jsonlogger.JsonFormatter(
    "%(name)s %(asctime)s %(levelname)s %(filename)s %(lineno)s %(process)d %(message)s",
    rename_fields={"levelname": "severity", "asctime": "timestamp"},
)

stdout_handler.setFormatter(fmt)
err_handler.setFormatter(fmt)

logger.addHandler(stdout_handler)
logger.addHandler(err_handler)
