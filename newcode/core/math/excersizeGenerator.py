import random

def _removeDecimal_0_fromNumber(number: float):
    if (roundNumber := int(number)) == number:
        return roundNumber
    return number

def _generateDecimalNumber(maxNumber: int, floatingPointAmount: int = 0):
    return _removeDecimal_0_fromNumber(round(random.random() * maxNumber, floatingPointAmount))

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

def _checkSolutionFloatingPointAmount(number1: float, number2: float, operand: str, floatingPointAmout: int = 0):
    if floatingPointAmout == 0:
        return True
    solution = calculate(number1, number2, operand)
    return round(solution, floatingPointAmout) == solution
        
        


def addition(maxNumber: int, maxSolution: int, floatingPointAmount: int = 0):
    while True:
        number1 = _generateDecimalNumber(maxNumber, floatingPointAmount)
        number2 = _generateDecimalNumber(maxNumber, floatingPointAmount)
        if number1 + number2 <= maxSolution and number1 + number2 >= 0 and _checkSolutionFloatingPointAmount(number1, number2, "+", floatingPointAmount):
            return number1, number2
        
def subtraction(maxNumber: int, maxSolution: int, floatingPointAmount: int = 0):
    while True:
        number1 = _generateDecimalNumber(maxNumber, floatingPointAmount)
        number2 = _generateDecimalNumber(maxNumber, floatingPointAmount)
        if number1 - number2 <= maxSolution and number1 - number2 >= 0 and _checkSolutionFloatingPointAmount(number1, number2, "-", floatingPointAmount):
            return number1, number2

def multiplication(maxNumber: int, maxSolution: int, floatingPointAmount: int = 0, secondNumberDecimal = False):
    while True:
        secondNumberFloatingPointAmout = floatingPointAmount if secondNumberDecimal else 0
        number1 = _generateDecimalNumber(maxNumber / (maxSolution / 100), floatingPointAmount)
        number2 = _generateDecimalNumber(maxNumber / (maxSolution / 100), secondNumberFloatingPointAmout)
        if number1 * number2 <= maxSolution and number1 * number2 >= 0 and _checkSolutionFloatingPointAmount(number1, number2, "*", floatingPointAmount):
            return number1, number2
        
def division(maxNumber: int, maxSolution: int, floatingPointAmount: int = 0, secondNumberDecimal = False):
    while True:
        secondNumberFloatingPointAmout = floatingPointAmount if secondNumberDecimal else 0
        number1 = _generateDecimalNumber(maxNumber / (maxSolution / 100), floatingPointAmount)
        number2 = _generateDecimalNumber(maxNumber / (maxSolution / 100), secondNumberFloatingPointAmout)
        try:
            if number1 / number2 <= maxSolution and number1 / number2 >= 0 and _checkSolutionFloatingPointAmount(number1, number2, "/", floatingPointAmount):
                return number1, number2
        except ZeroDivisionError: ... # rule out a crash from a division by zero
        
def multiplicationTables(*void): #? outrule crash when arguments are givin
    return multiplication(10, 100)

def percentage(maxNumber: int, void: None, floatingPointAmount: int = 0):
    while True:
        _percentage = random.randint(1, 100)
        number = _generateDecimalNumber(int(maxNumber / 100), floatingPointAmount)
        if _percentage / 100 * number == round(_percentage / 100 * number, floatingPointAmount):  # TODO
            return _percentage, number
        
        
# print(multiplication(100000, 100000, 2))
# print(percentage(600, 1))
# print(multiplicationTables())