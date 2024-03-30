import gFrame, globalVars
from core.math.mathBotBackgroundGenerator import MathBotGenerator
from random import choice

buttonValues = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ",", "<<", "enter"]

def int_or_float(number: int | float) -> int | float:
    try: 
        number = int(number)
    except ValueError:
        number = float(number)
    return number

class CalculatorButtons:
    answerString = ""
    excerciseString = ""
    feedback = {
        "positief": 
            ["goed zo", "top gedaan!", "knap!"], 
        "negatief": 
            ["jammer", "volgende keer beter", "helaas, fout"]
    }
    chooseClassButton = gFrame.Button(("20vw", "7vh"), gFrame.Color.WHITE)
    chooseClassButton.setBorder(5, gFrame.Color.BLUE)
    chooseClassButton.text("Kies je leerjaar", gFrame.Font.H1, gFrame.Color.BLACK)
    newExcerciseButton = gFrame.Button(("20vw", "7vh"), gFrame.Color.WHITE)
    newExcerciseButton.setBorder(5, gFrame.Color.YELLOW)
    newExcerciseButton.text("nieuwe vraag", gFrame.Font.H1, gFrame.Color.BLACK)
    
    excerciseText = gFrame.Text(excerciseString, 'comic sans', gFrame.ScreenUnit.vw(8), gFrame.Color.WHITE, italic=True)
    answerText = gFrame.Text(answerString, 'comic sans', gFrame.ScreenUnit.vw(8), gFrame.Color.WHITE, bold=True)
    feedbackText = gFrame.Text("", gFrame.Font.FONT150, gFrame.Color.WHITE)    
    def __init__(self) -> None:
        self.buttonList = []
        self.buttonSide = gFrame.ScreenUnit.vw(100) / len(buttonValues)
        
        buttonSize = (self.buttonSide, self.buttonSide)
        for value in buttonValues:
            button = gFrame.Button(buttonSize, gFrame.Color.GREY)
            button.setBorder(1, gFrame.Color.LIGHT_GRAY)
            button.text(value, gFrame.Font.H1, gFrame.Color.WHITE)
            self.buttonList.append(button)


class CalculatorScreen(CalculatorButtons):
    excerciseActive = False
    expectedResult = None
    def __init__(self) -> None:
        super().__init__()
        
    def checkInputButtons(self):
        button: gFrame.Button
        for index, button in enumerate(self.buttonList):
            if button.isClicked():
                value = buttonValues[index]
                if value == "<<":
                    self.answerString = self.answerString[:-1]
                elif value == "enter":
                    self._checkAnswer()
                elif value == ",":
                    if "," not in self.answerString and "." not in self.answerString:
                        self.answerString += value
                else:
                    self.answerString += value
                return
        
    def place(self):
        if not self.excerciseActive:
            self.mathBot = MathBotGenerator(globalVars.mathBotDifficulty, globalVars.mathBotClass)
            self.mathBot.startGenerator()
            self.excerciseActive = True
            self._getExcercise()                    
            
        if globalVars.menuButton.checkIfClicked():
            self._exitScreen()
            
        if self.chooseClassButton.isClicked():
            globalVars.currentScreen = globalVars.screens.chooseClass
            self._exitScreen()
            globalVars.app.switchPage()
            
        if self.newExcerciseButton.isClicked():
            self._getExcercise()        
            
        self.checkInputButtons()
        
        if globalVars.app.drawElements():
            globalVars.menuButton.place("93vw", "2vh")
            
            self.chooseClassButton.place("70vw", "2vh")
            self.newExcerciseButton.place("48vw", "2vh")
            
            button: gFrame.Button
            for index, button in enumerate(self.buttonList):
                button.place(index * self.buttonSide, gFrame.ScreenUnit.vh(100) - self.buttonSide)
            
            self.excerciseText.placeInRect(gFrame.Rect(0, "10vh", "100vw", "20vh"), gFrame.xTextPositioning.center, gFrame.yTextPositioning.top)
            
            self.answerText.setText(self.answerString)
            self.answerText.placeInRect(gFrame.Rect(0, "30vh", "100vw", "20vh"), gFrame.xTextPositioning.center, gFrame.yTextPositioning.top)
            
            self.feedbackText.placeInRect(gFrame.Rect(0, "50vh", "100vw", "20vh"), gFrame.xTextPositioning.center, gFrame.yTextPositioning.top)

    
    def _checkAnswer(self):
        self.answerString = self.answerString.replace(",", ".")
        if int_or_float(self.answerString) == self.expectedResult:
            self.feedbackText.setTextColor(gFrame.Color.GREEN)
            self.feedbackText.setText(choice(self.feedback["positief"]))
            self.newExcerciseButton.updateColor(gFrame.Color.GREEN)
        else:
            self.feedbackText.setTextColor(gFrame.Color.RED)
            self.feedbackText.setText(choice(self.feedback["negatief"]))
            
    def _exitScreen(self):
        globalVars.mathBotClass = None
        self.excerciseActive = False
        self.answerString = ""
        self.feedbackText.setText("")
        self.mathBot.stopGenerator()
        
    def _getExcercise(self):
        self.newExcerciseButton.updateColor(gFrame.Color.WHITE)
        number1, number2, mathType, self.expectedResult = self.mathBot.getExcerciseFromQueue()
        self.excerciseText.setText(f"{number1} {mathType} {number2} = ?")
        self.answerString = ""
        self.feedbackText.setText("")
        globalVars.app.requestUpdate()