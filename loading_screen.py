from pygameaddons import *

class LoadingScreen:
    def __init__(self, APP: AppConstructor, text: str) -> None:
        self.APP = APP
        self.text = text
        self.loadingEllipses = 0
        self.loadingWidget = Button((ScreenUnit.vw(50), ScreenUnit.vh(50)), Color.LIGHTGRAY, 5)
        self.loadingWidget.text(text, Font.customFont(ScreenUnit.vw(4)), Color.GREEN, overFlow.show)
  
    def place(self):
            if self.APP.everyAmountOfTicks(20):
                self.loadingWidget.text(self._loadingText(), Font.customFont(ScreenUnit.vw(4)), Color.GREEN, overFlow.show)
            self.loadingWidget.updateButtonSize(ScreenUnit.vw(50), ScreenUnit.vh(50))
            self.loadingWidget.border(Color.GREEN, 5)
            self.loadingWidget.place(ScreenUnit.vw(25), ScreenUnit.vh(25))            
            pygame.display.update(self.loadingWidget.getRect)     
        
    def _loadingText(self):
        self.loadingEllipses += 1
        if self.loadingEllipses > 3:
            self.loadingEllipses = 1
        return self.text + ("." * self.loadingEllipses)
        