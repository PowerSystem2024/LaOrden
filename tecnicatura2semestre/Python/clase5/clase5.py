# Comenzamos con funciones
#  mi_funcion() no se puede llamar antes de definir a una funcion
#  definimos una funcion

def mi_funcion():
    print('Saludos desde funcion')


mi_funcion()
mi_funcion()

# Desempaquetado de listas
def show(name, lastname):
    print(name + ' ' + lastname)
person = ['Ariel', 'Betancud']
show(person[0], person[1])
show(*person)
person2 = ('Osvaldo', 'Giordanini')
show(*person2)
person3 = {'lastname': 'Lucero', 'name', 'Natalia'}
show(**person3)


numbers = [1, 2, 3, 4, 5]
for n in numbers:
    print(n)
    if n == 3:
        break
else:
    print('Esto se termino')




# List compehension, lista de comprension
names = ['Paolo', 'Rodrigo', 'Lupe', 'Pepe']
alongP = [p for p in names if p[0] == 'P']
print(alongP)


bottleC = [{"name": "Quilmes", "country", "Arg"},
            {"name": "Corona", "country", "Mx"}
            {"name": "Stella Artois", "country", "Belgium"}
            ]

Arg = [b for b in bottleC if b["country"] == "Arg"]
print(Arg)
print(bottleC)


# Paso de argumentos (funciones)
def mi_funcion2(name, lastname):
    print("Saludos a todos los que ven a traves de youtube")
    print(f"Nombre: {name} , Apellido: {lastname}")

mi_funcion2("Jorge", "Lucero")
mi_funcion2("Ariel", "Betancud")
mi_funcion2("Analia", "Pedrosa")

# La palabra return en funciones

def sumar(a, b):
    return a + b

print(f"El resutlado de la suma es: {sumar(55, 45)}")


def sumar2(a = 0, b = 0):
    return a + b
resultado = sumar2()
print(f"El resultado de la suma: {resultado}")
print(f"El resultado de la suma: {sumar2(22, 56)}")


def listarNombres(*nombres):
    for nombre in nombres:
        print(nombre)
listarNombres("Lucas", "Jose", "Claudia")
listarNombres("Marcos", "Daniel", "Romina")


def listarTerminos(**terminos):
    for llave, valor in terminos.items():
        print(f'{llave} : {valor}')

listarTerminos(IDE='Integrated Development Environment', PK='Primary key')

def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)
nombres2 = ["Tito", "Pedro", "Carlos"]
desplegarNombres(nombres2)
desplegarNombres("Carla")
desplegarNombres((10, 11))



# Funciones recursivas
def factorial(numero):
    if numero ==1:
        return 1 
    else:
        return numero * factorial(numero-1)
resultado = factorial(5)
print(f"El factorial de 5 es: {resultado}")