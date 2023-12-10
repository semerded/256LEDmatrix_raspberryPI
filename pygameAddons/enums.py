from enum import Enum
class mouseButton(Enum):
    leftMouseButton = 1
    rightMouseButton = 2
    middleMouseButton = 3
    unknownbutton1 = 4
    unknownbutton2 = 5
    mouseButton4 = 6
    mouseButton5 = 7
    
class interactionType(Enum):
    mouseOver = 1
    mouseClick = 2
    mouseRelease = 3
    mouseHold = 4
    
class overFlow(Enum):
    ellipsis = 1
    hide = 2
    show = 3

class aspectRatios(Enum):
    ratio1to1 = "1/1"
    ratio16to9 = "16/9"
    ratio9to16 = "9/16"
    ratio4to3 = "4/3"
    ratio3to4 = "3/4"
    
class axis(Enum):
    x = 0
    y = 1
    z = 2