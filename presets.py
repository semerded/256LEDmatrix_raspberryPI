from pygameaddons import *
from matrix import Matrix
from copy import deepcopy
from functions import indexedLen
import json

class Presets:
    def __init__(self, APP: AppConstructor) -> None:
        self.APP = APP
        with open("presets.json") as presetsSaveFile:
            PRESETS = json.load(presetsSaveFile)
        self.createMatrixPresetList(PRESETS)
        self.currentMatrixIndex = 0
        self.buttonPrevious = Button((ScreenUnit.vh(10), ScreenUnit.vh(10)), Color.WHITE, 5)
        self.buttonPrevious.text("<", Font.FONT50)
        
        self.buttonNext = Button((ScreenUnit.vh(10), ScreenUnit.vh(10)), Color.WHITE, 5)
        self.buttonNext.text(">", Font.FONT100)
        
    
    def createMatrixPresetList(self, presets):
        self.matrixList = []
        for matrix in presets:
            tempMatrix = Matrix(len(matrix[0]), len(matrix))
            tempMatrix.setMatrix(matrix)
            self.matrixList.append(deepcopy(tempMatrix))
        

    def place(self):
        
        if self.buttonPrevious.onMouseClick():
            self.currentMatrixIndex -= 1
            
        if self.buttonNext.onMouseClick():
            self.currentMatrixIndex += 1
        
        if self.currentMatrixIndex < 0:
            self.currentMatrixIndex = indexedLen(self.matrixList)
            
        if self.currentMatrixIndex > indexedLen(self.matrixList):
            self.currentMatrixIndex = 0
            
        self.APP.requestUpdate # TEMP
        
        if self.APP.firstFrame() or self.APP.updateAvalible:
            self.APP.maindisplay.fill(Color.BLACK)
            self.buttonPrevious.place(ScreenUnit.vw(5), ScreenUnit.vh(45))
            self.buttonNext.place(ScreenUnit.vw(5), ScreenUnit.vh(45))
            self.matrixList[self.currentMatrixIndex].drawMatrix((ScreenUnit.vw(50) - (ScreenUnit.vh(95) / 2), ScreenUnit.vh(2.5)), ScreenUnit.vh(95))
            
            pygame.display.update()