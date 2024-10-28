class Persona2:
    def __init__(self, nombre, apellido, edad):
        self._nombre = nombre
        self._apellido = apellido
        self._edad = edad

    def mostrar_detalles(self):
        print(f'Los datos a mostrar son los siguientes:{
              self._nombre} {self._apellido} {self._edad}')

    @property
    def nombre(self):  # metodo getter
        return self._nombre
    print('Estamos utilizando el metodo get')

    @nombre.setter
    def nombre(self, nombre):  # metodo setter
        print('Estamos utilizando el metodo set')
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        self._apellido = apellido

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    def __del__(self):
        print(f'Persona2: {self._nombre} {self._apellido} {self._edad}')


if __name__ == '__main__':
    persona1 = Persona2('Ariel', 'Betancud', 41)
    print(persona1.nombre)  # llamamos al metodo getter

    persona1.nombre = 'Lucas'  # metodo setter
    print(persona1.nombre)
    print(persona1.mostrar_detalles())
# atributo read-only seria la edad porque no tiene el metodo set
    print(persona1.edad)

# Tarea clase 7

    persona2 = Persona2('Luciana', 'Fragueiro', 27)
    print(persona2.nombre)
    print(persona2.apellido)
    print(persona2.edad)
    persona2.nombre = 'Karen'
    persona2.apellido = "Bondi"
    persona2.edad = 25
    print(persona2.mostrar_detalles())

    persona3 = Persona2('Naibi', 'Moya', 28)
    print(persona3.nombre)
    print(persona3.apellido)
    print(persona3.edad)
    persona3.nombre = 'Maria'
    persona3.apellido = 'Lopez'
    persona3.edad = 23
    print(persona3.mostrar_detalles())

    persona4 = Persona2('Lucas', 'Gaitan', 45)
    print(persona4.nombre)
    print(persona4.apellido)
    print(persona4.edad)
    persona4.nombre = 'Martin'
    persona4.apellido = 'Cabo'
    persona4.edad = 34
    print(persona4.mostrar_detalles())

    print(__name__)
