from pygameaddons import *
from matrix import Matrix
from copy import deepcopy
from math import ceil
import json

class Presets:
    def __init__(self, APP: AppConstructor) -> None:
        self.APP = APP
        with open("presets.json") as presetsSaveFile:
            PRESETS = json.load(presetsSaveFile)
        self.createMatrixPresetList(PRESETS)
        
    
    def createMatrixPresetList(self, presets):
        self.matrixList = []
        for matrix in presets:
            tempMatrix = Matrix(len(matrix[0]), len(matrix))
            tempMatrix.setMatrix(matrix)
            self.matrixList.append(deepcopy(tempMatrix))
        self.maxScrollValue = ScreenUnit.vw(50) * ceil(len(self.matrixList) / 2)
        self.scroller = Scroll(self.maxScrollValue, scrollSpeed.medium)
        self.scrollValue = 0
        

    def place(self):
        
        self.scrollValue = self.scroller.scrollController()
        
        if Interactions.isScrolled():
            self.APP.requestUpdate
            
        # self.APP.requestUpdate # TEMP
        
        if self.APP.firstFrame() or self.APP.updateAvalible:
            self.APP.maindisplay.fill(Color.BLACK)
            
            secondPosition = False
            for index, matrix in enumerate(self.matrixList):
                xPos = ScreenUnit.vw(3) if not secondPosition else ScreenUnit.vw(52)
                yPos = ScreenUnit.vw(50) + ceil(index / 2)
                matrix.draw((xPos, yPos), ScreenUnit.vw(45))
                secondPosition = not secondPosition
            
            pygame.display.update()