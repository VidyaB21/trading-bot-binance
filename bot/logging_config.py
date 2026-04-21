from loguru import logger

def setup_logger():
    logger.add("bot.log", rotation="1 MB", level="INFO")
    return logger