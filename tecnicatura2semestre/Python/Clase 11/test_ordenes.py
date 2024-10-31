from Orden import Orden
from Producto import Producto

# Productos
producto1 = Producto("monitor", 1000.00)
producto2 = Producto("Mouse", 150.00)
producto3 = Producto("Microfono", 200)
producto4 = Producto("Brazo", 100)
producto5 = Producto("Lamp", 100)
producto6 = Producto("Pad", 50)

# Lista de productos
listaProducto1 = [producto1, producto2]

# Orden 1
orden1 = Orden(listaProducto1)
print(orden1)
print(f"Total de la orden 1: {orden1.calcular_total()}")
# Agregamos un producto nuevo
orden1.agregar_producto(producto5)
print(orden1)

#Orden 2
listaProducto2 = [producto3, producto4]
orden2 = Orden(listaProducto2)
print(orden2)
print(f"Total de la orden 1: {orden2.calcular_total()}")

#Agregamos un producto
orden2.agregar_producto(producto6)
print(orden2)
