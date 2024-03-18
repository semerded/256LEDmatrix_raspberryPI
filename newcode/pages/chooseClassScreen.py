import gFrame, globalVars

class ChooseClassScreen:
    classInfoText = gFrame.Text("In welk leerjaar zit je?", "Comic sans", "8vw", gFrame.Color.WHITE)
    
    def __init__(self) -> None:
        self.classButtonList = []
        for index in range(6):
            color = globalVars.fieldColors[index + 1][1]
            classButton = gFrame.Button(("12vw", "12vw"), color)
            classButton.text(f"{index + 1}", "Comic sans", "12vw", gFrame.Text.textColorFromColor(color))
            classButton.setBorder(5, gFrame.Color.WHITE)
            self.classButtonList.append(classButton)
            
            
    def checkForClick(self):
        button: gFrame.Button
        for index, button in enumerate(self.classButtonList):
            if button.isClicked():
                globalVars.mathBotClass = index + 1
                globalVars.currentScreen = globalVars.screens.chooseDifficulty
                return globalVars.app.switchPage()

    def place(self):
        self.checkForClick()
        globalVars.menuButton.checkIfClicked()
        if globalVars.app.drawElements():
            globalVars.menuButton.place("93vw", "2vh")
        
            button: gFrame.Button
            for index, button in enumerate(self.classButtonList):
                button.place(gFrame.ScreenUnit.vw(8) + (gFrame.ScreenUnit.vw(14) * index), "50vh")
    
            self.classInfoText.placeInRect(gFrame.Rect(0, "20vh", "100vw", "15vh"), gFrame.xTextPositioning.center, gFrame.yTextPositioning.top)