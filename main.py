import threading, math
import board, neopixel
from enum import Enum


#temp voor pg lib te verkrijgen
import sys
sys.path.append("../256LEDmatrix_raspberryPI/pygameAddons")
from pygameaddons import *

pixels = neopixel.NeoPixel(board.D18, 256, brightness = 0.1)



APP = AppConstructor(100, 100, pygame.FULLSCREEN, manualUpdating=True)
APP.centerApp()
# APP.setRelativeFullscreen
clock = pygame.time.Clock()

APP.setAspectratio(ScreenUnit.aspectRatio(aspectRatios.ratio16to9), height=ScreenUnit.dh(90))


    
fieldColors = [Color.BLACK, Color.RED, Color.ORANGE, Color.YELLOW, Color.GREEN, Color.LIGHTBLUE, Color.BLUE, Color.PURPLE, Color.PINK, Color.WHITE]
    

class Matrix:
    def __init__(self, matrixLength: int, matrixHeight: int) -> None:
        self.matrix = Matrix.makeEmptyMatrix(matrixLength, matrixHeight)
        self.sideMeasurement = 0
        self.matrixPosition = (0, 0)
        self.mouseGridpos = [0, 0]
        self.previousMouseGridPos = [0, 0]
        self.matrixRect = pygame.Rect(0, 0, 0, 0)
    # static
    def makeEmptyMatrix(length, height):
        matrix = []
        for i in range(height):
            matrixRow = []
            for j in range(length):
                matrixRow.append(0)
            matrix.append(matrixRow)
        return matrix
    
    def checkIfMatrix(possibleMatrix):
        isMatrix = True
        lenghtOfMatrixRow = len(possibleMatrix)
        if lenghtOfMatrixRow >= 2:
            for matrixColumn in range(lenghtOfMatrixRow):
                if len(matrixColumn) < 2:
                    isMatrix = False
        return isMatrix
     
    # instance               
    def drawMatrixGrid(self):
        currentGridPosition = [0,0]
        
        for row in self.matrix:
            for column in row:
                gridUnitRect = pygame.Rect(self.matrixPosition[0] + self.gridUnitSide * currentGridPosition[0], self.matrixPosition[1] + self.gridUnitSide * currentGridPosition[1], self.gridUnitSide, self.gridUnitSide)
                currentGridPosition[0] += 1
                Drawing.border(1, gridUnitRect, Color.LIGHTGRAY)
            currentGridPosition[1] += 1
            currentGridPosition[0] = 0
        self.matrixRect = pygame.Rect(self.matrixPosition[0], self.matrixPosition[1], self.gridUnitSide * self.getMatrixDimensions[0], self.gridUnitSide * self.getMatrixDimensions[1])
                
    def drawMatrixItems(self):
        currentGridPosition = [0,0]
        for row in self.matrix:
            for column in row:
                if column != 0:
                    matrixUnitRect = pygame.Rect(self.matrixPosition[0] + self.gridUnitSide * currentGridPosition[0], self.matrixPosition[1] + self.gridUnitSide * currentGridPosition[1], self.gridUnitSide, self.gridUnitSide)
                    Drawing.rectangleFromRect(matrixUnitRect, fieldColors[column])
                currentGridPosition[0] += 1
            currentGridPosition[1] += 1
            currentGridPosition[0] = 0
    
    def drawMatrix(self, position, sideMeasurement: int):
        self.matrixPosition = position
        
        self.sideMeasurement = sideMeasurement
        matrixWidth, matrixHeight = self.getMatrixDimensions # TODO! not reproducable
        self.gridUnitSide = self.sideMeasurement / matrixHeight
        self.drawMatrixGrid()
        self.drawMatrixItems()
        
    def checkForTouchInGrid(self):
        if Interactions.isHoldingInRect(self.matrixRect, mouseButton.leftMouseButton.value):
            self.findClickedGridUnit()
        else:
            self.previousMouseGridPos[0] = self.mouseGridpos[0]
            self.previousMouseGridPos[1] = self.mouseGridpos[1]
            
    def eraseMatrix(self):
        self.matrix = Matrix.makeEmptyMatrix(self.getMatrixDimensions[0], self.getMatrixDimensions[1])
            
            
    def findClickedGridUnit(self):
        mousePos = pygame.mouse.get_pos()
        mousePos = (mousePos[0] - self.matrixPosition[0], mousePos[1] - self.matrixPosition[1])
        self.mouseGridpos[0] = math.ceil(mousePos[0] / self.gridUnitSide)
        self.mouseGridpos[1] = math.ceil(mousePos[1] / self.gridUnitSide)
        if self.mouseGridpos[0] != self.previousMouseGridPos[0] or self.mouseGridpos[1] != self.previousMouseGridPos[1]:
            self.matrix[self.mouseGridpos[1] - 1][self.mouseGridpos[0] - 1] = currentColor
            self.drawMatrix(self.matrixPosition, self.sideMeasurement)
            self.previousMouseGridPos[0] = self.mouseGridpos[0]
            self.previousMouseGridPos[1] = self.mouseGridpos[1]
            APP.setUpdatePending
                
    @property
    def getMatrixDimensions(self):
        """
        returns the size of the matrix as tuple(size_Xaxis, size_Yaxis)
        """
        return len(self.matrix[0]), len(self.matrix)
    
    @property
    def getMatrix(self):
        return self.matrix
        
        
currentColor = 0

class ColorButtons:
    def __init__(self, buttonAmount) -> None:
        self.buttonSize = (ScreenUnit.vw(10), ScreenUnit.vh(7))
        self.previousHighlightedButton = currentColor
        self.buttonList = []
        for index in range(buttonAmount):
            self.buttonList.append(Button(self.buttonSize, fieldColors[index], 5)),
            self.buttonList[index].border(6, Color.GRAY)
    
    
    def placeButtons(self):
        global currentColor
        self.buttonSize = (ScreenUnit.vw(10), ScreenUnit.vh(7))
        counter = 0
        for index, button in enumerate(self.buttonList):
            button.updateButtonSize(self.buttonSize[0], self.buttonSize[1])
            button.place(ScreenUnit.vw(80), ScreenUnit.vh(1 + 9 * counter))
            if button.onMouseClick():
                currentColor = index         
            counter+=1
            if index == currentColor and self.previousHighlightedButton != currentColor:
                self.highlightActiveColor(index)
                self.previousHighlightedButton = currentColor
            
    def highlightActiveColor(self, index):
        buttonRect = self.buttonList[index].getButtonAndBorderRect
        Drawing.border(5, buttonRect, Color.GREEN, 10)
        APP.setUpdatePending
        
    @property
    def getButtonHeight(self):
        return ScreenUnit.vh(2 + 9 * len(self.buttonList))
        
        
class Pixels:
    def __init__(self, pixels) -> None:
        self.pixels = pixels
        
    def drawMatrixOnPhysicalMatrix(self, matrix: list[list]):
        ledCounter = 0
        reverse = True
        for row in matrix:
            if reverse:
                for column in reversed(row):
                    self.pixels[ledCounter] = fieldColors[column]                 
                    ledCounter += 1
            else:
                for column in row:
                    self.pixels[ledCounter] = fieldColors[column]
                    ledCounter += 1
            reverse = not reverse
 
    
MATRIX = Matrix(16, 16)
COLOR_PICKER_BUTTONS = ColorButtons(10)
LED_MATRIX = Pixels(pixels) # TODO change name

drawPixelOnMatrixButton = Button((ScreenUnit.vw(10), ScreenUnit.vh(7)), Color.WHITE, 5)
drawPixelOnMatrixButton.border(4, Color.GRAY)


    
while True:
    APP.eventHandler(pygame.event.get())
    clock.tick(60)
    APP.maindisplay.fill(Color.BLACK) 
   
    
    COLOR_PICKER_BUTTONS.placeButtons()
    MATRIX.checkForTouchInGrid()
    drawPixelOnMatrixButton.place(ScreenUnit.vw(75), COLOR_PICKER_BUTTONS.getButtonHeight)
    
    if drawPixelOnMatrixButton.onMouseClick():
        LED_MATRIX.drawMatrixOnPhysicalMatrix(MATRIX.getMatrix)
        
    
    if APP.firstFrame() or APP.updateAvalible:
        MATRIX.drawMatrix((0, 0), ScreenUnit.vh(100)) 
        COLOR_PICKER_BUTTONS.placeButtons()
        
        
    
    
def main():
    pass