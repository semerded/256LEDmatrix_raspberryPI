import gFrame, globalVars
from LEDs.LEDeffects import ledEffectsProperties
import json

class CarLedTab:
    firstShow = True
    
    def __init__(self, rect: gFrame.Rect, name: str, led_data_name: str, currentColor: tuple[str, gFrame.RGBvalue]) -> None:
        self.rect: gFrame.Rect = rect
        self.name = name

        self.led_data_name = led_data_name
        
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
        self.changeEffectButton = gFrame.Button((rect.rw(80), rect.rh(10)), gFrame.Color.WHITE, 5)
        self.changeEffectButton.setBorder(1, gFrame.Color.GRAY)
        self.changeEffectButton.text("verander effect", "comic sans", rect.rw(6), gFrame.Color.BLACK)
        
        self.effectText = gFrame.Text("huidig effect", "comic sans", rect.rw(10), gFrame.Color.WHITE)
        
        # speed
        self.speedSlider = gFrame.Slider((rect.rw(70), 20), 0.03, 0.5, gFrame.Color.AQUAMARINE, gFrame.Color.WHITE, startValue=0.1, reverse=True)
        self.speedSlider.setKnob(13, gFrame.Color.RED)
        
        self.speedText = gFrame.Text("effect snelheid", "comic sans", rect.rw(10), gFrame.Color.WHITE)
        
        # update led data
        self.updateLedDataButton = gFrame.Button((rect.rw(80), rect.rh(10)), gFrame.Color.WHITE, 5)
        self.updateLedDataButton.setBorder(5, gFrame.Color.GREEN)
        self.updateLedDataButton.text("pimp!", "comic sans", rect.rw(7), gFrame.Color.BLACK)
        
    def writeToLedDataFile(self):
        with open("LEDs/led_data.json") as fp:
            ledData = json.load(fp)
            if not globalVars.currentLedSelected == "knightrider":
                ledData[self.led_data_name]["type"] = globalVars.currentCarLedEffect.value
            
            if globalVars.currentLedSelected == "knightrider" or ledEffectsProperties[globalVars.currentCarLedEffect.value]["color"]:
                if globalVars.currentLedSelected == "carled":
                    ledData[self.led_data_name]["color"] = globalVars.fieldColors[globalVars.currentCarLedColor][1]
                else:
                    ledData[self.led_data_name]["color"] = globalVars.fieldColors[globalVars.currentKnightRiderColor][1]
            
            if globalVars.currentLedSelected == "knightrider" or ledEffectsProperties[globalVars.currentCarLedEffect.value]["speed"]:  
                ledData[self.led_data_name]["speed"] = self.speedSlider.getValue()
                
        with open("LEDs/led_data.json", "w") as fp:
            json.dump(ledData, fp, indent = 4, separators=(',',': '))
        
    def place(self, currentColor: tuple[str, gFrame.RGBvalue]):   
        if self.updateLedDataButton.isClicked():
            self.writeToLedDataFile()
        
        if globalVars.currentLedSelected == "knightrider" or ledEffectsProperties[globalVars.currentCarLedEffect.value]["speed"]:
            self._chooseSpeed()
            
        if globalVars.currentLedSelected == "knightrider" or ledEffectsProperties[globalVars.currentCarLedEffect.value]["color"]:
            self._chooseColor(currentColor)
                
        if not globalVars.currentLedSelected == "knightrider":      
            self._chooseEffect()
        
        self.firstShow = False
        
        if globalVars.app.drawElements():
            self.updateLedDataButton.place(self.rect.pw(10), self.rect.ph(87))
            
        
            
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
    
    def _chooseEffect(self):
        if self.changeEffectButton.isClicked():
            globalVars.currentScreen = globalVars.screens.carLEDeffectMenu
            globalVars.app.switchPage()
        
        if globalVars.app.drawElements():
            self.changeEffectButton.place(self.rect.pw(10), self.rect.ph(45))
            self.effectText.placeInRect(gFrame.Rect(self.rect.x, self.rect.y + self.rect.rh(30), self.rect.rw(70), self.rect.rh(10)))
                
    def _chooseSpeed(self):
        if self.speedSlider.handler():
            print(self.speedSlider.getValue())
            gFrame.Updating.requestUpdate()
            
        if globalVars.app.drawElements():
            self.speedText.placeInRect(gFrame.Rect(self.rect.x, self.rect.y + self.rect.rh(60), self.rect.width, self.rect.rh(10)))
            self.speedSlider.place(self.rect.pw(15), self.rect.ph(75))
            