from calculator.inputHandler import InputHandler
from calculator.calculator import Calculator
import json
import logging
import os
import string
import time


def start_logger(file_path: string = '/tmp/payment_calculator.log', log_level: string = 'DEBUG'):
    logging_levels = {
        'CRITICAL': logging.CRITICAL,
        'ERROR': logging.ERROR,
        'WARNING': logging.WARNING,
        'INFO': logging.INFO,
        'DEBUG': logging.DEBUG,
        'NOTSET': logging.NOTSET
    }

    # If environment is production no need to log all debug statements.
    if os.getenv('environment') == 'prod':
        log_level = 'INFO'

    # Set level for logs at file
    log_level = logging_levels[log_level]

    current_time = time.strftime("%Y%m%d-%H%M%S")
    current_time = ''
    file_path = f'{file_path.split(".")[0]}-{current_time}.{file_path.split(".")[1]}'

    logger = logging.getLogger()
    logger.setLevel(log_level)
    # create file handler which logs even debug messages
    fh = logging.FileHandler(file_path)
    fh.setLevel(log_level)
    # create console handler with a higher log level
    ch = logging.StreamHandler()
    ch.setLevel(logging.ERROR)
    # create formatter and add it to the handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    # add the handlers to the logger
    logger.addHandler(fh)
    logger.addHandler(ch)

    logger.info('Logger Setup Ready')


# If file is run as main module
if __name__ == '__main__':
    start_logger()
    inputHandler = InputHandler()
    inputHandler.read_data()
    inputHandler.parse_data()
    calculator = Calculator(amount=inputHandler.amount, interest=inputHandler.interest,
                            down_payment=inputHandler.down_payment, term=inputHandler.term)
    result = calculator.calculate()
    json_object = json.dumps(result, sort_keys=True, indent=4)
    print(json_object)
    with open("output.json", "w") as outfile:
        json.dump(result, outfile)
        logging.debug('File output.json created')





