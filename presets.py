from pygameaddons import *
from matrix import Matrix
from pixels import Pixels
from menu_button import MenuButton
from copy import deepcopy
from functions import indexedLen
import json, globals

class Presets:
    def __init__(self, APP: AppConstructor) -> None:
        self.APP = APP
        self.APP.requestUpdate
        with open("presets.json") as presetsSaveFile:
            PRESETS = json.load(presetsSaveFile)
        self.createMatrixPresetList(PRESETS)
        self.currentMatrixIndex = 0
        
        self.buttonPrevious = Button((ScreenUnit.vh(10), ScreenUnit.vh(10)), Color.WHITE, 5)
        self.buttonPrevious.text("<", Font.FONT50)
        self.buttonNext = Button((ScreenUnit.vh(10), ScreenUnit.vh(10)), Color.WHITE, 5)
        self.buttonNext.text(">", Font.FONT50)
        
        self.drawPixelOnLEDMatrixButton = Button((ScreenUnit.vw(18), ScreenUnit.vh(10)), Color.GREEN, 5)
        self.drawPixelOnLEDMatrixButton.text("Tekenen!", Font.H1)
        
        self.menuButton = MenuButton(*globals.smallButtonTemplate)
        
        self.PIXELS = Pixels(globals.pixels, self.APP, self.matrixList[0])

    
    def createMatrixPresetList(self, presets):
        self.matrixList = []
        for matrix in presets:
            tempMatrix = Matrix(len(matrix[0]), len(matrix))
            tempMatrix.setMatrix(matrix)
            self.matrixList.append(deepcopy(tempMatrix))
        

    def place(self):
        if not self.APP.firstFrame():
            if self.buttonPrevious.onMouseClick():
                self.currentMatrixIndex -= 1
                if self.currentMatrixIndex < 0:
                    self.currentMatrixIndex = indexedLen(self.matrixList)
                
            if self.buttonNext.onMouseClick():
                self.currentMatrixIndex += 1
                if self.currentMatrixIndex > indexedLen(self.matrixList):
                    self.currentMatrixIndex = 0
                    
            if self.menuButton.onMouseClick():
                globals.currentScreen = screens.menu
                self.APP.requestUpdate
                return
                
            if self.drawPixelOnLEDMatrixButton.onMouseClick():
                self.PIXELS.drawMatrixOnPhysicalMatrix(self.matrixList[self.currentMatrixIndex].getMatrix)
            
        self.APP.requestUpdate # TEMP
        
        if self.APP.firstFrame() or self.APP.updateAvalible:
            self.APP.maindisplay.fill(Color.BLACK)
            self.buttonPrevious.place(ScreenUnit.vw(5), ScreenUnit.vh(45))
            self.buttonNext.place(ScreenUnit.vw(95) - ScreenUnit.vh(10), ScreenUnit.vh(45))
            self.menuButton.place(ScreenUnit.vw(93), ScreenUnit.vh(2))
            self.drawPixelOnLEDMatrixButton.place(ScreenUnit.vw(80), ScreenUnit.vh(80))
            self.matrixList[self.currentMatrixIndex].drawMatrix((ScreenUnit.vw(50) - (ScreenUnit.vh(95) / 2), ScreenUnit.vh(2.5)), ScreenUnit.vh(95))
            
            pygame.display.update()
            