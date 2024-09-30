class Persona:


    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        #self.nombre = 'Juan'
        #self.apellido = 'Zalazar'
        #self.edad = 22


    def mostrar_detalle(self):
        print(f'Persona: {self.nombre} {self.apellido} {self.edad}')


#persona1 = Persona()
persona1 = Persona("Ariel", "Betancud", 40)
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)


persona2 = Persona("Osvaldo", "Giordanini", 45)
print(f"El objeto de la clase persona: {persona2.nombre} {persona2.apellido} su edad es: {persona2.edad}")


persona1.nombre = "Liliana"
persona1.apellido = "Buccella"
persona1.edad = 40
print(f"El objeto1 modificado de la clase persona: {persona1.nombre} {persona1.apellido} su edad es: {persona1.edad}")


# Los atribut son caracteristicas
# Los metoods son el comportamiento que van a tener los objetos (acciones)


persona1.mostrar_detalle()
persona2.mostrar_detalle()