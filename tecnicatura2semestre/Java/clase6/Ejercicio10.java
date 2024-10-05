package ciclos10;

// Ejercicio 10: Pedir 10 números y escribir la suma total
// Hacerlo con la clase Scanner y JOptionPane

import javax.swing.JOptionPane;

public class Ciclos10 {
    
    public static void main(String[] args) {


        int numero, suma = 0;

        for(int i = 1; i <= 10; i++){
            System.out.println("Digite un número: ");
            numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un número: "));
            suma += numero;
        }
        System.out.println("La suma de todos los número es : " + suma);
        JOptionPane.showMessageDialog(null, suma);

    }
}