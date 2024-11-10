from FiguraGeometrica import FiguraGeometrica
from Color import Color


class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, alto, ancho, color):
        # super().__init__(alto, ancho) esto no se hace si tenes herencia multiple, en su lugar llamas directamente a la clase padre correspondiente
        FiguraGeometrica.__init__(self, alto, ancho)
        Color.__init__(self, color)

    def calcular_area(self):
        return self._alto * self._ancho

    def __str__(self):
        return f"{FiguraGeometrica.__str__(self)}{Color.__str__(self)}"
