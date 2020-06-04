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
            LineaPregunta = ListaPreguntas[random.randint(1, 2)]

        elif self.num == 1:
            LineaPregunta = ListaPreguntas[random.randint(3, 3)]

        elif self.num == 2:
            LineaPregunta = ListaPreguntas[random.randint(4, 6)]

        elif self.num == 3:
            LineaPregunta = ListaPreguntas[random.randint(7, 7)]

        elif self.num == 4:
            LineaPregunta = ListaPreguntas[random.randint(8, 10)]

        elif self.num == 5:
            LineaPregunta = ListaPreguntas[random.randint(11, 13)]

        elif self.num == 6:
            LineaPregunta = ListaPreguntas[random.randint(14, 16)]

        elif self.num == 7:
            LineaPregunta = ListaPreguntas[random.randint(17, 17)]

        elif self.num == 8:
            LineaPregunta = ListaPreguntas[random.randint(18, 18)]

        elif self.num == 9:
            LineaPregunta = ListaPreguntas[random.randint(19, 22)]

        elif self.num == 10:
            LineaPregunta = ListaPreguntas[random.randint(23, 25)]

        elif self.num == 11:
            LineaPregunta = ListaPreguntas[random.randint(26, 26)]

        elif self.num == 12:
            LineaPregunta = ListaPreguntas[random.randint(27, 27)]

        elif self.num == 13:
            LineaPregunta = ListaPreguntas[random.randint(28, 28)]

        elif self.num == 14:
            LineaPregunta = ListaPreguntas[random.randint(29, 29)]

        elif self.num == 15:
            LineaPregunta = ListaPreguntas[random.randint(30, 31)]

        elif self.num == 16:
            LineaPregunta = ListaPreguntas[random.randint(32, 33)]

        elif self.num == 17:
            LineaPregunta = ListaPreguntas[random.randint(34, 35)]

        elif self.num == 18:
            LineaPregunta = ListaPreguntas[random.randint(36, 37)]

        self.csvData = LineaPregunta

        self.Pregunta = Text((180, 100), Text.Fpreguntas, self.csvData[0], (252, 148, 3))

        self.CódigoRespuestas = []
        self.Respuestas = []

        for i in range(4):
            self.CódigoRespuestas.append(self.csvData[2+2*i])

        self.CódigoRespuestas = [distutils.util.strtobool(i) for i in self.CódigoRespuestas]

        for i in range(4):
            self.Respuestas.append(Respuesta(Text((190, 230 + i * 80), Text.Fpreguntas, self.csvData[1+2*i], (252, 148, 3)),self.csvData[2+2*i]))

        self.value=int(self.csvData[9])

    def Preguntar(self):
        self.Pregunta.show()

        for i in range(4):
            self.Respuestas[i].text.show()