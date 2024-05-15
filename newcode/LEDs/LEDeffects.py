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
    _activeLEDperRing = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    
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
        self._riderPerRing(carLedMapping["voor"]["links"][0], 0, color)
        self._riderPerRing(carLedMapping["voor"]["links"][1], 1, color)
        self._riderPerRing(carLedMapping["voor"]["links"][2], 2, color)
        self._riderPerRing(carLedMapping["voor"]["rechts"][0], 3, color)
        self._riderPerRing(carLedMapping["voor"]["rechts"][1], 4, color)
        self._riderPerRing(carLedMapping["voor"]["rechts"][2], 5, color)
        self._riderPerRing(carLedMapping["achter"]["links"][0], 6, color)
        self._riderPerRing(carLedMapping["achter"]["links"][1], 7, color)
        self._riderPerRing(carLedMapping["achter"]["rechts"][0], 8, color)
        self._riderPerRing(carLedMapping["achter"]["rechts"][1], 9, color)
            

    def car(self, *void):
        self._colorLedRing(carLedMapping["voor"]["links"][1], Color.ORANGE)
        self._colorLedRing(carLedMapping["voor"]["rechts"][1], Color.ORANGE)
        self._colorLedRing(carLedMapping["achter"]["links"][1], Color.ORANGE)
        self._colorLedRing(carLedMapping["achter"]["rechts"][1], Color.ORANGE)
        
        self._colorLedRing(carLedMapping["voor"]["links"][0], Color.WHITE)
        self._colorLedRing(carLedMapping["voor"]["links"][2], Color.WHITE)
        
        self._colorLedRing(carLedMapping["voor"]["rechts"][0], Color.WHITE)
        self._colorLedRing(carLedMapping["voor"]["rechts"][2], Color.WHITE)
        
        self._colorLedRing(carLedMapping["achter"]["links"][0], Color.RED)
        self._colorLedRing(carLedMapping["achter"]["rechts"][0], Color.RED)
        
        sleep(0.3)
        
        self._colorLedRing(carLedMapping["voor"]["links"][1], Color.BLACK)
        self._colorLedRing(carLedMapping["voor"]["rechts"][1], Color.BLACK)
        self._colorLedRing(carLedMapping["achter"]["links"][1], Color.BLACK)
        self._colorLedRing(carLedMapping["achter"]["rechts"][1], Color.BLACK)
        
        sleep(0.3)

        
    def getEffectByName(self, name: str, color):
        self._effectNames[name](color)
        
    def _colorLedRing(self, ledRange: tuple[int, int], color):
        for index in range(ledRange[0], ledRange[1] + 1):
            self.pixels.pixels[index] = color
                
    def _riderPerRing(self, ledRange: tuple[int, int], index, color):
        _index = self._activeLEDperRing[index] + 1
        if _index + ledRange[0] > ledRange[1]:
            _index = 0
        
        if _index == 0:
            self.pixels.pixels[ledRange[1]] = Color.BLACK
        else:    
            self.pixels.pixels[ledRange[0] + _index - 1] = Color.BLACK
        self.pixels.pixels[_index] = color
        
        
            
    