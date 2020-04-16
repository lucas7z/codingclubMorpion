import pygame


class Case(pygame.sprite.Sprite):

    def __init__(self , rectx, recty, number):
        super().__init__()
        self.image = pygame.image.load('assets/blanc.png')
        self.image = pygame.transform.scale(self.image, (1,1))
        self.rect = (rectx+70,recty+50)
        self.number = number
        self.font=pygame.font.Font(None, 150)
        self.text = self.font.render(str(self.number),1,(0,0,0))
        self.isTaked = False
    def setText(self, text):
        self.font=pygame.font.Font(None, 150)
        self.text = self.font.render(str(text),1,(0,0,0))

class toPlay():
    def __init__(self):
        super().__init__()
        self.rect = (30,620)
        self.number = 1
        self.font=pygame.font.Font(None, 65)
        self.text = self.font.render("C'est au joueur numéro "+str(self.number),1,(255,255,255))
    def setNumero(self, numero):
        self.numero = numero
        self.font=pygame.font.Font(None, 65)
        self.text = self.font.render("C'est au joueur numéro "+str(self.numero),1,(255,255,255))