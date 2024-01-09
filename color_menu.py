import pygameaddons as app
import globals

class ColorMenu:
    def __init__(self, APP: app.AppConstructor) -> None:
        self.APP = APP
        self.buttonSize = (app.ScreenUnit.vw(18), app.ScreenUnit.vh(7))
        # self.buttonText = buttonText
        self.buttonList = []
        for index, color in enumerate(globals.fieldColors):
            self.buttonList.append(app.Button(self.buttonSize, color, 5)),
            self.buttonList[index].border(6, app.Color.GRAY)
            # self.buttonList[index].text(self.buttonText[index], app.Font.H1, app.Text.textColorFromColor(globals.fieldColors[index]))
        self.buttonPosition = [0, 0]
        
        self.confirmButton = app.Button((app.ScreenUnit.vw(90), app.ScreenUnit.vh(7)), app.Color.WHITE, 5)
        self.confirmButton.text("kies kleur!", app.Font.H1)
        self.confirmButton.border(4, app.Color.GREEN)
        
    def checkForButtonClick(self):
        for index, button in enumerate(self.buttonList):
            if button.onMouseClick():
                globals.currentColor = index 
                self.APP.requestUpdate
        
    def _placeButtons(self):
        for index, button in enumerate(self.buttonList):
            button.place(app.ScreenUnit.vw(1 + 20 * self.buttonPosition[0]), app.ScreenUnit.vh(1 + 9 * self.buttonPosition[1]))
            self.buttonPosition[1] += 1
            if self.buttonPosition[1] == 10:
                self.buttonPosition[1] = 0
                self.buttonPosition[0] += 1
            
            
        self.highlightActiveColor(globals.currentColor)
        self.buttonPosition = [0, 0]
        
    def highlightActiveColor(self, index):
        buttonRect = self.buttonList[index].getButtonAndBorderRect
        app.Drawing.border(5, buttonRect, app.Color.GREEN, 10)
        # self.APP.requestUpdate
        
    def place(self):
        if not self.APP.firstFrame():
            self.checkForButtonClick()
            
            if self.confirmButton.onMouseClick():
                globals.currentScreen = app.screens.drawing
                globals.colorPickerEnabled = False
                return self.APP.switchScreen()

        # self.APP.requestUpdate
        if self.APP.firstFrame() or self.APP.updateAvalible:
            self.APP.maindisplay.fill(app.Color.BLACK)
            self._placeButtons()
            self.confirmButton.place(app.ScreenUnit.vw(5), app.ScreenUnit.vh(92))
            app.pygame.display.update()
            
 