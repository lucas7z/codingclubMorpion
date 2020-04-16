import pygame, time
from game import Game

pygame.init()
pygame.display.set_caption("Morpion")
screen = pygame.display.set_mode((596,700))
background = pygame.image.load('assets/background.png')
game = Game()
running = True
while(running):
    game.TextToPlay.setNumero(game.inPlaying.numero)
    screen.blit(background,(0,0))
    for case in game.cases:
        if case.isTaked ==False:
            screen.blit(case.text, case.rect)
        else:
            screen.blit(case.image, case.rect)
    screen.blit(game.TextToPlay.text, game.TextToPlay.rect)
    pygame.display.flip()
    b = False
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            running = False
            pygame.quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_KP0:
                game.setCase(0)
                b = game.check()
            elif event.key == pygame.K_KP1:
                game.setCase(1)
                b = game.check()
            elif event.key == pygame.K_KP2:
                game.setCase(2)
                b = game.check()
            elif event.key == pygame.K_KP3:
                game.setCase(3)
                b = game.check()
            elif event.key == pygame.K_KP4:
                game.setCase(4)
                b = game.check()
            elif event.key == pygame.K_KP5:
                game.setCase(5)
                b = game.check()
            elif event.key == pygame.K_KP6:
                game.setCase(6)
                b = game.check()
            elif event.key == pygame.K_KP7:
                game.setCase(7)
                b = game.check()
            elif event.key == pygame.K_KP8:
                game.setCase(8)
                b = game.check()
    for case in game.cases:
        if case.isTaked ==False:
            screen.blit(case.text, case.rect)
        else:
            screen.blit(case.image, case.rect)
    pygame.display.flip()
    b=game.check()
    if game.win == True:
        time.sleep(2)
        running = False
        pygame.quit()
        print("Partie Terminé, remporté par le joueur "+game.winner+" !")
    if b==True:
        time.sleep(2)
        running = False
        pygame.quit()
        print("Partie Terminé pas de gagnant !")
           
        