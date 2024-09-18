package clase4;

import java.util.Scanner;

public class clase4 {
    public static void main(String[] args){
        Scanner entrada = new Scanner (System.in);
        int numero, suma = 0;
        do {
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
            suma+ = numero;
        }
        while (numero!=0);
        JOptionPane.showInputDialog(null, "La suma de todos los numeros ingresados es: " + suma);

    }
}