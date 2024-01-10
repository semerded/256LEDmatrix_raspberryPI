import globals
import pygameaddons as app
from undo_redo import DrawingHistory
from matrix import Matrix
from menu import Menu
from presets import Presets
from pixels import Pixels
from menu_button import MenuButton
from color_menu import ColorMenu
from current_color_indicator import CurrentColorIndicator

APP = app.AppConstructor(app.userScreenWidth, app.userScreenHeight, app.pygame.FULLSCREEN, manualUpdating=True)
# APP = AppConstructor(100, 100, manualUpdating=True)
# APP.centerApp()
clock = app.pygame.time.Clock()

APP.setAspectratio(app.ScreenUnit.aspectRatio(app.aspectRatios.ratio16to9), height=app.ScreenUnit.dh(100))

globals.smallButtonTemplate = smallButtonTemplate = ((app.ScreenUnit.vh(7), app.ScreenUnit.vh(7)), app.Color.BLACK)


class ColorButtons:
    def __init__(self, buttonAmount, buttonText) -> None:
        self.buttonSize = (app.ScreenUnit.vw(20), app.ScreenUnit.vh(7))
        self.buttonText = buttonText
        self.buttonList = []
        for index in range(buttonAmount):
            self.buttonList.append(app.Button(self.buttonSize, globals.fieldColors[index], 5)),
            self.buttonList[index].border(6, app.Color.GRAY)
            self.buttonList[index].text(self.buttonText[index], app.Font.H1, app.Text.textColorFromColor(globals.fieldColors[index]))

    def checkForButtonClick(self):
        for index, button in enumerate(self.buttonList):
            if button.onMouseClick():
                globals.colorPickerEnabled = False
                globals.currentColor = index 
                APP.requestUpdate
    
    def placeButtons(self):
        # self.buttonSize = (app.ScreenUnit.vw(20), app.ScreenUnit.vh(7))
        for index, button in enumerate(self.buttonList):
            button.updateButtonSize(self.buttonSize[0], self.buttonSize[1])
            
            button.place(app.ScreenUnit.vw(70), app.ScreenUnit.vh(1 + 9 * index))
                    
        self.highlightActiveColor(globals.currentColor)
            
    def highlightActiveColor(self, index):
        try:
            buttonRect = self.buttonList[index].getButtonAndBorderRect
            app.Drawing.border(5, buttonRect, app.Color.GREEN, 10)
            APP.requestUpdate
        except:
            pass
        
    @property
    def getButtonHeight(self):
        return app.ScreenUnit.vh(2 + 9 * len(self.buttonList))
        

MATRIX = Matrix(16, 16)
COLOR_PICKER_BUTTONS = ColorButtons(10, globals.COLOR_BUTTON_TEXT)

if globals.RPIconnected:
    LED_MATRIX = Pixels(globals.pixels, APP, MATRIX)
DRAWING_HISTORY = DrawingHistory(MATRIX.getMatrixDimensions)
MENU = Menu(APP)
PRESETS = Presets(APP)
COLOR_MENU = ColorMenu(APP)
COLOR_INDICATOR = CurrentColorIndicator(APP)

drawPixelOnLEDMatrixButton = app.Button((app.ScreenUnit.vw(15), app.ScreenUnit.vh(7)), app.Color.WHITE, 5)
drawPixelOnLEDMatrixButton.border(4, app.Color.GREEN)
drawPixelOnLEDMatrixButton.text("Teken!", app.Font.H1, overFlow=app.overFlow.show)
clearLEDMatrixButton = app.Button((app.ScreenUnit.vw(15), app.ScreenUnit.vh(7)), app.Color.WHITE)
clearLEDMatrixButton.border(4, app.Color.RED)
clearLEDMatrixButton.text("Verwijder", app.Font.H1, overFlow=app.overFlow.show)

menuButton = MenuButton(*globals.smallButtonTemplate)
undoButton = app.Button(*globals.smallButtonTemplate)
undoButton.icon("button_images/undo.png")
redoButton = app.Button(*globals.smallButtonTemplate)
redoButton.icon("button_images/redo.png")
colorWheel = app.Button(*globals.smallButtonTemplate)
colorWheel.icon("button_images/color_wheel.png")
colorPicker = app.Button(*globals.smallButtonTemplate)
colorPicker.icon("button_images/color_picker.png")

falseMatrixTouch = False # to make sure nothing is drawn when switching screens

class Screens:
    def drawing():
        global falseMatrixTouch
        if not APP.firstFrame():
            if not falseMatrixTouch and MATRIX.checkForTouchInGrid():
                APP.requestUpdate
                
            COLOR_PICKER_BUTTONS.checkForButtonClick()
            
            if globals.RPIconnected and drawPixelOnLEDMatrixButton.onMouseClick():
                LED_MATRIX.drawMatrixOnPhysicalMatrix(MATRIX.getMatrix)
                
            if clearLEDMatrixButton.onMouseClick():
                if globals.RPIconnected:
                    LED_MATRIX.erasePhysicalMatrix()
                else:
                    MATRIX.eraseMatrix()
                DRAWING_HISTORY.resetDrawingHistory()
                APP.requestUpdate
                
            if undoButton.onMouseClick():
                MATRIX.setMatrix(DRAWING_HISTORY.undo())
                APP.requestUpdate
            
            if redoButton.onMouseClick():
                MATRIX.setMatrix(DRAWING_HISTORY.redo())
                APP.requestUpdate
                
            if menuButton.onMouseClick():
                globals.currentScreen = app.screens.menu
                return APP.switchScreen()
                
            if colorWheel.onMouseClick():
                globals.currentScreen = app.screens.colorMenu
                return APP.switchScreen()
                
            if colorPicker.onMouseClick():
                globals.colorPickerEnabled = not globals.colorPickerEnabled
                APP.requestUpdate
              
              
            DRAWING_HISTORY.checkForChanges(MATRIX.getMatrix, app.pygame.Rect(0, 0, app.ScreenUnit.vh(100), app.ScreenUnit.vh(100))) 
        else:
            falseMatrixTouch = True

        if falseMatrixTouch and app.Interactions.isReleased(app.mouseButton.leftMouseButton):
            falseMatrixTouch = False
        
        # only draw when needed
        if APP.firstFrame() or APP.updateAvalible:
            APP.maindisplay.fill(app.Color.BLACK) 
            drawPixelOnLEDMatrixButton.place(app.ScreenUnit.vw(63), COLOR_PICKER_BUTTONS.getButtonHeight)
            clearLEDMatrixButton.place(app.ScreenUnit.vw(82), COLOR_PICKER_BUTTONS.getButtonHeight)
            
            if globals.colorPickerEnabled:
                colorPicker.border(3, app.Color.GREEN)
            else:
                colorPicker.border(0, app.Color.BLACK)
            
            menuButton.place(app.ScreenUnit.vw(93), app.ScreenUnit.vh(2))
            undoButton.place(app.ScreenUnit.vw(93), app.ScreenUnit.vh(10))
            redoButton.place(app.ScreenUnit.vw(93), app.ScreenUnit.vh(18))
            colorWheel.place(app.ScreenUnit.vw(93), app.ScreenUnit.vh(26))
            colorPicker.place(app.ScreenUnit.vw(93), app.ScreenUnit.vh(34))
            
            COLOR_INDICATOR.place(app.ScreenUnit.vw(60), app.ScreenUnit.vh(10))
            
            
            
            MATRIX.drawMatrix((0, 0), app.ScreenUnit.vh(100)) 
            COLOR_PICKER_BUTTONS.placeButtons()
        
    def presets():
        PRESETS.place()
    
    def menu():
        MENU.place()
        
    def colorMenu():
        COLOR_MENU.place()
        
        
SCREENS = [Screens.menu, Screens.presets, Screens.drawing, Screens.colorMenu]   
        

    
while True:
    APP.eventHandler(app.pygame.event.get())
    clock.tick(60) # refresh rate of monitor
    
    SCREENS[globals.currentScreen.value]() # show current screen

    # for row in MATRIX.getMatrix:
    #     print(row)
    # print("-------------------------------")
    
    # app quit protocol  
    if APP.keyboardRelease(app.pygame.K_ESCAPE):
        if globals.RPIconnected:
            LED_MATRIX.erasePhysicalMatrix()
        app.pygame.quit()
        app.sys.exit()
