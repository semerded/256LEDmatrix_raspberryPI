from pygameaddons import AppConstructor, ScreenUnit, Button, Color, Font, screens, pygame
import globals

class Menu:
    def __init__(self, APP: AppConstructor) -> None:
        self.APP = APP
        self.choicePresetButton = Button((ScreenUnit.vw(45), ScreenUnit.vh(90)), Color.LIGHT_GRAY, 10)
        self.choicePresetButton.text("Presets", Font.FONT50, Color.WHITE)
        self.choiceDrawButton = Button((ScreenUnit.vw(45), ScreenUnit.vh(90)), Color.LIGHT_GRAY, 10)
        self.choiceDrawButton.text("Tekenen", Font.FONT50, Color.WHITE)
        
    def place(self):
        self.choicePresetButton.addBorderOnHover(5, Color.WHITE)
        if self.choicePresetButton.onMouseClick():
            globals.currentScreen = screens.preset
            return self.APP.requestUpdate
         
        self.choiceDrawButton.addBorderOnHover(5, Color.WHITE)
        if self.choiceDrawButton.onMouseClick():
            globals.currentScreen = screens.drawing
            return self.APP.requestUpdate
            
        self.APP.requestUpdate
        
            
        if self.APP.firstFrame() or self.APP.updateAvalible:
            self.APP.maindisplay.fill(Color.BLACK)
            self.choiceDrawButton.place(ScreenUnit.vw(3), ScreenUnit.vh(5))
            self.choicePresetButton.place(ScreenUnit.vw(52), ScreenUnit.vh(5))
            pygame.display.update()




            
        