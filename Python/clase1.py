# lista = Ariel , Liliana, Natalia, Osvaldo

# Colecciones en Python

# Las listas es lo que se conoce en otros lenguajes como arreglos o vectores

nombres = ['Naty', 'Osvaldo', 'Lily', 'Ariel']
print(nombres)
print(nombres[0])   # imprimo naty
print(nombres[1])   # imprimo osvaldo
print(nombres[3])   # imprimo ariel
print(nombres[-1])  # imprimo Ariel

print(nombres[0:2])  # recorre del 0 al 1
# ir del inicio de la lista al indice (sin incluirlo)
print(nombres[ :3])  # muestra 0,1,2
# Desde el indice indicado hasa el final
print(nombres[1: ])
# Modificamos un valor
nombres[2] = 'Liliana'
nombres[0] = 'Natalia'
print(nombres)
# Iterar una lista
for nombre in nombres:  # nombre es singular, la lista es plural
    print(nombre)
else:
    print('Se acabaron los elementos de la lista')

# preguntamos cuantos elementos tiene
print(len(nombres))  # le pasamos como parametro la lista

# Agregamos un elemento
nombres.append('Marcelo')
nombres.append([1,2,3])
nombres.append(True)
nombres.append(10.45)
nombres.append([4,5])
nombres.append(7)
print(nombres)

# insertar un elemento en un indice especifico
nombres.insert(1, 'Alberto')
print(nombres)
nombres.insert(3, 'Debora')
print(nombres)

# Eliminamos un elemento
nombres.remove('Alberto')
print(nombres)

# Eliminar el ultimo elemento
nombres.pop()
print(nombres)

# Eliminar un indice especifico
del nombres[2]  # del significa delete (eliminar)
print(nombres)

# eliminar, borrar o olimpiar todos los elementos
nombres.clear()
print(nombres)

# Eliminar la lista
del nombres
# print(nombres)  # nos muestra el error

# definimos una tupla
cocina = ('cuchara', 'cuchillo', 'tenedor')
print(len(cocina))

# acceder a un elemento para esto utilizamos corchetes no parentesis
print(cocina[0])

# mostrar de manera inversa
print(cocina[-1])

# acceder a un rango
print(cocina[0:2])

# ejemplo
verduras = ('papa',) # una tupla necesita aunque sea de un elemento: la coma
# de lo contrario solo seria un tipo string cadena

# recorremos los elementos de la tupla
for cocinar in cocina:  # usamos end= para eliminar los saltos de lineas
    print(cocinar, end=' ')  # usamos end= para eliminar los saltos de lineas

cocinaLista= list(cocina)
cocinaLista[0] = 'Plato'
cocina = tuple(cocinaLista)
print('\n', cocina)

# del cocina
print(cocina)

# ejercicio rango
'''
Sintaxis de range(inicio<opcional>, fin <requerido>, incremento <opcional>)

'''

# ejercicio1: iterar un rango de 0 a 10 e imprimir numeros divisibles entre 3
print('Rango de 0 a 10 con numeros divisibles entre 3')
for i in range(11):
    if i % 3 == 0:
        print(i)

# ejercicio 2: crear un rango de numeros de 2 a 6 imprimelos
print('Rango de 2 a 6')
rango = range(2, 7)
for i in rango:
    print(i)

# ejercicio tuplas 

# dada la siguiente tupla
tupla = (13, 1, 8, 3, 2, 5, 8)  # definimos la tupla
# crear una lista que solo incluya los numeros menores a 5
# e imprima por consola [1,3,2]

lista = []  # definimos la lista
for elemento in tupla:
    if elemento < 5:
        lista.append(elemento)
print(lista)
