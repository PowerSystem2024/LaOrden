//ejercicio2 leer un numero e identificar si es positivo
//o negativo. El proceso se repetira hasta que 
//se introduzca un cero 0
package Java.Clase2;
import java.util.Scanner;
public class ejc3 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("Digite un numero: ");
        var numero = Integer.parseInt(entrada.nextLine());
        while(numero != 0){
            if(numero > 0){
                System.out.println("El numero "+numero+" es positivo");
            }else{
                System.out.println("El numero "+numero+" es negativo");
            }
            System.out.println("Digite otro numero: ");
            numero = Integer.parseInt(entrada.nextLine());
        }
        System.out.println("El numero"+numero+" finaliza el programa");
        entrada.close();
    }

}
