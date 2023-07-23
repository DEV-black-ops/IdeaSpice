import logging 
import sys
import os
from datetime import datetime

#seting log file name 
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(),'logs',LOG_FILE)

#making log_path folder 
os.makedirs(logs_path,exist_ok=True)

#creating log file at logs_path folder
LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

if __name__ == '__main__':
    logging.info("logging has started")
