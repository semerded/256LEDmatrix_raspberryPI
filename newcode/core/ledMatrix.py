from core.gMatrix import gMatrix
from pages.loadingScreen import LoadingScreen
import globalVars, gFrame
from threading import Thread

if globalVars.RPIconnected:
    import board, neopixel

class LEDmatrix(gMatrix):
    drawingBusy = False
    
    def __init__(self, colums: int, rows: int, matrixWidth: float, matrixHeight: float) -> None:
        super().__init__(colums, rows, matrixWidth, matrixHeight)
        if globalVars.RPIconnected:
            self.pixels: neopixel.NeoPixel = neopixel.NeoPixel(board.D18, 256, brightness = 0.1)
        self.LOADING_SCREEN = LoadingScreen("Aan het tekenen")
        
    def drawPhysicalMatrix(self, showLoadingScreen: bool = True):
        if globalVars.RPIconnected and not self.drawingBusy:
            self.drawingBusy = True
            Thread(target=self._threadedDrawingOnMatrix, args=(self.matrix,)).start()
            if showLoadingScreen:
                while self.drawingBusy:
                    self.LOADING_SCREEN.place()  
                return globalVars.app.switchPage()
        
    def _threadedDrawingOnMatrix(self, matrix: list[list[int]]):
        ledCounter = 0
        reverse = True
        for row in matrix:
            if reverse:
                row = reversed(row)
            for column in row:
                self.pixels[ledCounter] = globalVars.fieldColors[column][1]                 
                ledCounter += 1
        
            reverse = not reverse
        self.drawingBusy = False
        
    def erasePhysicalMatrix(self):
        self.eraseMatrix()
        globalVars.app.requestUpdate()
        self.fillMatrix(gFrame.Color.BLACK)
        
    def fillMatrix(self, color: gFrame.RGBvalue):
        super().fillMatrix(color)
        if globalVars.RPIconnected:
            self.pixels.fill(color)
        