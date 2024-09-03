# Repaso de set o conjunto
# para definir un conjunto
conjunto2 = set()
conjunto1 = {'bye',}
conjunto2.add(7)
conjunto2.add('Hola')
print(conjunto2)
conjunto1.add('hola')
print(conjunto1)
print(3 not in conjunto1)  # preguntamos si el numero 3 no esta en el conjunto1

# Como hacer la igualdad de dos conjuntos
print(conjunto1 == conjunto2)  # Nos devuelve como respuesta un booleano

# operaciones en conjuntos
conjunto3 = conjunto1 | conjunto2  # la linea une los dos conjuntos
print(conjunto3)

conjunto3 = conjunto1 & conjunto2  # que elemento tienen en comun
print(conjunto3)

conjunto3 = conjunto1 - conjunto2  # asigna el valor que esta en el conjunto1 y no en el conjunto2
print(conjunto3)

conjunto3 = conjunto2 - conjunto1
print(conjunto3)

conjunto3 = conjunto1 ^ conjunto2  # elementos que no comparten o que son diferentes entre ambos
print(conjunto3)

conjunto3 = conjunto1 | conjunto2
print(conjunto2.issubset(conjunto3))  # preguntamos si un conjunto es un subconjunto dentro de otro
print(conjunto1.issubset(conjunto3))
print(conjunto3.issubset(conjunto1))
print(conjunto3.issubset(conjunto2))

print(conjunto3.issubset(conjunto1)) # si los elementos del conj1 estan dentro del 3
print(conjunto3.issubset(conjunto2))  # si es Verdadero quiere decir que el conj3 es un superconjunto
print(conjunto2.issubset(conjunto3))

# como saber si ambos conjuntos son disconexos, esto es si no compartes elementos en comun
print(conjunto1.isdisjoint(conjunto2))  # no hay cosas en comun

# convertir un conjunto totalmente en inmutable
conjunto1 = frozenset  # esto hace que el conjunto sea totalmente inmutable
# no se puede agregar, modificar ni eliminar elementos del conjunto

# repaso diccionarios
diccionarioNuevo = {'Azul': 'Blue','Rojo': 'Red', 'Verde': 'Green', 'Amarillo': 'Yellow'}
print(diccionarioNuevo)

# Como eliminar
del(diccionarioNuevo['Azul'])
print(diccionarioNuevo)

# Los diccionarios pueden almacenar diferentes tipos de datos
diccionario2 = {'Ariel':{'Edad': 40, 'Altura': 1.83}, 'Osvaldo': [45, 1.85], 'Natalia': [35, 1.67]}
print(diccionario2)

seleccionArgentina = {10: {'Nombre': 'Lionel Messi', 'Edad': 35, 'Altura': 1.70, 'Precio': '50 Millones', 'Posicion': 'Extremo Derecho'},
                      11: {'Nombre': 'Angel Di Maria', 'Edad': 34, 'Altura': 1.80, 'Precio': '12 Millones', 'Posicion': 'Extremo Derecho'},
                      24: {'Nombre': 'Paulo Dybala', 'Edad': 28, 'Altura': 1.77, 'Precio': '35 Millones', 'Posicion': 'Media Punta'},
                      19: {'Nombre': 'Nicolas Otamendi', 'Edad': 34, 'Altura': 1.83, 'Precio': '3.5 Millones', 'Posicion': 'Defensa Central'},
                      1: {'Nombre': 'Franco Armanni', 'Edad': 35, 'Altura': 1.89, 'Precio': '3.5 Millones', 'Posicion': 'Portero'}
                      }
print(seleccionArgentina)

for llave, valor in seleccionArgentina.items():
    print(llave,valor)

# como tarea agregar por lo menos 4 jugadores mas al diccionario seleccionArgentina

print('Tenemos cargados en el diccionario la cantidad de jugadores: ', end=' ')
print(len(seleccionArgentina))

# pilas usando listas
pila = [1, 2, 3]

# agregar elementos  ala pila por el final
pila.append(4)
pila.append(5)
print(pila)

# sacamos elementos desde el final
elementoBorrado = pila.pop()  # Quia el ultimo elemento y lo guarda en la variable
print(f'Sacamos el elemento {elementoBorrado}')
print(f'La pila ahora quedo asi: {pila}')

# Colas con listas
#Estructuras de datos de tipo fifo(first input/first output)
cola = ['Ariel', 'Osvaldo', 'Liliana', 'Pilar']

# Agregamos elementos al final de la cola
cola.append('Natalia')
cola.append('Jose')
print(cola)

# Sacamos elementos de la cola
seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)











