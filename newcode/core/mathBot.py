import random, json

with open("core/mathBotRules.json") as fp:
    rules = json.load(fp)


class MathBot:
    def __init__(self, difficulty: int, classNumber: int) -> None:
        self.difficulty = difficulty
        self.classNumber = classNumber
        self.parameters = rules[classNumber - 1][difficulty - 1]
    
    def getQuestion(self):
        operand = random.choice(self.parameters["operand"])
        
        if (numbers := self.specialRules(operand)) != False:
            numbers = MathBot.getNumbers(self.parameters["maxNumber1"], self.parameters["maxNumber2"], operand, self.parameters["maxRange"])
        expectedResult = MathBot.calculate(*numbers, operand)
        return *numbers, operand, expectedResult

    def specialRules(self, operand):
        if operand == "maaltafel":
            return MathBot.getNumbers(10, 10, "*", 100)

        if self.classNumber == 4:
            pass

    @staticmethod
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
    
    @staticmethod
    def getNumbers(maxNumber1: int, maxNumber2: int, type: str, maxRange: int, minRange: int = 1):
        while True:
            number1 = random.randint(minRange, maxNumber1)
            number2 = random.randint(minRange, maxNumber2)
            if MathBot.calculate(number1, number2, type) in range(minRange, maxRange + 1):
                return number1, number2

    

# if __name__ == "__main__":
#     print(eersteJaar())
#     print(tweedeJaar())
#     print(derdeJaar())
#     print(vierdeJaar())
    
