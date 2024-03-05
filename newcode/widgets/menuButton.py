import gFrame, globalVars

class MenuButton:
    def __init__(self) -> None:
        self.menuButton = gFrame.Button(*globalVars.iconButtonTemplate)
        self.menuButton.icon("drawingButtonsIcons/menu.png")
        
    def place(self, left, top):
        self.menuButton.place(left, top)
        
    def checkIfClicked(self):
        if self.menuButton.isClicked():
            globalVars.currentScreen = globalVars.screens.menu
            globalVars.app.switchPage()
            return True