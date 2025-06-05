import logging
import os
import datetime

class Logger:
    # Directory where log files will be stored
    logs_dir = r"C:\Users\PC\PycharmProjects\pythonProject\Provineer_regression_tests\logs"
    if not os.path.exists(logs_dir):
        os.makedirs(logs_dir)

    # Log file name with timestamp
    file_name = os.path.join(logs_dir, f"log_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log")

    # Initialize logger
    logger = logging.getLogger('ProvineerLogger')
    logger.setLevel(logging.INFO)

    # File handler for logging to a file
    file_handler = logging.FileHandler(file_name, encoding='utf-8')
    file_handler.setLevel(logging.INFO)

    # Console handler for logging to console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # Formatter for logs
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Avoid duplicate handlers
    if not logger.handlers:
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    @classmethod
    def write_log_to_file(cls, data: str):
        """Logs the given data using INFO level"""
        cls.logger.info(data)

    @classmethod
    def info(cls, message: str):
        """Logs an INFO level message"""
        cls.logger.info(message)

    @classmethod
    def error(cls, message: str):
        """Logs an ERROR level message"""
        cls.logger.error(message)

    @classmethod
    def debug(cls, message: str):
        """Logs a DEBUG level message"""
        cls.logger.debug(message)

    @classmethod
    def add_start_step(cls, method: str):
        """Logs the start of a test step"""
        test_name = os.environ.get('PYTEST_CURRENT_TEST', 'Unknown Test')

        data_to_add = f"\n-----\n"
        data_to_add += f"Test: {test_name}\n"
        data_to_add += f"Start time: {str(datetime.datetime.now())}\n"
        data_to_add += f"Start method: {method}\n"
        data_to_add += "\n"

        cls.info(data_to_add)

    @classmethod
    def add_end_step(cls, url: str, method: str):
        """Logs the end of a test step"""
        data_to_add = f"End time: {str(datetime.datetime.now())}\n"
        data_to_add += f"End method: {method}\n"
        data_to_add += f"URL: {url}\n"
        data_to_add += f"\n-----\n"

        cls.info(data_to_add)
