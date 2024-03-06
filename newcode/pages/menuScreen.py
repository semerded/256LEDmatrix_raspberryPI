import gFrame, globalVars

class MenuScreen:
    buttonSize = ("45vw", "45vh")
    
    drawingScreenButton = gFrame.Button(buttonSize, gFrame.Color.RED)
    drawingScreenButton.text("tekenen", gFrame.Font.FONT50, gFrame.Color.BLACK)
    
    presetScreenButton = gFrame.Button(buttonSize, gFrame.Color.YELLOW)
    presetScreenButton.text("voorbeelden", gFrame.Font.FONT50, gFrame.Color.BLACK)
    
    calculatorScreenButton = gFrame.Button(buttonSize, gFrame.Color.GREEN)
    calculatorScreenButton.text("rekenrobot", gFrame.Font.FONT50, gFrame.Color.BLACK)

    _ButtonScreenButton = gFrame.Button(buttonSize, gFrame.Color.BLUE)
    _ButtonScreenButton.text("ik weet het niet", gFrame.Font.FONT50, gFrame.Color.BLACK)
    
    def __init__(self) -> None:
        pass
    
    def place(self):
        if globalVars.app.drawElements():
            self.drawingScreenButton.place("2vw", "2vh")
            self.presetScreenButton.place("52vw", "2vh")
            self.calculatorScreenButton.place("2vw", "52vh")
            self._ButtonScreenButton.place("52vw", "52vh")
            
        if self.drawingScreenButton.isClicked():
            globalVars.currentScreen = globalVars.screens.drawing
            return globalVars.app.switchPage()
                
        if self.presetScreenButton.isClicked():
            globalVars.currentScreen = globalVars.screens.preset
            return globalVars.app.switchPage()
                
        if self.calculatorScreenButton.isClicked():
            globalVars.currentScreen = globalVars.screens.chooseClass
            return globalVars.app.switchPage()
    
            # TODO add function for button