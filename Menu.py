__author__ = 'AnkuR'
import pygame
from Engine import screen,clock,FPS


menus=(pygame.image.load('_menu.bmp'),pygame.image.load('_instr.bmp'),pygame.image.load('_credits.bmp'))


def menuloop():
    global old,new
    screen.blit(menus[0], (0,0))
    pygame.display.update()
    old=new=0
    while MenuManager.events():
        if old!=new:
            screen.fill((0,0,0))
            screen.blit(menus[new], (0,0))
            pygame.display.update()
            old=new

        clock.tick(FPS)





class MenuManager:
    @staticmethod
    def events():
        global new
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # if close button(X) is pressed, then quit the program
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_m:
                    new=0
                elif event.key == pygame.K_i:
                    new=1
                elif event.key == pygame.K_c:
                    new=2
                elif event.key == pygame.K_p:
                    return False

        return True

