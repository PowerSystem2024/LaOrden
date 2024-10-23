/*ejercicio4: pedir numeros hasta que se teclee uno negativo,
 * mostrar cuantos numeros se han introducido.
 * Lo hacemos primero con la clase Scanner
 * luego con la clase JOptions
 */
package Java.Leccion2.EjercicioCiclos04;
import java.util.Scanner;
public class Ciclos04 {
public static void main(String[] args) {
    Scanner entrada = new Scanner(System.in);
    int numero, conteo = 0;
    System.out.println("Digite un numero: ");
    numero = Integer.parseInt(entrada.nextLine());
    while(numero >= 0) {
        System.out.println("El numero: "+numero+" es POSITIVO");
        conteo++;
        System.out.println("Digite otro numero: ");
        numero = Integer.parseInt(entrada.nextLine());
    }
    System.out.println("Ingresaste "+conteo+" numeros que no son negativos");
    entrada.close();
}
}
