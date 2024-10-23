package Java.Leccion2.EjercicioCiclos08;

import javax.swing.JOptionPane;

/*ejercicio9: pedir el dia, mes y año de una fecha e
 * indicar si la fecha es correcta. Suponiendo que
 * todos los meses son de 30 dias
 */
public class Ejercicio08 {
    public static void main(String[] args) {
        int numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
        int i = 1;
        while(i <= numero){
            JOptionPane.showMessageDialog(null, i);
            i++;
        } 
    }
}
