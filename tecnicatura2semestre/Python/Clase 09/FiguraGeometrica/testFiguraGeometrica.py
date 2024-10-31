from Cuadrado import Cuadrado
from Rectangulo import Rectangulo
from Color import Color
from FiguraGeometrica import FiguraGeometrica

cuadrado1 = Cuadrado(5, 5, "Azul")
cuadrado1.alto = -10
print(cuadrado1.ancho)
print(cuadrado1.alto)
print(cuadrado1.color)
print(f"La superficie es: {cuadrado1.calcular_area()}")

# MRO = Method Resolution Order
print(Cuadrado.mro())

rectangulo1 = Rectangulo(5, 9, "Verde")
rectangulo1.ancho = 11

print(rectangulo1.ancho)
print(rectangulo1.alto)
print(rectangulo1.color)
print(f"La superficie es: {rectangulo1.calcular_area()}")

#figura1 = FiguraGeometrica() no se puede isntanciar, es abstracta
