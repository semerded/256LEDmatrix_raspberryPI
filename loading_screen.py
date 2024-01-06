import pygameaddons as app

class LoadingScreen:
    def __init__(self, APP: app.AppConstructor, text: str) -> None:
        self.APP = APP
        self.text = text
        self.loadingEllipses = 0
        self.loadingWidget = app.Button((app.ScreenUnit.vw(50), app.ScreenUnit.vh(50)), app.Color.LIGHTGRAY, 20)
        self.loadingWidget.text(text, app.Font.customFont(int(app.ScreenUnit.vw(8))), app.Color.GREEN, app.overFlow.show)
  
    def place(self):
            self.APP.eventHandler(app.pygame.event.get())
            if self.APP.everyAmountOfTicks(10):
                self.loadingWidget.text(self._loadingText(), app.Font.customFont(int(app.ScreenUnit.vw(8))), app.Color.GREEN, app.overFlow.show)
                app.pygame.display.flip()   

            self.loadingWidget.updateButtonSize(app.ScreenUnit.vw(50), app.ScreenUnit.vh(50))
            self.loadingWidget.border(10, app.Color.GREEN)
            self.loadingWidget.place(app.ScreenUnit.vw(25), app.ScreenUnit.vh(25))            
        
    def _loadingText(self):
        self.loadingEllipses += 1
        if self.loadingEllipses > 3:
            self.loadingEllipses = 1
        return self.text + ("." * self.loadingEllipses)
        