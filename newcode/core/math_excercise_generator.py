import random

def calculate(number1, number2, operand):
    if operand == "+":
        return number1 + number2
    elif operand == "-":
        return number1 - number2
    elif operand in ("*", "maaltafel"):
        return number1 * number2
    elif operand == "/":
        return number1 / number2
    elif "%" in operand:
        return number1 / 100 * number2
    
def _removeDecimal_0_fromNumber(number: float):
    if (roundNumber := int(number)) == number:
        return roundNumber
    return number

def _generateDecimalNumber(maxNumber: int, floatingPointAmount: int = 0):
    return _removeDecimal_0_fromNumber(round(random.random() * (maxNumber - 1) + 1, floatingPointAmount))


def addition(maxNumber: int, maxSolution: int, floatingPointAmount: int = 0):
    while True:
        number1 = _generateDecimalNumber(maxNumber, floatingPointAmount)
        number2 = _generateDecimalNumber(maxNumber, floatingPointAmount)
        if number1 + number2 <= maxSolution and number1 + number2 >= 0:
            return number1, number2
        
def subtraction(maxNumber: int, maxSolution: int, floatingPointAmount: int = 0):
    while True:
        number1 = _generateDecimalNumber(maxNumber, floatingPointAmount)
        number2 = _generateDecimalNumber(maxNumber, floatingPointAmount)
        if number1 - number2 <= maxSolution and number1 - number2 >= 0:
            return number1, number2

def multiplication(maxNumber: int, maxSolution: int, floatingPointAmount: int = 0, secondNumberDecimal = False):
    while True:
        secondNumberFloatingPointAmout = floatingPointAmount if secondNumberDecimal else 0
        number1 = _generateDecimalNumber(maxNumber, floatingPointAmount)
        number2 = _generateDecimalNumber(maxNumber, secondNumberFloatingPointAmout)
        if number1 * number2 <= maxSolution and number1 * number2 >= 0:
            return number1, number2
        
def division(maxNumber: int, maxSolution: int, floatingPointAmount: int = 0, secondNumberDecimal = False):
    while True:
        secondNumberFloatingPointAmout = floatingPointAmount if secondNumberDecimal else 0
        number1 = _generateDecimalNumber(maxNumber, floatingPointAmount)
        number2 = _generateDecimalNumber(maxNumber, secondNumberFloatingPointAmout)
        try:
            if number1 / number2 <= maxSolution and number1 / number2 >= 0:
                return number1, number2
        except ZeroDivisionError: ... # rule out a crash from a division by zero

def percentage(maxNumber: int, floatingPointAmount: int = 0):
    while True:
        _percentage = random.randint(1, 100)
        number = _generateDecimalNumber(maxNumber, floatingPointAmount)
        return _percentage, number
