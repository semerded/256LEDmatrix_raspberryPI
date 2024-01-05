import board, neopixel
from threading import Thread
import globals
from pygameaddons import *
from loading_screen import LoadingScreen
from undo_redo import DrawingHistory
from matrix import Matrix
from menu import Menu

pixels = neopixel.NeoPixel(board.D18, 256, brightness = 0.1)




APP = AppConstructor(100, 100, pygame.FULLSCREEN, manualUpdating=True)
# APP = AppConstructor(100, 100, manualUpdating=True)
# APP.centerApp()
clock = pygame.time.Clock()

APP.setAspectratio(ScreenUnit.aspectRatio(aspectRatios.ratio16to9), height=ScreenUnit.dh(100))

class ColorButtons:
    def __init__(self, buttonAmount, buttonText) -> None:
        self.buttonSize = (ScreenUnit.vw(20), ScreenUnit.vh(7))
        self.previousHighlightedButton = globals.currentColor
        self.buttonText = buttonText
        self.buttonList = []
        for index in range(buttonAmount):
            self.buttonList.append(Button(self.buttonSize, globals.fieldColors[index], 5)),
            self.buttonList[index].border(6, Color.GRAY)
            self.buttonList[index].text(self.buttonText[index], Font.H1, Text.textColorFromColor(self.buttonList[index].getRect))

    
    
    def placeButtons(self):
        self.buttonSize = (ScreenUnit.vw(20), ScreenUnit.vh(7))
        for index, button in enumerate(self.buttonList):
            button.updateButtonSize(self.buttonSize[0], self.buttonSize[1])
            
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
        self.drawingBusy = False
        self.LOADING_SCREEN = LoadingScreen(APP, "Aan het tekenen")
        
    def drawMatrixOnPhysicalMatrix(self, matrix: list[list[int]]):
        self.drawingBusy = True
        Thread(target=self._threadedDrawingOnMatrix, args=(matrix,)).start()
        while self.drawingBusy:
            self.LOADING_SCREEN.place()        
        
    def _threadedDrawingOnMatrix(self, matrix: list[list[int]]):
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
        self.drawingBusy = False
            
    def erasePhysicalMatrix(self):
        MATRIX.eraseMatrix()
        APP.updateDisplay()
        self.pixels.fill(Color.BLACK)
        

        
        
 
COLOR_BUTTON_TEXT = ["zwart", "rood", "oranje", "geel", "groen", "lichtblauw", "donkerblauw", "paars", "roze", "wit"]
MATRIX = Matrix(16, 16)
COLOR_PICKER_BUTTONS = ColorButtons(len(globals.fieldColors), COLOR_BUTTON_TEXT)
LED_MATRIX = Pixels(pixels)
DRAWING_HISTORY = DrawingHistory(MATRIX.getMatrixDimensions)
MENU = Menu(APP)

drawPixelOnLEDMatrixButton = Button((ScreenUnit.vw(15), ScreenUnit.vh(7)), Color.WHITE, 5)
drawPixelOnLEDMatrixButton.border(4, Color.GREEN)
drawPixelOnLEDMatrixButton.text("Teken!", Font.H1, overFlow=overFlow.show)
clearLEDMatrixButton = Button((ScreenUnit.vw(15), ScreenUnit.vh(7)), Color.WHITE)
clearLEDMatrixButton.border(4, Color.RED)
clearLEDMatrixButton.text("Verwijder", Font.H1, overFlow=overFlow.show)

smallButtonTemplate = ((ScreenUnit.vh(7), ScreenUnit.vh(7)), Color.LIGHTGRAY)


# TODO add icons
menuButton = Button(*smallButtonTemplate) # TODO add menu

undoButton = Button(*smallButtonTemplate)

redoButton = Button(*smallButtonTemplate)

class Screens:
    def drawing():
        if MATRIX.checkForTouchInGrid():
            APP.requestUpdate
        
        if drawPixelOnLEDMatrixButton.onMouseClick():
            LED_MATRIX.drawMatrixOnPhysicalMatrix(MATRIX.getMatrix)
            
        if clearLEDMatrixButton.onMouseClick():
            LED_MATRIX.erasePhysicalMatrix()
            DRAWING_HISTORY.resetDrawingHistory()
            
        if undoButton.onMouseClick():
            MATRIX.overWriteMatrix(DRAWING_HISTORY.undo())
            APP.requestUpdate
        
        if redoButton.onMouseClick():
            MATRIX.overWriteMatrix(DRAWING_HISTORY.redo())
            APP.requestUpdate
            
        if menuButton.onMouseClick():
            globals.currentScreen = screens.menu
            APP.requestUpdate
            return

        DRAWING_HISTORY.checkForChanges(MATRIX.getMatrix, pygame.Rect(0, 0, ScreenUnit.vh(100), ScreenUnit.vh(100))) 
        APP.requestUpdate
        # only draw when needed
        if APP.firstFrame() or APP.updateAvalible:
            APP.maindisplay.fill(Color.BLACK) 
            drawPixelOnLEDMatrixButton.place(ScreenUnit.vw(63), COLOR_PICKER_BUTTONS.getButtonHeight)
            clearLEDMatrixButton.place(ScreenUnit.vw(82), COLOR_PICKER_BUTTONS.getButtonHeight)
            
            menuButton.place(ScreenUnit.vw(90), ScreenUnit.vh(2))
            undoButton.place(ScreenUnit.vw(90), ScreenUnit.vh(11))
            redoButton.place(ScreenUnit.vw(90), ScreenUnit.vh(20))
            
            MATRIX.drawMatrix((0, 0), ScreenUnit.vh(100)) 
            COLOR_PICKER_BUTTONS.placeButtons()
        
    def presets():
        print(True)
    
    def menu():
        MENU.place()
        
        
SCREENS = [Screens.menu, Screens.presets, Screens.drawing]   
        

    
while True:
    APP.eventHandler(pygame.event.get())
    clock.tick(60) # refresh rate of monitor
    
    SCREENS[globals.currentScreen.value]() # show current screen
    
    # app quit protocol  
    if APP.keyboardRelease(pygame.K_ESCAPE):
        LED_MATRIX.erasePhysicalMatrix()
        pygame.quit()
        sys.exit()
