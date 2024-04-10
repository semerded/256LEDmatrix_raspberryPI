import board, neopixel, json
from time import sleep

ledCount = 80
pixels: neopixel.NeoPixel = neopixel.NeoPixel(board.D10, ledCount, 0.4)

while True:
    with open("LEDs/led_data.json") as fp:
        data = json.load(fp)
    
    if not data["active"]:
        break
    
    ledData = data["front_light"]
    
    
    sleep(0.2)
    