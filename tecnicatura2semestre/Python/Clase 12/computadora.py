from monitor import Monitor
from raton import Raton
from teclado import Teclado


class Computadora:
    contador_computadoras = 0

    def __init__(self, nombre, monitor, teclado, raton):
        Computadora.contador_computadoras += 1
        self._id_computadora = Computadora.contador_computadoras
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton

    def __str__(self):
        return f"""
        {self._nombre}:{self._id_computadora}
        Monitor: {self._monitor}
        Teclado: {self._teclado}
        Raton: {self._raton}
        """


if __name__ == "__main__":
    teclado1 = Teclado("HP", "USB")
    monitor1 = Monitor("LG", "32")
    raton1 = Raton("Razer", "BT")
    computadora1 = Computadora("MSI", monitor1, teclado1, raton1)

    print(computadora1)
