import globalVars
from time import sleep
from threading import Thread

if globalVars.RPIconnected:
    import board, neopixel
    
"""
voor (links en rechts):
    1 ronde neopixel van 16 leds
    2 ronde neopixels van 12 leds

voor (midden):
    1 "knight rider" led strip van 9 leds
    
achter (links en rechts):
    1 ronde neopixel van 16 leds
"""
    
    
class DecorationLEDS:
    _ledMatrixLedCount = 256
    def __init__(self, ledCount: int) -> None:
        if globalVars.RPIconnected:
            self.pixels: neopixel.NeoPixel = neopixel.NeoPixel(board.D18, self._ledMatrixLedCount + ledCount, brightness = 0.1)
        self.ledCount = ledCount

    def startDecorationLEDS(self):
        Thread(target=self._decorationLedsLoop).start()
        
    def _decorationLedsLoop(self):
        while globalVars.programRunning:
            
            sleep(0.5)
            
    def setColor(self, color: tuple[int]):
        for index in range(self._ledMatrixLedCount, self._ledMatrixLedCount + self.ledCount):
            self.pixels[index] == color