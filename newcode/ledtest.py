import board

from LEDs.LED_segments.knightrider import KnightRider

knightRider = KnightRider(board.D21, 9, 100, 0.5)

from LEDs.LED_segments.front_lights import FrontLights

frontLights = FrontLights(board.D10, 80, 0.4)

knightRider.loop()