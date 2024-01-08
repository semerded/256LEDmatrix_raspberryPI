import pygameaddons as app
from matrix import Matrix
from pixels import Pixels
from menu_button import MenuButton
from copy import deepcopy
from functions import indexedLen
import json, globals

class Presets:
    def __init__(self, APP: app.AppConstructor) -> None:
        self.APP = APP
        self.APP.requestUpdate
        with open("presets.json") as presetsSaveFile:
            PRESETS = json.load(presetsSaveFile)
        self.createMatrixPresetList(PRESETS)
        self.currentMatrixIndex = 0
        
        self.buttonPrevious = app.Button((app.ScreenUnit.vh(10), app.ScreenUnit.vh(10)), app.Color.WHITE, 5)
        self.buttonPrevious.text("<", app.Font.FONT50)
        self.buttonNext = app.Button((app.ScreenUnit.vh(10), app.ScreenUnit.vh(10)), app.Color.WHITE, 5)
        self.buttonNext.text(">", app.Font.FONT50)
        
        self.drawPixelOnLEDMatrixButton = app.Button((app.ScreenUnit.vw(18), app.ScreenUnit.vh(10)), app.Color.GREEN, 5)
        self.drawPixelOnLEDMatrixButton.text("Tekenen!", app.Font.H1)
        
        self.menuButton = MenuButton(*globals.smallButtonTemplate)
        if globals.RPIconnected:
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
                globals.currentScreen = app.screens.menu
                return self.APP.switchScreen()
                
            if globals.RPIconnected and self.drawPixelOnLEDMatrixButton.onMouseClick():
                self.PIXELS.drawMatrixOnPhysicalMatrix(self.matrixList[self.currentMatrixIndex].getMatrix)
            
            self.APP.requestUpdate # TEMP
        
        if self.APP.firstFrame() or self.APP.updateAvalible:
            self.APP.maindisplay.fill(app.Color.BLACK)
            self.buttonPrevious.place(app.ScreenUnit.vw(5), app.ScreenUnit.vh(45))
            self.buttonNext.place(app.ScreenUnit.vw(95) - app.ScreenUnit.vh(10), app.ScreenUnit.vh(45))
            self.menuButton.place(app.ScreenUnit.vw(93), app.ScreenUnit.vh(2))
            self.drawPixelOnLEDMatrixButton.place(app.ScreenUnit.vw(80), app.ScreenUnit.vh(80))
            self.matrixList[self.currentMatrixIndex].drawMatrix((app.ScreenUnit.vw(50) - (app.ScreenUnit.vh(95) / 2), app.ScreenUnit.vh(2.5)), app.ScreenUnit.vh(95))
            
            app.pygame.display.update()
            