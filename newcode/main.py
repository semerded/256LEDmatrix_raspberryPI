import gFrame, globalVars
import pygame, sys
from core.ledMatrix import LEDmatrix

LED_MATRIX = LEDmatrix(16, 16, "100vh", "100vh")

from screens.menuScreen import MenuScreen
from screens.drawingScreen import DrawingScreen
from screens.colorMenu import ColorMenu
from screens.calculatorScreen import CalculatorScreen
from screens.presetScreen import PresetScreen

SCREEN_LISTING = [MenuScreen(), DrawingScreen(LED_MATRIX), ColorMenu()]

while True:
    globalVars.app.eventHandler()
    globalVars.app.fill(gFrame.Color.BLACK) 
    
    SCREEN_LISTING[globalVars.currentScreen.value].place()
    
    if gFrame.Interactions.isKeyReleased(pygame.K_ESCAPE):
        if globalVars.RPIconnected:
            LED_MATRIX.erasePhysicalMatrix()
        pygame.quit()
        sys.exit()
    