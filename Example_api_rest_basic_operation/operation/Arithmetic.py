from operation.ArithmeticError import Error


class Operation:
    """Class where are defined all operations"""

    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2
        self.isValid()

    def isValid(self):
        for a, b in zip(self.v1, self.v2):
            if (type(a) != int and type(a) != float) or (type(b) != int and type(b) != float):
                raise Error("Invalid data type", 500)
        if len(self.v1) != len(self.v2):
            raise Error("Lists of values should have same length", 500)

    def sum(self):
        return [a + b for a, b in zip(self.v1, self.v2)]

    def subtract(self):
        return [a - b for a, b in zip(self.v1, self.v2)]

    def multiply(self):
        return [a * b for a, b in zip(self.v1, self.v2)]

    def divide(self):
        if 0 in self.v2:
            raise Error("Invalid division by zero", 500)
        return [a / b for a, b in zip(self.v1, self.v2)]
