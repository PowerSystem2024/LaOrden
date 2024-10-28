/*ejercicio 5 realizar un juego para adivinar un numero
para ello generar un numero aleatorio entre 0-100
y luego ir pidiendo numeros indicando "Es mayor" o
"es menor" segun sea yaor o menor con respecto a N
El proceso termina cuando el usuario acierta y mostramos 
el numero de intentos hechos*/
package Leccion2.EjercicioCiclos05;
import java.util.Scanner;
public class Ciclos05 {
public static void main(String[] args) {
    Scanner entrada = new Scanner(System.in);
    int numero, aleatorio, conteo = 0;
    aleatorio = (int)(Math.random()*100);
    do{
        System.out.println("Digite un numero: ");
        numero = Integer.parseInt(entrada.nextLine());
        if(numero < aleatorio){
            System.out.println("Digite un numero mayor");
        }else if(numero > aleatorio){
            System.out.println("Digite un numero menor");
        }else{
            System.out.println("FELICITACIONES, has adivinado el numero");
    }
    conteo++;
}while(numero != aleatorio);
System.out.println("Adivinaste el numero en: "+conteo+ " intentos");
entrada.close();
}
}
