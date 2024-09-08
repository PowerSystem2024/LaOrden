
# lista = Ariel, Liliana, Natalia, Osvaldo

nombres = ['Naty', 'Osvaldo', 'Lily', 'Ariel']

print(nombres)
print(nombres[0])
print(nombres[1])
print(nombres[3])
print(nombres[-1])
print(nombres[-2])

print(nombres[0:2]) # Solo muestra el indice 0, 1 pero no el indice 2

# Ir al inicio de la lista al indice sin incluirlo
print(nombres[_:3])_ #indices a mostrar 0, 1, 2

# Desde el indice indicado hasta el final
print(nombre[1:_])

# Modificamos un valor
nombres[0] = 'Natalia'
nombres[3] = 'Liliana'
print(nombres)

# Iterar una lista
for nombre in nombre:
    print(nombre)
else:
    print('No hay mas elementos en la lista')


# Preguntamos cuantos elementos tiene
print(len(nombres))_# le pasamos como parametros la lista

# Agregamos un elemento

nombres.append('Marcelo')
print(nombres)

# Insertar un elemento en indice especifico
nombres.insert(1, 'Alberto')
print(nombres)
nombres.insert(3, 'Debora')
print(nombres)

# Eliminamos un elemento
nombres.remove('Alberto')
print(nombres)

# Eliminar el último elemento
nombres.pop()
print(nombres)

## Eliminar un indice espcifico
del nombres[2]
print(nombres)

# Eliminar todos los elementos
nombres.clear()
print(nombres)

# ELiminar la lista
del nombres
print(nombres)


# Definimos una tupla
cocina = ('Cuchara', 'Cuchillo', 'Tenedor')
print(len(cocina))

# Acceder a un elemtno, usamos corchetes
print(cocina[-1])

## Acceder a un rango
print(cocina[0: 2])

# Ejemplo
verduras = ('papa', ) # Una tupla necesita aunque sea de un elemento: la coma, 
                     # de lo contrario solo seria un tipo str cadena



# Recorremos los elementos de la tupla
for cocinar in cocina:
    print(cocinar, end=' ') #" Elimina todos los saltos de lineas"


cocinaLista = list(cocina)
cocinaLista[0] = 'Plato'
cocina = tuple(cocinaLista)
print('\n', cocina)




tupla = (4, 'Hola', 6.78, [1,2,3], 4, 'Hola')
print(tupla)

print(4 in tupla)
conjunto = set()
conjunto1 = {}
conjunto.add(7)
print(3 not in conjunto1)
print(conjunto == conjunto1)


conjunto3 = conjunto1 | conjunto2

conjunto3 = conjunto1 & conjunto2

conjunto3 = conjunto1 - conjunto2


print(conjunto1.issubset(conjunto3))
print(conjunto2.issubset(conjunto3))
print(conjunto3.issubset(conjunto2))
print(conjunto3.issubset(conjunto1))

print(conjunto1.issuperset(conjunto2))
print(conjunto2.issuperset(conjunto1))
print(conjunto3.issuperset(conjunto3))

print(conjunto1.isdisjoint(conjunto2))

conjunto1 = frozenset

diccionarioNuevo = {'Azul': 'Blue', 'Rojo': 'Red', 'Verde': 'Green'}

del (diccionarioNuevo['Azul'])

diccionario2 = {
    'Ariel': {
        'Edad': 40,
        'Altura': 1.83
    },
    'Osvaldo': {
        'Edad': 45,
        'Altura': 1.85
    },
    'Natalia': {
        'Edad': 35,
        'Altura': 1.67
    }
}
print(diccionarioNuevo)

seleccionArgentina = {}

for llave, valor in diccionario2.items():
    print(llave, valor)


## Pilas uasndo listas
pila = [1,2,3]
pila.append(4)
elementoBorrado = pila.pop()
print(elementoBorrado)

## Colas
cola = ['Ariel', 'Osvaldo', 'Liliana']
cola.append('Natalia')
seRetira = cola.pop(0)

print(f'Atentido el cliente: {seRetira}' )