from Empleado import Empleado
from Gerente import Gerente


def imprimir_detalle(objeto):
   
    # De manera indirecta llama al str de la clase Empleado o de la clase Gerente
    print(objeto)

    # Esto es unicamente para ver el tipo de dato que recibe
    print(type(objeto))

    print(objeto.mostrar_detalle())

    if(isinstance(objeto, Gerente)):
        print(objeto.departamento)



empleado1 = Empleado("Leandro", 1500)
imprimir_detalle(empleado1)

gerente1 = Gerente("Javier", 2500, "Sistemas")
imprimir_detalle(gerente1)