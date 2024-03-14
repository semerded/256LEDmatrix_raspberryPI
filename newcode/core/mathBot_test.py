from mathBot import MathBot

def testCalculate(number1, number2, type, solution):
    result = MathBot.calculate(int(number1), int(number2), type)
    try:
        assert result == solution
    except AssertionError:
        print(f"fout met: {number1} {type} {number2} = {result}, maar verwachte {solution}")
    
        
# def testRange(number1, number2, result, range)

for i in range(1000):
    testCalculate(*MathBot.eersteJaar())
    testCalculate(*MathBot.tweedeJaar())
    testCalculate(*MathBot.derdeJaar())
    testCalculate(*MathBot.vierdeJaar())
    # testCalculate(*MathBot.eersteJaar())
print("test klaar")