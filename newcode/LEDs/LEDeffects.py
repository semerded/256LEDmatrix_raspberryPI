from time import sleep
from gFrame.elements.colors import Color

class LEDeffects:
    rainbowColors = [Color.RED, Color.ORANGE, Color.YELLOW, Color.GREEN, Color.BLUE, Color.PINK, Color.PURPLE]
    _currentLED = 0
    _currentRainbow = 0
    _ascending = True
    
    def __init__(self, pixels, ledAmount: int) -> None:
        self.pixels = pixels
        self.ledAmount = ledAmount
        self._effectNames = {"static": self.static, "rainbow": self.rainbowfull, "rider": self.rider, "rainbowrider": self.rainbowRider}

    def rainbowfull(self, *void):
        self.static(self.rainbowColors[self._currentRainbow])
        self._currentRainbow += 1
        if self._currentRainbow == len(self.rainbowColors):
            self._currentRainbow = 0
        
    def static(self, color):
        self.pixels.fill(color)
        
    def rainbowRider(self, *void):
        self.rider(self.pixels, self.rainbowColors[self._currentRainbow], self.ledAmount)
        self._currentRainbow += 1
        if self._currentRainbow == len(self.rainbowColors):
            self._currentRainbow = 0
    
    def rider(self, color):
        self.pixels.pixels[self._currentLED] = color
        
        if self._ascending and self._currentLED > 0:
            self.pixels.pixels[self._currentLED - 1] = (0, 0, 0)
        elif not self._ascending and self._currentLED < self.ledAmount - 1:
            self.pixels.pixels[self._currentLED + 1] = (0, 0, 0)
        
        if self._currentLED == 0 and not self._ascending:
            self._ascending = True
        elif self._currentLED == self.ledAmount - 1 and self._ascending:
            self._ascending = False 

        self._currentLED += 1 if self._ascending else - 1
        
    def getEffectByName(self, name: str):
        return self._effectNames[name]
    