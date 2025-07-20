import logging
import os

def configure_logger():
    log_dir = 'logs'
    os.makedirs(log_dir, exist_ok=True)

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    file_handler = logging.FileHandler(os.path.join(log_dir, 'app.log'))
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.INFO)

    if not logger.handlers:
        logger.addHandler(file_handler)
