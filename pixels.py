import pygameaddons as app
from matrix import Matrix
from threading import Thread
from loading_screen import LoadingScreen
import globals

class Pixels:
    def __init__(self, pixels, APP: app.AppConstructor, MATRIX: Matrix) -> None:
        self.pixels = pixels
        self.MATRIX = MATRIX
        self.drawingBusy = False
        self.APP = APP
        self.LOADING_SCREEN = LoadingScreen(self.APP, "Aan het tekenen")
        
    def drawMatrixOnPhysicalMatrix(self, matrix: list[list[int]]):
        self.drawingBusy = True
        Thread(target=self._threadedDrawingOnMatrix, args=(matrix,)).start()
        while self.drawingBusy:
            self.LOADING_SCREEN.place()        
        
    def _threadedDrawingOnMatrix(self, matrix: list[list[int]]):
        ledCounter = 0
        reverse = True
        for row in matrix:
            if reverse:
                for column in reversed(row):
                    self.pixels[ledCounter] = globals.fieldColors[column]                 
                    ledCounter += 1
            else:
                for column in row:
                    self.pixels[ledCounter] = globals.fieldColors[column]
                    ledCounter += 1
            reverse = not reverse
        self.drawingBusy = False
            
    def erasePhysicalMatrix(self):
        self.MATRIX.eraseMatrix()
        self.APP.updateDisplay()
        self.pixels.fill(app.Color.BLACK)
        