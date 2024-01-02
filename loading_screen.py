from pygameaddons import *

class LoadingScreen:
    def __init__(self, APP: AppConstructor, text: str) -> None:
        self.APP = APP
        self.text = text
        self.loadingEllipses = 0
        self.loadingWidget = Button((ScreenUnit.vw(50), ScreenUnit.vh(50)), Color.LIGHTGRAY, 20)
        self.loadingWidget.text(text, Font.customFont(int(ScreenUnit.vw(8))), Color.GREEN, overFlow.show)
  
    def place(self):
            self.APP.eventHandler(pygame.event.get())
            if self.APP.everyAmountOfTicks(10):
                self.loadingWidget.text(self._loadingText(), Font.customFont(int(ScreenUnit.vw(8))), Color.GREEN, overFlow.show)
                pygame.display.update(self.loadingWidget.getRect)     

            self.loadingWidget.updateButtonSize(ScreenUnit.vw(50), ScreenUnit.vh(50))
            self.loadingWidget.border(10, Color.GREEN)
            self.loadingWidget.place(ScreenUnit.vw(25), ScreenUnit.vh(25))            
        
    def _loadingText(self):
        self.loadingEllipses += 1
        if self.loadingEllipses > 3:
            self.loadingEllipses = 1
        return self.text + ("." * self.loadingEllipses)
        