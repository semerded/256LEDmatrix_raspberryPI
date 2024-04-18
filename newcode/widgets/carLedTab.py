import gFrame, globalVars
import gFrame.baseImporter
from LEDs.LEDeffects import ledEffectsProperties

class CarLedTab:
    firstShow = True
    
    def __init__(self, rect: gFrame.Rect, name: str, currentColor: gFrame.RGBvalue, chooseEffect: bool = True, chooseColor: bool = True, chooseSpeed: bool = True) -> None:
        self.rect: gFrame.Rect = rect
        self.name = name
        self.chooseEffect = chooseEffect
        self.chooseColor = chooseColor
        self.chooseSpeed = chooseSpeed
        
        self.currentEffect = "static"
        
        self.colorText = gFrame.Text("huidige kleur", "comic sans", rect.rw(10), gFrame.Color.BLACK)
                
        self.colorCurrentIndicator = gFrame.Button((rect.rw(80), rect.rh(15)), currentColor)
        self.colorCurrentIndicator.setBorder(1, gFrame.Color.WHITE)
        
        
        
    def place(self, currentColor):
        self._chooseColor(currentColor)
        
        if globalVars.app.drawElements():
            pass
            
    def _chooseColor(self, currentColor):
        if self.colorCurrentIndicator.isClicked():
            globalVars.currentScreen = globalVars.screens.carLEDcolorMenu
            globalVars.app.switchPage()
        
        if globalVars.app.drawElements():
            self.colorCurrentIndicator.updateColor(currentColor)
            self.colorCurrentIndicator.text("klik hier om de kleur te veranderen", "comic sans", self.rect.rw(4), gFrame.Text.textColorFromColor(currentColor))
            self.colorText.placeInRect(gFrame.Rect(self.rect.x, self.rect.y, self.rect.width, self.rect.rh(10)))
            self.colorCurrentIndicator.place(self.rect.pw(10), self.rect.ph(15))
            if self.firstShow: # to counter a weird bug
                self.colorCurrentIndicator.place(self.rect.pw(10), self.rect.ph(15))
                self.firstShow = False
                
            
            
            