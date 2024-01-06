import globals
import pygameaddons as app
from undo_redo import DrawingHistory
from matrix import Matrix
from menu import Menu
from presets import Presets
from pixels import Pixels
from menu_button import MenuButton

APP = app.AppConstructor(100, 100, app.pygame.FULLSCREEN, manualUpdating=True)
# APP = AppConstructor(100, 100, manualUpdating=True)
# APP.centerApp()
clock = app.pygame.time.Clock()

APP.setAspectratio(app.ScreenUnit.aspectRatio(app.aspectRatios.ratio16to9), height=app.ScreenUnit.dh(100))

globals.smallButtonTemplate = smallButtonTemplate = ((app.ScreenUnit.vh(7), app.ScreenUnit.vh(7)), app.Color.BLACK)


class ColorButtons:
    def __init__(self, buttonAmount, buttonText) -> None:
        self.buttonSize = (app.ScreenUnit.vw(20), app.ScreenUnit.vh(7))
        self.previousHighlightedButton = globals.currentColor
        self.buttonText = buttonText
        self.buttonList = []
        for index in range(buttonAmount):
            self.buttonList.append(app.Button(self.buttonSize, globals.fieldColors[index], 5)),
            self.buttonList[index].border(6, app.Color.GRAY)
            self.buttonList[index].text(self.buttonText[index], app.Font.H1, app.Text.textColorFromColor(globals.fieldColors[index]))

    
    
    def placeButtons(self):
        self.buttonSize = (app.ScreenUnit.vw(20), app.ScreenUnit.vh(7))
        for index, button in enumerate(self.buttonList):
            button.updateButtonSize(self.buttonSize[0], self.buttonSize[1])
            
            button.place(app.ScreenUnit.vw(70), app.ScreenUnit.vh(1 + 9 * index))
            if button.onMouseClick():
                globals.currentColor = index         
        self.highlightActiveColor(globals.currentColor)
            
    def highlightActiveColor(self, index):
        buttonRect = self.buttonList[index].getButtonAndBorderRect
        app.Drawing.border(5, buttonRect, app.Color.GREEN, 10)
        APP.requestUpdate
        
    @property
    def getButtonHeight(self):
        return app.ScreenUnit.vh(2 + 9 * len(self.buttonList))
        
        


        
        
 
COLOR_BUTTON_TEXT = ["zwart", "rood", "oranje", "geel", "groen", "lichtblauw", "donkerblauw", "paars", "roze", "wit"]
MATRIX = Matrix(16, 16)
COLOR_PICKER_BUTTONS = ColorButtons(len(globals.fieldColors), COLOR_BUTTON_TEXT)
LED_MATRIX = Pixels(globals.pixels, APP, MATRIX)
DRAWING_HISTORY = DrawingHistory(MATRIX.getMatrixDimensions)
MENU = Menu(APP)
PRESETS = Presets(APP)

drawPixelOnLEDMatrixButton = app.Button((app.ScreenUnit.vw(15), app.ScreenUnit.vh(7)), app.Color.WHITE, 5)
drawPixelOnLEDMatrixButton.border(4, app.Color.GREEN)
drawPixelOnLEDMatrixButton.text("Teken!", app.Font.H1, overFlow=app.overFlow.show)
clearLEDMatrixButton = app.Button((app.ScreenUnit.vw(15), app.ScreenUnit.vh(7)), app.Color.WHITE)
clearLEDMatrixButton.border(4, app.Color.RED)
clearLEDMatrixButton.text("Verwijder", app.Font.H1, overFlow=app.overFlow.show)



# TODO add icons
menuButton = MenuButton(*globals.smallButtonTemplate)
undoButton = app.Button(*globals.smallButtonTemplate)
undoIcon = app.Image("button_images/undo.png")
undoIcon.resize(*globals.smallButtonTemplate[0])
redoButton = app.Button(*globals.smallButtonTemplate)
redoIcon = app.Image("button_images/redo.png")
redoButton.resize(*globals.smallButtonTemplate[0])


class Screens:
    def drawing():
        if not APP.firstFrame():
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
                globals.currentScreen = app.screens.menu
                APP.requestUpdate
                return

            DRAWING_HISTORY.checkForChanges(MATRIX.getMatrix, app.pygame.Rect(0, 0, app.ScreenUnit.vh(100), app.ScreenUnit.vh(100))) 
        APP.requestUpdate
        # only draw when needed
        if APP.firstFrame() or APP.updateAvalible:
            APP.maindisplay.fill(app.Color.BLACK) 
            drawPixelOnLEDMatrixButton.place(app.ScreenUnit.vw(63), COLOR_PICKER_BUTTONS.getButtonHeight)
            clearLEDMatrixButton.place(app.ScreenUnit.vw(82), COLOR_PICKER_BUTTONS.getButtonHeight)
            
            menuButton.place(app.ScreenUnit.vw(93), app.ScreenUnit.vh(2))
            undoButtonPosition = (app.ScreenUnit.vw(93), app.ScreenUnit.vh(10))
            undoButton.place(*undoButtonPosition)
            undoIcon.place(*undoButtonPosition)
            redoButtonPosition = (app.ScreenUnit.vw(93), app.ScreenUnit.vh(18))
            redoButton.place(*redoButtonPosition)
            redoIcon.place(*redoButtonPosition)
            
            MATRIX.drawMatrix((0, 0), app.ScreenUnit.vh(100)) 
            COLOR_PICKER_BUTTONS.placeButtons()
        
    def presets():
        PRESETS.place()
    
    def menu():
        MENU.place()
        
        
SCREENS = [Screens.menu, Screens.presets, Screens.drawing]   
        

    
while True:
    APP.eventHandler(app.pygame.event.get())
    clock.tick(60) # refresh rate of monitor
    
    SCREENS[globals.currentScreen.value]() # show current screen

    # for row in MATRIX.getMatrix:
    #     print(row)
    # print("-------------------------------")
    
    # app quit protocol  
    if APP.keyboardRelease(app.pygame.K_ESCAPE):
        LED_MATRIX.erasePhysicalMatrix()
        app.pygame.quit()
        app.sys.exit()
