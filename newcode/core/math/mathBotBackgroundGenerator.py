from core.math.mathBot import MathBot
from threading import Thread
from pages.loadingScreen import LoadingScreen
from time import sleep

class MathBotGenerator(MathBot):
    generatorActive = False
    
    def __init__(self, difficulty: int, classNumber: int) -> None:
        super().__init__(difficulty, classNumber)
        self.LOADING_SCREEN = LoadingScreen("aan het denken")
        
        #shared resources with thread
        self.excerciseQueue = []
        
    def _generator(self):
        while self.generatorActive:
            if len(self.excerciseQueue) < 10:
                self.excerciseQueue.append(super().getExcercise())
            sleep(0.05) # save resources
            
    
    def getExcerciseFromQueue(self):
        if len(self.excerciseQueue) != 0:
            return self.excerciseQueue.pop(0)
        else:
            while True:
                self.LOADING_SCREEN.place()
                if len(self.excerciseQueue) > 0:
                    break
            return self.excerciseQueue.pop(0)
                
        
    def startGenerator(self):
        self.generatorActive = True
        Thread(target=self._generator).start()
        
    def stopGenerator(self):
        self.generatorActive = False 