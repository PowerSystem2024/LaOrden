package Ciclos;

import java.util.Scanner;

public class clase1Ejercicio2 {
    public static void main(String[] args){
        Scanner entrada = new Scanner (System.in);
        var numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "());
                while numero !=0 {
            if (numero < 0) {
                System.out.println("El numero es negativo");
            }
            else {
                System.out.println("El numero es positivo");
            }
            numero = JOptionpane.showInputDialog("Digite otro numero: "());
        }
        System.out.println( "El numero " + numero + " finaliza el programa");
    }
}