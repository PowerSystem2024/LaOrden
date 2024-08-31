# Ejercicio 1: Iterar un rango de 0 a 10 pero con un incremento de 2 en 2 en lugar de 1 en 1

for i in range(1, 10, 2):
    print(i)
print("---")
# Ejercicio 2: Crear un rango de numeros de 2 a 6 e imprimir

for i in range(2, 7):
    print(i)
print("---")
# Ejercicio 3: Crear un rango de 3 a 10 pero con un incremento de 2 en 2

for i in range(3, 10, 2):
    print(i)


# Dada la siguiente tupla Crear una lista que solo incluya los numeros menores a 5 e imprimirlos
tupla = (13, 1, 8, 3, 2, 5, 8)

lista = []
for i in tupla:
    if i < 5:
        lista.append(i)

print(lista)