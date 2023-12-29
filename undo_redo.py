from pygameaddons import *
from matrix import Matrix


class DrawingHistory:
    def __init__(self, matrixDimensions: tuple[int, int]) -> None:
        self.drawingHistory = []
        self.drawingHistory.append(Matrix.makeEmptyMatrix(*matrixDimensions))
    
    def undo(self):
        pass
    
    def redo(self):
        pass
    
    def checkForChanges(self, currentMatrix: list[list[int]]):
        if self._checkForDifferenceInNewMatrix:
            self.drawingHistory.append(currentMatrix)
        self._checkForHistoryOverflow()
        print(len(self.drawingHistory))
    
    def _checkForDifferenceInNewMatrix(self, currentMatrix: list[list[int]]):
        if self.drawingHistory[-1] != currentMatrix:
            return True
        return False
    
    def _checkForHistoryOverflow(self):
        while len(self.drawingHistory) > 50:
            self.drawingHistory.pop(0)