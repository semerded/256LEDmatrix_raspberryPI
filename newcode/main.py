import gFrame, globalVars, pygame

# globalVars.app = gFrame.AppConstructor("50dw", "50dh", manualUpdating=True)
globalVars.app = gFrame.AppConstructor("100dw", "100dh", pygame.FULLSCREEN, manualUpdating=True)
globalVars.app.centerApp()
# gFrame.Display.setAspectRatio(gFrame.aspectRatios.ratio16to9, "100dw")

from LEDs.reset_led_data import resetLedData
resetLedData()

from widgets.menuButton import MenuButton
globalVars.menuButton = MenuButton()

from LEDs.ledMatrix import LEDmatrix

LED_MATRIX = LEDmatrix(16, 16, "100vh", "100vh")

from pages.menuScreen import MenuScreen
from pages.drawingScreen import DrawingScreen
from pages.colorMenu import ColorMenu
from pages.calculatorScreen import CalculatorScreen
from pages.presetScreen import PresetScreen
from pages.chooseClassScreen import ChooseClassScreen
from pages.chooseDifficultyScreen import ChooseDifficultyScreen
from pages.carLEDscreen import CarLEDscreen
from pages.carLEDcolorMenu import CarLedColorMenu
from pages.carLEDeffectMenu import CarLedEffectMenu

PAGE_LISTING = [MenuScreen(), DrawingScreen(LED_MATRIX), ColorMenu(), PresetScreen(LED_MATRIX), CalculatorScreen(), ChooseClassScreen(), ChooseDifficultyScreen(), CarLEDscreen("LEDs/led_data.json"), CarLedColorMenu(), CarLedEffectMenu()]

import sys
from LED__switch import LEDswitch

# @gFrame.debugging
def main():
    print("main succesfully launched")
    LEDswitch(True)
    while True:
        try:
            globalVars.app.eventHandler()
            globalVars.app.fill(gFrame.Color.BLACK) 
            
            PAGE_LISTING[globalVars.currentScreen.value].place()
            
            if gFrame.Interactions.isKeyReleased(pygame.K_ESCAPE):
                if globalVars.RPIconnected:
                    LED_MATRIX.erasePhysicalMatrix()
                globalVars.programRunning = False
                LEDswitch(False)
                pygame.quit()
                sys.exit()
                
        except KeyboardInterrupt:
            globalVars.programRunning = False
            LEDswitch(False)

if __name__ == '__main__':
    main()