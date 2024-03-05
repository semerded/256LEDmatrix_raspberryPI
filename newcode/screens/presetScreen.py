import gFrame, json, globalVars
from core.matrix import Matrix
from core.ledMatrix import LEDmatrix
from widgets.menuButton import MenuButton
from copy import deepcopy

class PresetScreen:
    buttonPrevious = gFrame.Button(("10vh", "10vh"), gFrame.Color.WHITE, 5)
    buttonPrevious.text("<", gFrame.Font.FONT50, gFrame.Color.BLACK, bold=True)
    
    buttonNext = gFrame.Button(("10vh", "10vh"), gFrame.Color.WHITE, 5)
    buttonNext.text(">", gFrame.Font.FONT50, gFrame.Color.BLACK, bold=True)
    
    drawPixelOnLEDMatrixButton = gFrame.Button(("18vw", "10vh"), gFrame.Color.GREEN, 5)
    drawPixelOnLEDMatrixButton.text("Tekenen!", gFrame.Font.FONT50, gFrame.Color.BLACK)
    
    menuButton = MenuButton()
    
    currentMatrixIndex = 0
    reloadMatrix = True
    
    def __init__(self, LEDmatrix: LEDmatrix) -> None:
        with open("presets.json") as fp:
            self._createMatrixPresetList(json.load(fp))
        self.LED_MATRIX = LEDmatrix
        self.LED_MATRIX.setMatrix(deepcopy(self.matrixList[self.currentMatrixIndex].matrix))
        
    def _createMatrixPresetList(self, presets):
        self.matrixList = []
        for matrix in presets:
            tempMatrix = Matrix(len(matrix[0]), len(matrix))
            tempMatrix.setMatrix(deepcopy(matrix))
            self.matrixList.append(tempMatrix)
        
    def place(self):
        if self.reloadMatrix:
            self.LED_MATRIX.setMatrix(deepcopy(self.matrixList[self.currentMatrixIndex].matrix))
            self.reloadMatrix = False
            
        if self.buttonPrevious.isClicked():
            self.currentMatrixIndex -= 1
            if self.currentMatrixIndex < 0:
                self.currentMatrixIndex = len(self.matrixList) - 1
            self.LED_MATRIX.setMatrix(deepcopy(self.matrixList[self.currentMatrixIndex].matrix))
            globalVars.app.requestUpdate()
            
        if self.buttonNext.isClicked():
            self.currentMatrixIndex += 1
            if self.currentMatrixIndex > len(self.matrixList) - 1:
                self.currentMatrixIndex = 0
            self.LED_MATRIX.setMatrix(deepcopy(self.matrixList[self.currentMatrixIndex].matrix))
            globalVars.app.requestUpdate()
        
        if self.menuButton.checkIfClicked():
            self.reloadMatrix = True
            return
        
        if globalVars.app.drawElements():
            self.buttonPrevious.place("5vw", "45vh")
            self.buttonNext.place(gFrame.ScreenUnit.vw(95) - gFrame.ScreenUnit.vh(10), "45vh")
            
            self.LED_MATRIX.place(gFrame.ScreenUnit.vw(50) - (gFrame.ScreenUnit.vh(50)), 0)
            
            self.menuButton.place("93vw", "2vh")
            
            self.drawPixelOnLEDMatrixButton.place("80vw", "80vh")
