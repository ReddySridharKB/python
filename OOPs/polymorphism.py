class Calculator:
    def calculate(self, a, b):
        print(a + b)


class Multiply:
    def calculate(self, a, b):
        print(a * b)


class Subtract:
    def calculate(self, a, b):
        print(a - b)


add = Calculator()
multiply = Multiply()
subtract = Subtract()

add.calculate(10, 5)
multiply.calculate(10, 5)
subtract.calculate(10, 5)