#print("Rango de 0 a 10 con numeros diisibles entre 3")
#for i in range (11):
#    if i % 3 == 0:
#        print(i)
#
#print("Rango con valores de inicio = 2 y fin = 6")
#rango = range(2, 7)
#for i in rango:
#    print(i)
#
##print("Rango con valores de inicio = 3, fin = 10, incremento = 2")
#for i in range(3,11,2):
#   print(i)
#definimos una tupla
#cocina =("cuchara", "cuchillo", "tenedor")
#
#print(len(cocina))
##mostrar el primer elemento
#print(cocina[0])
##mostrar de manera inversa
#print(cocina[-1])
##acceder a un rango
#print(cocina[0:1])
##ejemplo
#verduras = ("papa",)
##recorremos los elementos de la tupla
#for cocinar in cocina:
#    print(cocinar, end=" ")
#cocinaLista = list(cocina)
#cocinaLista[0] = "plato"
#cocina = tuple(cocinaLista)
#print("\n", cocina)
#
#del cocina
#print(cocina)

#tuple = (13, 1, 8, 3, 2, 5, 8)
#list = []
#for elemento in tuple:
#    if elemento < 5:
#        list.append(elemento)
#print(list)
#conjunto2 = set()
#conjunto1 = {"bye", }
#conjunto2.add(7)
#conjunto2.add("Hola")
#print(conjunto2)
#conjunto1.add("hola")
#print(conjunto1)
#print(3 not in conjunto)
##como hacer igualdad entre dos conjuntos
#print (conjunto1 == conjunto2)
##operaciones en conjuntos
#conjunto3 = conjunto1 | conjunto2 #la linea une los dos conjuntos
#print (conjunto3)
#conjunto3 = conjunto1 & conjunto2 #que elemento tienen en comun
#print (conjunto3)
#conjunto3 = conjunto1 - conjunto2 #asigna el valor que esta en el conjunto 1 y no en el conjunto 2 
#print (conjunto3)
#conjunto3 = conjunto2 - conjunto1
#print(conjunto3)
#conjunto3 = conjunto1 ^ conjunto2 #Elementos que comparten o que son diferentes entre ambos 
#print (conjunto3)
#conjunto3 = conjunto1 | conjunto2 #Aqui preguntamos si un conjunto es un subconjunto de otro 
#print(conjunto2.issubset(conjunto3))
#print(conjunto1.issubset(conjunto3))
#print(conjunto3.issubset(conjunto1))
#print(conjunto3.issubset(conjunto2))
#
#print(conjunto3.issuperset(conjunto1))#preguntamos si los elementos del conjuntol estan dentro del 3
#print(conjunto3.issuperset(conjunto2))
#print(conjunto2.issuperset(conjunto3))
#
##Como saber si ambos conjuntos son disconezos, esto es si no comparten elementos en comun 
#print(conjunto1.isdisjoint(conjunto2))
##convertir un conjunto totalmente inmutable+
#conjunto1 = frozenset
#
##REPASO DICCIONARIO 
#del (diccionarioNuevo ["Azul"])
#print (diccionarioNuevo)
#
##los diccionarios pueden almacenar diferentes tipos de datos 
#diccionario2 = {"Ariel": {"Edad" : 40, "Altura" : 1.83}, "Osvaldo" : [45, 1.85], "Natalia" : [35, 1.67]}
#print(diccionario2)
#
#
#
#seleccionArgentina = {
#    10: {"Nombre" : "Lionel Messi", "Edad" : 35, "Altura" : 1.70, "Precio" : "50 millones", "Posicion" : "Extremo derecho"},
#    11 : {"Nombre" : "Angel Di Maria", "Edad" : 34, "Altura" : 1.80, "Precio" : "12 millones", "Posicion" : "Extremo derecho"},
#    24 : {"Nombre" : "Paulo Dybala", "Edad" : 28, "Altura" : 1.77, "Precio" : "35 millones", "Posicion" : "Media Punta"},
#    19 : {"Nombre" : "Nicolas Otamendi", "Edad" : 34, "Altura" : 1.83, "Precio" : "50 millones", "Posicion" : "Defensa central"},
#    1 : {"Nombre" : "Franco Armani", "Edad" : 35, "Altura" : 1.89, "Precio" : "3.5 Millones", "Posicion" : "Arquero"},
#    7 : {"Nombre" : "Rodrigo De Paul", "Edad" : 28, "Altura" : 1.80, "Precio" : "40 millones", "Posicion" : "Mediocampista"},
#    3 : {"Nombre" : "Nicolás Tagliafico", "Edad" : 30, "Altura" : 1.72, "Precio" : "9 millones", "Posicion" : "Lateral izquierdo"},
#    22 : {"Nombre" : "Lautaro Martínez", "Edad" : 25, "Altura" : 1.74, "Precio" : "75 millones", "Posicion" : "Delantero centro"},
#    8 : {"Nombre" : "Marcos Acuña", "Edad" : 31, "Altura" : 1.72, "Precio" : "12 millones", "Posicion" : "Lateral izquierdo"}
#}
#
#for llave, valor in seleccionArgentina.items()
#    print(llave, valor)
print("Tenemos cargados en el diccionario la cantidad de jugadores: ", end)
print(len(seleccionArgentina))

#Pilas usando listas 
pila = [1, 2, 3]

#agregar elementos a la pila por el final 
pila.append(4)
pila.append(5)
print(pila)

#Sacamos elementos desde el final
elementoBorrado = pila.pop() #quita el ultimo elemento y lo guarda en la variable
print(f"Sacamos el elemento{elementoBorrado}")
print(f"La fila ahora quedo asi ")

#Colas con listas 
#Estructuras de datos tipo fifo( first input /first output)

cola = ["Ariel", "Osvaldo", "Liliana", "Pilar"]
cola.append("Natalia")
cola.append("Jose")
print (cola)

#Sacamos elementos de la cola 
seRetira = cola.pop(0)
print(f"Atendido{seRetira}")
print (cola)