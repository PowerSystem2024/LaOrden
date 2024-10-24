package Leccion2.EjercicioCiclos11;
/* Ejercicio 11: diseñar un programa que meustre el producto de 
 * los 10 primero numeros impares
 * hacerlo con JOptionPane
 */
import javax.swing.JOptionPane;
public class Ciclos11 {
    public static void main(String[] args) {
        long producto = 1;
        for(int i = 1; i <= 20; i+=2){
            producto *=i;
        }
        JOptionPane.showMessageDialog(null, "El producto de los numeros impares es: "+producto);
    }
}
