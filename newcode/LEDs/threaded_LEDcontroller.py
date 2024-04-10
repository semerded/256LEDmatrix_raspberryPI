import globalVars
from threading import Thread
import board, neopixel    
from gFrame.elements.colors import Color
    
    
class Threaded_LEDcontroller:
    def __init__(self, pin: board, ledCount: int, brightness: float = 0.1) -> None:
        self.pixels: neopixel.NeoPixel = neopixel.NeoPixel(pin, ledCount, brightness = brightness)
        self.ledCount = ledCount
        self.controllerActive = False
        self.ledFunction = None

    def startThread(self, loop):
        self.controllerActive = True
        self.ledFunction = loop
        Thread(target=self._LEDloop).start()
        
    def _LEDloop(self):
        while self.controllerActive and globalVars.programRunning:
            self.ledFunction()
            
    def stopThread(self):
        self.controllerActive = False