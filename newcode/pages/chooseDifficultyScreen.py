import gFrame, globalVars

class ChooseDifficultyScreen:
    difficultyInfoText = gFrame.Text("Moeilijkheid van de oefeningen", "Comic sans", "6vw", gFrame.Color.WHITE)
    
    difficultyInnerText = ["Makkelijk", "Gemiddeld", "Moeilijk"]
    difficultyColor = [gFrame.Color.GREEN, gFrame.Color.YELLOW, gFrame.Color.RED]
    
    def __init__(self) -> None:
        self.difficultyButtonList = []
        for index in range(3):
            color = self.difficultyColor[index]
            difficultyButton = gFrame.Button(("24vw", "12vw"), color)
            difficultyButton.text(self.difficultyInnerText[index], "comic sans", gFrame.ScreenUnit.vw(4.5), gFrame.Text.textColorFromColor(color))
            difficultyButton.setBorder(5, gFrame.Color.WHITE)
            self.difficultyButtonList.append(difficultyButton)
            
            
    def checkForClick(self):
        button: gFrame.Button            
        for index, button in enumerate(self.difficultyButtonList):
            if button.isClicked():
                globalVars.mathBotDifficulty = index + 1
                globalVars.currentScreen = globalVars.screens.calculator
                return globalVars.app.switchPage()

    def place(self):
        self.checkForClick()
        globalVars.menuButton.checkIfClicked()
        if globalVars.app.drawElements():
            globalVars.menuButton.place("93vw", "2vh")
            button: gFrame.Button
            for index, button in enumerate(self.difficultyButtonList):
                button.place(gFrame.ScreenUnit.vw(8) + (gFrame.ScreenUnit.vw(28) * index), "50vh")
                
            self.difficultyInfoText.placeInRect(gFrame.Rect(0, "20vh", "100vw", "15vh"), gFrame.xTextPositioning.center, gFrame.yTextPositioning.top)