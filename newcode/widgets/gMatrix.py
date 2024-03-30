import gFrame, globalVars
from core.matrix import Matrix
import math

class gMatrix(Matrix):
    mouseGridpos = [0, 0]
    
    def __init__(self, colums: int, rows: int, matrixWidth: float, matrixHeight: float) -> None:
        super().__init__(colums, rows)
        self.matrixSize = gFrame.ScreenUnit.convertMultipleUnits(matrixWidth, matrixHeight)
        self.matrixUnitSize = [self.matrixSize[0] / colums, self.matrixSize[1] / rows]
        self.rect = gFrame.Rect.placeHolder()
        
    def place(self, left: float, top: float):
        self.rect = gFrame.Rect((left, top), self.matrixSize)
        currentMatrixPosition = [0, 0]

        for row in self.matrix:
            for column in row:
                unitRect = gFrame.Rect(left + (self.matrixUnitSize[0] * currentMatrixPosition[0]), top + (self.matrixUnitSize[1] * currentMatrixPosition[1]), self.matrixUnitSize[0], self.matrixUnitSize[1])
                if column != 0:
                    gFrame.Draw.rectangleFromRect(unitRect, globalVars.fieldColors[column][1])
                gFrame.Draw.borderFromRect(unitRect, 1, gFrame.Color.LIGHT_GRAY)
                currentMatrixPosition[0] += 1
            currentMatrixPosition[1] += 1
            currentMatrixPosition[0] = 0
            
    def checkForInteraction(self):
        if gFrame.Interactions.isMousePressingInRect(gFrame.mouseButton.leftMouseButton, self.rect):
            mousePos = gFrame.pygame.mouse.get_pos()
            mousePos = (mousePos[0] - self.rect.x, mousePos[1] - self.rect.y)
            if (mouseGridX := math.ceil(mousePos[0] / self.matrixUnitSize[0])) > 0 and (mouseGridY := math.ceil(mousePos[1] / self.matrixUnitSize[1])) > 0:
                self.mouseGridpos[0] = mouseGridX
                self.mouseGridpos[1] = mouseGridY
                if globalVars.colorPickerEnabled:
                    globalVars.currentColor = self.matrix[self.mouseGridpos[1] - 1][self.mouseGridpos[0] - 1]
                    globalVars.colorPickerEnabled = False   
                else:
                    self.matrix[self.mouseGridpos[1] - 1][self.mouseGridpos[0] - 1] = globalVars.currentColor
                gFrame.Updating.requestUpdate()
    
    def fillMatrix(self, color):
        self.matrix = Matrix.createNewMatrix(self.matrixDimensions[0], self.matrixDimensions[1], color)
