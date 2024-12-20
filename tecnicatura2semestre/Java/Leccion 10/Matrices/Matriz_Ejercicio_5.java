/*
 * Ejercicio5: crear y cargar una matriz de tamaño n x m mostrar la suma
 * de cada fila y de cada columna.
 */
package Leccion10.Matrices;
import java.util.Scanner;
import javax.swing.JOptionPane;
public class Matriz_Ejercicio_5 {
    public static void main(String[] args) {
        @SuppressWarnings("resource")
        Scanner entrada = new Scanner(System.in);
        int matriz[][],nFilas,nCol,sumaFilas,sumaCol;
        int posFila,posCol;

        nFilas = Integer.parseInt(JOptionPane.showInputDialog("Digite el numero de filas: "));
        nCol = Integer.parseInt(JOptionPane.showInputDialog("Digite el numero de columnas: "));
        matriz = new int [nFilas][nCol];
        int filas[]=new int[nFilas];
        int columnas[]=new int [nCol];

        System.out.println("Rellenando la matriz: ");
        for(int i = 0;i<nFilas;i++){
            for(int j=0;j<nCol;j++){
                System.out.println("Matriz ["+i+"] ["+j+"]: ");
                matriz[i][j] = entrada.nextInt();
            }
        }
        System.out.println("\nMatriz Original:" );
        for(int i=0;i<nFilas;i++){
            for(int j=0;j<nCol;j++){
                System.out.println(matriz[i][j]+" ");
            }
            System.out.println("");
        }
        posFila=0;
        for(int i=0;i<nFilas;i++){
            sumaFilas=0;
            for(int j=0;j<nCol;j++){
                sumaFilas+=matriz[i][j];
            }
            filas[posFila]=sumaFilas;
            posFila++;
        }
        posCol = 0;
        for(int j=0;j<nCol;j++){
            sumaCol=0;
            for(int i=0;i<nFilas;i++){
                sumaCol+=matriz[i][j];
            }
            columnas[posCol]=sumaCol;
            posCol++;
        }
        System.out.println("\nLa suma de las filas es: ");
        for(int i=0;i<nFilas;i++){
            System.out.println(filas[i]+" - ");
        }
        System.out.println("");
        System.out.println("\nLa suma de las columnas es: ");
        for(int i=0;i<nCol;i++){
            System.out.println(columnas[i]+" - ");
        }
    }
    
}
