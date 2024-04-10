import random, core.math_excercise_generator as ex


def _removeDecimal_0_fromNumber(number: float):
    if (roundNumber := int(number)) == number:
        return roundNumber
    return number

def _generateDecimalNumber(maxNumber: int, floatingPointAmount: int = 0):
    return _removeDecimal_0_fromNumber(round(random.random() * (maxNumber - 1) + 1, floatingPointAmount))

def _checkIfSolutionHasSameFloatingPointAmount(number1: float, number2: float, operand: str, floatingPointAmout: int = 0):
    solution = calculate(number1, number2, operand)
    return round(solution, floatingPointAmout) == solution
        
def calculate(number1, number2, operand):
    return ex.calculate(number1, number2, operand) # overwrite base function


"""
implementations of the 'math_excercise_generator' functions
"""
def addition(maxNumber: int, maxSolution: int, floatingPointAmount: int = 0):
    while True:
        number1, number2 = ex.addition(maxNumber, maxSolution, floatingPointAmount)
        if _checkIfSolutionHasSameFloatingPointAmount(number1, number2, "+", floatingPointAmount):
            return number1, number2
        
def subtraction(maxNumber: int, maxSolution: int, floatingPointAmount: int = 0):
    while True:
        number1, number2 = ex.subtraction(maxNumber, maxSolution, floatingPointAmount)
        if _checkIfSolutionHasSameFloatingPointAmount(number1, number2, "-", floatingPointAmount):
            return number1, number2

def multiplication(maxNumber: int, maxSolution: int, floatingPointAmount: int = 0, secondNumberDecimal = False):
    while True:
        number1, number2 = ex.multiplication(maxNumber / (maxSolution / 100), maxSolution, floatingPointAmount, secondNumberDecimal)
        if _checkIfSolutionHasSameFloatingPointAmount(number1, number2, "*", floatingPointAmount):
            return number1, number2
        
def division(maxNumber: int, maxSolution: int, floatingPointAmount: int = 0, secondNumberDecimal = False):
    while True:
        number1, number2 = ex.division(maxNumber / (maxSolution / 100), maxSolution, floatingPointAmount, secondNumberDecimal)
        if _checkIfSolutionHasSameFloatingPointAmount(number1, number2, "/", floatingPointAmount) and number1 != number2:
            return number1, number2
        
def multiplicationTables(*void): #? outrule crash when arguments are givin
    return ex.multiplication(10, 100)

def percentage(maxNumber: int, void: None, floatingPointAmount: int = 0):
    while True:
        _percentage, number = ex.percentage(maxNumber / 100, floatingPointAmount)
        number = int(number)
        if _percentage / 100 * number == round(_percentage / 100 * number, floatingPointAmount):  # TODO
            return _percentage, number
        
        
# print(multiplication(100000, 100000, 2))
# print(percentage(600, 1))
# print(multiplicationTables())


# print(division(100000, 100000))