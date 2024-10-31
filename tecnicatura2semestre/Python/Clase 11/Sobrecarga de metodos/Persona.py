class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __add__(self, other):
        return f"{self.nombre} {other.nombre}"

    def __sub__(self, other):
        return self.edad - other.edad


persona1 = Persona("Leandro", 25)
persona2 = Persona("Enriquez", 5)

# Esta seria la sintaxis interna y automatica
# persona1.__add__(persona2)

# Esta seria la verdadera sintaxis, no es necesario invocar el metodo de manera manual, ya solo con el operador + identifica que son objetos y llama a automaticamente al metodo
print(persona1 + persona2)
print(persona1 - persona2)
