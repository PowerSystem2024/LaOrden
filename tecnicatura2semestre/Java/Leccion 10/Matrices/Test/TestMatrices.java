package Leccion10.Matrices.Test;
import Leccion10.Matrices.domain.Persona;
public class TestMatrices {
    public static void main(String[] args) {
        int edades[][] = new int [3][2];
        System.out.println("edades = "+edades);
        edades[0][0] = 5; //llenado manual
        edades[0][1] = 7; //es una diferente columna
        edades[1][0] = 8;
        edades[1][1] = 4;
        edades[2][0] = 2;
        edades[2][1] = 9;

        System.out.println("edades 0-0 = "+ edades[0][0]);
        System.out.println("edades 0-1 = "+ edades[0][1]);
        System.out.println("edades 1-0 = "+ edades[1][0]);
        System.out.println("edades 1-1 = "+ edades[1][1]);
        System.out.println("edades 2-0 = "+ edades[2][0]);
        System.out.println("edades 2-1 = "+ edades[2][1]);
        System.out.println("Recorremos la matriz a traves del ciclo for");
        for(int fila = 0; fila < edades.length;fila++){
            for(int col = 0; col < edades[fila].length;col++){
                System.out.println("edades"+fila+"-"+col+": "+edades[fila][col]);
            }
        }
        //sintaxis clasica
        //String frutas[][] = new String[3][2];

        //Sintaxis simplificada
        String frutas[][] = {{"Limon", "Pomelo"},{"Ciruela", "Kiwi"},{"Banana","Manzana"}};

        //for(int i = 0; i < frutas.length;i++){
        //    for(int j = 0; j < frutas[i].length;j++){
        //        System.out.println("frutas"+i+"-"+j+": "+frutas[i][j]);
        //    }
        //}
        //creamos una matriz de objetos
        Persona personas[][] = new Persona[2][3];
        imprimir(frutas);
        //Asignamos valores a la matriz
        personas[0][0] = new Persona("Ariel");
        personas[0][1] = new Persona("Osvaldo");
        personas[0][2] = new Persona("Liliana");
        personas[1][0] = new Persona("Natalia");
        personas[1][1] = new Persona("Marcelo");
        personas[1][2] = new Persona("Debora");
        System.out.println("Matriz de Personas: ");
        imprimir(personas);
    }
    public static void imprimir(Object matriz[][]){
        for(int i = 0; i < matriz.length;i++){
            for(int j = 0; j < matriz[i].length; j++){
                System.out.println("matriz "+i+"-"+j+": "+matriz[i][j]);
            }
        }
    }
}
