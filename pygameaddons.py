try:
    import pygame
except ImportError:
    raise ImportError("install pygame with 'pip install pygame'")
try:
    import pygame_textinput
except ImportError:
    pygame__textinputImported = False
else:
    pygame__textinputImported = True

    
import random, logging
from multipledispatch import dispatch

import sys, os
from typing_extensions import TypeAlias, Literal


from enums import *
from colors import Color
from fonts import Font

pygame.init()

screenUnit: TypeAlias = int | str
modifiableFunctions: TypeAlias = Literal[
    "quit"
]

RGBvalue: TypeAlias = tuple[int, int, int]
font : TypeAlias = pygame.font

def notBelowZero(input: int | float) -> (int | float):
    if input < 0:
        return 0
    return input


# pygameLogger = logging.basicConfig() # TODO add logger



displayInfo = pygame.display.Info()
userScreenWidth = displayInfo.current_w
userScreenHeight = displayInfo.current_h
appScreenWidth = 0
appScreenHeight = 0
mainDisplay = None
screenUpdate = False

mouseButtonsStatus = [False, False, False, False, False]
previousMouseButtonStatus = []

class logger():
    def __init__(self, logger: bool = True, endReport: bool = False) -> None:
        self.logger = logger
        self.endReport = endReport
        
    


class AppConstructor():
    def __init__(self, screenWidth, screenHeight, *flags, manualUpdating: bool = False) -> None:
        global mainDisplay
        self.screenWidth = displayInfo.current_w
        self.screenHeight = displayInfo.current_h
        self.APPdisplayFlags = flags
        self.manualUpdating = manualUpdating
        self.frameCounter = 0
        self.updatePending = True

        self.minimumScreenWidth = None
        self.minimumScreenHeight = None
        self.modifiedFunctions = {"quit": None}

        self.APPdisplay = pygame.display.set_mode(
            (screenWidth, screenHeight), *flags)
        mainDisplay = self.APPdisplay
        
        self.resetFlank = False
        self.screenSizeUpdated = False
        self.aspectRatioActive = False
        Interactions.resetPreviousMouseButtonStatus()

    def eventHandler(self, appEvents: pygame.event):
        global appScreenWidth, appScreenHeight
        if not self.manualUpdating:
            Updating.updateDisplay()
        elif self.updatePending:
            Updating.updateDisplay()
            self.updatePending = False
        else:
            if self.frameCounter < 2:
                Updating.updateDisplay()
                
        if self.resetFlank:
            Interactions.resetPreviousMouseButtonStatus()
            self.resetFlank = False
            
        self.appEvents = appEvents
        for event in self.appEvents:
            if event.type == pygame.QUIT:
                if self.modifiedFunctions["quit"] == None:
                    pygame.quit()
                    sys.exit()
                else:
                    self.modifiedFunctions["quit"]()

            if event.type == pygame.WINDOWRESIZED:
                appScreenWidth, appScreenHeight = self.getAppScreenDimensions
                if self.minimumScreenWidth != None and self.minimumScreenHeight != None:
                    self.checkForMinimumScreenSizeBreaches()
                if self.aspectRatioActive and self.getAppScreenDimensions[0] != userScreenWidth:
                    self.updateAspectRatio()
                self.updatePending = True
                

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseButtonsStatus[event.button] = True
                Interactions.mouseButtonPositiveFlank(event.button)
                self.resetFlank = True

            if event.type == pygame.MOUSEBUTTONUP:
                mouseButtonsStatus[event.button] = False
                Interactions.mouseButtonNegativeFlank(event.button)
                self.resetFlank = True
        self.frameCounter += 1
    def resizeAppscreen(self, screenWidth, screenHeight, *flags):
        self.APPdisplayFlags = flags
        self.APPdisplay = pygame.display.set_mode(
            (screenWidth, screenHeight), *flags)
        self.__updateMainDisplay()

    def setModifiableFunctions(self, **kwargs: modifiableFunctions):  # TODO
        for modifiedFunction, newFunction in kwargs.items():
            self.modifiedFunctions[modifiedFunction] = newFunction

    def setMinimumScreenDimensions(self, minimumScreenWidth: screenUnit = None, minimumScreenHeight: screenUnit = None):
        if minimumScreenWidth != None:
            self.minimumScreenWidth = minimumScreenWidth
        else:
            self.minimumScreenWidth = None
        if minimumScreenHeight != None:
            self.minimumScreenHeight = minimumScreenHeight
        else:
            self.minimumScreenHeight = None
            
    def setAspectratio(self, aspectRatio: int | float, width: int | None = None, height: int | None = None):
        """
        calculates the aspect ratio from the width or height and resizes the screen to that size\n
        when no size is givin, the size will be calculated from the current width of the screen\n
        when 2 sizes are givin, the size from the givin width will be used\n
        use the function 'ScreenUnit.aspectRatio' to get the aspect ratio
        """
        self.aspectRatioActive = True
        self.aspectRatio = aspectRatio
        self.__checkAspectRatioAxis(width, height)
        
        if width == None and height == None:
            width = self.getAppScreenDimensions[0]
        width, height = self.__calculateAspectRatioAxis(width, height)
        self.resizeAppscreen(width, height, *self.APPdisplayFlags)
        
    def updateAspectRatio(self):
        if self.aspectRatioAxis == axis.x:
            width = self.getAppScreenDimensions[0]
            height = 0
        else:
            height = self.getAppScreenDimensions[1]
            width = 0
        width, height = self.__calculateAspectRatioAxis(width, height)
        self.resizeAppscreen(width, height, *self.APPdisplayFlags)
            
    def __calculateAspectRatioAxis(self, width, height):
        if self.aspectRatioAxis == axis.x:
            height = width / self.aspectRatio
        else:
            width = height * self.aspectRatio
        return width, height            
        
    def updateAspectRatioAxis(self, newAxis: axis):
        self.aspectRatioAxis = newAxis    
        
    def disableAspectRatio(self):
        self.aspectRatioActive = False
        
    def __checkAspectRatioAxis(self, width, height):
        if width == None and height != None:
            self.aspectRatioAxis = axis.y
        else:
            self.aspectRatioAxis = axis.x
    
    def __updateMainDisplay(self):
        global mainDisplay, appScreenWidth, appScreenHeight
        mainDisplay = self.APPdisplay
        appScreenWidth, appScreenHeight = self.getAppScreenDimensions
            
    def isScreenResized(self):
        if self.screenSizeUpdated:
            self.screenSizeUpdated = False
            return True
        return False
        
    def centerApp(self):
        os.environ['SDL_VIDEO_CENTERED'] = '1'

    def checkForMinimumScreenSizeBreaches(self):
        w, h = self.getAppScreenDimensions
        updateScreen = False
        if w < self.minimumScreenWidth:
            w = self.minimumScreenWidth
            updateScreen = True
        if h < self.minimumScreenHeight:
            h = self.minimumScreenHeight
            updateScreen = True
        if updateScreen:
            self.resizeAppscreen(w, h, *self.APPdisplayFlags)
            
    def updateDisplay(self):
        Updating.updateDisplay()
        
    def firstFrame(self):
        if self.getFrameCounter < 2:
            return True
        return False

    @property
    def setRelativeFullscreen(self):
        self.APPdisplay = pygame.display.set_mode(
            (self.screenWidth, self.screenHeight), *self.APPdisplayFlags)
        self.setModifiableFunctions()

    @property
    def getAppScreenDimensions(self):
        displayInfo = pygame.display.Info()
        return displayInfo.current_w, displayInfo.current_h

    @property
    def getdisplayDimensions(self):
        return (self.screenWidth, self.screenHeight)
    
    @property
    def getFrameCounter(self):
        return self.frameCounter

    @property
    def maindisplay(self) -> pygame.surface:
        """pygame main surface"""
        return self.APPdisplay
    
    @property
    def setUpdatePending(self):
        self.updatePending = True
        
    @property
    def updateAvalible(self):
        return self.updatePending
        


class Scroll():
    def __init__(self) -> None:
        pass

    @property
    def set_scroll(self):
        self.__scrollActivated = True

    @property
    def get_scroll(self):
        return self.__scrollActivated


class ScreenUnit:
    def convert():
        ...

    def precent(parentSize, percent):
        return parentSize / 100 * percent

    def dw(screenUnit: float) -> float:
        """
        display width
        """
        return userScreenWidth / 100 * screenUnit

    def dh(screenUnit: float) -> float:
        """
        display height
        """
        return userScreenHeight / 100 * screenUnit
    
    def vw(screenUnit: float) -> float:
        """
        view width 
        """
        return  appScreenWidth / 100 * screenUnit
    
    def vh(screenUnit: float) -> float:
        """
        view height
        """
        return appScreenHeight / 100 * screenUnit
    
    @dispatch(int, int)
    def aspectRatio(xRatio: int, yRatio: int) -> (int | float):
        return xRatio / yRatio 
    
    @dispatch(aspectRatios)
    def aspectRatio(aspectRatio: aspectRatios):
        aspectRatioValues = aspectRatio.value.split("/")
        return int(aspectRatioValues[0]) / int(aspectRatioValues[1])
    
    # def calculateAspectRatio(width: screenUnit, height: screenUnit):
    #     return width / height


class Image:
    def __init__(self, fileName: str, nameHint: str = "") -> None:
        self.image = pygame.image.load(fileName, nameHint)
        self.imageSize = self.getSize
        self.imagePosition = (0, 0)

    def resizeAndKeepProportions(self, width: float, height: float):
        aspectRatio = self.getAspectRatio
        imageWidth, imageHeight = self.getSize
        if aspectRatio < 1:
            width = int(imageWidth * aspectRatio)
        else:
            height = int(imageHeight / aspectRatio)
        self.scale(width, height)

    def scale(self, width, height):
        self.image = pygame.transform.scale(self.image, (width, height))
        self.imageSize = self.getSize

    def isMouseOver(self):
        return Interactions.isMouseOver(self.getImageRect)

    def isClicked(self, mouseButton: mouseButton):
        return Interactions.isClickedInRect(self.getImageRect, mouseButton)

    def isReleased(self, mouseButton: mouseButton):
        return Interactions.isReleasedInRect(self.getImageRect, mouseButton)

    def isHolding(self, mouseButton: mouseButton):
        return Interactions.isHoldingInRect(self.getImageRect, mouseButton)

    def place(self, xPosition: float, yPosition: float):
        self.imagePosition = (xPosition, yPosition)
        self.image.blit(mainDisplay, self.imagePosition)

    @property
    def getAspectRatio(self):
        imageWidth, imageHeight = self.getSize
        return imageWidth / imageHeight

    @property
    def getSize(self):
        return self.image.get_size()

    @property
    def getPosition(self):
        return self.imagePosition

    @property
    def getImageRect(self):
        return pygame.Rect(*self.getPosition, *self.getSize)

    @property
    def getImage(self):
        return self.image

class Interactions:
    def __init__(self) -> None:
        pass
            
    def resetPreviousMouseButtonStatus():
        global previousMouseButtonStatus
        previousMouseButtonStatus = []
        for i in range(len(mouseButton)):
            previousMouseButtonStatus.append(False)

    def isMouseButtonPressed(mouseButton: mouseButton):
        if mouseButtonsStatus[mouseButton]:
            return True
        return False

    def mouseButtonPositiveFlank(mouseButton: mouseButton):
        if mouseButtonsStatus[mouseButton] and not previousMouseButtonStatus[mouseButton]:
            previousMouseButtonStatus[mouseButton] = True
            return True
        return False

    def mouseButtonNegativeFlank(mouseButton: mouseButton):
        if not mouseButtonsStatus[mouseButton] and previousMouseButtonStatus[mouseButton]:
            previousMouseButtonStatus[mouseButton] = True
            return True
        return False

    def isMouseOver(rect: pygame.Rect):
        mousePos = pygame.mouse.get_pos()
        if rect.collidepoint(mousePos):
            return True
        return False
    
    def isMouseInArea(topCord: int, bottomCord: int):
        rect = pygame.Rect(topCord, bottomCord)
        return Interactions.isMouseOver(rect)

    def isClicked(mouseButton: mouseButton):
        if Interactions.mouseButtonPositiveFlank(mouseButton):
            return True
        return False
    
    def isClickedInRect(rect: pygame.Rect, mouseButton: mouseButton):
        if Interactions.isMouseOver(rect) and Interactions.isClicked(mouseButton):
            return True
        return False

    def isReleased(mouseButton: mouseButton):
        if Interactions.mouseButtonNegativeFlank(mouseButton):
            return True
        return False
    
    def isReleasedInRect(rect: pygame.Rect, mouseButton: mouseButton):
        if Interactions.isMouseOver(rect) and Interactions.isReleased(mouseButton):
            return True
        return False

    def isHolding(mouseButton: mouseButton):
        if Interactions.isMouseButtonPressed(mouseButton):
            return True
        return False
    
    def isHoldingInRect(rect: pygame.Rect, mouseButton: mouseButton):
        if Interactions.isMouseOver(rect) and Interactions.isMouseButtonPressed(mouseButton):
            return True
        return False

class Text:

    pass

    def place(self):
        pass
    
class Updating:
    def updateDisplay():
        pygame.display.update()
        
    def __init__(self, **kwargs) -> None:
        self.objectList = kwargs
        self.emptyObjectList = kwargs
        
    def resetObjectList(self):
        self.objectList = self.emptyObjectList


class Button:
    def __init__(self,
                 size: tuple[screenUnit, screenUnit],
                 color: RGBvalue,
                 borderRadius:int = -1
                 ) -> None:
        self.buttonSize = size
        self.buttonColor = color
        self.defaultButtonColor = color
        self.borderRadius = borderRadius
        self.__text = None
        # self.buttonAtributes = Updating(__text=False, __border=False)
        self.borderWidth = 0
        self.buttonRect = pygame.Rect(0, 0, 0, 0)
        self.textSurface = pygame.Surface((0, 0))

    # static
    def simpleButton(size,
                     position, 
                     backgroundColor: RGBvalue = Color.LIGHTGRAY, 
                     text: str = "", 
                     font: font = Font.H3,
                     textColor: RGBvalue = Color.BLACK, 
                     cornerRadius: int = -1, 
                     borderWidth: int = 0,
                     borderColor: RGBvalue = Color.BLACK,
                     ) -> bool:
        
        buttonRect = Drawing.rectangle(position[0], position[1], size[0], size[1], backgroundColor, cornerRadius)
        if borderWidth > 0:
            buttonRect = Drawing.border(borderWidth, buttonRect, borderColor, cornerRadius)
        if text != "":
            buttonText = font.render(text, True, textColor)
            mainDisplay.blit(buttonText, (position[0] + size[0] / 2 - buttonText.get_width() / 2, position[1] + size[1] / 2 - buttonText.get_height() / 2))
        return Interactions.isClickedInRect(buttonRect, mouseButton.leftMouseButton.value)
        
    # instance
    def text(self, text: str, textFont: pygame.font = Font.H4, textColor: RGBvalue = Color.BLACK, overFlow = overFlow.ellipsis):
        self.__text = Text.textOverflow(text, textFont, self.buttonSize[0], overFlow)
        self.__textFont = textFont
        self.__textColor = textColor
        # self.buttonAtributes["__text"] = True

    def border(self, borderWidth: int, borderColor: RGBvalue):
        self.borderWidth = borderWidth
        self.borderColor = borderColor

    def radius(self, borderRadius):
        self.borderRadius = borderRadius

    def onMouseOver(self):
        return Interactions.isMouseOver(self.buttonRect)

    def onMouseClick(self, mouseButton: mouseButton = mouseButton.leftMouseButton):
        return Interactions.isClickedInRect(self.buttonRect, mouseButton.value)
    
    def onMouseRelease(self, mouseButton: mouseButton = mouseButton.leftMouseButton):
        return Interactions.isReleasedInRect(self.buttonRect, mouseButton.value)

    def onMouseHold(self, mouseButton: mouseButton = mouseButton.leftMouseButton):
        return Interactions.isHoldingInRect(self.buttonRect, mouseButton.value)

    def changeColorOnHover(self, hoverColor: RGBvalue):
        if self.onMouseOver():
            self.buttonColor = hoverColor
        else:
            self.buttonColor = self.defaultButtonColor 
        
    def changeColorOnMouseClick(self, clickColor: RGBvalue):
        if self.onMouseHold():
            self.buttonColor = clickColor
        else:
            self.buttonColor = self.defaultButtonColor
            
    def __placeButtonRect(self):
        Drawing.rectangleFromRect(self.buttonRect, self.buttonColor, Drawing.calculateInnerBorderRadius(self.borderRadius, self.borderWidth))
        
    def __placeText(self):
        if self.__text != None:
            self.textSurface = self.__textFont.render(self.__text, True, self.__textColor)
            textPosX, textPosY = Text.centerTextInRect(self.textSurface, self.buttonRect)
            mainDisplay.blit(self.textSurface, (textPosX, textPosY))
                
    def __placeBorder(self):
        if self.borderWidth > 0:
            Drawing.border(self.borderWidth, self.buttonRect, self.borderColor, self.borderRadius)
        

    def place(self, left, top):
        self.buttonRect = pygame.Rect(left, top, self.buttonSize[0], self.buttonSize[1])
        self.fullRect = pygame.Rect(left - self.borderWidth / 2, top - self.borderWidth / 2, self.buttonSize[0] + self.borderWidth, self.buttonSize[1] + self.borderWidth)
        self.__placeButtonRect()
        self.__placeText()
        self.__placeBorder()
        
    def updateButtonSize(self, width, height):
        self.buttonSize = (width, height)
    
    @property
    def getFullSize(self):
        return self.buttonSize[0] + 2 * self.borderWidth, self.buttonSize[1] + 2 * self.borderWidth
    
    @property
    def getRect(self):
        return self.buttonRect
    
    @property
    def getButtonAndBorderRect(self):
        return self.fullRect
    
    

class Text:
    def __init__(self) -> None:
        pass
    
    def textOverflow(text: str, font: pygame.font, maxWidth: int | float, overFlowType: overFlow = overFlow.ellipsis) -> str:
        if font.size(text)[0] < maxWidth:
            return text
        
        if overFlowType == overFlow.show:
            return text
        elif overFlowType == overFlow.ellipsis:
            ellipsisWidth = font.size("...")[0]
            maxWidth -= ellipsisWidth - ellipsisWidth / 3
            overFlowTrailing = "..."
        else:
            overFlowTrailing = ""
            
        newText = ""
        textWidth = 0
        for letter in text:
            textWidth += font.size(letter)[0]
            if textWidth < maxWidth - 10:
                newText += letter
            else:
                return newText.strip() + overFlowTrailing
        return text

    def simpleText( position: tuple[int,int], text: str, font: pygame.font = Font.H3, color: RGBvalue = Color.BLACK):
        textsurface = font.render(f"{text}", True, color)       
        mainDisplay.blit(textsurface, (position[0], position[1]))
        return textsurface

    def centerTextInRect(textSurface: pygame.Surface, rect: pygame.Rect) -> tuple[float, float]:
        xPos = rect.x + (rect.width / 2) - (textSurface.get_width() / 2)
        yPos = rect.y + (rect.height / 2) - (textSurface.get_height() / 2)
        return xPos, yPos
        

    def centerd(self):
        ...


class Drawing:
    def rectangle(xPosition: float, yPosition: float, width: float, height: float, color: RGBvalue = Color.LIGHTGRAY, cornerRadius: int = -1):
        return pygame.draw.rect(mainDisplay, color, pygame.Rect(xPosition, yPosition, width, height), border_radius=cornerRadius)
    
    def rectangleFromRect(rect: pygame.Rect, color: RGBvalue = Color.LIGHTGRAY, cornerRadius: int = -1):
        return pygame.draw.rect(mainDisplay, color, rect, border_radius=cornerRadius)
        
    def border(borderWidth: int, rectValue: pygame.Rect | tuple[float, float, float, float], color: RGBvalue = Color.BLACK, cornerRadius: int = -1) -> pygame.Rect:
        if isinstance(rectValue, pygame.Rect):
            xPosition = rectValue.x - borderWidth / 2
            yPosition = rectValue.y - borderWidth / 2
            width = rectValue.width + borderWidth
            height = rectValue.height + borderWidth
        else:
            xPosition = rectValue[0] - borderWidth / 2
            yPosition = rectValue[1] - borderWidth / 2
            width = rectValue[2] - borderWidth
            height = rectValue[3] - borderWidth
        return pygame.draw.rect(mainDisplay, color, pygame.Rect(xPosition, yPosition, width, height), width=borderWidth, border_radius=cornerRadius)
    
    def calculateInnerBorderRadius(outerBorderRadius, borderWidth):
        return notBelowZero(outerBorderRadius - borderWidth)
        
    
class Animate:
    def __init__(self) -> None:
        pass
    
    def moveTo(startCords, endCords, timeInMs):
        pass
            
class Textbox:
    def __init__(self) -> None:
        pass