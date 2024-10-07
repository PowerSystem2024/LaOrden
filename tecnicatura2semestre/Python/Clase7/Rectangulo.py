class Rectangulo:

    """
    crear una clase llamada rectangulo, debe tener 2 atributos: altura y base
    el nombre del metodo sera calcular el area utilizando la formula:
    area=basee*altura, pero la base u la altura deben ser ingresadas por
    el usuario y los objetots deben ser tres
    """
    def __init__(self,altura,base):
        self.altura = altura
        self.base = base

    def calcular_area(self):
        return self.base * self.altura

base = int(input('Digite el numero para la base del rectangulo: '))
altura = int(input('Digite el numero para la altura del rectangulo: '))
rectangulo1 = Rectangulo(base, altura)
print(f'El area del rectangulo es: {rectangulo1.calcular_area()}')
