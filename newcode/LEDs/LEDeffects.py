from time import sleep
from gFrame.elements.colors import Color

currentLED = 0
currentRainbow = 0
ascending = True

rainbowColors = [Color.RED, Color.ORANGE, Color.YELLOW, Color.GREEN, Color.BLUE, Color.PINK, Color.PURPLE]
def rainbowfull(pixels):
    global currentRainbow
    static(pixels, rainbowColors[currentRainbow])
    currentRainbow += 1
    if currentRainbow == len(rainbowColors):
        currentRainbow = 0
        

def static(pixels, color):
    pixels.fill(color)
        
        
def rainbowRider(pixels, ledAmount):
    global currentRainbow
    rider(pixels, rainbowColors[currentRainbow], ledAmount)
    currentRainbow += 1
    if currentRainbow == len(rainbowColors):
        currentRainbow = 0
    

def rider(pixels, color, ledAmount):
    global currentLED, ascending
    pixels.pixels[currentLED] = color
    
    if ascending and currentLED > 0:
        pixels.pixels[currentLED - 1] = (0, 0, 0)
    elif not ascending and currentLED < ledAmount - 1:
        pixels.pixels[currentLED + 1] = (0, 0, 0)
    
    if currentLED == 0 and not ascending:
        ascending = True
    elif currentLED == ledAmount - 1 and ascending:
        ascending = False 

    currentLED += 1 if ascending else - 1
    
    
    