package Java.Leccion2.EjercicioCiclos08;
/*ejercicio9: pedir el dia, mes y año de una fecha e
 * indicar si la fecha es correcta. Suponiendo que
 * todos los meses son de 30 dias
 */
import java.util.Scanner;
public class Ciclo08 {
    public static void main(String[] args) {
        @SuppressWarnings("resource")
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite un numero: ");
        int numero = Integer.parseInt(entrada.nextLine());
        int i = 1;
        while(i <= numero){
            System.out.println(i);
            i++;
        }
    }
}
