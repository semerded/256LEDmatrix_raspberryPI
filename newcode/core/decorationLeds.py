import globalVars
from time import sleep
from threading import Thread

if globalVars.RPIconnected:
    import board, neopixel
    
    
class DecorationLEDS:
    _ledMatrixLedCount = 256
    def __init__(self, ledCount: int) -> None:
        if globalVars.RPIconnected:
            self.pixels: neopixel.NeoPixel = neopixel.NeoPixel(board.D18, self._ledMatrixLedCount + ledCount, brightness = 0.1)
        self.ledCount = ledCount

    def startDecorationLEDS(self):
        Thread(target=self._decorationLedsLoop).start()
        
    def _decorationLedsLoop(self):
        while True:
            
            sleep(0.5)
            
    def setColor(self, color: tuple[int]):
        for index in range(self._ledMatrixLedCount, self._ledMatrixLedCount + self.ledCount):
            self.pixels[index] == color