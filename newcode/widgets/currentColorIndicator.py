import gFrame, globalVars

class CurrentColorIndicator:
    def __init__(self) -> None:
        pass
        
    def place(self, left, top):
        left, top = gFrame.ScreenUnit.convertMultipleUnits(left, top)
        pencilEraser = gFrame.Draw.rectangle(left, top, gFrame.ScreenUnit.vw(5), gFrame.ScreenUnit.vh(8), gFrame.Color.RED)
        gFrame.Draw.borderFromRect(pencilEraser, 1, gFrame.Color.RED)
        pencilDivider = gFrame.Draw.rectangle(left, top + gFrame.ScreenUnit.vh(8), gFrame.ScreenUnit.vw(5), gFrame.ScreenUnit.vh(1), gFrame.Color.WHITE)
        gFrame.Draw.borderFromRect(pencilDivider, 1, gFrame.Color.WHITE)
        pencilCover = gFrame.Draw.rectangle(left, top + gFrame.ScreenUnit.vh(9), gFrame.ScreenUnit.vw(5), gFrame.ScreenUnit.vh(50), globalVars.currentColor)
        gFrame.Draw.borderFromRect(pencilCover, 1, gFrame.Color.WHITE)
        gFrame.Draw.polygon([(left, top + gFrame.ScreenUnit.vh(59)), (left + gFrame.ScreenUnit.vw(5), top + gFrame.ScreenUnit.vh(59)), (left + gFrame.ScreenUnit.vw(2.5), top + gFrame.ScreenUnit.vh(66))], gFrame.Color.BEIGE)
        gFrame.Draw.polygon([(left + gFrame.ScreenUnit.vw(2), top + gFrame.ScreenUnit.vh(64)), (left + gFrame.ScreenUnit.vw(3), top + gFrame.ScreenUnit.vh(64)), (left + gFrame.ScreenUnit.vw(2.5), top + gFrame.ScreenUnit.vh(65.5))], globalVars.currentColor)