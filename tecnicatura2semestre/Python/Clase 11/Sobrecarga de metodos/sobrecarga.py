# Sobrecarga de un operador significa que un mismo operador puede comportarse de diferentes formas, se va a comportar de distinta forma dependiendo con el tipo de datos con el cual este trabajando.

# En enteros suma
a = 3
b = 5
print(a + b)

# En string concatena
a = 'Hola'
b = 'mundo'
print(a + b)

# Une dos listas
a = [3, 4, 5]
b = [6, 7, 8]
print(a + b)


# Esto tambien se puede hacer con clases en py, pero tenemos que agregar la sobrecarga de un metodo dependiendo del operador que querramos sobrecargar.
# Ej:
# La sobrecarga de operadores permite que los operadores realicen operacion con objetos personalizados, esto mejora la legibilidad del codigo

# Todos los operadores con guiones bajos __operador__ son conocidos como dunder method

# Sobrecarga  y sobre escritura son dos conceptos distintos, sobrecarga esta explicado arriba y sobreescritura tiene que ver con la herencia
# Operadores aritmeticos
# + __add__
# - __sub__
# * __mul__
# / __truedib__
# // _floordiv__
# % __mod__
# ** __pow__

# Operadores logicos
# == __eq__
# < __lt__
# > __gt__
# <= __le__
# >= __ge__
# != __ne__

# Operadores de asignacion
# -= __isub__
# += __iadd__
# *= __imul__
# /= __idiv__
# //= __ifloordiv__
# %= __imod__
# **= __ipow__

# Operadores unarios
# - __neg__
# + __pos__
# ~ __invert__



# Esto si fuesen objetos no se podrian hacer, va a necesitar una sobrecarga para poder realizar la operacion
# miObjeto1 + miObjeto2 =
