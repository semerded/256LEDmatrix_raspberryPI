from widgets.colorPallete import ColorPallete
import globalVars

class CarLedColorMenu():    
    def __init__(self) -> None:
        self.pallete = ColorPallete()
        
    def place(self):
        self.pallete.checkForConfirmButtonClick(globalVars.screens.carLED)
        if (color := self.pallete.checkForColorClick()) != None:
            if globalVars.currentLedSelected == "carled":
                globalVars.currentCarLedColor = color
            else:
                globalVars.currentKnightRiderColor = color
        
        if globalVars.currentLedSelected == "carled":
            self.pallete.place(globalVars.currentCarLedColor)
        else:
            self.pallete.place(globalVars.currentKnightRiderColor)
            