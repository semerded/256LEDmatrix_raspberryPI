import gFrame, globalVars

globalVars.app = gFrame.AppConstructor("100dw", "100dh", manualUpdating=True)
globalVars.app.centerApp()
# gFrame.Display.setAspectRatio(gFrame.aspectRatios.ratio16to9, "100dw")

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

PAGE_LISTING = [MenuScreen(), DrawingScreen(LED_MATRIX), ColorMenu(), PresetScreen(LED_MATRIX), CalculatorScreen(), ChooseClassScreen(), ChooseDifficultyScreen(), CarLEDscreen()]

import pygame, sys, json

# @gFrame.debugger
def main():
    print("main succesfully launched")
    fp = open("LEDs/led_data.json")
    data = json.load(fp)
    data["active"] = True
    fp.close()
    fp = open("LEDs/led_data.json", "w")
    json.dump(data, fp, indent = 4, separators=(',',': '))
    fp.close()
    while True:
        try:
            globalVars.app.eventHandler()
            globalVars.app.fill(gFrame.Color.BLACK) 
            
            PAGE_LISTING[globalVars.currentScreen.value].place()
            
            if gFrame.Interactions.isKeyReleased(pygame.K_ESCAPE):
                if globalVars.RPIconnected:
                    LED_MATRIX.erasePhysicalMatrix()
                globalVars.programRunning = False
                with open("LEDs/led_data.json", "r+") as fp:
                    data = json.load(fp)
                    data["active"] = False
                    fp.seek(0)
                    json.dump(data, fp, indent = 4, separators=(',',': '))
                pygame.quit()
                sys.exit()
        except KeyboardInterrupt:
            globalVars.programRunning = False
            with open("LEDs/led_data.json", "r+") as fp:
                data = json.load(fp)
                data["active"] = False
                fp.seek(0)
                json.dump(data, fp, indent = 4, separators=(',',': '))
                

if __name__ == '__main__':
    main() 