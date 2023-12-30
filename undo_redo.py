from pygameaddons import *
from matrix import Matrix
from copy import deepcopy


class DrawingHistory:
    def __init__(self, matrixDimensions: tuple[int, int]) -> None:
        self.drawingHistory = []
        self.drawingHistory.append(Matrix.makeEmptyMatrix(*matrixDimensions))
    
    def undo(self):
        pass
    
    def redo(self):
        pass
    
    def checkForChanges(self, currentMatrix: list[list[int]], matrixRect):
<<<<<<< HEAD
        if self._checkForDifferenceInNewMatrix(currentMatrix) and not Interactions.isHoldingInRect(matrixRect, mouseButton.leftMouseButton): #TODO only add matrix when mouse is not pressed
            self.drawingHistory.append(deepcopy(currentMatrix))
=======
        if self._checkForDifferenceInNewMatrix(currentMatrix) and not Interactions.isReleased(mouseButton.leftMouseButton.value): #TODO only add matrix when mouse is not pressed
            self.drawingHistory.append(currentMatrix)
>>>>>>> fbd4a9e6790444a08202707b388ac3b37fcdb2a5
            
        self._checkForHistoryOverflow()
        # print(len(self.drawingHistory))
    
    def _checkForDifferenceInNewMatrix(self, currentMatrix: list[list[int]]):
        if self.drawingHistory[-1] == currentMatrix:
            print(True)
            return False
        print(False)
        return True
    
    def _checkForHistoryOverflow(self):
        while len(self.drawingHistory) > 50:
            self.drawingHistory.pop(0)