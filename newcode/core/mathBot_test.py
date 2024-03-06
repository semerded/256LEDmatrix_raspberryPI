from mathBot import MathBot

def testCalculate(number1, number2, type, solution):
    result = MathBot.calculate(int(number1), int(number2), type)
    try:
        assert result == solution
    except AssertionError:
        print(number1, number2, type, solution, result)

for i in range(1000):
    testCalculate(*MathBot.eersteJaar())
    testCalculate(*MathBot.tweedeJaar())
    testCalculate(*MathBot.derdeJaar())
    # testCalculate(*MathBot.eersteJaar())