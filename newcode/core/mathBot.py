import random


class MathBot:

    def calculate(number1, number2, type):
        if type == "+":
            return number1 + number2
        elif type == "-":
            return number1 - number2
        elif type == "*":
            return number1 * number2
        elif type == "/":
            return number1 / number2
        elif type == "%":
            return 
    
    def getType(*validtypes: str):
        return random.choice(validtypes)
    
    def getNumbers(maxRange, type, minRange = 1):
        while True:
            number1 = random.randint(minRange, maxRange)
            number2 = random.randint(minRange, maxRange)
            if MathBot.calculate(number1, number2, type) in range(minRange, maxRange + 1):
                return number1, number2
            
    def maaltafel():
        return random.randint(1, 10), random.randint(1, 10), "*"

    def eersteJaar():
        type = MathBot.getType("+", "-")
        number1, number2 = MathBot.getNumbers(20, type)
        solution = MathBot.calculate(number1, number2, type)
        return str(number1), str(number2), type, solution
    
    def tweedeJaar():
        if random.randint(1, 4) == 1:
            number1, number2, type = MathBot.maaltafel()
        else:
            type = MathBot.getType("+", "-")
            number1, number2 = MathBot.getNumbers(100, type)
        solution = MathBot.calculate(number1, number2, type)
        return str(number1), str(number2), type, solution
    
    def derdeJaar():
        if random.randint(1, 2) == 1:
            number1, number2, type = MathBot.maaltafel()
        else:
            type = MathBot.getType("+", "-")
            number1, number2 = MathBot.getNumbers(1000, type)
        solution = MathBot.calculate(number1, number2, type)
        return str(number1), str(number2), type, solution
    
    def getQuestion(classNumber):
        return classList[classNumber - 1]()
    
    def vierdeJaar():
        rand = random.randint(1, 2)
        if rand == 1:
            type = MathBot.getType("+", "-")
            number1, number2 = MathBot.getNumbers(10000, type)
        elif rand == 2:
            type = MathBot.getType("+", "-")
            number1, number2 = MathBot.getNumbers(10000, type, 1000)
            number1 *= 10
            number2 *= 10

            
            
        solution = MathBot.calculate(number1, number2, type)
        return str(number1), str(number2), type, solution
    
classList = [MathBot.eersteJaar, MathBot.tweedeJaar, MathBot.derdeJaar]

if __name__ == "__main__":
    print(MathBot.eersteJaar())
    print(MathBot.tweedeJaar())
    print(MathBot.derdeJaar())
    print(MathBot.vierdeJaar())
    
