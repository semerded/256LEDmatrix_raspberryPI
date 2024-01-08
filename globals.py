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
               Color.SAFFRON,
               Color.REDWOOD,
               Color.ECRU,
               Color.BITTERSWEET,
               Color.OLIVE_GREEN,
               Color.DARK_GREEN,
               Color.LESS_GREEN,
               Color.BRUNSWICK_GREEN,
               Color.TURQUISE,
               Color.AQUAMARINE,
               Color.TEA_GREEN,
               Color.SPRING_GREEN,
               Color.LIGHT_GREEN,
               Color.LESS_BLUE,
               Color.MOONSTONE,
               Color.RUSSIAN_VIOLET,
               Color.STEEL_PINK,
               Color.NAVY_BLUE,
               Color.CELESTIAL_BLUE,
               Color.VIOLET_BLUE,
               Color.SKY_BLUE,
               Color.CELESTIAL_BLUE,
               Color.DARK_PURPLE,
               Color.BEIGE,
               Color.GHOST_WHITE,
               Color.BLACK_OLIVE,
               Color.LICORICE,
               Color.DARKMODE,
               Color.CREAM,
               Color.COFFEE,
               Color.CAFE_NOIR,
               Color.BROWN,
               Color.GOLD
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

if RPIconnected:
    pixels = neopixel.NeoPixel(board.D18, 256, brightness = 0.1)

smallButtonTemplate = ((app.ScreenUnit.vh(7), app.ScreenUnit.vh(7)), Color.BLACK)