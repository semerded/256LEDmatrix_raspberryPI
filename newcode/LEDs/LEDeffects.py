from time import sleep
from gFrame.elements.colors import Color
from LEDs.carLedMapping import carLedMapping

ledEffectsProperties = {
    "statisch": {
        "color": True,
        "speed": False
    },
    "regenboog": {
        "color": False,
        "speed": True
    },
    "roller": {
        "color": True,
        "speed": True
    },
    "regenboogroller": {
        "color": False,
        "speed": True
    },
    "auto lichten": {
        "color": False,
        "speed": False
    }
}

class LEDeffects:
    rainbowColors = [Color.RED, Color.ORANGE, Color.YELLOW, Color.GREEN, Color.BLUE, Color.PINK, Color.PURPLE]
    _currentLED = 0
    _currentRainbow = 0
    _ascending = True
    
    def __init__(self, pixels, ledAmount: int) -> None:
        self.pixels = pixels
        self.ledAmount = ledAmount
        self._effectNames = {"statisch": self.static, "regenboog": self.rainbowfull, "roller": self.rider, "regenboogroller": self.rainbowRider, "auto lichten": self.car}

    def rainbowfull(self, *void):
        self.static(self.rainbowColors[self._currentRainbow])
        self._currentRainbow += 1
        if self._currentRainbow == len(self.rainbowColors):
            self._currentRainbow = 0
        
    def static(self, color):
        self.pixels.fill(color)
        sleep(0.1)
        
    def rainbowRider(self, *void):
        self.rider(self.rainbowColors[self._currentRainbow])
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

    def car(self, *void):
        self._colorLedRing(carLedMapping["voor"]["links"][0], Color.ORANGE)
        self._colorLedRing(carLedMapping["voor"]["rechts"][0], Color.ORANGE)
        self._colorLedRing(carLedMapping["achter"]["links"][0], Color.ORANGE)
        self._colorLedRing(carLedMapping["achter"]["rechts"][0], Color.ORANGE)
        
        self._colorLedRing(carLedMapping["voor"]["links"][1], Color.WHITE)
        self._colorLedRing(carLedMapping["voor"]["links"][2], Color.WHITE)
        
        self._colorLedRing(carLedMapping["voor"]["rechts"][1], Color.WHITE)
        self._colorLedRing(carLedMapping["voor"]["rechts"][2], Color.WHITE)
        
        self._colorLedRing(carLedMapping["achter"]["links"][1], Color.WHITE)
        self._colorLedRing(carLedMapping["achter"]["rechts"][1], Color.WHITE)
        
        sleep(0.5)
        
        self._colorLedRing(carLedMapping["voor"]["links"][0], Color.BLACK)
        self._colorLedRing(carLedMapping["voor"]["rechts"][0], Color.BLACK)
        self._colorLedRing(carLedMapping["achter"]["links"][0], Color.BLACK)
        self._colorLedRing(carLedMapping["achter"]["rechts"][0], Color.BLACK)
        
        sleep(0.5)

        
    def getEffectByName(self, name: str, color):
        self._effectNames[name](color)
        
    def _colorLedRing(self, ledRange: tuple[int, int], color):
            for index in range(ledRange[0], ledRange[1] + 1):
                self.pixels.pixels[index] = color
    