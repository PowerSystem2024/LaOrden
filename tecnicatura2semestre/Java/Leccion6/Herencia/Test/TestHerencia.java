package Leccion6.Herencia.Test;
import Leccion6.Herencia.Empleado;
import java.util.Date;
import Leccion6.Herencia.Cliente;
public class TestHerencia {
    public static void main(String[] args) {
        Empleado empleado1 = new Empleado("Ariel", 57000);
        System.out.println("empleado= "+empleado1);

        Date fecha1 = new Date();

        Cliente cliente1 = new Cliente(fecha1, true, "Bety", 'F', 32, "9 de julio 1413");
        System.out.println("cliente1 = "+ cliente1);
    }
}
