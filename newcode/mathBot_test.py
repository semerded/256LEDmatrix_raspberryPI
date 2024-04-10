from core.math.mathBot import MathBot
from core.math.excersizeGenerator import calculate

def testCalculate(number1, number2, type, solution):
    result = calculate((number1), (number2), type)
    try:
        assert result == solution
    except AssertionError:
        print(f"fout met: {number1} {type} {number2} = {result}, maar verwachte {solution}")
    
for _class in range(5):
    for _difficulty in range(3):
        bot = MathBot(_difficulty + 1, _class + 1)
        for i in range(1000):
            sol = bot.getExcercise()
            testCalculate(*sol)

print("test klaar")
