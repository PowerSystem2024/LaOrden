class Vehiculo:
    '''
    Definir una clase padre llamada Vehiculo y dos clases hijas llamdas Auto y Bicicleta, las cuales heredan de la clase padre Vehiculo. La clase padre debe tener los siguientes atributos y metodos:

    Vehiculo(clase padre)
    -Atributos(color, ruedas)
    -Metodos(__init__() y __str__())

    Auto(clase hija de vehiculo)
    -Atributos(velocidad (km/hr))
    -Metodos(__init__() y __str__())

    Bicicleta(clase hija de vehiculo)
    -Atributos(tipo(urbana/montaña-etc))
    -Metodos(__init__() y __str__())

    Crear un objeto de cada clase
    '''

    def __init__(self, color, ruedas):
        self._color = color
        self._ruedas = ruedas

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    @property
    def ruedas(self):
        return self._ruedas

    @ruedas.setter
    def ruedas(self, ruedas):
        self._ruedas = ruedas

    def __str__(self):
        return f"Color: {self._color}, Ruedas: {self._ruedas}"


class Auto(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self._velocidad = velocidad

    @property
    def velocidad(self):
        return self._velocidad

    @velocidad.setter
    def velocidad(self, velocidad):
        self._velocidad = velocidad

    def __str__(self):
        return f"Velocidad: {self._velocidad}km/h {super().__str__()}"


class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self._tipo = tipo

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo

    def __str__(self):
        return f"Tipo: {self._tipo} {super().__str__()}"\

auto1=Auto("Rojo", 4, "200")
print(auto1.color)
