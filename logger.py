import logging

logging.basicConfig(
    filename='chartova.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(funcName)s: - %(message)s',
    datefmt='%H:%M:%S',
)
