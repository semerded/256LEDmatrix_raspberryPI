from pygameaddons import *
from matrix import Matrix
from copy import deepcopy


class DrawingHistory:
    def __init__(self, matrixDimensions: tuple[int, int]) -> None:
        self.matrixDimensions = matrixDimensions
        self.resetDrawingHistory()
        
    def resetDrawingHistory(self):
        self.drawingHistory = []
        self.currentHistoryIndex = 0
        self.drawingHistory.append(Matrix.makeEmptyMatrix(*self.matrixDimensions))
    
    def undo(self):
        if self.currentHistoryIndex > 0:
            self.currentHistoryIndex -= 1
        return self.drawingHistory[self.currentHistoryIndex]
    
    def redo(self):
        pass
    
    def checkForChanges(self, currentMatrix: list[list[int]], matrixRect):
        if self._checkForDifferenceInNewMatrix(currentMatrix) and not Interactions.isHoldingInRect(matrixRect, mouseButton.leftMouseButton.value): #TODO only add matrix when mouse is not pressed
            self._checkIfCurrentHistoryIndexIs()
            self.currentHistoryIndex += 1
            self.drawingHistory.append(deepcopy(currentMatrix))
            
        self._checkForHistoryOverflow()
        print(len(self.drawingHistory))
    
    def _checkForDifferenceInNewMatrix(self, currentMatrix: list[list[int]]):
        if self.drawingHistory[self.currentHistoryIndex] == currentMatrix:
            # print(True)
            return False
        # print(False)
        return True
    
    def _checkForHistoryOverflow(self):
        while len(self.drawingHistory) > 50:
            self.drawingHistory.pop(0)
    
    def _checkIfCurrentHistoryIndexIs(self): # TODO fix name
        if self.currentHistoryIndex != len(self.drawingHistory) - 1:
            self.drawingHistory = self.drawingHistory[:self.currentHistoryIndex]
            
    @property
    def getCurrentHistoryIndex(self):
        return self.currentHistoryIndex