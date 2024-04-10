import gFrame, globalVars

class CarLEDscreen:
    def __init__(self) -> None:
        pass
    
    
    def place(self):
        globalVars.menuButton.checkIfClicked()
        if globalVars.app.drawElements():
            globalVars.menuButton.place("93vw", "2vh")

