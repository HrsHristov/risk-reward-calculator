# utils.py
import logging

def setup_logger(name=__name__, level=logging.INFO):
    """
    Sets up and returns a logger with a console handler.
    """
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler()
        handler.setLevel(level)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    logger.setLevel(level)
    return logger

if __name__ == "__main__":
    logger = setup_logger("utils")
    logger.info("Logger is configured.")
