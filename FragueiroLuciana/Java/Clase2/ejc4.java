//ejercicio2 leer un numero e identificar si es positivo
//o negativo. El proceso se repetira hasta que 
//se introduzca un cero 0
package Java.Clase2;
import javax.swing.JOptionPane;
public class ejc4 {
    public static void main(String[] args) {
        var numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "));
        while(numero != 0){
            if(numero > 0){
                JOptionPane.showMessageDialog(null, "El numero "+numero+" es positivo");
            }else{
                JOptionPane.showMessageDialog(null, "El numero "+numero+" es negativo");
            }
            numero =Integer.parseInt(JOptionPane.showInputDialog("Digite otro numero: "));
        }
        JOptionPane.showMessageDialog(null, "El numero"+numero+" finaliza el programa");
    }
}
