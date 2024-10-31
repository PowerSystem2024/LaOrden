class MiClase:  # Em py todas las clases son objetos
    # Variable de clase, este atributo dara a cada objeto el mismo valor, vendria a ser como una constante, solo se puede acceder directamente desde la clase
    variable_clase = "Esta es una variable de clase"

    def __init__(self, variable_instancia):  # La variable de instancia, da diferentes valores
        self.variable_instancia = variable_instancia

    # Metodos estaticos como a las variables estaticas se asocian a la clase y no al objeto, para ejecutar un metodo estatico sera a traves de la clase y necesitan un decorador, un __ini__ esta dentro del ambito dinamico ya que esta creado para la instancia de objetos
    @staticmethod
    def metodo_estatico():  # Metodo estatico se asocia a la clase
        print(MiClase.variable_clase)

    # El cls es una referencia a la clase en si misma, igualmente puede usarse con otras palabras
    @classmethod
    def metodo_clase(cls):
        print(cls.variable_clase)

    def metodo_instancia(self):
        self.metodo_clase()
        self.metodo_estatico()
        print(self.variable_clase)
        print(self.variable_instancia)


# Esta es la unica forma de acceder a una variable de clase, no desde un objeto sino desde la clase misma, tambien los objetos pueden acceder a la misma pero todos tendran el mismo valor ya que el valor de esta variable esta asociada con una clase y no con un objeto.
print(MiClase.variable_clase)

# Esta es una variable de instancia, se accede a partir de un objeto.
miClase1 = MiClase("Esta es una variable de instancia")
print(miClase1.variable_instancia)
print(MiClase.variable_clase)
miClase2 = MiClase("Esta es otra prueba de variable de instancia")
print(miClase2.variable_instancia)
print(miClase2.variable_clase)

# Podemos crear una variable de clase fuera de la clase y llamarla desde la clase y desde un objeto
MiClase.variable_clase2 = "Valor de variable de clase 2"
print(MiClase.variable_clase2)
print(miClase1.variable_clase2)


# Llamamos al metodo estatico
MiClase.metodo_estatico()
MiClase.metodo_clase()

# El contexto dinamico puede acceder al estatico mediante un objeto, pero nunca un contexto estatico puede acceder a un dinamico

miObjeto1 = MiClase("Variable de instancia")
miObjeto1.metodo_clase()

miObjeto1.metodo_instancia
