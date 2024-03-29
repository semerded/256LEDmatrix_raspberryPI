import random
import core.math.excersizeGenerator as generator
from core.math.mathBotRules import rules

generatorRefference =   { 
                        "+": generator.addition, 
                        "-": generator.subtraction, 
                        "*": generator.multiplication, 
                        "/": generator.division, 
                        "maaltafel": generator.multiplicationTables, 
                        "%": generator.percentage
                        }

class MathBot:
    def __init__(self, difficulty: int, classNumber: int) -> None:
        self.difficulty = difficulty
        self.classNumber = classNumber
        self.parameters = rules[classNumber - 1][difficulty - 1]
    
    def getExcercise(self):
        operand = random.choice(self.parameters["operand"])
        
        numbers = self.getNumbersPerClass(self.parameters["maxNumber"], self.parameters["maxSolution"], operand)
        expectedResult = generator.calculate(*numbers, operand)
        operand = self._correctOperand(operand)
        return *numbers, operand, expectedResult

        
    def getNumbersPerClass(self, maxNumber: int, maxSolution: int, operand: str):
        if self.classNumber == 1:
            return self.eersteJaar(maxNumber, maxSolution, operand)
        elif self.classNumber == 2:
            return self.tweedeJaar(maxNumber, maxSolution, operand)
        elif self.classNumber == 3:
            return self.derdeJaar(maxNumber, maxSolution, operand)
        elif self.classNumber == 4:
            return self.vierdeJaar(maxNumber, maxSolution, operand)
        elif self.classNumber == 5:
            return self.vijfdeJaar(maxNumber, maxSolution, operand)
        
    def _correctOperand(self, operand: str):  
        if operand == "maaltafel":
            return "*"
        elif operand == "%":
            return "% van"
        return operand
    
    def getNumbers(self, maxNumber: int, maxSolution: int, operand: str, floatingPointAmount: int = 0):
        return generatorRefference[operand](maxNumber, maxSolution, floatingPointAmount)
    
    def getNumbersEndingWithZero(self, maxNumber: int, maxSolution: int, operand: str, floatingPointAmout: int = 0):
        
        return tuple([number * 10 for number in generatorRefference[operand](int(maxNumber / 10), maxSolution, floatingPointAmout)])
        
        
    #* classes
    
    def eersteJaar(self, maxNumber: int, maxSolution: int, operand: str):
        return self.getNumbers(maxNumber, maxSolution, operand)


    def tweedeJaar(self, maxNumber: int, maxSolution: int, operand: str):
        return self.getNumbers(maxNumber, maxSolution, operand)
        
        
    def derdeJaar(self, maxNumber: int, maxSolution: int, operand: str):
        return self.getNumbers(maxNumber, maxSolution, operand)

    
    def vierdeJaar(self, maxNumber: int, maxSolution: int, operand: str):
        if self.difficulty == 1:
            return self.getNumbers(maxNumber, maxSolution, operand)
        
        elif self.difficulty == 2:
            floatingPointAmount = random.randint(1, 3) if random.randint(0, 5) == 1 else 0
            
            if random.randint(0, 3) == 1:
                return self.getNumbersEndingWithZero(maxNumber, maxSolution, operand, floatingPointAmount)
            
            return self.getNumbers(int(maxNumber / 10), int(maxSolution / 10), operand, floatingPointAmount)
                    
        elif self.difficulty == 3:
            floatingPointAmount = random.randint(1, 3) if random.randint(0, 2) == 1 else 0
            if random.randint(0, 2) == 1:
                return self.getNumbersEndingWithZero(maxNumber, maxSolution, operand)
            return self.getNumbers(int(maxNumber / 10), int(maxSolution / 10), operand, floatingPointAmount)
    
    
    def vijfdeJaar(self, maxNumber: int, maxSolution: int, operand: str):
        floatingPointAmount = random.randint(1, 4) if random.randint(0, 5 - self.difficulty) == 1 else 0
        return self.getNumbers(maxNumber, maxSolution, operand, floatingPointAmount)

    
    def zesdeJaar(self, maxNumber: int, maxSolution: int, operand: str):
        pass
            
            
            
        

