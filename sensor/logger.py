import logging
import os
from datetime import datetime

log_file_name = f"{datetime.now().strftime('%d%m%Y-%H%M%S')}.log"

#Create Folder Directory Path
log_file_dir = os.path.join(os.getcwd(),"logs") #os.getcwd() gets the current directory whereas 
#os.path.join() adds the remaining texts/directory #For Ex:- /config/workspace/sensor/logs is the text in log_file_dir

#Create Folder
os.makedirs(log_file_dir,exist_ok=True)

#Join directories
log_file_path = os.path.join(log_file_dir,log_file_name)

#Code for Logging
logging.basicConfig(
    filename = log_file_path,
    format='[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s',
    #Includes time, line number, logger name, severity level, and log message in the output.
    level = logging.INFO)
