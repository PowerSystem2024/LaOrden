# Ejercicio 2: Funcio con *args para multiplicar 
# Crear una funcion para multiplicar los valroes recibidos de tiupo numerico, utilizando
# argumentos variavbles como parametros de la funcion y resgresar como resultado la 
# multiplicacion de todos los valreos pasados como argumentos


def multiplicar_valores(*numeros):
    resultado = 1
    for numero in numeros:
        resultado *= numero
    return resultado

print(multiplicar_valores(1, 2, 3, 4, 5 ))