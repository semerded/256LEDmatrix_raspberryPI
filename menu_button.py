import pygameaddons as app

class MenuButton:
    def __init__(self, size: tuple[int, int], color: app.RGBvalue, borderRadius: int = -1) -> None:
        self.menuButton = app.Button(size, color, borderRadius)
        self.menuButtonImage = app.Image("button_images/menu.png")
        self.menuButtonImage.resize(app.ScreenUnit.vh(7), app.ScreenUnit.vh(7))
    
    def place(self, left, top):
        self.menuButton.place(left, top)
        self.menuButtonImage.place(left, top)
        
    def onMouseClick(self):
        return self.menuButton.onMouseClick()
    