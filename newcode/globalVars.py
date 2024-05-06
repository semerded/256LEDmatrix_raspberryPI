programRunning = True

import gFrame

app: gFrame.AppConstructor = None

try:
    import board, neopixel  #? check if a rpi is connected with the required libraries
except ImportError:
    print("program will run without LEDmatrix capibilities")
    RPIconnected = False
else:
    RPIconnected = True
    del board, neopixel  # clean up namespaces



iconButtonTemplate = (("7vh", "7vh"), gFrame.Color.BLACK)
colorPickerEnabled = False

fieldColors = [
    # basic colors
    ("zwart", gFrame.Color.BLACK),
    ("rood", gFrame.Color.RED),
    ("oranje", gFrame.Color.ORANGE),
    ("geel", gFrame.Color.YELLOW),
    ("groen", gFrame.Color.GREEN),
    ("lichtblauw", gFrame.Color.LIGHT_BLUE),
    ("donkerblauw", gFrame.Color.BLUE),
    ("paars", gFrame.Color.PURPLE),
    ("roze", gFrame.Color.PINK),
    ("wit", gFrame.Color.WHITE),
    # extra colors
    ("", gFrame.Color.LESS_RED),
    ("lava rood", gFrame.Color.LAVA_RED),
    ("bitter zoet", gFrame.Color.BITTERSWEET),
    ("", gFrame.Color.REDWOOD),
    ("bruin", gFrame.Color.BROWN),
    ("goud", gFrame.Color.GOLD),
    ("", gFrame.Color.SAFFRON),
    ("ecru", gFrame.Color.ECRU),
    ("", gFrame.Color.BRUNSWICK_GREEN),
    ("donkergroen", gFrame.Color.DARK_GREEN),
    ("", gFrame.Color.LESS_GREEN),
    ("olijf groen", gFrame.Color.OLIVE_GREEN),
    ("ligthgroen", gFrame.Color.LIGHT_GREEN),
    ("aquamarine", gFrame.Color.AQUAMARINE),
    ("lente groen", gFrame.Color.SPRING_GREEN),
    ("thee groen", gFrame.Color.TEA_GREEN),
    ("turquise", gFrame.Color.TURQUISE),
    ("maansteen", gFrame.Color.MOONSTONE),
    ("", gFrame.Color.LESS_BLUE),
    ("navy blauw", gFrame.Color.NAVY_BLUE),
    ("russisch violet", gFrame.Color.RUSSIAN_VIOLET),
    ("staal roze", gFrame.Color.STEEL_PINK),
    ("lucht blauw", gFrame.Color.SKY_BLUE),
    ("celestial blauw", gFrame.Color.CELESTIAL_BLUE),
    ("violet blauw", gFrame.Color.VIOLET_BLUE),
    ("", gFrame.Color.CELESTIAL_BLUE),
    ("donker paars", gFrame.Color.DARK_PURPLE),
    ("beige", gFrame.Color.BEIGE),
    ("geest wit", gFrame.Color.GHOST_WHITE),
    ("donker olijf", gFrame.Color.BLACK_OLIVE),
    ("room", gFrame.Color.CREAM),
    ("koffie", gFrame.Color.COFFEE),
    ("cafe noir", gFrame.Color.CAFE_NOIR)
]

currentColor = 0

currentCarLedColor = 9
currentKnightRiderColor = 1
currentLedSelected = "carled"

from enum import Enum
class ledEffect(Enum):
    static = "statisch"
    rainbow = "regenboog"
    rider = "roller"
    rainbowrider = "regenboogroller"
    car = "auto lichten"
    
    
currentCarLedEffect = ledEffect.static

from pages.screenEnum import screens

currentScreen = screens.menu

from widgets.menuButton import MenuButton
menuButton: MenuButton

mathBotClass = None
mathBotDifficulty = 1