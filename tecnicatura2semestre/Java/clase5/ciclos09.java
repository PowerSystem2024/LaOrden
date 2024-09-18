package clase5;

import javax.swing.JOptionPane;

public class ciclos09 {
    public static void main(String[] args) {
        int dia = Integer.parseInt(JOption.showInputDialog("Digite el dia: "));
        int mes = Integer.parseInt(JOption.showInputDialog("Digite el mes: "));
        int anio = Integer.parseInt(JOption.showInputDialog("Digite el año: "));
        if (dia != 0) &&(dia <= 30) {
            if ((mes != 0))&&(mes <= 12) {
                if (anio != 0)&&(anio <= 2022) {
                    JOption.showMessageDialog(null, "La fecha ingresada es: " + dia + "/" + mes + "/" + anio);

                }
        else{
                    SJOption.showMessageDialog(null, "Fecha incorrecta, año incorrecto");
                }
            }
            else{
                SJOption.showMessageDialog(null, "Fecha incorrecta, mes incorrecto");
            }

        }
        else{
            SJOption.showMessageDialog(null, "Fecha incorrecta, dia incorrecto");

        }
    }
}
