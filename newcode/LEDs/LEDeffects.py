from time import sleep
from gFrame.elements.colors import Color


rainbowColors = [Color.RED, Color.ORANGE, Color.YELLOW, Color.GREEN, Color.BLUE, Color.PINK, Color.PURPLE]
def rainbow(pixels):
    for color in rainbowColors:
        pixels.fill(color)
        sleep(0.2)

    