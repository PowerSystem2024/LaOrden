# Ejericico 1: crear una funcion para sumar los valores recibidos de tipo numericos
# utilizando argumentos variables *args como parametro de la funcion y agregar como restulado
# la suma de todo los valres pasados como argumentos.

def sumar_valor(*args):
    resultado = 0
    for valor in args:
        resultado += valor
    return resultado

print(sumar_valor(3, 5, 9))