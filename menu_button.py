from pygameaddons import *

class MenuButton:
    def __init__(self, size: tuple[int, int], color: RGBvalue, borderRadius: int = -1) -> None:
        self.menuButton = Button(size, color, borderRadius)
        self.menuButtonImage = Image("button_images/menu.png")
        self.menuButtonImage.resize(ScreenUnit.vh(7), ScreenUnit.vh(7))
    
    def place(self, left, top):
        self.menuButton.place(left, top)
        self.menuButtonImage.place(left, top)
        
    def onMouseClick(self):
        return self.menuButton.onMouseClick()
    