import random, json

with open("core/mathBotRules.json") as fp:
    rules = json.load(fp)


class MathBot:
    def __init__(self, difficulty: int, classNumber: int) -> None:
        self.difficulty = difficulty
        self.classNumber = classNumber
        self.parameters = rules[classNumber - 1][difficulty - 1]
    
    def getExcercise(self):
        operand = random.choice(self.parameters["operand"])
        
        numbers = self.getNumbersPerClass(self.parameters["maxNumber1"], self.parameters["maxNumber2"], operand, self.parameters["maxRange"])
        expectedResult = MathBot.calculate(*numbers, operand)
        return *numbers, operand, expectedResult


    @staticmethod
    def calculate(number1, number2, operand):
        if operand == "+":
            return number1 + number2
        elif operand == "-":
            return number1 - number2
        elif operand == "*":
            return number1 * number2
        elif operand == "/":
            return number1 / number2
        elif operand == "%":
            return 
    
    @staticmethod
    def getNumbers(maxNumber1: int, maxNumber2: int, operand: str, maxRange: int, minRange: int = 1):
        while True:
            number1 = random.randint(minRange, maxNumber1)
            number2 = random.randint(minRange, maxNumber2)
            print(number1, number2, operand)
            if MathBot.calculate(number1, number2, operand) in range(minRange, maxRange + 1):
                return number1, number2
            
    def getNumbersPerClass(self, maxNumber1: int, maxNumber2: int, operand: str, maxRange: int):
        if self.classNumber == 1:
            return self.eersteJaar(maxNumber1, maxNumber2, operand, maxRange)
        elif self.classNumber == 2:
            return self.tweedeJaar(maxNumber1, maxNumber2, operand, maxRange)
        elif self.classNumber == 3:
            return self.derdeJaar(maxNumber1, maxNumber2, operand, maxRange)
        elif self.classNumber == 4:
            return self.vierdeJaar(maxNumber1, maxNumber2, operand, maxRange)
            
    def eersteJaar(self, maxNumber1: int, maxNumber2: int, operand: str, maxRange: int):
        return MathBot.getNumbers(maxNumber1, maxNumber2, operand, maxRange)

    def tweedeJaar(self, maxNumber1: int, maxNumber2: int, operand: str, maxRange: int):
        return MathBot.getNumbers(maxNumber1, maxNumber2, operand, maxRange)
        
    def derdeJaar(self, maxNumber1: int, maxNumber2: int, operand: str, maxRange: int):
        if operand == "maaltafels":
            return MathBot.getNumbers(10, 10, "*", 100)
        return MathBot.getNumbers(maxNumber1, maxNumber2, operand, maxRange)
    
    def vierdeJaar(self, maxNumber1: int, maxNumber2: int, operand: str, maxRange: int):
        if operand == "maaltafels":
            return MathBot.getNumbers(10, 10, "*", 100)
        
        elif self.difficulty == 2:
            if random.randint(0, 3) == 0:
                if operand in ("+", "-"):
                    return tuple([10*x for x in MathBot.getNumbers(int(maxNumber1 / 10), int(maxNumber2 / 10), operand, int(maxRange / 10), minRange=1000)])
                else:
                    return tuple([10*x for x in MathBot.getNumbers(int(maxNumber1 / 10), int(maxNumber2 / 10), operand, int(maxRange / 10))])
                    
        elif self.difficulty == 3:
            if random.randint(0, 2) == 0:
                if operand in ("+", "-"):
                    return tuple([10*x for x in MathBot.getNumbers(int(maxNumber1 / 10), int(maxNumber2 / 10), operand, int(maxRange / 10), minRange=1000)])
                else:
                    return tuple([10*x for x in MathBot.getNumbers(int(maxNumber1 / 10), int(maxNumber2 / 10), operand, int(maxRange / 10))])
                    
        return MathBot.getNumbers(int(maxNumber1 / 10), int(maxNumber2 / 10), operand, int(maxRange / 10))

