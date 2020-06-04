import random
import csv
from Interactivos import *
import distutils
from distutils import util


class Respuesta():
    def __init__(self, text, correct):
        self.text = text
        self.correct = correct


class Pregunta():
    def __init__(self, num):
        txtf = open("Recursos/Preguntas.csv", newline='')
        Reader = csv.reader(txtf)

        ListaPreguntas = []

        for i in Reader:
            ListaPreguntas.append(i)

        self.num = num

        LineaPregunta = ""

        if self.num == 0:
            LineaPregunta = ListaPreguntas[random.randint(0, 1)]

        elif self.num == 1:
            LineaPregunta = ListaPreguntas[random.randint(2, 2)]

        elif self.num == 2:
            LineaPregunta = ListaPreguntas[random.randint(3, 5)]

        elif self.num == 3:
            LineaPregunta = ListaPreguntas[random.randint(6, 6)]

        elif self.num == 4:
            LineaPregunta = ListaPreguntas[random.randint(7, 9)]

        elif self.num == 5:
            LineaPregunta = ListaPreguntas[random.randint(10, 12)]

        elif self.num == 6:
            LineaPregunta = ListaPreguntas[random.randint(13, 15)]

        elif self.num == 7:
            LineaPregunta = ListaPreguntas[random.randint(16, 16)]

        elif self.num == 8:
            LineaPregunta = ListaPreguntas[random.randint(17, 17)]

        elif self.num == 9:
            LineaPregunta = ListaPreguntas[random.randint(18, 21)]

        elif self.num == 10:
            LineaPregunta = ListaPreguntas[random.randint(22, 24)]

        elif self.num == 11:
            LineaPregunta = ListaPreguntas[random.randint(25, 25)]

        elif self.num == 12:
            LineaPregunta = ListaPreguntas[random.randint(26, 26)]

        elif self.num == 13:
            LineaPregunta = ListaPreguntas[random.randint(27, 27)]

        elif self.num == 14:
            LineaPregunta = ListaPreguntas[random.randint(28, 28)]

        elif self.num == 15:
            LineaPregunta = ListaPreguntas[random.randint(29, 30)]

        elif self.num == 16:
            LineaPregunta = ListaPreguntas[random.randint(31, 32)]

        elif self.num == 17:
            LineaPregunta = ListaPreguntas[random.randint(33, 34)]

        elif self.num == 18:
            LineaPregunta = ListaPreguntas[random.randint(35, 36)]

        self.csvData = LineaPregunta

        self.Pregunta = Text((45, 407), Text.Fpreg24, self.csvData[0], (100,100,100))

        self.CódigoRespuestas = []
        self.Respuestas = []

        for i in range(4):
            self.CódigoRespuestas.append(self.csvData[2+2*i])

        self.CódigoRespuestas = [distutils.util.strtobool(i) for i in self.CódigoRespuestas]

        c=0
        for i in range(2):
            for j in range(2):
                self.Respuestas.append(Respuesta(Text((40 + i * 490, 497 + j * 88), Text.Fpreg18, self.csvData[1+2*c], (100,100,100)),self.csvData[2+2*i]))
                c+=1


        self.value=int(self.csvData[9])

    def Preguntar(self):
        self.Pregunta.show()

        for i in range(4):
            self.Respuestas[i].text.show()