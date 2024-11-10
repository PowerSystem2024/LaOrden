# Ejercicio 3: Funcion recursiva
# Imprimir numeros de 5 a 1 de manera descendente usando funciones recursivas
# Puede ser cualquier valor positivo, por ejemplo, si pasamos el 5 debe imprimir
# 5
# 4
# 3
# 2
# 1
# Si se ingresa numero negativo no  imprimer nada


def imprimit_numeros_recursivos(numero):
    if numero >= 1:
        print(numero)
        imprimit_numeros_recursivos(numero-1)
    elif numero == 0:
        return 
    elif numero <= 0:
        print('Valor ingresado incorrecto...')

imprimit_numeros_recursivos(3)

imprimit_numeros_recursivos(int(input('Digite un numero')))

