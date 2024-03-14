import gFrame, globalVars
from core.mathBot import MathBot
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
    questionString = ""
    feedback = {
        "positief": 
            ["goed zo", "top gedaan!", "knap!"], 
        "negatief": 
            ["jammer", "volgende keer beter", "helaas, fout"]
    }
    chooseClassButton = gFrame.Button(("20vw", "7vh"), gFrame.Color.WHITE)
    chooseClassButton.setBorder(5, gFrame.Color.BLUE)
    chooseClassButton.text("Kies je leerjaar", gFrame.Font.H1, gFrame.Color.BLACK)
    newQuestionButton = gFrame.Button(("20vw", "7vh"), gFrame.Color.WHITE)
    newQuestionButton.setBorder(5, gFrame.Color.YELLOW)
    newQuestionButton.text("nieuwe vraag", gFrame.Font.H1, gFrame.Color.BLACK)
    
    questionText = gFrame.Text(questionString, gFrame.Font.FONT150, gFrame.Color.WHITE, italic=True)
    answerText = gFrame.Text(answerString, gFrame.Font.FONT150, gFrame.Color.WHITE, bold=True)
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
    questionActive = False
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
                    if "," not in self.answerString:
                        self.answerString += value
                else:
                    self.answerString += value
                return
        
    def place(self):
        if not self.questionActive:
            self.mathBot = MathBot(globalVars.mathBotDifficulty, globalVars.mathBotClass)
            self.newQuestionButton.updateColor(gFrame.Color.WHITE)
            number1, number2, mathType, self.expectedResult = self.mathBot.getQuestion()
            self.questionText.setText(f"{number1} {mathType} {number2} = ?")
            self.questionActive = True
            globalVars.app.requestUpdate()
            
        if globalVars.menuButton.checkIfClicked():
            globalVars.mathBotClass = None
            self.questionActive = False
            self.answerString = ""
            self.feedbackText.setText("")
            
        if self.chooseClassButton.isClicked():
            globalVars.currentScreen = globalVars.screens.chooseClass
            globalVars.mathBotClass = None
            self.questionActive = False
            self.answerString = ""
            self.feedbackText.setText("")
            globalVars.app.switchPage()
            
        if self.newQuestionButton.isClicked():
            self.questionActive = False
            self.answerString = ""
            self.feedbackText.setText("")
            
        self.checkInputButtons()
        
        if globalVars.app.drawElements():
            globalVars.menuButton.place("93vw", "2vh")
            
            self.chooseClassButton.place("70vw", "2vh")
            self.newQuestionButton.place("48vw", "2vh")
            
            button: gFrame.Button
            for index, button in enumerate(self.buttonList):
                button.place(index * self.buttonSide, gFrame.ScreenUnit.vh(100) - self.buttonSide)
            
            self.questionText.placeInRect(gFrame.Rect(0, "10vh", "100vw", "20vh"), gFrame.xTextPositioning.center, gFrame.yTextPositioning.top)
            
            self.answerText.setText(self.answerString)
            self.answerText.placeInRect(gFrame.Rect(0, "30vh", "100vw", "20vh"), gFrame.xTextPositioning.center, gFrame.yTextPositioning.top)
            
            self.feedbackText.placeInRect(gFrame.Rect(0, "50vh", "100vw", "20vh"), gFrame.xTextPositioning.center, gFrame.yTextPositioning.top)

    
    def _checkAnswer(self):
        self.answerString = self.answerString.replace(",", ".")
        givinAnswer = int_or_float(self.answerString)
        if givinAnswer == self.expectedResult:
            self.feedbackText.setTextColor(gFrame.Color.GREEN)
            self.feedbackText.setText(choice(self.feedback["positief"]))
            self.newQuestionButton.updateColor(gFrame.Color.GREEN)
        else:
            self.feedbackText.setTextColor(gFrame.Color.RED)
            self.feedbackText.setText(choice(self.feedback["negatief"]))
            