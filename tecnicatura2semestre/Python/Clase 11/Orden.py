from Producto import Producto


class Orden:
    contador_orden = 0

    def __init__(self, productos):
        Orden.contador_orden += 1
        self._id_orden = Orden.contador_orden
        self._productos = list(productos)

    # Esto es para agregar un nuevo producto
    def agregar_producto(self, producto):
        self._productos.append(producto)

    def calcular_total(self):
        # creamos una varialbe temporal para almacenar
        total = 0
        for producto in self._productos:
            total += producto.precio
        return total

    def __str__(self):
        productos_str = ""
        for producto in self.productos:
            productos_str += producto.__str__() + ' | '
        return f"Orden: {self._id_orden}, \nProducto: {productos_str}"

    @property
    def productos(self):
        return self._productos

    @productos.setter
    def productos(self, productos):
        self._productos = productos


if __name__ == "__main__":
    producto1 = Producto("camiseta", 100.00)
    producto2 = Producto("Pantalon", 150.00)
    productos1 = [producto1, producto2]  # Lista de productos
    # Objeto de la primer orden de lista de productos
    orden1 = Orden(productos1)
    print(orden1)

    # Tarea modificar la orden  ingresando nuevos productos con sus nombres y precios, crear una nueva lista de productos y agregarla a la orde 2

    producto3 = Producto("Microfono", 200)
    producto4 = Producto("Brazo", 100)
    listaCompra = [producto3, producto4]
    orden2 = Orden(listaCompra)
    print(orden2)
