import logging
import os
from datetime import datetime

LOG_PATH = os.path.join(os.getcwd(), "logs")
LOG_FILE = f"""{datetime.now().strftime("%m_%d_%Y_%H_%M_%S")}.log"""

os.makedirs(LOG_PATH, exist_ok=True)

ABS_LOG_FILE_PATH = os.path.join(LOG_PATH, LOG_FILE)

logging.basicConfig(level=logging.DEBUG,
                    filename=ABS_LOG_FILE_PATH,
                    filemode="w",
                    format="%(asctime)s %(lineno)d %(name)s - %(levelname)s - %(message)s"
                    )
