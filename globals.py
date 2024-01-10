from colors import Color
from enums import screens
try:
    import board, neopixel
except ImportError:
    RPIconnected = False
else:
    RPIconnected = True
import pygameaddons as app

            
fieldColors = [ 
               # basic colors
               Color.BLACK,
               Color.RED, 
               Color.ORANGE, 
               Color.YELLOW, 
               Color.GREEN, 
               Color.LIGHT_BLUE, 
               Color.BLUE, 
               Color.PURPLE, 
               Color.PINK, 
               Color.WHITE,
               # extra colors
               Color.LESS_RED,
               Color.LAVA_RED,
               Color.BITTERSWEET,
               Color.REDWOOD,
               Color.BROWN,
               Color.GOLD,
               Color.SAFFRON,
               Color.ECRU,
               Color.BRUNSWICK_GREEN,
               Color.DARK_GREEN,
               Color.LESS_GREEN,
               Color.OLIVE_GREEN,
               Color.LIGHT_GREEN,
               Color.AQUAMARINE,
               Color.SPRING_GREEN,
               Color.TEA_GREEN,
               Color.TURQUISE,
               Color.MOONSTONE,
               Color.LESS_BLUE,
               Color.NAVY_BLUE,
               Color.RUSSIAN_VIOLET,
               Color.STEEL_PINK,
               Color.SKY_BLUE,
               Color.CELESTIAL_BLUE,
               Color.VIOLET_BLUE,
               Color.CELESTIAL_BLUE,
               Color.DARK_PURPLE,
               Color.BEIGE,
               Color.GHOST_WHITE,
               Color.BLACK_OLIVE,
               Color.CREAM,
               Color.COFFEE,
               Color.CAFE_NOIR,
               ]
# 45 colors
currentColor = 0

COLOR_BUTTON_TEXT = [
                    # basic colors
                    "zwart", 
                     "rood", 
                     "oranje", 
                     "geel", 
                     "groen", 
                     "lichtblauw", 
                     "donkerblauw", 
                     "paars", 
                     "roze",
                     "wit"
                     # extra colors
                     ]


currentScreen = screens.menu

colorPickerEnabled = False


if RPIconnected:
    pixels = neopixel.NeoPixel(board.D18, 256, brightness = 0.1)

smallButtonTemplate = ((app.ScreenUnit.vh(7), app.ScreenUnit.vh(7)), Color.BLACK)

def getCurrentColor():
    return fieldColors[currentColor]