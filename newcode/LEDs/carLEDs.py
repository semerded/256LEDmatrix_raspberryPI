"""
voor (links en rechts):
    1 ronde neopixel van 16 leds
    2 ronde neopixels van 12 leds

voor (midden):
    1 "knight rider" led strip van 9 leds
    
achter (links en rechts):
    1 ronde neopixel van 16 leds
    
121
"""

import board # GPIO 10, 12, 18, 21


listing = {
    "big_front": [[0, 15], [40, 55]],
    "small_front": [[16, 27], [28, 39], [56, 67], [68, 79]],
    "rear": [[80, 95], [96, 111]],
}

from LEDs.LED_segments.knightrider import KnightRider

knightRider = KnightRider(board.D21, 9, 100, 0.5)

from LEDs.LED_segments.front_lights import 

frontLights = 

from LEDs.LED_segments.rear_lights import RearLights

rearLights = RearLights(board.D12, 80, 0.4)

