import board, neopixel    
from gFrame.elements.colors import Color
    
    
class Threaded_LEDcontroller:
    def __init__(self, pin: board, ledCount: int, brightness: float = 0.1) -> None:
        self.ledCount = ledCount
        self.controllerActive = False
        self.ledFunction = None

    