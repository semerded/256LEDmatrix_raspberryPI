import gFrame, globalVars, json
from widgets.carLedTab import CarLedTab

class CarLEDscreen:
    carLedTextSelector = gFrame.Button(("20vw", "10vh"), gFrame.Color.BLACK)
    carLedTextSelector.text("Auto Lampen", "comic sans", gFrame.ScreenUnit.vw(3), gFrame.Color.WHITE)
    carLedTextSelector.setBorder(3, gFrame.Color.GRAY)
    
    knightriderTextSelector = gFrame.Button(("20vw", "10vh"), gFrame.Color.BLACK)
    knightriderTextSelector.text("KnightRider", "comic sans", gFrame.ScreenUnit.vw(3), gFrame.Color.WHITE)
        
    ledTab = gFrame.Rect("50vw", "10vh", "40vw", "80vh")

    def __init__(self, LEDjsonDataFilePath: str) -> None:
        self.dataPath = LEDjsonDataFilePath
        
        self.carLedTab = CarLedTab(self.ledTab, "Auto Lampen", "car_light", globalVars.fieldColors[globalVars.currentCarLedColor])
        self.knightRiderTab = CarLedTab(self.ledTab, "KnightRider", "knightrider", globalVars.fieldColors[globalVars.currentKnightRiderColor])
    
    
    def place(self):       
        globalVars.menuButton.checkIfClicked()
        
        if self.carLedTextSelector.isClicked():
            self.carLedTextSelector.setBorder(3, gFrame.Color.GRAY)
            self.knightriderTextSelector.setBorder(0, gFrame.Color.GRAY)
            globalVars.currentLedSelected = "carled"
            globalVars.app.switchPage()
        
        if self.knightriderTextSelector.isClicked():
            self.knightriderTextSelector.setBorder(3, gFrame.Color.GRAY)
            self.carLedTextSelector.setBorder(0, gFrame.Color.GRAY)
            globalVars.currentLedSelected = "knightrider"
            globalVars.app.switchPage()
        
        self.carLedTab.place(globalVars.fieldColors[globalVars.currentCarLedColor]) if globalVars.currentLedSelected == "carled" else self.knightRiderTab.place(globalVars.fieldColors[globalVars.currentKnightRiderColor])
        

        
        if globalVars.app.drawElements():
            globalVars.menuButton.place("93vw", "2vh")
            
            self.carLedTextSelector.place("30vw", "35vh")
            self.knightriderTextSelector.place("30vw", "55vh")
                            
            gFrame.Draw.border(*self.ledTab.unpack(), 3, gFrame.Color.GRAY, cornerRadius=5)
            
            top = gFrame.ScreenUnit.vh(35) + 1 if globalVars.currentLedSelected == "carled" else gFrame.ScreenUnit.vh(55) + 1
            gFrame.Draw.rectangle(gFrame.ScreenUnit.vw(50) - 4, top, 6, gFrame.ScreenUnit.vh(10) - 3, gFrame.Color.BLACK)
