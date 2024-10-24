package Leccion2.EjercicioCiclos01;

import java.util.Scanner;
/*ejercicio 1: leer un numero y mostrar su cuadrado, repetir el
proceso hasta que se introduzca un numero negativo*/
public class Ciclos01 {
        public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
    
        int numero, cuadrado;
        System.out.println("Digite un numero: ");
        numero = Integer.parseInt(entrada.nextLine());
        while (numero >= 0) { //mientras el numero sea igual a cero o positivo
            cuadrado = (int)Math.pow(numero, 2);
            System.out.println("El numero " +numero+" elevado al cuadrado es:"+cuadrado);
            System.out.println("Digite un numero: ");
            numero = Integer.parseInt(entrada.nextLine());
        }
        System.out.println("El programa ha finalizado");
        entrada.close();
    }
}
