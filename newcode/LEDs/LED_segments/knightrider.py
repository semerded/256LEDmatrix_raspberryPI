from LEDs.threaded_LEDcontroller import Threaded_LEDcontroller
from gFrame.elements.colors import Color
from time import sleep
import board

class KnightRider(Threaded_LEDcontroller):
    _currentLED = 0
    _ascending = True
    
    def __init__(self, pin: board, ledCount: int, msBetweenLed: int, brightness: float = 0.1) -> None:
        super().__init__(pin, ledCount, brightness)
        self.previousActiveTime = 0
        self.msDelay = msBetweenLed
        self.color = Color.RED 
        super().startThread(self.loop)   
        
    def loop(self):
        self.pixels[self._currentLED] = self.color
        
        if self._ascending and self._currentLED > 0:
            self.pixels[self._currentLED - 1] = Color.BLACK
        elif not self._ascending and self._currentLED < self.ledCount - 1:
            self.pixels[self._currentLED + 1] = Color.BLACK
        
        if self._currentLED == 0 and not self._ascending:
            self._ascending = True
        elif self._currentLED == self.ledCount - 1 and self._ascending:
            self._ascending = False 
            
        self._currentLED += 1 if self._ascending else - 1
        
        sleep(self.msDelay / 1000)
            
    
    def setColor(self, color):
        self.color = color 
        
    def setDelayInterval(self, interval: int):
        self.msDelay = interval