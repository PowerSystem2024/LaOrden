package Leccion4.ProyectoCaja;

public class PruebaCaja {
    public static void main(String[] args) {
        // Variables locales
        int medidaAncho = 3; // Valores ingresados en código duro
        int medidaAlto = 2;
        int medidaProf = 6;

        Caja caja1 = new Caja(); // Instanciamos el objeto, constructor vacío
        caja1.ancho = medidaAncho; // Le pasamos valores al objeto;
        caja1.alto = medidaAlto;
        caja1.profundo = medidaProf;
        int resultado = caja1.calcularVolumen(); // Llamamos al método

        // Primer resultado
        System.out.println("Resultado volumen caja 1: " + resultado);

        Caja caja2 = new Caja(2, 4, 6); // Llamamos al constructor 2 con nuevos argumentos
        // LLamamos con el nuevo objeto al método para un nuevo calculo
        System.out.println("Resultado volumen caja 2: " + caja2.calcularVolumen());


    }
}
