import gFrame, globalVars
from core.ledMatrix import LEDmatrix
from widgets.menuButton import MenuButton

class ColorButtons:
    def __init__(self, buttonAmount: int) -> None:
        self.buttonSize = (gFrame.ScreenUnit.vw(20), gFrame.ScreenUnit.vh(7))
        self.buttonList = []
        for index in range(buttonAmount):
            self.buttonList.append(gFrame.Button(self.buttonSize, globalVars.fieldColors[index][1], 5)),
            self.buttonList[index].setBorder(6, gFrame.Color.GRAY)
            self.buttonList[index].text(globalVars.fieldColors[index][0], gFrame.Font.H1, gFrame.Text.textColorFromColor(globalVars.fieldColors[index][1]))
    
    def place(self):
        # self.buttonSize = (gFrame.ScreenUnit.vw(20), gFrame.ScreenUnit.vh(7))
        button: gFrame.Button
        for index, button in enumerate(self.buttonList):
            button.place(gFrame.ScreenUnit.vw(70), gFrame.ScreenUnit.vh(1 + 9 * index))
            
            if globalVars.currentColor == index:
                gFrame.Draw.borderFromRect(button.getBorderRect, 5, gFrame.Color.GREEN, 10)
                
    def checkForButtonClick(self):
        button: gFrame.Button
        for index, button in enumerate(self.buttonList):
            if button.isClicked():
                globalVars.colorPickerEnabled = False
                globalVars.currentColor = index
                globalVars.app.requestUpdate()
        
    # @property
    # def getButtonHeight(self):
    #     return gFrame.ScreenUnit.vh(2 + 9 * len(self.buttonList))

class DrawingScreen:
    drawPixelOnLEDMatrixButton = gFrame.Button(("15vw", "7vh"), gFrame.Color.WHITE, borderRadius=5)
    drawPixelOnLEDMatrixButton.setBorder(4, gFrame.Color.GREEN)
    drawPixelOnLEDMatrixButton.text("Teken!", gFrame.Font.H1, gFrame.Color.BLACK, overFlow=gFrame.overFlow.show)
    clearLEDMatrixButton = gFrame.Button(("15vw", "7vh"), gFrame.Color.WHITE, borderRadius=5)
    clearLEDMatrixButton.setBorder(4, gFrame.Color.RED)
    clearLEDMatrixButton.text("Verwijder", gFrame.Font.H1, gFrame.Color.BLACK, overFlow=gFrame.overFlow.show)
    
    menuButton = MenuButton()
    undoButton = gFrame.Button(*globalVars.iconButtonTemplate)
    undoButton.icon("drawingButtonsIcons/undo.png")
    redoButton = gFrame.Button(*globalVars.iconButtonTemplate)
    redoButton.icon("drawingButtonsIcons/redo.png")
    colorWheel = gFrame.Button(*globalVars.iconButtonTemplate)
    colorWheel.icon("drawingButtonsIcons/color_wheel.png")
    colorPicker = gFrame.Button(*globalVars.iconButtonTemplate)
    colorPicker.icon("drawingButtonsIcons/color_picker.png")
    
    def __init__(self, ledMatrix: LEDmatrix) -> None:
        self.LED_MATRIX = ledMatrix
        self.COLOR_PICKER_BUTTONS = ColorButtons(9)
    
    def place(self):
        # if globals.RPIconnected and drawPixelOnLEDMatrixButton.isClicked():
        #         LED_MATRIX.drawMatrixOnPhysicalMatrix(.getMatrix)
                
        if self.clearLEDMatrixButton.isClicked():
            # if globals.RPIconnected:
            #     LED_MATRIX.erasePhysicalMatrix()
            # else:
            #     MATRIX.eraseMatrix()
            # DRAWING_HISTORY.resetDrawingHistory()
            globalVars.app.requestUpdate() # TODO nieuwe update van gFrame
            
        if self.undoButton.isClicked():
            # MATRIX.setMatrix(DRAWING_HISTORY.undo())
            globalVars.app.requestUpdate()
        
        if self.redoButton.isClicked():
            # MATRIX.setMatrix(DRAWING_HISTORY.redo())
            globalVars.app.requestUpdate()
            
        self.menuButton.checkIfClicked()
            
            
        if self.colorWheel.isClicked():
            globalVars.currentScreen = globalVars.screens.colorMenu
            return globalVars.app.switchPage()
            
        if self.colorPicker.isClicked():
            globalVars.colorPickerEnabled = not globalVars.colorPickerEnabled
            globalVars.app.requestUpdate()
        
        self.LED_MATRIX.checkForInteraction() 
        
        self.COLOR_PICKER_BUTTONS.checkForButtonClick()   
        
        #* drawing
        if globalVars.app.drawElements():
        
            self.drawPixelOnLEDMatrixButton.place("63vw", "90vh")
            self.clearLEDMatrixButton.place("82vw", "90vh")
            
            # if globals.colorPickerEnabled:
            #     colorPicker.border(3, gFrame.Color.GREEN)
            # else:
            #     colorPicker.border(0, gFrame.Color.BLACK)
            
            self.menuButton.place("93vw", "2vh")
            self.undoButton.place("93vw", "10vh")
            self.redoButton.place("93vw", "18vh")
            self.colorWheel.place("93vw", "26vh")
            self.colorPicker.place("93vw", "34vh")
            self.COLOR_PICKER_BUTTONS.place()
        
        # COLOR_INDICATOR.place(gFrame.ScreenUnit.vw(60), gFrame.ScreenUnit.vh(10))
        
        
        
            self.LED_MATRIX.place(0, 0) 
        # COLOR_PICKER_BUTTONS.placeButtons()
            
        # DRAWING_HISTORY.checkForChanges(MATRIX.getMatrix, gFrame.pygame.Rect(0, 0, gFrame.ScreenUnit.vh(100), gFrame.ScreenUnit.vh(100))) 
