# TIPO SET
# Todo pertenece al grupo de las colecciones
# Lista = Mantiene un orden y se puede modificar (array o vectores)
# Tuple = Mantiene un orden pero no se puede modificar
# Set = no tiene un orden, no se puede modificar pero si se puede agregar o eliminar, no mantiene ningun indice, es sin orden y sin indice
# Diccionario = no tiene orden ni indice

planetas = {"Marte", "Jupiter", "Venus"}
print(planetas)

# Usamos la funcion len para obtener la longitud de del set
print(len(planetas))

# Revisamos si un elemento existe dentro del set (hay que respetar hasta las mayusculas y acentos), devuelve un elemento booleano
print("Marte" in planetas)

print("marte" in planetas)

# Tambien podemos preguntar a la negativa
print("Mercurio" is not planetas)

# Agregar un elemento, no se puede agregar elementos duplicados
planetas.add("Tierra")
planetas.add("Tierra")
print(planetas)

# Eliminar elementos de un set, asi como para buscarlos tampoco se puede eliminar un elemento al cual el falto un acento o una mayuscula
planetas.remove("Tierra")
# planetas.remove("venus")
# Para eliminar tambien se puede usar la funcion discard, si se ingresa mal el elemento simplemente no lo elimina pero no genera error
planetas.discard("jupiter")
print(planetas)

# Limpiamos el set, es decir lo vaciamos
planetas.clear()
print(planetas)

# Eliminar el set o conjunto
del planetas
# print(planetas)

# **DICCIONARIOS**
# Al igual que los set no tienen indice, se accede desde la llave
# "Messi":10 un diccionario esta ocmpuesto por dos elementos, una llave y un valor
# dict(key, value)
diccionario = {
    "IDE": "INtegrated Development Enviroment",
    "POO": "Programacion orientada a objetos",
    "SABD": "Sistema de administracion de base de datos"
}
print(diccionario)

print(len(diccionario))

# Acceder a un diccionario con llave(key)
print(diccionario["IDE"])

# Otra forma de recueprar un elemento
print(diccionario.get("POO"))

# Modificamos un elemento
print("---")
diccionario["IDE"] = "Entorno de Desarrollo integrado"
print(diccionario)

# Recorrer los elementos, en este caso solo accede a la llave pero no al valor
for i in diccionario:
    print(i)

# De esta forma accedemos a la key y al value
for i, j in diccionario.items():
    print(i, j)

# otra manera de acceder solo a las keys o values independientemente
for i in diccionario.keys():
    print(i)

for j in diccionario.values():
    print(j)

# Comprobar existencia de un elemento
print("IDE" in diccionario)

# Agregar un elemento (no se puede agregar una llave duplicada)
diccionario["PK"] = "Primary key"
print(diccionario)

# Eliminar un elemento, al colocar la key tambien se borra el value
diccionario.pop("SABD")

# Vaciar un diccionario
diccionario.clear()
print(diccionario)

# ELiminar diccionario
del diccionario
#print(diccionario)


