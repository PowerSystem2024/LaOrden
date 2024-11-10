from abc import ABC
#ABC significa: abstract base class, convierte una clase en abstracta

class FiguraGeometrica(ABC):
    def __init__(self, alto, ancho):
        # Desde aca se pueden hacer validaciones
        if self._validar_valores(alto):
            self._alto = alto
        else:
            self._alto = 0
            print(f"Valor erroneo para el alto: {alto}")
        if self._validar_valores(ancho):
            self._ancho = ancho
        else:
            print(f"Valor erroneo para le ancho: {ancho}")
            self._ancho = 0

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, alto):
        if self._validar_valores(alto):
            self._alto = alto
        else:
            print(f"Valor erroneo de alto: {alto}")

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, ancho):
        if self._validar_valores(ancho):
            self._ancho = ancho
        else:
            print(f"Valor erroneo de ancho: {ancho}")

    
    def calcular_area(self):
        pass

    def __str__(self, alto, ancho):

        return f"Alto: {self.alto} Ancho: {self.ancho}"

    def _validar_valores(self, valor):
        return True if 0 < valor < 10 else False
