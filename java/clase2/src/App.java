import java.util.Scanner;
import javax.swing.JOptionPane;

public class App {
    @SuppressWarnings({ "unused", "resource" })
    public static void main(String[] args) throws Exception {
        Scanner input = new Scanner(System.in);
        // Ejercicio 1: Leer un numero y mostrar su cuadrado, repetir el proceso hasta
        // que se introduzca un numero negativo
        int num, cuadrado;

        do {
            num = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un valor numerico: "));
            cuadrado = (int) Math.pow(num, 2);
            System.out.println("El cuadrado de " + num + " es: " + cuadrado);
        } while (num >= 0);

        System.out.println("Fin del ciclo");

        // Ejercicio 2: Leer un numero e indicar si es positivo o negativo. El proceso
        // se reptira hasta que se introduzca un 0
        int numero;
        String estado = "";
        do {
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero"));
            if (numero > 0) {
                estado = "positivo";
            } else if (numero < 0) {
                estado = "negativo";
            } else {
                estado = "neutro";
            }
            JOptionPane.showMessageDialog(null, "El numero " + numero + " es: " + estado);
        } while (numero != 0);

        JOptionPane.showMessageDialog(null, "Fin del ciclo");
    }

    @Override
    public String toString() {
        return "App []";
    }
}
