import logging


class Calculator:
    def __init__(self, amount: float = 0.0, interest: float = 0.0, down_payment: float = 0.0, term: float = 0.0):
        """Calculator(a, b, c, d) -> Calculator
        returns an instance of Calculator class"""
        self.logger = logging.getLogger(__name__)
        self.amount = amount
        self.interest = interest
        self.down_payment = down_payment
        self.term = term
        self.monthly_payment = 0.0
        self.total_interest = 0.0
        self.total_payment = 0.0

    def calculate(self):
        """ calculate() -> dict
        Return the dictionary containing self.monthly_payment, self.total_payment, self.total_interest
            if interest is equals to 0 it will raise a division by zero exception.
            return {
                'monthly payment': float,
                'total payment': float,
                'total interest': float
            }"""
        # P = Initial principal or loan amount
        p = int(self.amount - self.down_payment)
        # r = Interest rate per period
        r = self.interest / 12
        # n = Total number of payments or periods
        n = int(self.term * 12)

        self.monthly_payment = round(p * ((r * ((r + 1) ** n)) / (((r + 1) ** n) - 1)), 2)
        self.total_payment = round(self.monthly_payment * n, 2)
        self.total_interest = round(self.total_payment - p, 2)
        return {
            "monthly payment": self.monthly_payment,
            "total payment": self.total_payment,
            "total interest": self.total_interest
        }




