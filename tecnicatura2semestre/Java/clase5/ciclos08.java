package clase5;

import javax.swing.JOptionPane;

public class ciclos08 {
    public static void main(String[] args) {
        int numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
        int i = 1;
        while (i <= numero){
            JOptionPane.showInputDialog(null, i)
            i++;
        }

    }
}