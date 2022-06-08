import logging
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
filename = os.path.join(dir_path, "test_log.log")

# could do just, but don't
# filename = "test_log.log"

# logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# file handler
file_handler = logging.FileHandler(filename)
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

logger.addHandler(file_handler)

def main():
    logging.info("test")

if __name__ == "__main__":
    main()