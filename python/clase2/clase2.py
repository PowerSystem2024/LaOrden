# tipo set
planetas = {'Marte','Jupiter','Venus'}
print(len(planetas))  #usamos la funcion len = length significa largo

#revisar si un elemento existe dentro de set
print('Jupiter' in planetas)

# agregar un elemento
planetas.add('Tierra') # add es una funcion
print(planetas)

# eliminar elementos puede arrojar un error si el elemento no existe
planetas.remove('Jupiter') # esta funcion ante un mal ingreso u inexistencia del elemento da error
print(planetas)

planetas.discard('tierra') # esta funcion no nos presenta ningun error
print(planetas)

# Limpiar set o conjunto
planetas.clear()
print(planetas)

# Eliminar set o conjunto
del planetas
# print(planetas) #al eliminar nos muestra error

# 'Maradona' :10 Un diccionario esta compuesto por dos elementos
# UNA LLAVE Y UN VALOR
# dict(key,value)
diccionario = {
    'IDE':'Integrated Development Environment',
    'POO':'Programación Orientada a Objetos',
    'SABD':'Sistema de Administración de Base de Datos'
}
# Verificar la cantidad de elementos del diccionario
print(len(diccionario))
print(diccionario)

# Acceder a un diccionario con la llave(key)
print(diccionario['IDE'])

# Otra forma de recuperar un elemento
print(diccionario.get('POO'))
print(diccionario.get('SABD'))

# Modificamos elementos
diccionario['IDE'] = 'Entorno de Desarrollo Integrado'
print(diccionario)

# Como recorrer los elementos
for termino in diccionario:  # recorremos mostrando solo las llaves
    print(termino)

# Necesitamos una funcion para recorrer un diccionario
for termino, valor in diccionario.items():
    print(termino,valor)

# Otras maneras de acceder a un diccionario
for termino in diccionario.keys(): # Estamos usando una funcion
     print(termino)  # Muestra solo las llaves

for valor in diccionario.values(): # Usamos una funcion para acceder al valor
    print(valor)

# Comprobar la existencia de algun elemento
print('IDE' in diccionario)  # devuelve un booleano

# Agregar un elemento
diccionario['PK'] = 'Primary key'
print(diccionario)

# Eliminar un elemento
diccionario.pop('SABD')
print(diccionario)

# Vaciar un diccionario
diccionario.clear()
print(diccionario)

# Eliminar diccionario
del diccionario  #el diccionario se borro

# Concatenar listas
lista1 = [1,2,3]
lista2 = [4,5,6]
lista3 = lista1+lista2
print(lista3)

lista3.extend([7,8,9])  # Funcion para agregar varios elementos a una lista
print(lista3)

print(lista3.index(5))  # Funcion para ubicar en que indice esta el valor ingresado
# print(lista3.index(0))  # esto daria un error por no ser el elemento parte de la lista

# Como saber cuantos valores repetidos hay dentro de una lista
print(lista3.count(1))  # cuenta cuantos valores iguales hay dentro de la lista

# Para poner al reves una lista
lista3.reverse()
print(lista3)

# para que una lista se multiplique repitiendo sus elementos
lista3 = lista3 * 2
print(lista3)

# Metodos de ordenamiento, en python es una funcion
lista3.sort()  # ordena los elementos ascendentemente
print(lista3)
lista3.sort(reverse=True)  # ordena descendentemente
print(lista3)

# repaso de tuplas
tupla = (4, 'Hola', 6.78, [1,2,78], 4, 'Hola')  # puede tener diferentes tipos de datos dentro
print(tupla)

print(4 in tupla)  # accion booleana, su respuesta es de tipo booleana
# Lo que podemos usar dentro de tuplas son: index, coun, len
# En tuplas se puede convertir de tupla a lista y de lista a tupla
#  
