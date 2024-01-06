import pygameaddons as app
from matrix import Matrix
from copy import deepcopy
from functions import indexedLen


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
        return deepcopy(self.drawingHistory[self.currentHistoryIndex])
    
    def redo(self):
        if self.currentHistoryIndex < indexedLen(self.drawingHistory):
            self.currentHistoryIndex += 1
        return deepcopy(self.drawingHistory[self.currentHistoryIndex])
    
    def checkForChanges(self, currentMatrix: list[list[int]], matrixRect):
        if self._checkForDifferenceInNewMatrix(currentMatrix) and not app.Interactions.isHoldingInRect(matrixRect, app.mouseButton.leftMouseButton.value): 
            self._checkIfHistoryNeedsOverwrite(currentMatrix)
                
            self.currentHistoryIndex += 1
            self.drawingHistory.append(deepcopy(currentMatrix))
        self._checkForHistoryOverflow()

    def _checkForDifferenceInNewMatrix(self, currentMatrix: list[list[int]]):
        if self.drawingHistory[self.currentHistoryIndex] != currentMatrix:
            return True
        return False
    
    def _checkForHistoryOverflow(self):
        while len(self.drawingHistory) > 50:
            self.drawingHistory.pop(0)
            self.currentHistoryIndex -= 1
    
    def _checkIfHistoryNeedsOverwrite(self, currentMatrix: list[list[int]]): 
        if indexedLen(self.drawingHistory) != self.currentHistoryIndex and currentMatrix not in self.drawingHistory:
            self.drawingHistory = self.drawingHistory[:self.currentHistoryIndex + 1]
            
    @property
    def getCurrentHistoryIndex(self):
        return self.currentHistoryIndex