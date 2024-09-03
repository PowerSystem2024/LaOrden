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

tuple = (13, 1, 8, 3, 2, 5, 8)
list = []
for elemento in tuple:
    if elemento < 5:
        list.append(elemento)
print(list)