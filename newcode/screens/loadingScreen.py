import gFrame, globalVars

class LoadingScreen:
    loadingEllipses = 0
    
    def __init__(self, text: str) -> None:
        self.APP = globalVars.app
        self.text = text
        self.font = gFrame.Font.customFont(int(gFrame.ScreenUnit.vw(8)))
        self.loadingWidget = gFrame.Button("50vw", "50vh", gFrame.Color.LIGHT_GRAY, borderRadius=20)
        self.loadingWidget.setBorder(10, gFrame.Color.GREEN)
        self.loadingWidget.text(text, self.font, gFrame.Color.GREEN, overFlow=gFrame.overFlow.show)

    def place(self):
            self.APP.eventHandler()
            if self.APP.everyAmountOfTicks(10):
                self.loadingWidget.text(self._loadingText(), self.font, gFrame.Color.GREEN, overFlow=gFrame.overFlow.show)
                gFrame.Updating.updateDisplay()
            
            self.loadingWidget.place(*gFrame.ScreenUnit.centerRectInScreen(self.loadingWidget.getRect))            
        
    def _loadingText(self):
        self.loadingEllipses += 1
        if self.loadingEllipses > 3:
            self.loadingEllipses = 1
        return self.text + ("." * self.loadingEllipses)
        