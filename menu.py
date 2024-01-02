from pygameaddons import *
import globals

class Menu:
    def __init__(self, APP: AppConstructor) -> None:
        self.APP = APP
        self.choicePresetButton = Button((ScreenUnit.vw(45), ScreenUnit.vh(90)), Color.LIGHTGRAY, 10)
        self.choicePresetButton.text("Presets", Font.FONT50, Color.WHITE)
        self.choiceDrawButton = Button((ScreenUnit.vw(45), ScreenUnit.vh(90)), Color.LIGHTGRAY, 10)
        self.choiceDrawButton.text("Tekenen", Font.FONT50, Color.WHITE)
        
    def place(self):
        if self.APP.isScreenResized():
            self.choicePresetButton.updateButtonSize(ScreenUnit.vw(45), ScreenUnit.vh(90))
            self.choiceDrawButton.updateButtonSize(ScreenUnit.vw(45), ScreenUnit.vh(90))
            self.APP.requestUpdate
            
        self.choicePresetButton.addBorderOnHover(5, Color.WHITE)
        if self.choicePresetButton.onMouseRelease():
            globals.currentScreen = screens.preset
    
        self.choiceDrawButton.addBorderOnHover(5, Color.WHITE)
        if self.choiceDrawButton.onMouseRelease():
            globals.currentScreen = screens.drawing
            
        if self.APP.firstFrame() or self.APP.updateAvalible:
            self.APP.maindisplay.fill(Color.BLACK)
            self.choiceDrawButton.place(ScreenUnit.vw(3), ScreenUnit.vh(5))
            self.choicePresetButton.place(ScreenUnit.vw(3), ScreenUnit.vh(5))




            
        