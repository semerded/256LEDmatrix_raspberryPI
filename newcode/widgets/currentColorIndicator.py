import gFrame, globalVars

class CurrentColorIndicator:
    def __init__(self) -> None:
        pass
        
    def place(self, left, top):
        pencilEraser = gFrame.Draw.rectangle(left, top, gFrame.ScreenUnit.vw(5), gFrame.ScreenUnit.vh(8), gFrame.Color.RED)
        gFrame.Draw.border(1, pencilEraser, gFrame.Color.RED)
        pencilDivider = gFrame.Draw.rectangle(left, top + gFrame.ScreenUnit.vh(8), gFrame.ScreenUnit.vw(5), gFrame.ScreenUnit.vh(1), gFrame.Color.WHITE)
        gFrame.Draw.border(1, pencilDivider, gFrame.Color.WHITE)
        pencilCover = gFrame.Draw.rectangle(left, top + gFrame.ScreenUnit.vh(9), gFrame.ScreenUnit.vw(5), gFrame.ScreenUnit.vh(50), globals.getCurrentColor())
        gFrame.Draw.border(1, pencilCover, gFrame.Color.WHITE)
        gFrame.pygame.draw.polygon(gFrame.mainDisplay, gFrame.Color.BEIGE, [(left, top + gFrame.ScreenUnit.vh(59)), (left + gFrame.ScreenUnit.vw(5), top + gFrame.ScreenUnit.vh(59)), (left + gFrame.ScreenUnit.vw(2.5), top + gFrame.ScreenUnit.vh(66))])
        gFrame.pygame.draw.polygon(gFrame.mainDisplay, globals.getCurrentColor(), [(left + gFrame.ScreenUnit.vw(2), top + gFrame.ScreenUnit.vh(64)), (left + gFrame.ScreenUnit.vw(3), top + gFrame.ScreenUnit.vh(64)), (left + gFrame.ScreenUnit.vw(2.5), top + gFrame.ScreenUnit.vh(65.5))])