import pygameaddons as app
import globals

class CurrentColorIndicator:
    def __init__(self, APP: app.AppConstructor) -> None:
        self.APP = APP
        
    def place(self, left, top):
        pencilEraser = app.Drawing.rectangle(left, top, app.ScreenUnit.vw(5), app.ScreenUnit.vh(8), app.Color.RED)
        app.Drawing.border(1, pencilEraser, app.Color.RED)
        pencilDivider = app.Drawing.rectangle(left, top + app.ScreenUnit.vh(8), app.ScreenUnit.vw(5), app.ScreenUnit.vh(1), app.Color.WHITE)
        app.Drawing.border(1, pencilDivider, app.Color.WHITE)
        pencilCover = app.Drawing.rectangle(left, top + app.ScreenUnit.vh(9), app.ScreenUnit.vw(5), app.ScreenUnit.vh(50), globals.getCurrentColor())
        app.Drawing.border(1, pencilCover, app.Color.WHITE)
        app.pygame.draw.polygon(app.mainDisplay, app.Color.BEIGE, [(left, top + app.ScreenUnit.vh(59)), (left + app.ScreenUnit.vw(5), top + app.ScreenUnit.vh(59)), (left + app.ScreenUnit.vw(2.5), top + app.ScreenUnit.vh(66))])
        app.pygame.draw.polygon(app.mainDisplay, globals.getCurrentColor(), [(left + app.ScreenUnit.vw(2), top + app.ScreenUnit.vh(64)), (left + app.ScreenUnit.vw(3), top + app.ScreenUnit.vh(64)), (left + app.ScreenUnit.vw(2.5), top + app.ScreenUnit.vh(65.5))])