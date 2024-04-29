import gFrame, globalVars
import gFrame.baseImporter
from LEDs.LEDeffects import ledEffectsProperties

class CarLedTab:
    firstShow = True
    
    def __init__(self, rect: gFrame.Rect, name: str, currentColor: tuple[str, gFrame.RGBvalue], chooseEffect: bool = True, chooseColor: bool = True, chooseSpeed: bool = True) -> None:
        self.rect: gFrame.Rect = rect
        self.name = name
        self.chooseEffect = chooseEffect
        self.chooseColor = chooseColor
        self.chooseSpeed = chooseSpeed
        
        # color
        self.colorText = gFrame.Text("huidige kleur:", "comic sans", rect.rw(10), gFrame.Color.WHITE)
                
        self.changeColorButton = gFrame.Button((rect.rw(80), rect.rh(10)), gFrame.Color.WHITE, 5)
        self.changeColorButton.setBorder(1, gFrame.Color.GRAY)
        self.changeColorButton.text("verander kleur", "comic sans", rect.rw(6), gFrame.Color.BLACK)
        
        self.currentColorIndicator = gFrame.Button((rect.rw(30), rect.rh(10)), currentColor[1], 5)
        self.currentColorIndicator.text(currentColor[0], "comic sans", rect.rw(4), gFrame.Text.textColorFromColor(currentColor[1]), overFlow=gFrame.overFlow.show)
        self.currentColorIndicator.setBorder(1, gFrame.Color.GRAY)
        
        # effect
        self.currentEffect = "static"
        self.effectText = gFrame.Text("huidig effect", "comic sans", rect.rw(10), gFrame.Color.WHITE)
        
        # speed
        self.speedSlider = gFrame.Slider((rect.rw(70), 20), 0, 100, gFrame.Color.AQUAMARINE, gFrame.Color.WHITE)
        self.speedSlider.setKnob(13, gFrame.Color.RED)
        
        
        
    def place(self, currentColor: tuple[str, gFrame.RGBvalue]):   
        if self.chooseSpeed:
            self._chooseSpeed()
            
        if self.chooseColor:
            self._chooseColor(currentColor)
                        
        if self.chooseEffect:
            self._chooseEffect()
        
        if globalVars.app.drawElements():
            pass
            
    def _chooseColor(self, currentColor: tuple[str, gFrame.RGBvalue]):
        if self.changeColorButton.isClicked():
            globalVars.currentScreen = globalVars.screens.carLEDcolorMenu
            globalVars.app.switchPage()
        
        if globalVars.app.drawElements():
            
            self.colorText.placeInRect(gFrame.Rect(self.rect.x, self.rect.y, self.rect.rw(70), self.rect.rh(10)))
            self.currentColorIndicator.updateColor(currentColor[1])
            self.currentColorIndicator.text(currentColor[0], "comic sans", self.rect.rw(4), gFrame.Text.textColorFromColor(currentColor[1]))
            self.currentColorIndicator.place(self.rect.pw(69), self.rect.ph(2))
            self.changeColorButton.place(self.rect.pw(10), self.rect.ph(15))
            if self.firstShow: # to counter a weird bug
                self.currentColorIndicator.place(self.rect.pw(69), self.rect.ph(2))
                self.changeColorButton.place(self.rect.pw(10), self.rect.ph(15))
                self.firstShow = False
    
    def _chooseEffect(self):
        if globalVars.app.drawElements():
            self.effectText.placeInRect(gFrame.Rect(self.rect.x, self.rect.y + self.rect.rh(30), self.rect.width, self.rect.rh(10)))
                
    def _chooseSpeed(self):
        if self.speedSlider.handler():
            gFrame.Updating.requestUpdate()
            
        if globalVars.app.drawElements():
            self.speedSlider.place(self.rect.pw(15), self.rect.ph(60))
            pass
            