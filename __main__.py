from time import localtime, strftime
import pygame
from pygame.locals import *
import os
import sys

SCREEN_WIDTH = 310
SCREEN_HEIGHT = 80
COLOR = (224,128,128)

def esPrimo(numero):
    if (numero <= 1):
        return False
    if (numero in [2,3,5]):
        return True
    if ((numero % 6) in [2, 3, 4, 0]):
        return False
    top = int(numero**0.5) + 2

    for div in range(5,top,6):
        if (numero % div == 0):
            return False
        if  (numero % (div + 2) == 0):
            return False

    return True

def prueba():
    maxFallos = 0
    fallos = 0
    for hora in range(0, 24):
        for minuto in range(0, 60):
            for segundo in range(0,60):
                valor = hora * 10000 + minuto * 100 + segundo
                if esPrimo(valor):
                    print(valor, ", ", fallos)
                    if (fallos > maxFallos):
                        maxFallos = fallos
                    fallos = 0
                else:
                    fallos += 1
    print ("Lapso máximo : ", maxFallos, " segundos")

def modoTexto():
    tiempo = localtime()
    valor = tiempo.tm_hour * 10000 + tiempo.tm_min * 100 +tiempo.tm_sec
    if esPrimo(valor):
        print(strftime("%H:%M:%S", tiempo), end = '\r')

def main():
    pygame.init()
#    pygame.mixer.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("PriClock")
    pygame.font.init() 

    font = pygame.font.Font("DSEG7Classic-Regular.ttf", 64)
    text_surface = font.render("-WAIT-", False, (110, 110, 110))
    screen.blit(text_surface, (0,5))
    clock = pygame.time.Clock()
    pygame.display.flip()
    fondo = font.render("88.88.88", False, (24, 16, 16))
    puntos = False
    tiempoDis = False
    fallos = 0

    while 1:
        clock.tick(2)
        tiempo = localtime()
        valor = tiempo.tm_hour * 10000 + tiempo.tm_min * 100 + tiempo.tm_sec
        if esPrimo(valor):
            screen.fill((0,0,0))
            tiempoDis = tiempo
            fallos = 0
        else:
            fallos = fallos + 1

        if tiempoDis:
            screen.blit(fondo, (0,5))
            if puntos:
                text_surface = font.render(strftime("%H.%M.%S", tiempoDis), False, COLOR)
                puntos = False
            else:
                text_surface = font.render(strftime("%H%M%S", tiempoDis), False, COLOR)
                puntos = True
            screen.blit(text_surface, (0,5))

        pygame.draw.rect(screen, COLOR, pygame.Rect(5, 73, fallos * 2 + 1, 5))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)



if __name__ == "__main__":
#    prueba()
#    modoTexto()
    main()