import gFrame, globalVars
from core.ledMatrix import LEDmatrix

class DrawingScreen:
    drawPixelOnLEDMatrixButton = gFrame.Button(("15vw", "7vh"), gFrame.Color.WHITE, borderRadius=5)
    drawPixelOnLEDMatrixButton.setBorder(4, gFrame.Color.GREEN)
    drawPixelOnLEDMatrixButton.text("Teken!", gFrame.Font.H1, gFrame.Color.BLACK, overFlow=gFrame.overFlow.show)
    clearLEDMatrixButton = gFrame.Button(("15vw", "7vh"), gFrame.Color.WHITE, borderRadius=5)
    clearLEDMatrixButton.setBorder(4, gFrame.Color.RED)
    clearLEDMatrixButton.text("Verwijder", gFrame.Font.H1, gFrame.Color.BLACK, overFlow=gFrame.overFlow.show)
    
    menuButton = gFrame.Button(*globalVars.iconButtonTemplate)
    menuButton.icon("drawingButtonsIcons/menu.png")
    undoButton = gFrame.Button(*globalVars.iconButtonTemplate)
    undoButton.icon("drawingButtonsIcons/undo.png")
    redoButton = gFrame.Button(*globalVars.iconButtonTemplate)
    redoButton.icon("drawingButtonsIcons/redo.png")
    colorWheel = gFrame.Button(*globalVars.iconButtonTemplate)
    colorWheel.icon("drawingButtonsIcons/color_wheel.png")
    colorPicker = gFrame.Button(*globalVars.iconButtonTemplate)
    colorPicker.icon("drawingButtonsIcons/color_picker.png")
    
    def __init__(self, ledMatrix: LEDmatrix) -> None:
        self.ledMatrix = ledMatrix
    
    def place(self):
        # if globals.RPIconnected and drawPixelOnLEDMatrixButton.isClicked():
        #         LED_MATRIX.drawMatrixOnPhysicalMatrix(.getMatrix)
                
        if DrawingScreen.clearLEDMatrixButton.isClicked():
            # if globals.RPIconnected:
            #     LED_MATRIX.erasePhysicalMatrix()
            # else:
            #     MATRIX.eraseMatrix()
            # DRAWING_HISTORY.resetDrawingHistory()
            globalVars.app.updatePending = True # TODO nieuwe update van gFrame
            
        if DrawingScreen.undoButton.isClicked():
            # MATRIX.setMatrix(DRAWING_HISTORY.undo())
            globalVars.app.updatePending = True
        
        if DrawingScreen.redoButton.isClicked():
            # MATRIX.setMatrix(DRAWING_HISTORY.redo())
            globalVars.app.updatePending = True
            
        if DrawingScreen.menuButton.isClicked():
            globalVars.currentScreen = 1
            return globalVars.app.switchPage()
            
        if DrawingScreen.colorWheel.isClicked():
            globalVars.currentScreen = 2
            return globalVars.app.switchPage()
            
        if DrawingScreen.colorPicker.isClicked():
            globalVars.colorPickerEnabled = not globalVars.colorPickerEnabled
            globalVars.app.updatePending = True
        
        # if globalVars.app.updatePending:
        
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
        
        # COLOR_INDICATOR.place(gFrame.ScreenUnit.vw(60), gFrame.ScreenUnit.vh(10))
        
        
        
        self.ledMatrix.place(0, 0) 
        # COLOR_PICKER_BUTTONS.placeButtons()
            
        # DRAWING_HISTORY.checkForChanges(MATRIX.getMatrix, gFrame.pygame.Rect(0, 0, gFrame.ScreenUnit.vh(100), gFrame.ScreenUnit.vh(100))) 
