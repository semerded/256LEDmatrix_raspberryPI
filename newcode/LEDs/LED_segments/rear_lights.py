from LEDs.threaded_LEDcontroller import Threaded_LEDcontroller
import board

class RearLights(Threaded_LEDcontroller):
    def __init__(self, pin: board, ledCount: int, brightness: float = 0.1) -> None:
        super().__init__(pin, ledCount, brightness)
        