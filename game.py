import pygame
from case import *
from players import *

class Game():
    def __init__(self):
        super().__init__()
        self.win = False
        self.winner = 0
        self.cases = pygame.sprite.Group()
        self.case0 = Case(0,0,0)
        self.case1 = Case(1*198,0,1)
        self.case2 = Case(2*198,0,2)
        self.case3 = Case(0,198,3)
        self.case4 = Case(1*198,198,4)
        self.case5 = Case(2*198,198,5)
        self.case6 = Case(0,2*198,6)
        self.case7 = Case(1*198,2*198,7)
        self.case8 = Case(2*198,2*198,8)
        self.cases.add(self.case0)
        self.cases.add(self.case1)
        self.cases.add(self.case2)
        self.cases.add(self.case3)
        self.cases.add(self.case4)
        self.cases.add(self.case5)
        self.cases.add(self.case6)
        self.cases.add(self.case7)
        self.cases.add(self.case8)
        self.playerX = PlayerX(self)
        self.playerO = PlayerO(self)
        self.inPlaying = self.playerX
        self.TextToPlay = toPlay()
    def changeToPlay(self):
        if self.inPlaying.numero==1:
            self.inPlaying = self.playerO
        else:
            self.inPlaying = self.playerX
    def setCase(self, numberCase):
        if numberCase ==0:
            if self.inPlaying.numero==1:
                if self.case0.isTaked == False:
                    self.case0.image = pygame.image.load('assets/croix.png')
                    self.case0.image = pygame.transform.scale(self.case0.image, (100,100))
                    self.inPlaying = self.playerO
                    self.case0.isTaked = True
                    self.inPlaying.addCase(0)
            else:
                if self.case0.isTaked == False:
                    self.case0.image = pygame.image.load('assets/rond.png')
                    self.case0.image = pygame.transform.scale(self.case0.image, (100,100))
                    self.inPlaying = self.playerX
                    self.case0.isTaked = True
                    self.inPlaying.addCase(0)
        elif numberCase==1:
            if self.inPlaying.numero==1:
                if self.case1.isTaked == False:
                    self.case1.image = pygame.image.load('assets/croix.png')
                    self.case1.image = pygame.transform.scale(self.case1.image, (100,100))
                    self.inPlaying = self.playerO
                    self.case1.isTaked = True
                    self.inPlaying.addCase(1)
            else:
                if self.case1.isTaked == False:
                    self.case1.image = pygame.image.load('assets/rond.png')
                    self.case1.image = pygame.transform.scale(self.case1.image, (100,100))
                    self.inPlaying = self.playerX
                    self.case1.isTaked = True
                    self.inPlaying.addCase(1)
        elif numberCase==2:
            if self.inPlaying.numero==1:
                if self.case2.isTaked == False:
                    self.case2.image = pygame.image.load('assets/croix.png')
                    self.case2.image = pygame.transform.scale(self.case2.image, (100,100))
                    self.inPlaying = self.playerO
                    self.case2.isTaked = True
                    self.inPlaying.addCase(2)
            else:
                if self.case7.isTaked == False:
                    self.case2.image = pygame.image.load('assets/rond.png')
                    self.case2.image = pygame.transform.scale(self.case2.image, (100,100))
                    self.inPlaying = self.playerX
                    self.case2.isTaked = True
                    self.inPlaying.addCase(2)
        elif numberCase==3:
            if self.inPlaying.numero==1:
                if self.case3.isTaked == False:
                    self.case3.image = pygame.image.load('assets/croix.png')
                    self.case3.image = pygame.transform.scale(self.case3.image, (100,100))
                    self.inPlaying = self.playerO
                    self.case3.isTaked = True
                    self.inPlaying.addCase(3)
            else:
                if self.case3.isTaked == False:
                    self.case3.image = pygame.image.load('assets/rond.png')
                    self.case3.image = pygame.transform.scale(self.case3.image, (100,100))
                    self.inPlaying = self.playerX
                    self.case3.isTaked = True
                    self.inPlaying.addCase(3)
        elif numberCase==4:
            if self.inPlaying.numero==1:
                if self.case4.isTaked == False:
                    self.case4.image = pygame.image.load('assets/croix.png')
                    self.case4.image = pygame.transform.scale(self.case4.image, (100,100))
                    self.inPlaying = self.playerO
                    self.case4.isTaked = True
                    self.inPlaying.addCase(4)
            else:
                if self.case4.isTaked == False:
                    self.case4.image = pygame.image.load('assets/rond.png')
                    self.case4.image = pygame.transform.scale(self.case4.image, (100,100))
                    self.inPlaying = self.playerX
                    self.case4.isTaked = True
                    self.inPlaying.addCase(4)
        elif numberCase==5:
            if self.inPlaying.numero==1:
                if self.case5.isTaked == False:
                    self.case5.image = pygame.image.load('assets/croix.png')
                    self.case5.image = pygame.transform.scale(self.case5.image, (100,100))
                    self.inPlaying = self.playerO
                    self.case5.isTaked = True
                    self.inPlaying.addCase(5)
            else:
                if self.case5.isTaked == False:
                    self.case5.image = pygame.image.load('assets/rond.png')
                    self.case5.image = pygame.transform.scale(self.case5.image, (100,100))
                    self.inPlaying = self.playerX
                    self.case5.isTaked = True
                    self.inPlaying.addCase(5)
        elif numberCase==6:
            if self.inPlaying.numero==1:
                if self.case6.isTaked == False:
                    self.case6.image = pygame.image.load('assets/croix.png')
                    self.case6.image = pygame.transform.scale(self.case6.image, (100,100))
                    self.inPlaying = self.playerO
                    self.case6.isTaked = True
                    self.inPlaying.addCase(6)
            else:
                if self.case6.isTaked == False:
                    self.case6.image = pygame.image.load('assets/rond.png')
                    self.case6.image = pygame.transform.scale(self.case6.image, (100,100))
                    self.inPlaying = self.playerX
                    self.case6.isTaked = True
                    self.inPlaying.addCase(6)
        elif numberCase==7:
            if self.inPlaying.numero==1:
                if self.case7.isTaked == False:
                    self.case7.image = pygame.image.load('assets/croix.png')
                    self.case7.image = pygame.transform.scale(self.case7.image, (100,100))
                    self.inPlaying = self.playerO
                    self.case7.isTaked = True
                    self.inPlaying.addCase(7)
            else:
                if self.case7.isTaked == False:
                    self.case7.image = pygame.image.load('assets/rond.png')
                    self.case7.image = pygame.transform.scale(self.case7.image, (100,100))
                    self.inPlaying = self.playerX
                    self.case7.isTaked = True
                    self.inPlaying.addCase(7)
        elif numberCase==8:
            if self.inPlaying.numero==1:
                if self.case8.isTaked == False:
                    self.case8.image = pygame.image.load('assets/croix.png')
                    self.case8.image = pygame.transform.scale(self.case8.image, (100,100))
                    self.inPlaying = self.playerO
                    self.case8.isTaked = True
                    self.inPlaying.addCase(8)
            else:
                if self.case8.isTaked == False:
                    self.case8.image = pygame.image.load('assets/rond.png')
                    self.case8.image = pygame.transform.scale(self.case8.image, (100,100))
                    self.inPlaying = self.playerX
                    self.case8.isTaked = True
                    self.inPlaying.addCase(8)
    def check(self):
        b = False
        if self.case0.isTaked == False:b = True
        if self.case1.isTaked == False:b = True
        if self.case2.isTaked == False:b = True
        if self.case3.isTaked == False:b = True
        if self.case4.isTaked == False:b = True
        if self.case5.isTaked == False:b = True
        if self.case6.isTaked == False:b = True
        if self.case7.isTaked == False:b = True
        if self.case8.isTaked == False:b = True
        if b ==False:
            return True