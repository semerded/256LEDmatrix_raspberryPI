from colors import Color
from enums import screens
import board, neopixel
import pygameaddons as app


fieldColors = [Color.BLACK, Color.RED, Color.ORANGE, Color.YELLOW, Color.GREEN, Color.LIGHTBLUE, Color.BLUE, Color.PURPLE, Color.PINK, Color.WHITE]
currentColor = 0

currentScreen = screens.menu

pixels = neopixel.NeoPixel(board.D18, 256, brightness = 0.1)

smallButtonTemplate = ((app.ScreenUnit.vh(7), app.ScreenUnit.vh(7)), Color.LIGHTGRAY)