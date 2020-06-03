import pygame
from Pantallas import Pantalla

pygame.init()

screen=pygame.display.set_mode((960,640))
pygame.display.set_caption("Quién quiere ser Nobel")

icono = pygame.image.load("Recursos/Imagen/icono.png")
pygame.display.set_icon(icono)

'''

Lista de variables:
0 = QUIT event
1 = MOUSEBUTTONUP
2 = MOUSEBUTTONDOWN
3 = KEYUP
4 = KEYDOWN
5 = MOUSEMOTION

'''

Eventos = [True, False, False, (), (), ()]

Pantalla.CargaPantalla0()

while Eventos[0]:

    pygame.display.update()


    if Pantalla.Pantalla == 0 and Pantalla.Cargado == 0:
        Pantalla.Pantalla0()
    elif Pantalla.Pantalla == 0:
        Pantalla.CargaPantalla0()

    if Pantalla.Pantalla == 1 and Pantalla.Cargado == 1:
        Pantalla.Pantalla1()
    elif Pantalla.Pantalla == 1:
        Pantalla.CargaPantalla1()

    if Pantalla.Pantalla == 2 and Pantalla.Cargado == 2:
        Pantalla.Pantalla2()
    elif Pantalla.Pantalla == 2:
        Pantalla.CargaPantalla2()

    if Pantalla.Pantalla == 3 and Pantalla.Cargado == 3:
        Pantalla.Pantalla3()
    elif Pantalla.Pantalla == 3:
        Pantalla.CargaPantalla3()


    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            Eventos[0] = False
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                Eventos[2] = True
                Eventos[1] = False

        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                Eventos[1] = True
                Eventos[2] = False
        if event.type == pygame.MOUSEMOTION:
            Eventos[5] = event.pos