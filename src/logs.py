import logging
import os
from datetime import datetime

# Set up logging
LOG_FILE = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log"
path = os.path.join(os.getcwd(), "logs", LOG_FILE)
os.makedirs(os.path.dirname(path), exist_ok=True)
log_file_path = os.path.join(os.getcwd(), "logs", LOG_FILE)
logging.basicConfig(filename=log_file_path,format = '[%(asctime)s] - Line:%(lineno)d -Name:%(filename)s - [%(levelname)s] - %(message)s', level=logging.INFO)

if __name__ == "__main__":
    logging.info("Logging setup complete. Log file created at: %s", log_file_path)