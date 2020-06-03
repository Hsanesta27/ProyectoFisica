import pygame
from Interactivos import *
from Preguntas import *
import math
import time


class Pantalla:
    Pantalla = 0
    Cargado = 0
    TextoP = 0
    Iteración = 0
    '''
    0 = MENÚ PRINCIPAL
    1 = PRESENTACIÓN
    2 = JUEGO
    3 = RESULTADOS
    '''

    Widgets = []
    Texts = []

    @staticmethod
    def CargaPantalla0():
        Pantalla.Cargado = 0
        Logo = Widget((286, 50), "Recursos/Imagen/Logo.png")

        BotónJugar = Button((320, 480), (
            "Recursos/Imagen/BotónJugar.png", "Recursos/Imagen/BotónJugar.png", "Recursos/Imagen/BotónJugarTocado.png"),
                            0,
                            3)

        Pantalla.Widgets = [Logo, BotónJugar]

        Créditos = Text((480, 616), Text.LM24, "Creado por Lucía Benlloch y Hugo Sánchez", (2, 0, 99))

        Pantalla.Texts = [Créditos]

    @staticmethod
    def CargaPantalla1():
        Pantalla.Cargado = 1
        Pantalla.TextoP = 0
        Pantalla.Iteración = 0

        Fondo = Widget((0, 0), "Recursos/Imagen/ImagenPlató.jpg")

        Chat = Widget((0, 560), "Recursos/Imagen/Chat.png")

        Pantalla.Widgets = [Fondo, Chat]

        '''Quién quiere ser nobel! El juego en el que tendrás que resolver 30 preguntas  de ciencia para llevarte no solo el millón de dólares que suponen el premio sino el doble, estás preparad@? pues adelante y mucha suerte!'''

        P1_1 = Text((0, 565), Text.arial24,
                    "Quién quiere ser nobel! El juego en el que tendrás que resolver 30 preguntas de",
                    (2, 0, 99))
        P1_2 = Text((0, 589), Text.arial24,
                    "ciencia para llevarte no solo el millón de dólares que suponen el premio, sino el doble!", (2, 0, 99))

        P1 = (P1_1, P1_2)

        P2 = Text((0, 565), Text.arial24, "Estás list@?", (2, 0, 99))

        P3 = Text((0, 565), Text.arial24, "Pues adelante y mucha suerte!", (2, 0, 99))

        Pantalla.Texts = [P1, P2, P3]

    @staticmethod
    def CargaPantalla2():
        Pantalla.Cargado=2

        Fondo1=Widget((0,0),"Recursos/Imagen/FondoParaPreguntas.jpg")
        Fondo2 = Widget((0,380), "Recursos/Imagen/FondoPreguntasBajo.png")

        BasePregunta=Button((0,382),("Recursos/Imagen/PreguntaAzul.png","Recursos/Imagen/PreguntaRoja.png","Recursos/Imagen/PreguntaVerde.png"),0,3)
        BaseRespuestas=[]

        for i in range(2):
            for j in range(2):
                BaseRespuestas.append(Button((0+490*i,470+88*j),("Recursos/Imagen/RespuestaAzul.png","Recursos/Imagen/RespuestaRoja.png","Recursos/Imagen/RespuestaVerde.png"),0,3))

        Pantalla.Widgets=[Fondo1,Fondo2,BasePregunta,BaseRespuestas]
        Pantalla.Texts=[]

    @staticmethod
    def CargaPantalla3():
        pass

    @staticmethod
    def Pantalla0():
        for Text in Pantalla.Texts:
            Text.show()

        for Widget in Pantalla.Widgets:
            Widget.show()

        if Pantalla.Widgets[1].Clicked():
            Pantalla.Widgets[1].ChangeState(1)
            Pantalla.Pantalla = 1
        if Pantalla.Widgets[1].Touched():
            Pantalla.Widgets[1].ChangeState(2)
        elif not Pantalla.Widgets[1].Touched():
            Pantalla.Widgets[1].ChangeState(0)

    @staticmethod
    def Pantalla1():
        from Main import Eventos

        for Widget in Pantalla.Widgets:
            Widget.show()

        if Pantalla.TextoP == 0:
            for i in range(len(Pantalla.Texts[Pantalla.TextoP])):
                Pantalla.Texts[Pantalla.TextoP][i].show()
        else:
            Pantalla.Texts[Pantalla.TextoP].show()

        time.sleep(0.1)

        CortarIteración = False

        if Pantalla.Iteración==0:
            pass
        elif Eventos[2]:
            Pantalla.TextoP += 1
            CortarIteración=True

        if Pantalla.TextoP > 2:
            Pantalla.Pantalla = 2

        if not CortarIteración:
            Pantalla.Iteración+=1
    @staticmethod
    def Pantalla2():
        for Text in Pantalla.Texts:
            Text.show()

        for Widget in Pantalla.Widgets:
            if Widget==Pantalla.Widgets[3]:
                for i in Widget:
                    i.show()
            else:
                Widget.show()

    @staticmethod
    def Pantalla3():
        pass
