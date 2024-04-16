import gFrame, globalVars

class CarLEDscreen:
    carLedTextSelector = gFrame.Button(("20vw", "10vh"), gFrame.Color.BLACK)
    carLedTextSelector.text("Auto Lampen", "comic sans", gFrame.ScreenUnit.vw(3), gFrame.Color.WHITE)
    knightriderTextSelector = gFrame.Button(("20vw", "10vh"), gFrame.Color.BLACK)
    knightriderTextSelector.text("KnightRider", "comic sans", gFrame.ScreenUnit.vw(3), gFrame.Color.WHITE)
    
    def __init__(self) -> None:
        pass
    
    
    def place(self):
        globalVars.menuButton.checkIfClicked()
        
        if self.carLedTextSelector.isClicked():
            self.carLedTextSelector.setBorder(3, gFrame.Color.GRAY)
            self.knightriderTextSelector.setBorder(0, gFrame.Color.GRAY)
        
        if self.knightriderTextSelector.isClicked():
            self.knightriderTextSelector.setBorder(3, gFrame.Color.GRAY)
            self.carLedTextSelector.setBorder(0, gFrame.Color.GRAY)

        
        if globalVars.app.drawElements():
            globalVars.menuButton.place("93vw", "2vh")
            
            self.carLedTextSelector.place("30vw", "35vh")
            self.knightriderTextSelector.place("30vw", "55vh")
            
            gFrame.Draw.border("50vw", "10vh", "40vw", "80vh", 3, gFrame.Color.GRAY, cornerRadius=5)
            gFrame.Draw.rectangle(gFrame.ScreenUnit.vw(50) - 2, gFrame.ScreenUnit.vh(35) + 1, 3, gFrame.ScreenUnit.vh(10) - 3, gFrame.Color.BLACK)
            

