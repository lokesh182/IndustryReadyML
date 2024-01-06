import logging  #logger is for the purpose of logging all the information about the execution
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" #LOG_FILE is used to store the log file name
log_path = os.path.join(os.getcwd(),"logs",LOG_FILE) #log_path is used to store the path of the log file
os.makedirs(log_path,exist_ok=True) #os.makedirs() is used to create a directory

LOG_FILE_PATH = os.path.join(log_path,LOG_FILE)

logging.basicConfig(
    filename = LOG_FILE_PATH,
    format = "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level = logging.INFO,
)
logger = logging.getLogger(__name__)
