import gFrame, globalVars
from LEDs.ledMatrix import LEDmatrix
from core.undo_redo import DrawingHistory
from widgets.currentColorIndicator import CurrentColorIndicator

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
    
    undoButton = gFrame.Button(*globalVars.iconButtonTemplate)
    undoButton.icon("drawingButtonsIcons/undo.png")
    redoButton = gFrame.Button(*globalVars.iconButtonTemplate)
    redoButton.icon("drawingButtonsIcons/redo.png")
    colorWheel = gFrame.Button(*globalVars.iconButtonTemplate)
    colorWheel.icon("drawingButtonsIcons/color_wheel.png")
    colorPicker = gFrame.Button(*globalVars.iconButtonTemplate)
    colorPicker.icon("drawingButtonsIcons/color_picker.png")
    colorBucket = gFrame.Button(*globalVars.iconButtonTemplate)
    colorBucket.icon("drawingButtonsIcons/color_bucket.png")
    delete = gFrame.Button(*globalVars.iconButtonTemplate)
    delete.icon("drawingButtonsIcons/delete.png")
    
    def __init__(self, ledMatrix: LEDmatrix) -> None:
        self.LED_MATRIX = ledMatrix
        self.COLOR_PICKER_BUTTONS = ColorButtons(9)
        self.DRAWING_HISTORY = DrawingHistory(self.LED_MATRIX.matrixDimensions)
        self.CURRENT_COLOR_INDICATOR = CurrentColorIndicator()
    
    def place(self):
        if gFrame.Interactions.isMousePressing(gFrame.mouseButton.leftMouseButton):
            # if globals.RPIconnected and drawPixelOnLEDMatrixButton.isClicked():
            #         LED_MATRIX.drawMatrixOnPhysicalMatrix(.getMatrix)
                    
            if self.clearLEDMatrixButton.isClicked():
                if globalVars.RPIconnected:
                    self.LED_MATRIX.erasePhysicalMatrix()
                else:
                    self.LED_MATRIX.eraseMatrix()
                self.DRAWING_HISTORY.resetDrawingHistory()
                globalVars.app.requestUpdate() # TODO nieuwe update van gFrame
                
            if self.undoButton.isClicked():
                self.LED_MATRIX.setMatrix(self.DRAWING_HISTORY.undo())
                globalVars.app.requestUpdate()
            
            if self.redoButton.isClicked():
                self.LED_MATRIX.setMatrix(self.DRAWING_HISTORY.redo())
                globalVars.app.requestUpdate()
                
            globalVars.menuButton.checkIfClicked()
                
                
            if self.colorWheel.isClicked():
                globalVars.currentScreen = globalVars.screens.colorMenu
                return globalVars.app.switchPage()
                
            if self.colorPicker.isClicked():
                globalVars.colorPickerEnabled = not globalVars.colorPickerEnabled
                globalVars.app.requestUpdate()
                
            if self.colorBucket.isClicked():
                self.LED_MATRIX.fillMatrix(globalVars.currentColor)
                globalVars.app.requestUpdate()
                
            if self.delete.isClicked():
                self.LED_MATRIX.fillMatrix(0)
                globalVars.app.requestUpdate()
            
            self.LED_MATRIX.checkForInteraction() 
            
            self.COLOR_PICKER_BUTTONS.checkForButtonClick() 
            
        self.DRAWING_HISTORY.checkForChanges(self.LED_MATRIX.matrix, gFrame.Rect(0, 0, "100vh", "100vh"))  
            
        #* drawing
        if globalVars.app.drawElements():
        
            self.drawPixelOnLEDMatrixButton.place("63vw", "90vh")
            self.clearLEDMatrixButton.place("82vw", "90vh")
            
            if globalVars.colorPickerEnabled:
                self.colorPicker.setBorder(3, gFrame.Color.GREEN)
            else:
                self.colorPicker.setBorder(0, gFrame.Color.BLACK)
            
            globalVars.menuButton.place("93vw", "2vh")
            self.undoButton.place("93vw", "10vh")
            self.redoButton.place("93vw", "18vh")
            self.colorWheel.place("93vw", "26vh")
            self.colorPicker.place("93vw", "34vh")
            self.colorBucket.place("93vw", "42vh")
            self.delete.place("93vw", "50vh")
            self.COLOR_PICKER_BUTTONS.place()
        
            self.CURRENT_COLOR_INDICATOR.place("60vw", "10vh")
        
        
        
            self.LED_MATRIX.place(0, 0) 
        # COLOR_PICKER_BUTTONS.placeButtons()
            
        # DRAWING_HISTORY.checkForChanges(MATRIX.getMatrix, gFrame.pygame.Rect(0, 0, gFrame.ScreenUnit.vh(100), gFrame.ScreenUnit.vh(100))) 
