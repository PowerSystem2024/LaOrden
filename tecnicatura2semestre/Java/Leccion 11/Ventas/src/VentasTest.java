public class VentasTest {
    public static void main(String[] args) {

        Producto producto1 = new Producto("Pantalon", 9500.00);
        Producto producto2 = new Producto("Campera", 29000.00);

        Orden orden1 = new Orden();
        Orden orden2 = new Orden();

        // AGregamso productos al arreglo
        orden1.agregarProducto(producto1);
        orden1.agregarProducto(producto2);
        orden1.mostrarOrden();

        // Tarea:
        // Crear mas objetos de tipo Producto
        // Crear mas objetos de tipo Orden

        // Crear productos
        Producto producto3 = new Producto("Camisa", 11000.00);
        Producto producto4 = new Producto("Gorra", 290.00);
        Producto producto5 = new Producto("Zapatos", 12000.00);
        Producto producto6 = new Producto("Gorra", 1500.00);

        Orden orden3 = new Orden();
        Orden orden4 = new Orden();
        Orden orden5 = new Orden();

        orden3.agregarProducto(producto3);
        orden3.agregarProducto(producto4);

        orden4.agregarProducto(producto4);
        orden4.agregarProducto(producto5);
        orden4.agregarProducto(producto6);

        orden5.agregarProducto(producto3);
        orden5.agregarProducto(producto5);

        orden3.mostrarOrden();
        orden4.mostrarOrden();
        orden5.mostrarOrden();

    }
}