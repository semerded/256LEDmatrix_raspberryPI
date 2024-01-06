import globals
from pygameaddons import *
from undo_redo import DrawingHistory
from matrix import Matrix
from menu import Menu
from presets import Presets
from pixels import Pixels






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
            self.buttonList[index].text(self.buttonText[index], Font.H1, Text.textColorFromColor(globals.fieldColors[index]))

    
    
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
        
        


        
        
 
COLOR_BUTTON_TEXT = ["zwart", "rood", "oranje", "geel", "groen", "lichtblauw", "donkerblauw", "paars", "roze", "wit"]
MATRIX = Matrix(16, 16)
COLOR_PICKER_BUTTONS = ColorButtons(len(globals.fieldColors), COLOR_BUTTON_TEXT)
LED_MATRIX = Pixels(globals.pixels)
DRAWING_HISTORY = DrawingHistory(MATRIX.getMatrixDimensions)
MENU = Menu(APP)
PRESETS = Presets(APP)

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
            MATRIX.setMatrix(DRAWING_HISTORY.undo())
            APP.requestUpdate
        
        if redoButton.onMouseClick():
            MATRIX.setMatrix(DRAWING_HISTORY.redo())
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
        PRESETS.place()
    
    def menu():
        MENU.place()
        
        
SCREENS = [Screens.menu, Screens.presets, Screens.drawing]   
        

    
while True:
    APP.eventHandler(pygame.event.get())
    clock.tick(60) # refresh rate of monitor
    
    SCREENS[globals.currentScreen.value]() # show current screen

    for row in MATRIX.getMatrix:
        print(row)
    print("-------------------------------")
    
    # app quit protocol  
    if APP.keyboardRelease(pygame.K_ESCAPE):
        LED_MATRIX.erasePhysicalMatrix()
        pygame.quit()
        sys.exit()
