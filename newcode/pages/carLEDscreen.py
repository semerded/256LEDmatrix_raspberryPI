import gFrame, globalVars, json

class CarLEDscreen:
    carLedTextSelector = gFrame.Button(("20vw", "10vh"), gFrame.Color.BLACK)
    carLedTextSelector.text("Auto Lampen", "comic sans", gFrame.ScreenUnit.vw(3), gFrame.Color.WHITE)
    carLedTextSelector.setBorder(3, gFrame.Color.GRAY)
    
    knightriderTextSelector = gFrame.Button(("20vw", "10vh"), gFrame.Color.BLACK)
    knightriderTextSelector.text("KnightRider", "comic sans", gFrame.ScreenUnit.vw(3), gFrame.Color.WHITE)
    
    selectedButton: int = 1
    
    def __init__(self, LEDjsonDataFilePath: str) -> None:
        self.dataPath = LEDjsonDataFilePath
    
    
    def place(self):
        globalVars.menuButton.checkIfClicked()
        
        if self.carLedTextSelector.isClicked():
            self.carLedTextSelector.setBorder(3, gFrame.Color.GRAY)
            self.knightriderTextSelector.setBorder(0, gFrame.Color.GRAY)
            self.selectedButton = 1
        
        if self.knightriderTextSelector.isClicked():
            self.knightriderTextSelector.setBorder(3, gFrame.Color.GRAY)
            self.carLedTextSelector.setBorder(0, gFrame.Color.GRAY)
            self.selectedButton = 2

        
        if globalVars.app.drawElements():
            globalVars.menuButton.place("93vw", "2vh")
            
            self.carLedTextSelector.place("30vw", "35vh")
            self.knightriderTextSelector.place("30vw", "55vh")
                            
            gFrame.Draw.border("50vw", "10vh", "40vw", "80vh", 3, gFrame.Color.GRAY, cornerRadius=5)
            
            top = gFrame.ScreenUnit.vh(35) + 1 if self.selectedButton == 1 else gFrame.ScreenUnit.vh(55) + 1
            gFrame.Draw.rectangle(gFrame.ScreenUnit.vw(50) - 2, top, 3, gFrame.ScreenUnit.vh(10) - 3, gFrame.Color.BLACK)
            

    def writeDataToJson(self):
        with open(self.dataPath) as fp:
            json.dump(..., fp, indent=4)