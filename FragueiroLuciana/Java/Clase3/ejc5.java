/* ejercicio 3: leer numeros hasta aque se introduzca un cero
 * para cada uno indicar si es par o impar.
 * primero lo haremos con la clase Scanner
 * Luego con la clase JOptionPane
 */
package Java.Clase3;
import java.util.Scanner;
public class ejc5 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numero;
        System.out.println("digite un numero: ");
        numero = Integer.parseInt(entrada.nextLine());
        while (numero != 0) {
            if(numero % 2 == 0){
                System.out.println("El numero ingresado "+numero+" es PAR");
            }else{
                System.out.println("El numero ingresado "+numero+" es IMPAR");
            }
            System.out.println("Digite otro numero: ");
            numero = Integer.parseInt(entrada.nextLine()); 
        }
        System.out.println("El numero ingresado es :"+numero+" finaliza el programa");
        entrada.close();
    }

}