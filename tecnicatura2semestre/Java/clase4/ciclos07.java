package clase4;

import java.util.Scanner;

public class ciclos07 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        int numero, conteo = 0, suma = 0;
        float promedio = 0;
        numero = Integer.parseInt(JOptionPane.showMessageDialog("Digite otro numero: ");
        while (numero >= 0) {
            suma += numero;
            conteo++;
            numero = Integer.parseInt(JOptionPane.showMessageDialog("Digite otro numero: ");
        }
        if (conteo == 0)
            JOptionPane.showMessageDialog(null,"Error, la division entre cero no existe");
        }
        else{
        promedio = (float) suma / conteo
        JOptionPane.showMessageDialog(null, "El promedio es: "+ promedio);
        }
}
