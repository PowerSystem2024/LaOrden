# LISTAS (append, insert, remove, clear, pop, del)
# La inicializamos
nombres = ["Lean", "Luciana", "Santiago", "Javier"]
print(nombres)

# Accedemos a un elemento determinado
print(nombres[0])
print(nombres[1])
print(nombres[2])

# En caso que sea una lista larga y necesitar recorrer de atras para adelante podemos uasr numeros negativos -1 seria el primero, -2 el anteultimo y asi.
print(nombres[-1])
print(nombres[-2])

# Lo siguiente nos sirve para imprimir un rango (solo muestra el indice 0, 1 pero no el 2)
print(nombres[0:2])

# Esta forma lo que hace es como decirle, mostra desde el inicio hasta el indice 3
print(nombres[:3])

# Lo mismoi se puede hacer en el otro sentido
print(nombres[1:])

# Modificar un valor dentro de la lista
nombres[3] = "Nico"
print(nombres)

# Iterar la lista
for i in nombres:  # la variable es singular, la lista plural
    print(i)
else:
    print("Se acabaron los elementos de la lista")

# Preguntamos cuantos elementos tiene una lista
print(len(nombres))  # le pasamos como parametro la lista

# Agregamos un elemento, una lista puede contener cualquier tipo de dato, inclusive una lista dentro de otra lista
nombres.append("Maria")
nombres.append([1,2,3])
nombres.append(True)

print(nombres)

# insertar un elemento en un indice especifico
nombres.insert(1, "Javier")
print(nombres)

# Eliminamos un elemento de nuestra lista indicando el valor del elemento
nombres.remove("Javier")
print(nombres)

# Eliminar el el elemento en la ultima posicion
nombres.pop()
print(nombres)

# Eliminar un elemento pero desde su indice
del nombres[2]
print(nombres)

# Eliminar todos los elementos
nombres.clear()
print(nombres)

#Eliminar el elemento lista
#del nombres
#print(nombres)

# Concatenar listas
lista1 = [1, 2, 3, 1]
lista2 = [4, 5, 6]
lista3 = lista1+lista2
print(lista3)

# agregar elementos en lista
lista3.extend([7, 8, 9])
print(lista3)

#Funcion para ubicar el indice del valor ingresado
print(lista3.index(5))

#Saber cuantos valores repetidos hay en la lista
print(lista3.count(1))

#Invertir una lista
lista3.reverse()
print(lista3)

# TUPLAS es una listsa pero inmutable, funciona como un constante
# Las mismas son inmutables

# La inicializamos
cocina = ("Cuchara", "Cuchillo", "Tenedor")
print(cocina)

# Le pedimos que nos imprima la longitud
print(len(cocina))

# Accedemos a un elemento determinado
print(cocina[1])

# Mostramos de manera inversa
print(cocina[-1])

# Accedemos a un rango
print(cocina[0:1]) #Recodar que no incluye el ultimo numero

#Ejemplo (aunque se coloquen corchetes si es solo un elemento se comportara como una lista (array))
verduras = ("papa")

#Recorremos los elementos de una tupla en esta opcion el print utiliza la funcion \n para generar el salto de linea
for i in cocina:
    print(i) 

#Recorremos los elementos de una tupla en esta opcion se utiliza la funcion end=" " para que no genere saltos de lineas
for i in cocina:
    print(i, end=" ") 

#La unica forma de modificar una tupla es convertirla a una lista, modificarla y luego convertirla nuevamente en una tupla
#Esto no es una buena practica, si se cree que se requiere modificar hay que usar listas no tuplas
cocinaLista = list(cocina)
cocinaLista[0] = "Plato"
cocina = tuple(cocinaLista)

print('\n', cocina)

#Una tupla acepta varios tipos de datos, incluso una tupla dentro de otra
tupla= (4,6.7,[1,2], "Hola")
print(tupla)

#Tambien asi como en las listas paodemos preguntar si un elemento esta o no esta dentro de la misma
print(4 in tupla)
print ("Hola" not in tupla)