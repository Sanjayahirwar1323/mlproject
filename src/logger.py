import logging ##A log is a record of events, messages, or errors generated by a program during execution. Logs help developers and system administrators track what happens inside a system, debug issues, and monitor application behavior.
import os
from datetime import datetime 

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" ## log file name 
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE) ## .getcwd mean current directory and it use to create path of log file || logs_dir: /Users/sanjayahirwar/Documents/logs
os.makedirs(logs_path,exist_ok=True) ## create log path as directory as above code is treating file as directoty and also duplicate folder true ||this will create the "logs" folder if it doesn't exist


LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE) ##join||LOG_FILE_PATH: /Users/sanjayahirwar/Documents/logs/03_10_2025_14_30_45.log

logging.basicConfig(
    filename=LOG_FILE_PATH,  ## 
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    
)
##if __name__=="__main__": ## TO CHECK EVERY THING IS WORKING FINE OR NOT
    ##logging.info("Logging has started") ## out put logs folder created 