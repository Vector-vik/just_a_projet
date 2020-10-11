"""Настройка логгера."""
import logging
import os
import sys

logger = logging.getLogger(os.environ.get('APP_NAME', 'Unknown app'))
logger.setLevel(int(os.environ.get('LOGGER_LEVEL', 0)))

out_handler = logging.StreamHandler(stream=sys.stdout)
err_handler = logging.StreamHandler(stream=sys.stderr)

out_handler.setLevel(logging.DEBUG)
err_handler.setLevel(logging.WARNING)

formatter = logging.Formatter(
    fmt='{asctime} [{levelname}] {name}:{funcName} >>> {message}',
    style='{',
)

out_handler.setFormatter(formatter)
err_handler.setFormatter(formatter)

logger.addHandler(out_handler)
logger.addHandler(err_handler)

logger.propagate = True
