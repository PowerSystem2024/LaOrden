import java.util.Scanner

public class clase3ejercicio {
    public static void main(String[] args){
        Scanner entrada = new Scanner(System.in);
        int numero, conteo = 0;
        System.out.println("Digite un numero: ");
        numero = Integer.parseInt(JOptionPane.showInputDialog("Digite un numero: "());
        while (numero >= 0){
            JOptionPane.showMessageDialog(null, "El numero " +numero+" es POSITIVO");
            conteo++;
            numero = Integer.parseInt(JOptionpane.showInputDialog("Digite otro numero: "));
            }
        JOptionPane.showMessageDialog(null, "A ingresado " + conteo + " numero que no son negativos");