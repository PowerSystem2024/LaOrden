import java.util.Scanner;

public class clase3ejercicio2 {
    public static void main(String[] args){
        Scanner entrada = new Scanner(System.in);
        int numero, aleatorio, conteo = 0;
        aleatorio = (int) (Math.random()*100);
        do {
            System.out.println("Digite un numero: ");
            numero = Integer.parseInt(entrada.nextLine());
            if (numero<aleatorio){
                JOptionPane.showMessageDialog(null,"Digite un numero mayor");
            }
            else if (numero>aleatorio){
                JOptionPane.showMessageDialog(null,"Digite un numero menor");
            }
            else {
                JOptionPane.showMessageDialog(null,"Felicidades has adivinado el numero");
            }
            conteo++;
        }while (numero!=aleatorio)
        JOptionPane.showMessageDialog(null,"Adivinaste el numero en: "+ conteo + " intentos ");
    }
}