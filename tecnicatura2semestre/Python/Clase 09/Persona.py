class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    # Para que los atributos de esta clase puedan ser usados cuando importamos esta clase en otra hay que sobreescribirlos, es lo mismo que lo que se conoce como toString en java, Override
    def __str__(self):
        return f"Persona:[Nombre: {self._nombre}, Edad: {self._edad}]"


class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self._sueldo = sueldo

    @property
    def sueldo(self):
        return self._sueldo

    @sueldo.setter
    def sueldo(self, sueldo):
        self._sueldo = sueldo

    def __str__(self):
        return f"Empleado: [Sueldo: {self._sueldo}] {super().__str__()}"


empleado1 = Empleado("Leandro", "Enriquez", 7500)
print(empleado1.nombre)
print(empleado1.edad)
print(empleado1.sueldo)
