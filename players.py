import pygame

class PlayerX(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.numero = 1
        self.cases = []
    def addCase(self, case):
        self.cases.append(case)
        checkWin(self.cases, self.numero, self.game)

class PlayerO(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.numero = 2
        self.cases = []
    def addCase(self, case):
        self.cases.append(case)
        checkWin(self.cases,self.numero, self.game)


def checkWin(cases, number, game):
    b = False
    if 0 in cases and 1 in cases and 2 in cases:
        b = True
    if 3 in cases and 4 in cases and 5 in cases:
        b = True
    if 6 in cases and 7 in cases and 8 in cases:
        b = True
    if 0 in cases and 3 in cases and 6 in cases:
        b = True
    if 1 in cases and 4 in cases and 7 in cases:
        b = True
    if 2 in cases and 5 in cases and 8 in cases:
        b = True
    if 0 in cases and 4 in cases and 8 in cases:
        b = True
    if 2 in cases and 4 in cases and 6 in cases:
        b = True
    if b ==True:
        game.win = True
        game.winner = number
