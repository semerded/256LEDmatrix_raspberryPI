import globalVars
from threading import Thread
import board, neopixel    
    
    
class Threaded_LEDcontroller:
    def __init__(self, pin: board, ledCount: int, brightness: float = 0.1) -> None:
        self.pixels: neopixel.NeoPixel = neopixel.NeoPixel(pin, ledCount, brightness = brightness)
        self.ledCount = ledCount
        self.controllerActive = False

    def startThread(self, loop):
        self.controllerActive = True
        Thread(target=loop).start()
        
    def LEDloop(self, func):
        while self.controllerActive and globalVars.programRunning:
            func()
            
    def stopThread(self):
        self.controllerActive = False