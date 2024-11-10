class Persona:
    contador_personas = 0  # variable de clase

    @classmethod
    def generar_siguiente_valor(cls):
        cls.contador_personas += 1
        return cls.contador_personas

    def __init__(self, nombre, edad):
        # llamamos a la variable de clase y le agregamos un contador
        self.id_persona = Persona.generar_siguiente_valor()
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"Persona[{self.id_persona} {self.nombre} {self.edad}]"


persona1 = Persona("Leandro", 30)
print(persona1)
persona2 = Persona("Jojo", 33)
print(persona2)
persona3 = Persona("Meme", 44)
print(persona3)

# Al hacer el llamado al init y acuenta como +1
Persona.generar_siguiente_valor()
# Por eso en este llamado esta persona ya es 5
persona4 = Persona("Lili", 22)
print(persona4)
