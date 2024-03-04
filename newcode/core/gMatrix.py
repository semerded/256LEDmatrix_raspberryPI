import gFrame, globalVars
from core.matrix import Matrix

class gMatrix(Matrix):
    def __init__(self, colums: int, rows: int, matrixWidth: float, matrixHeight: float) -> None:
        super().__init__(colums, rows)
        self.matrixSize = gFrame.ScreenUnit.convertMultipleUnits(matrixWidth, matrixHeight)
        self.matrixUnitSize = [self.matrixSize[0] / colums, self.matrixSize[1] / rows]
        
    def place(self, left: float, top: float):
        self.rect = gFrame.Rect((left, top), self.matrixSize)
        currentMatrixPosition = [0, 0]

        for row in self.matrix:
            for column in row:
                unitRect = gFrame.Rect(left + (self.matrixUnitSize[0] * currentMatrixPosition[0]), top + (self.matrixUnitSize[1] * currentMatrixPosition[1]), self.matrixUnitSize[0], self.matrixUnitSize[1])
                if column != 0:
                    gFrame.Draw.rectangleFromRect(unitRect, globalVars.currentColor)
                gFrame.Draw.borderFromRect(unitRect, 1, gFrame.Color.LIGHT_GRAY)
                currentMatrixPosition[0] += 1
            currentMatrixPosition[1] += 1
            currentMatrixPosition[0] = 0