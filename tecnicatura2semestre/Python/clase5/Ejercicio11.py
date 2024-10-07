# Ejercicio 11: Agenda telefonica
# Hacer un programa que simule una agenda de contactos. Crear un diccionario
# donde la clave sea el nombe del usuario y el valor sea el telfono, el
# programa tendra el siguiente menu de opciones:
# 1. Nuevo contacto
# 2. Borrar contacto
# 3. Ver contactos existentes
# 4. Salir


agenda = {}

while True:
    print('MENÚ')
    print('1. Nuevo contacto')
    print('2. Borrar contacto')
    print('3. Ver contactos existentes')
    print('4. Salir')
    opcion = int(input('Digite una opción de menú'))
    if opcion == 1:
        nombre = input('Digite el nombre de opción de menú')
        telefono = input('Digite el número de teléfono')
        if nombre not in agenda:
            agenda[nombre] = telefono
            prunt('Contacto creado correctamente')
        else:
            print('El contacto con este nombre ya existe')
    elif opcion == 2:
        nombre = input('Cual es el nombre del contacto? ')
        if nombre in agenda:
            del (agenda[nombre])
            print('Se ha eliminado el contacto')
        else:
            print('Este contacto no existe en la agenda')
    elif opcion == 3:
        print('Agenda de contactos')
        for clave, valor in agenda.items():
            print(f'Nombre: {clave}. Teléfono: {valor}')
    elif opcion == 4:
        print('Saliste de la aplicación')
        break