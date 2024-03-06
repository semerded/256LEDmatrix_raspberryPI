import gFrame, globalVars
from core.mathBot import MathBot

buttonValues = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ",", "<<", "enter"]

class CalculatorButtons:
    answerString = ""
    chooseClassButton = gFrame.Button(("15vw", "7vh"), gFrame.Color.WHITE)
    question = gFrame.Text("", gFrame.Font.FONT150, gFrame.Color.WHITE, italic=True)
    answer = gFrame.Text(answerString, gFrame.Font.FONT150, gFrame.Color.WHITE, bold=True)
    
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
                    pass
                else:
                    self.answerString += value
                globalVars.app.requestUpdate()
                return
        
    def place(self):
        if globalVars.menuButton.checkIfClicked():
            globalVars.mathBotClass = None
            self.answerString = ""
            
        self.checkInputButtons()
        
        if globalVars.app.drawElements():
            globalVars.menuButton.place("93vw", "2vh")
            
            button: gFrame.Button
            for index, button in enumerate(self.buttonList):
                button.place(index * self.buttonSide, gFrame.ScreenUnit.vh(100) - self.buttonSide)
            
            self.answer.setText(self.answerString)
            self.answer.placeInRect(gFrame.Rect(0, "50vh", "100vw", "15vh"), gFrame.xTextPositioning.center, gFrame.yTextPositioning.top)