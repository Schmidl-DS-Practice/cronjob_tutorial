import logging
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
## could do just, but don't
# filename = "test_log.log"
filename = os.path.join(dir_path, "test_log.log")
print(dir_path)
print(filename)

## Logger
# formatter = "%(asctime)s - %(levelname)s - %(message)s"
# logging.basicConfig(filename=filename, format=formatter, encoding='utf-8', level=logging.INFO)

# the below is not working. read: https://docs.python.org/3/howto/logging.html to understand the below better
# Logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# File Handler
file_handler = logging.FileHandler(filename)
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
logger.addHandler(file_handler)

def do_logging():
    logger.info("test")

if __name__ == "__main__":
    do_logging()