class Persona:  #creamos una clase
    def __init__(self, nombre, apellido, dni, edad, *args, **kwargs):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self._dni = dni  #este atributo esta encapsulado de una manera sugerida
        self.args = args
        self.kwargs = kwargs

    def mostrar_detalle(self):
        print(f'La clase Persona tiene los siguientes datos: {self.nombre} {self.apellido} {self._dni} Su edad es: {self.edad}, la direccion es : {self.args}, los datos importantes son: {self.kwargs}')

persona1 = Persona('Ariel', 'Betancud', 343452435, 40)
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)
print(f'El objeto1 de la clase persona: {persona1.nombre} {persona1.apellido} Su edad es: {persona1.edad}')

persona2 = Persona('Osvaldo', 'Giordanini',56546463, 45)
print(f'El objeto2 de la clase persona: {persona2.nombre} {persona2.apellido} Su edad es: {persona2.edad}')

persona1.nombre = 'Liliana'
persona1.apellido = 'Buccella'
print(f'El objeto1 modificado de la clase persona: {persona1.nombre} {persona1.apellido} Su edad es: {persona1.edad}')

#los atributos son : caracteristicas
# los metodos son: el comportamiento que van a tener los objetos (acciones)

persona1.mostrar_detalle() # la referencia en este caso se pasa de manera automatica
persona2.mostrar_detalle()

#clase 7

#Persona.mostrar_detalle(persona1) debemos pasarle una referencia para el self o dara error
persona1.telefono = '2434565245235'
print(f'Este es el numero de telefono de: {persona1.nombre} {persona1.telefono}') #hemos creado un atributo de un objeto

#print(persona2.telefono) el objeto persona2 no tiene este atributo, da error

persona3 = Persona('Rogelio', 'Romero',23546462, 22, 'Telefono', '434556564', 'Calle Lopez', 823, 'Manzana', 77, 'Casa', 18, Altura=1.83, Peso=105, CFavorito='Azul', Auto='Citroen', Modelo= 2021)
persona3.mostrar_detalle()
# print(persona3._dni)  esto no se debe utilizar (esta encapsulad)esto dice que lo desconocemos en python
# persona3.__nombre esta totalmente encapsulado