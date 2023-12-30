from pygameaddons import *
import globals
import math

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
                    Drawing.rectangleFromRect(matrixUnitRect, globals.fieldColors[column])
                currentGridPosition[0] += 1
            currentGridPosition[1] += 1
            currentGridPosition[0] = 0
    
    def drawMatrix(self, position, sideMeasurement: int):
        self.matrixPosition = position
        
        self.sideMeasurement = sideMeasurement
        matrixWidth, matrixHeight = self.getMatrixDimensions # TODO! not reproducable
        self.gridUnitSide = self.sideMeasurement / matrixHeight
        self.drawMatrixItems()
        self.drawMatrixGrid()
        
    def checkForTouchInGrid(self) -> bool:
        if Interactions.isHoldingInRect(self.matrixRect, mouseButton.leftMouseButton.value):
            return self.findClickedGridUnit()
        else:
            self.previousMouseGridPos[0] = self.mouseGridpos[0]
            self.previousMouseGridPos[1] = self.mouseGridpos[1]
            return False
            
    def eraseMatrix(self):
        self.matrix = Matrix.makeEmptyMatrix(self.getMatrixDimensions[0], self.getMatrixDimensions[1])
        
    def overWriteMatrix(self, newMatrix):
        self.matrix = newMatrix            
            
    def findClickedGridUnit(self) -> bool: # return value for screen updating
        mousePos = pygame.mouse.get_pos()
        mousePos = (mousePos[0] - self.matrixPosition[0], mousePos[1] - self.matrixPosition[1])
        self.mouseGridpos[0] = math.ceil(mousePos[0] / self.gridUnitSide)
        self.mouseGridpos[1] = math.ceil(mousePos[1] / self.gridUnitSide)
        if self.mouseGridpos[0] != self.previousMouseGridPos[0] or self.mouseGridpos[1] != self.previousMouseGridPos[1]:
            self.matrix[self.mouseGridpos[1] - 1][self.mouseGridpos[0] - 1] = globals.currentColor
            self.drawMatrix(self.matrixPosition, self.sideMeasurement)
            self.previousMouseGridPos[0] = self.mouseGridpos[0]
            self.previousMouseGridPos[1] = self.mouseGridpos[1]
            return True
        return False
                
    @property
    def getMatrixDimensions(self):
        """
        returns the size of the matrix as tuple(size_Xaxis, size_Yaxis)
        """
        return len(self.matrix[0]), len(self.matrix)
    
    @property
    def getMatrix(self):
        return self.matrix
        