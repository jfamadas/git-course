import numpy as np

class Calculator:
    """ A simple calculator App"""

    def add(x, y):
        """Add Function"""
        return x + y

    def subtract(x, y):
        """Subtract Function"""
        return x - y

    def multiply(x, y):
        """Multiply Function"""
        return x * y

    def divide(x, y):
        """Divide Function"""
        if y == 0:
            raise ValueError('Can not divide by zero!')

        return x / y

    def sqrt(x):
        """squareRoot"""
        if x < 0:
            raise ValueError('Can not calculate sqrt of a negative number.')

        return np.sqrt(x)

# if __name__ == "__main__":
#     print(Calculator.sqrt(-4))

