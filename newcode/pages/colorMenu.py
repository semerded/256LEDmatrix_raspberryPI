from widgets.colorPallete import ColorPallete
import globalVars

class ColorMenu():    
    def __init__(self) -> None:
        self.pallete = ColorPallete()
        
    def place(self):
        self.pallete.checkForConfirmButtonClick(globalVars.screens.drawing)
        if (color := self.pallete.checkForColorClick()) != None:
            globalVars.currentColor = color
        self.pallete.place(globalVars.currentColor)