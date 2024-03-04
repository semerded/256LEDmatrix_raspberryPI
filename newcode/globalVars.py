import gFrame

app = gFrame.AppConstructor("50dw", "50dh", manualUpdating=True)
gFrame.Display.setAspectRatio(gFrame.aspectRatios.ratio16to9, "50dw")

try:
    import board, neopixel  # check if a rpi is connected with the required libraries
except ImportError:
    print("program will run without LEDmatrix capibilities")
    RPIconnected = False
else:
    RPIconnected = True
    del board, neopixel  # clean up namespaces



iconButtonTemplate = (("7vh", "7vh"), gFrame.Color.BLACK)
currentScreen = 0
colorPickerEnabled = False

fieldColors = [
    # basic colors
    ("", gFrame.Color.BLACK),
    ("", gFrame.Color.RED),
    ("", gFrame.Color.ORANGE),
    ("", gFrame.Color.YELLOW),
    ("", gFrame.Color.GREEN),
    ("", gFrame.Color.LIGHT_BLUE),
    ("", gFrame.Color.BLUE),
    ("", gFrame.Color.PURPLE),
    ("", gFrame.Color.PINK),
    ("", gFrame.Color.WHITE),
    # extra colors
    ("", gFrame.Color.LESS_RED),
    ("", gFrame.Color.LAVA_RED),
    ("", gFrame.Color.BITTERSWEET),
    ("", gFrame.Color.REDWOOD),
    ("", gFrame.Color.BROWN),
    ("", gFrame.Color.GOLD),
    ("", gFrame.Color.SAFFRON),
    ("", gFrame.Color.ECRU),
    ("", gFrame.Color.BRUNSWICK_GREEN),
    ("", gFrame.Color.DARK_GREEN),
    ("", gFrame.Color.LESS_GREEN),
    ("", gFrame.Color.OLIVE_GREEN),
    ("", gFrame.Color.LIGHT_GREEN),
    ("", gFrame.Color.AQUAMARINE),
    ("", gFrame.Color.SPRING_GREEN),
    ("", gFrame.Color.TEA_GREEN),
    ("", gFrame.Color.TURQUISE),
    ("", gFrame.Color.MOONSTONE),
    ("", gFrame.Color.LESS_BLUE),
    ("", gFrame.Color.NAVY_BLUE),
    ("", gFrame.Color.RUSSIAN_VIOLET),
    ("", gFrame.Color.STEEL_PINK),
    ("", gFrame.Color.SKY_BLUE),
    ("", gFrame.Color.CELESTIAL_BLUE),
    ("", gFrame.Color.VIOLET_BLUE),
    ("", gFrame.Color.CELESTIAL_BLUE),
    ("", gFrame.Color.DARK_PURPLE),
    ("", gFrame.Color.BEIGE),
    ("", gFrame.Color.GHOST_WHITE),
    ("", gFrame.Color.BLACK_OLIVE),
    ("", gFrame.Color.CREAM),
    ("", gFrame.Color.COFFEE),
    ("", gFrame.Color.CAFE_NOIR)
]

currentColor = gFrame.Color.RED
