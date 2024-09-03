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
#print("Rango con valores de inicio = 3, fin = 10, incremento = 2")
#for i in range(3,11,2):
#    print(i)
#tipo set
#planetas = {"marte", "jupiter", "venus"}
#print(len(planetas))
##revisar si un elemento existe dentro de set
#print("jupiter" in planetas)
#
##agregar un elemento
#planetas.add("tierra")
#
##Eliminar elementos, puede arrojar un error si el elemento no existe
#planetas.remove("jupiter")
#print(planetas)
#planetas.discard("tierra")
#print(planetas)
#planetas.clear()
##limpiamos set
#print(planetas)
##eliminar set o conjunto 
#del planetas
#print (planetas)
diccionario = {
    "IDE" : "Integrated Depevelopment Enviroment",
    "POO" : "Programacion Orientada a Objetos", 
    "SABD" : "Sistema de Administracion de Base de Datos"
}
#verificar la cantidad de elementos en el diccionario 
print(len(diccionario))
print(diccionario)
#acceder al diccionario con la llave(key)
print(diccionario["IDE"])
print(diccionario["POO"])
print(diccionario["SABD"])
#mODIFICAMOS ELEMENTOS 
diccionario["IDE"] = "Entorno de Desarrollo Integrado"
print(diccionario)
#Como recorrer elementos 
for termino in diccionario:
    print(termino)
#Necesitamos una funcion para recorrer un diccionario 
for termino, valor in diccionario.items():
    print(termino,valor)
#Otras maneras de acceder a un diccionario 
for termino in diccionario.keys():
    print(termino)
for valor in diccionario.values():
    print (valor)
#Comprobar la existencia de un elemento 
print("IDE" in diccionario)
#Agregar un elemento 
diccionario["PK"] = "Primary Key"
print(diccionario)
#Eliminar un elemento
diccionario.pop("SABD")
print(diccionario)
#VAciar un diccionario
diccionario.clear()
print(diccionario)
#Eliminar un diciionario
del diccionario 