import threading, math
import board, neopixel
from enum import Enum
from pygameaddons import *
import globals
from undo_redo import DrawingHistory
from matrix import Matrix

pixels = neopixel.NeoPixel(board.D18, 256, brightness = 0.1)



APP = AppConstructor(100, 100, pygame.FULLSCREEN, manualUpdating=True)
APP.centerApp()
clock = pygame.time.Clock()

# APP.setAspectratio(ScreenUnit.aspectRatio(aspectRatios.ratio16to9), height=ScreenUnit.dh(90))

class ColorButtons:
    def __init__(self, buttonAmount, buttonText) -> None:
        self.buttonSize = (ScreenUnit.vw(20), ScreenUnit.vh(7))
        self.previousHighlightedButton = globals.currentColor
        self.buttonText = buttonText
        self.buttonList = []
        for index in range(buttonAmount):
            self.buttonList.append(Button(self.buttonSize, globals.fieldColors[index], 5)),
            self.buttonList[index].border(6, Color.GRAY)
    
    
    def placeButtons(self):
        self.buttonSize = (ScreenUnit.vw(20), ScreenUnit.vh(7))
        for index, button in enumerate(self.buttonList):
            button.updateButtonSize(self.buttonSize[0], self.buttonSize[1])
            
            button.text(self.buttonText[index], Font.H1, Color.GREY)
            button.place(ScreenUnit.vw(70), ScreenUnit.vh(1 + 9 * index))
            if button.onMouseClick():
                globals.currentColor = index         
        self.highlightActiveColor(globals.currentColor)
            
    def highlightActiveColor(self, index):
        buttonRect = self.buttonList[index].getButtonAndBorderRect
        Drawing.border(5, buttonRect, Color.GREEN, 10)
        APP.requestUpdate
        
    @property
    def getButtonHeight(self):
        return ScreenUnit.vh(2 + 9 * len(self.buttonList))
        
        
class Pixels:
    def __init__(self, pixels) -> None:
        self.pixels = pixels
        
    def drawMatrixOnPhysicalMatrix(self, matrix: list[list]):
        ledCounter = 0
        reverse = True
        for row in matrix:
            if reverse:
                for column in reversed(row):
                    self.pixels[ledCounter] = globals.fieldColors[column]                 
                    ledCounter += 1
            else:
                for column in row:
                    self.pixels[ledCounter] = globals.fieldColors[column]
                    ledCounter += 1
            reverse = not reverse
            
    def erasePhysicalMatrix(self):
        MATRIX.eraseMatrix()
        APP.updateDisplay()
        self.pixels.fill(Color.BLACK)
        
 
COLOR_BUTTON_TEXT = ["zwart", "rood", "oranje", "geel", "groen", "lichtblauw", "donkerblauw", "paars", "roze", "wit"]
MATRIX = Matrix(16, 16)
COLOR_PICKER_BUTTONS = ColorButtons(len(globals.fieldColors), COLOR_BUTTON_TEXT)
LED_MATRIX = Pixels(pixels)
DRAWING_HISTORY = DrawingHistory(MATRIX.getMatrixDimensions)

drawPixelOnLEDMatrixButton = Button((ScreenUnit.vw(15), ScreenUnit.vh(7)), Color.WHITE, 5)
drawPixelOnLEDMatrixButton.border(4, Color.GREEN)
drawPixelOnLEDMatrixButton.text("Teken!", Font.H1, overFlow=overFlow.show)
clearLEDMatrixButton = Button((ScreenUnit.vw(15), ScreenUnit.vh(7)), Color.WHITE)
clearLEDMatrixButton.border(4, Color.RED)
clearLEDMatrixButton.text("Verwijder", Font.H1, overFlow=overFlow.show)


    
while True:
    APP.eventHandler(pygame.event.get())
    clock.tick(60) # refresh rate of monitor
    APP.maindisplay.fill(Color.BLACK) 
   
    
    COLOR_PICKER_BUTTONS.placeButtons()
    if MATRIX.checkForTouchInGrid():
        APP.requestUpdate
    drawPixelOnLEDMatrixButton.place(ScreenUnit.vw(63), COLOR_PICKER_BUTTONS.getButtonHeight)
    if drawPixelOnLEDMatrixButton.onMouseClick():
        LED_MATRIX.drawMatrixOnPhysicalMatrix(MATRIX.getMatrix)
        
    clearLEDMatrixButton.place(ScreenUnit.vw(82), COLOR_PICKER_BUTTONS.getButtonHeight)
    if clearLEDMatrixButton.onMouseClick():
        LED_MATRIX.erasePhysicalMatrix()
    
    DRAWING_HISTORY.checkForChanges(MATRIX.getMatrix) 
    
    if APP.firstFrame() or APP.updateAvalible:
        MATRIX.drawMatrix((0, 0), ScreenUnit.vh(100)) 
        COLOR_PICKER_BUTTONS.placeButtons()
        
    if APP.keyboardRelease(pygame.K_ESCAPE):
        LED_MATRIX.erasePhysicalMatrix()
        pygame.quit()
        sys.exit()
        
                
        
    
        
        
    
    
def main():
    pass