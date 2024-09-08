

# Sintaxis de range(inicio<opcional>), fin<requerido>, incremento<opcional>)



# Ejercicio 1: Crear un rango de 0 a 10 es imprimir numeros divisibles entre 3

for i in range(11):
    if i % 3 == 0:
        print(i)


# Ejercicio 2: Crear un rango de numeros de 2 a 6 
rango = range(2, 7)
for i in rango:
    print(i)



# Ejercicio 3: Crear un rango de 3 a 10 con incremento 2 

print('Ejercicio 3')
for i in range(3, 11, 2):
    print(i)

