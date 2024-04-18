import gFrame, globalVars

class ColorPallete:
    buttonSize = ("18vw", "7vh")
    
    confirmButton = gFrame.Button(("90vw", "7vh"), gFrame.Color.WHITE, 5)
    confirmButton.text("kies kleur!", gFrame.Font.H1, gFrame.Color.BLACK, bold=True)
    confirmButton.setBorder(4, gFrame.Color.GREEN)
    
    def __init__(self) -> None:
        self.buttonList = []
        for index, color in enumerate(globalVars.fieldColors):
            self.buttonList.append(gFrame.Button(self.buttonSize, color[1], 5))
            self.buttonList[index].text(color[0], gFrame.Font.H1, gFrame.Text.textColorFromColor(color[1]))
            self.buttonList[index].setBorder(6, gFrame.Color.GRAY)
            
    def place(self, currentlySelected):        
        if globalVars.app.drawElements():
            buttonPosition = [0, 0]
            for index, button in enumerate(self.buttonList):
                button.place(gFrame.ScreenUnit.vw(1 + 20 * buttonPosition[0]), gFrame.ScreenUnit.vh(1 + 9 * buttonPosition[1]))
                buttonPosition[1] += 1
                if buttonPosition[1] == 10:
                    buttonPosition[1] = 0
                    buttonPosition[0] += 1
                
                if currentlySelected == index:
                    gFrame.Draw.borderFromRect(button.getBorderRect, 5, gFrame.Color.GREEN, 10)
            self.confirmButton.place("5vw", "92vh")
        
    def checkForColorClick(self):
        button: gFrame.Button
        for index, button in enumerate(self.buttonList):
            if button.isClicked():
                globalVars.app.requestUpdate()
                return index
                
    def checkForConfirmButtonClick(self, pageToSwitchTo: globalVars.screens):        
        if self.confirmButton.isClicked():
            globalVars.currentScreen = pageToSwitchTo
            return globalVars.app.switchPage()
            