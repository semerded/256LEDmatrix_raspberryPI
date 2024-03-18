import gFrame, globalVars

globalVars.app = gFrame.AppConstructor("50dw", "50dh", manualUpdating=True)
globalVars.app.centerApp()
gFrame.Display.setAspectRatio(gFrame.aspectRatios.ratio16to9, "50dw")

from widgets.menuButton import MenuButton
globalVars.menuButton = MenuButton()

import pygame, sys
from core.ledMatrix import LEDmatrix

LED_MATRIX = LEDmatrix(16, 16, "100vh", "100vh")

from pages.menuScreen import MenuScreen
from pages.drawingScreen import DrawingScreen
from pages.colorMenu import ColorMenu
from pages.calculatorScreen import CalculatorScreen
from pages.presetScreen import PresetScreen
from pages.chooseClassScreen import ChooseClassScreen
from pages.chooseDifficultyScreen import ChooseDifficultyScreen

PAGE_LISTING = [MenuScreen(), DrawingScreen(LED_MATRIX), ColorMenu(), PresetScreen(LED_MATRIX), CalculatorScreen(), ChooseClassScreen(), ChooseDifficultyScreen()]

while True:
    globalVars.app.eventHandler()
    globalVars.app.fill(gFrame.Color.BLACK) 
    
    PAGE_LISTING[globalVars.currentScreen.value].place()
    
    if gFrame.Interactions.isKeyReleased(pygame.K_ESCAPE):
        if globalVars.RPIconnected:
            LED_MATRIX.erasePhysicalMatrix()
        pygame.quit()
        sys.exit()
    