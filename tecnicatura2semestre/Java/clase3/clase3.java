import java.util.Scanner;

public class clase3 {
    public static void main(String[] args){
        Scanner entrada =new Scanner(System.in);
        int numero;

        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
        while (numero != 0) {
            if (numero % 2 == 0) {
                System.out.println("El numero ingresado " + numero + " es PAR");
            } else {
                System.out.println("El numero ingresado " + numero + " es IMPAR");
            }
            System.out.println("Digite otro numero: ");
            numero = Integer.parseInt(JOptionpane.showInputDialog("Digite otro numero: "());
        }
        JOptionpane.showMessageDialog(null, "El numero ingresado es "+ numero " finaliza el programa");
    }
}