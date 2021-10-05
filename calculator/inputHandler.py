import logging
import sys


class InputHandler:
    def __init__(self):
        """InputHandler() -> InputHandler
        returns an instance of InputHandler class"""
        self.logger = logging.getLogger(__name__)
        self.data = []
        self.amount = 0.0
        self.interest = 0.0
        self.down_payment = 0.0
        self.term = 0.0
        self.valid_keys = ['amount', 'interest', 'downpayment', 'term']

    def __str__(self):
        """Converts current instance class into a string"""
        return '{{ amount:{}, interest:{}, down_payment:{}, term:{} }}'.format(
            self.amount, self.interest, self.down_payment, int(self.term))

    def read_data(self):
        """read_data() -> None
        Reads input strings until an empty string is found and store it in InputHandler class."""
        print('Input data now:')
        for line in sys.stdin:
            self.logger.debug(f'stdin:{line}')
            if '' == line.strip():
                self.logger.info('Empty line found')
                break
            else:
                self.data.append(line.strip().lower())
        self.logger.debug(f'data:{self.data}')


    def parse_data(self):
        """parse_data() -> None
        iterates each element stored in self.data and parses line per line.
        once data is parsed validates any missing required field."""
        for line in self.data:
            if ':' not in line:
                self.logger.error(f'Invalid input data: {line}, expecting format key:value')
                break
            self.parse_line(line)
        self.validate_missing_data()
        self.logger.debug(f'Input data:{self.data}')

    def parse_line(self, line):
        """
        :param line: parses a line into either self.amount, self.interest, self.down_payment or self.term
        """
        # We can be confident line contains ':'
        # We validate keys are the keys we expect and values are valid values.
        (key, value) = [item.strip() for item in line.split(':')]
        if '%' in value:
            self.validate_interest(key, value)
        else:
            self.validate_key(key)
            self.validate_value(value)
            value = float(value)

            if key == 'amount':
                self.logger.debug(f'{key}:{value} key pair found')
                self.amount = value
            elif key == 'interest':
                self.logger.debug(f'{key}:{value} key pair found')
                self.interest = value / 100
            elif key == 'downpayment':
                self.logger.debug(f'{key}:{value} key pair found')
                self.down_payment = value
            elif key == 'term':
                self.logger.debug(f'{key}:{value} key pair found')
                self.term = value
            else:
                self.logger.error(f'{key}:{value} Invalid key pair found')

    def validate_key(self, key):
        """validate_key(string)->None
        Validates each key added in data is an expected key."""
        if key not in self.valid_keys:
            self.logger.error(f'Invalid key: {key}, expected: {str.join("/", self.valid_keys)}')
            sys.exit()

    def validate_interest(self, key, value):
        """validate_interest(string, string)-> None
        validates the input that includes a % is in valid format."""
        if '%' not in value[:-1] and key == 'interest':
            self.interest = float(value.strip('%')) / 100
        else:
            self.logger.error('Invalid interest input, valid formats: interest:float / interest:float%')
            sys.exit()

    def validate_value(self, value):
        """validate_value() -> None
        Validates the input values are valid. Every value should be able to be converted to a float"""
        try:
            float(value)
        except ValueError:
            self.logger.error(f'Invalid value: {value}')
            sys.exit()

    def validate_missing_data(self):
        """validate_missing_data() -> None
        Validates if any field is missing."""
        missing_data = False
        if not self.amount:
            self.logger.error(f'Missing key pair amount:value')
            missing_data = True
        if not self.interest:
            self.logger.error(f'Missing key pair interest:value')
            missing_data = True
        if not self.term:
            self.logger.error(f'Missing key pair term:value')
            missing_data = True
        if missing_data:
            sys.exit()
