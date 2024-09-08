
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