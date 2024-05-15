import gFrame, globalVars

class CarLedEffectMenu:
    def __init__(self) -> None:
        self.header = gFrame.Text("Kies een effect", "comic sans", gFrame.ScreenUnit.vh(8), gFrame.Color.WHITE)
        
        self.body = gFrame.Rect(0, gFrame.ScreenUnit.vh(10), gFrame.ScreenUnit.vw(100), gFrame.ScreenUnit.vh(90))

        self.buttonProp = ((self.body.rw(45), self.body.rh(30)), gFrame.Color.GRAY)
        self.textProp = ("comic sans", self.body.rh(8), gFrame.Color.WHITE)
        self.borderProp = (3, gFrame.Color.REDWOOD)
        
        self.effectStaticButton = gFrame.Button(*self.buttonProp)
        self.effectStaticButton.text("statisch", *self.textProp)
        self.effectStaticButton.setBorder(*self.borderProp)
        
        self.effectRainbowButton = gFrame.Button(*self.buttonProp)
        self.effectRainbowButton.text("regenboog", *self.textProp)
        self.effectRainbowButton.setBorder(*self.borderProp)
        
        self.effectRiderButton = gFrame.Button(*self.buttonProp)
        self.effectRiderButton.text("roller", *self.textProp)
        self.effectRiderButton.setBorder(*self.borderProp)
        
        self.effectRainbowRiderButton = gFrame.Button(*self.buttonProp)
        self.effectRainbowRiderButton.text("regenboogroller", *self.textProp)
        self.effectRainbowRiderButton.setBorder(*self.borderProp)
        
        self.effectCarButton = gFrame.Button(*self.buttonProp)
        self.effectCarButton.text("auto lichten", *self.textProp)
        self.effectCarButton.setBorder(*self.borderProp)
        
        self.effectSnakeButton = gFrame.Button(*self.buttonProp)
        self.effectSnakeButton.text("slang", *self.textProp)
        self.effectSnakeButton.setBorder(*self.borderProp)
        
    def place(self):
        globalVars.menuButton.checkIfClicked()
        
        if self.effectStaticButton.isClicked():
            globalVars.currentCarLedEffect = globalVars.ledEffect.static
            globalVars.currentScreen = globalVars.screens.carLED
            globalVars.app.switchPage()
            
        if self.effectRainbowButton.isClicked():
            globalVars.currentCarLedEffect = globalVars.ledEffect.rainbow
            globalVars.currentScreen = globalVars.screens.carLED
            globalVars.app.switchPage()
            
        if self.effectRiderButton.isClicked():
            globalVars.currentCarLedEffect = globalVars.ledEffect.rider
            globalVars.currentScreen = globalVars.screens.carLED
            globalVars.app.switchPage()
            
        if self.effectRainbowRiderButton.isClicked():
            globalVars.currentCarLedEffect = globalVars.ledEffect.rainbowrider
            globalVars.currentScreen = globalVars.screens.carLED
            globalVars.app.switchPage()
            
        if self.effectCarButton.isClicked():
            globalVars.currentCarLedEffect = globalVars.ledEffect.car
            globalVars.currentScreen = globalVars.screens.carLED
            globalVars.app.switchPage()
            
        if self.effectSnakeButton.isClicked():
            globalVars.currentCarLedEffect = globalVars.ledEffect.snake
            globalVars.currentScreen = globalVars.screens.carLED
            globalVars.app.switchPage()

        if globalVars.app.drawElements():
            globalVars.menuButton.place("93vw", "2vh")
            self.header.placeInRect(gFrame.Rect(0, 0, gFrame.ScreenUnit.vw(100), gFrame.ScreenUnit.vh(10)))
            
            self.effectStaticButton.place(self.body.pw(2.5), self.body.ph(0))
            self.effectRainbowButton.place(self.body.pw(52.5), self.body.ph(0))
            self.effectRiderButton.place(self.body.pw(2.5), self.body.ph(33))
            self.effectRainbowRiderButton.place(self.body.pw(52.5), self.body.ph(33))
            self.effectCarButton.place(self.body.pw(2.5), self.body.ph(66))
            self.effectSnakeButton.place(self.body.pw(52.5), self.body.ph(66))
            