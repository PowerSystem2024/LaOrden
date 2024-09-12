import java.util.Scanner;
import javax.swing.JOptionPane;
import java.util.Random;

public class App {
    @SuppressWarnings("resource")
    public static void main(String[] args) throws Exception {
        Scanner input = new Scanner(System.in);

        // Ejercicio 3
        // Leer numeros hasta que se introduzca un cero para cada uno indicar si es par
        // o impar, primero hacerlo con clase Scanner y luego con la clase JOptionPane.
        int num;
        do {
            System.out.println("Introducir un numero");
            num = input.nextInt();
            if (num % 2 == 0) {
                System.out.println("El numero " + num + " es par");
            } else {
                System.out.println("El numero " + num + " es impar");
            }
        } while (num != 0);

        int numero;
        do {
            numero = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un valor numerico: "));
            if (numero % 2 == 0) {
                JOptionPane.showMessageDialog(null, "El numero " + numero + " es par");
            } else {
                JOptionPane.showMessageDialog(null, "El numero " + numero + " es impar");
            }
        } while (numero != 0);

        // Ejercicio 4
        // Pedir numeros hasta que se teclee uno negativo y mostrar cuantos numeros se
        // han introducido, realizarlo con la clase scanner y otro con la clase
        // JOptionPane
        int num1, contador;
        contador = -1;
        do {
            System.out.println("Introducir un numero");
            num1 = input.nextInt();
            contador++;
        } while (num1 >= 0);
        System.out.println("La cantidad de numeros ingresados es de: " + contador);

        int num2;
        contador = -1;
        do {
            num2 = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un numero: "));
            contador++;
        } while (num2 >= 0);
        JOptionPane.showMessageDialog(null, "La cantidad de numeros ingresados es de: " + contador);

        // Ejercicio 5
        // Realizar un juego para adivinar unn numero para ello generar un numero
        // aleatorio entre 0-100 y luego ir pidiendo numeros indicando si es mayor o
        // menor
        Random random = new Random();

        int num3, num4, cont;

        cont = -1;
        num3 = random.nextInt(100);

        do {
            num4 = Integer.parseInt(JOptionPane.showInputDialog("Ingrese un numero: "));
            cont++;
            if (num4 > num3) {
                JOptionPane.showMessageDialog(null, "El numero ingresado es mayor");
            } else if (num4 < num3) {
                JOptionPane.showMessageDialog(null, "El numero ingresado es menor");
            } else {
                JOptionPane.showMessageDialog(null,
                        "Excelente!!! el numero misterioso era: " + num3 + ". El numero de intentos fue: " + cont);
            }
        } while (num3 != num4);

    }
}
