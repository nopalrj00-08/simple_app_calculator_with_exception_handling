class Calculator:
    """--OOP MATH OPERATIONS--"""
    def Addition(self, number_1, number_2):
        return number_1 + number_2
    def Subtraction(self, number_1, number_2):
        return number_1 - number_2
    def Multiplication(self, number_1, number_2):
        return number_1 * number_2
    def Division(self, number_1, number_2):
        try:
            return number_1 / number_2
        except ZeroDivisionError:
            if number_2 == 0:
                return "You can't divide by zero"