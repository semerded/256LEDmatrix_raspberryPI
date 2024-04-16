import board, neopixel, json, sys

class _Segment:
    def __init__(self, pin: board, ledCount: int, brightness: float = 0.1) -> None:
        self.pixels: neopixel.NeoPixel = neopixel.NeoPixel(pin, ledCount, brightness=brightness)
        self.ledCount = ledCount
        
    def loadData(self, dataName: str):
        with open("LEDs/led_data.json") as fp:
            data = json.load(fp)
        
        if not data["active"]:
            self.pixels.fill((0, 0, 0))
            self.pixels.show()
            sys.exit()
        
        return data[dataName]   

    def fill(self, color):
        self.pixels.fill(color)         
