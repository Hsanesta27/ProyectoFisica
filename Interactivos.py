import pygame
from PIL import Image


class Widget:

    def __init__(self, coords, path):
        self.coordinates = coords
        self.path1 = path
        self.gameImage = pygame.image.load(path)

    def show(self):
        from Main import screen
        screen.blit(self.gameImage, self.coordinates)


class Button(Widget):
    def __init__(self, coords, paths, value, type):
        super().__init__(coords, paths[value])

        self.value = value
        self.type = type

        self.gameImages = []
        self.PILimages = []

        for i in range(type):
            self.gameImages.append(pygame.image.load(paths[i]))
            self.PILimages.append(Image.open(paths[i]))

        self.defaultValue = 0

    def ChangeState(self, newState=1):

        self.value = newState
        self.gameImage = self.gameImages[newState]

    def Touched(self):
        from Main import Eventos

        GlobalCoordinates = Eventos[5]

        self.PILsize = self.PILimages[self.value].size

        if len(GlobalCoordinates) == 2:
            RelativeCoordinates = (GlobalCoordinates[0] - self.coordinates[0],
                                   GlobalCoordinates[1] - self.coordinates[1])

            MouseInside = False

            if 0 <= RelativeCoordinates[0] < self.PILsize[0] - 1 and 0 <= RelativeCoordinates[1] < self.PILsize[1] - 1:
                MouseInside = True

            if MouseInside:

                PixelColor = self.PILimages[self.value].getpixel(
                    (RelativeCoordinates[0] - 1, RelativeCoordinates[1] - 1))

                if len(PixelColor) == 4:
                    if PixelColor[3] == 255:
                        return True
                    else:
                        return False
                else:
                    return True
            else:
                return False

    def Clicked(self):
        from Main import Eventos

        if self.Touched() and Eventos[2]:
            return True
        else:
            return False


class Text:
    pygame.font.init()

    LM24 = pygame.font.Font("Recursos/Fuentes/latinmodern-math.otf", 24)
    LM32 = pygame.font.Font("Recursos/Fuentes/latinmodern-math.otf", 32)
    LM16 = pygame.font.Font("Recursos/Fuentes/latinmodern-math.otf", 16)
    arial20 = pygame.font.Font("Recursos/Fuentes/ArialCE.ttf", 20)
    arial24 = pygame.font.Font("Recursos/Fuentes/ArialCE.ttf", 24)
    arial42 = pygame.font.Font("Recursos/Fuentes/ArialCE.ttf", 42)
    Fpreguntas = pygame.font.Font("Recursos/Fuentes/ArialDef.ttf", 20)

    def __init__(self, coords, font, str, color):
        self.message = str
        self.color = color
        self.coordinates = coords
        self.font = font

        self.TextObject = False

    def show(self):
        from Main import screen

        self.TextObject = self.font.render(self.message, True, self.color)
        screen.blit(self.TextObject, self.coordinates)