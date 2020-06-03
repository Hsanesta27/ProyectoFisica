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


        '''
        '''

        if self.num == 0:
            LineaPregunta = ListaPreguntas[random.randint(1, 5)]

        elif self.num == 1:
            LineaPregunta = ListaPreguntas[random.randint(6, 7)]

        elif self.num == 2:
            LineaPregunta = ListaPreguntas[random.randint(8, 9)]

        elif self.num == 3:
            LineaPregunta = ListaPreguntas[random.randint(10, 13)]

        elif self.num == 4:
            LineaPregunta = ListaPreguntas[random.randint(14, 14)]

        elif self.num == 5:
            LineaPregunta = ListaPreguntas[random.randint(15, 15)]

        elif self.num == 6:
            LineaPregunta = ListaPreguntas[random.randint(16, 18)]

        elif self.num == 7:
            LineaPregunta = ListaPreguntas[random.randint(19, 21)]

        elif self.num == 8:
            LineaPregunta = ListaPreguntas[random.randint(22, 22)]

        elif self.num == 9:
            LineaPregunta = ListaPreguntas[random.randint(23, 23)]

        elif self.num == 10:
            LineaPregunta = ListaPreguntas[random.randint(24, 24)]

        elif self.num == 11:
            LineaPregunta = ListaPreguntas[random.randint(25, 25)]

        elif self.num == 12:
            LineaPregunta = ListaPreguntas[random.randint(26, 27)]

        elif self.num == 13:
            LineaPregunta = ListaPreguntas[random.randint(28, 28)]

        elif self.num == 14:
            LineaPregunta = ListaPreguntas[random.randint(29, 29)]

        elif self.num == 15:
            LineaPregunta = ListaPreguntas[random.randint(30, 30)]

        self.csvData = LineaPregunta

        if self.csvData[1] == "0":
            self.Pregunta = Text((180, 100), Text.Fpreguntas, self.csvData[0], (252, 148, 3))
        else:
            self.Pregunta = Text((180, 100), Text.Fpreguntas, self.csvData[0], (252, 148, 3))

        self.CódigoRespuestas = []
        self.Respuestas = []

        c = [2, 3, 4]

        for i in range(4):
            self.CódigoRespuestas = [self.csvData[4], self.csvData[7], self.csvData[10], self.csvData[13]]

            self.CódigoRespuestas = [distutils.util.strtobool(i) for i in self.CódigoRespuestas]

            if self.csvData[c[1]] == "0":
                self.Respuestas.append(
                    Respuesta(Text((190, 230 + i * 80), Text.Fpreguntas, self.csvData[c[0]], (252, 148, 3)),
                              self.csvData[c[2]]))
            else:
                self.Respuestas.append(
                    Respuesta(Text((190, 230 + i * 80), Text.Fpreguntas, self.csvData[c[0]], (252, 148, 3)),
                              self.csvData[c[2]]))

            c = [x + 3 for x in c]

    def Preguntar(self):
        self.Pregunta.show()

        for i in range(4):
            self.Respuestas[i].text.show()