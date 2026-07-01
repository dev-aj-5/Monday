import logging
from pathlib import Path
from datetime import datetime

# ==========================================
# Log Directory
# ==========================================

LOG_FOLDER = Path("logs")
LOG_FOLDER.mkdir(exist_ok=True)

LOG_FILE = LOG_FOLDER / f"{datetime.now().strftime('%Y-%m-%d')}.log"

# ==========================================
# Logger
# ==========================================

logger = logging.getLogger("Monday")

logger.setLevel(logging.INFO)

# Prevent duplicate handlers on restart
logger.handlers.clear()

# ==========================================
# Formatter
# ==========================================

formatter = logging.Formatter(
    "[%(levelname)s] %(asctime)s | %(message)s",
    datefmt="%H:%M:%S"
)

# ==========================================
# Console Handler
# ==========================================

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)

# ==========================================
# File Handler
# ==========================================

file_handler = logging.FileHandler(
    LOG_FILE,
    encoding="utf-8"
)

file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)

# ==========================================
# Register Handlers
# ==========================================

logger.addHandler(console_handler)
logger.addHandler(file_handler)

# ==========================================
# Wrapper Functions
# ==========================================

def info(message: str):
    logger.info(message)


def warning(message: str):
    logger.warning(message)


def error(message: str):
    logger.error(message)


def critical(message: str):
    logger.critical(message)


def debug(message: str):
    logger.debug(message)