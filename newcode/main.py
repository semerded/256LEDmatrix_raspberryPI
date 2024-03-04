import gFrame, globalVars
import pygame, sys





from core.ledMatrix import LEDmatrix

LED_MATRIX = LEDmatrix(16, 16, "100vh", "100vh")

from screens.drawing import DrawingScreen
# from screens.colorMenu import _
# from screens.calculator import _
# from screens.presets import _
# from screens.menu import _

drawingScreen = DrawingScreen(LED_MATRIX)

SCREEN_LISTING = [drawingScreen]



while True:
    globalVars.app.eventHandler()
    globalVars.app.fill(gFrame.Color.BLACK) 
    
    drawingScreen.place()
    
    if gFrame.Interactions.isKeyReleased(pygame.K_ESCAPE):
        if globalVars.RPIconnected:
            LED_MATRIX.erasePhysicalMatrix()
        pygame.quit()
        sys.exit()
    