/* ejercicio 3: leer numeros hasta aque se introduzca un cero
 * para cada uno indicar si es par o impar.
 * primero lo haremos con la clase Scanner
 * Luego con la clase JOptionPane
 */
package Java.Leccion2.EjercicioCiclos03;
import javax.swing.JOptionPane;
public class Ejercicio03 {
    public static void main(String[] args) {
        int numero;
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
        while (numero != 0) {
            if(numero % 2 == 0){
                JOptionPane.showMessageDialog(null, "El numero "+numero+" es PAR");
            }else{
                JOptionPane.showMessageDialog(null, "El numero "+numero+" es IMPAR");
            }
            numero =Integer.parseInt(JOptionPane.showInputDialog("Digite otro numero: ")); 
        }
        JOptionPane.showMessageDialog(null, "El numero"+numero+" finaliza el programa");

    }

}
