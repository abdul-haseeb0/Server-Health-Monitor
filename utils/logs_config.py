import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

LOG_DIR = Path('logs')
LOG_DIR.mkdir(exist_ok=True)

handler = RotatingFileHandler(
    LOG_DIR / 'shmlogs.log',
    maxBytes=4 * 1024 * 1024,
    backupCount=5
)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[handler],
    level=logging.INFO,
)

def get_logger():
    return logging.getLogger(__name__)