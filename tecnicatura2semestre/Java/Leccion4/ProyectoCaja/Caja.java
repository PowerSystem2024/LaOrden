package Leccion4.ProyectoCaja;

/* 
    Proyecto caja:
    Ejercicio 1: Crear un proyecto según las especificaciones mostradas a continuación.
    La fórmula es: volumen = ancho * alto * profundidad
 */

public class Caja {

     // Atributos
    int ancho;
    int alto;
    int profundo;

     // Métodos y constructores
    public Caja(){
    }

    // Constructor con parámetros
    public Caja(int ancho, int alto, int profundo){ // Constructor 2
        this.ancho = ancho;
        this.alto = alto;
        this.profundo = profundo;
    } 

    public int calcularVolumen(){ // Método para calcular
        return ancho * alto * profundo;
    }



}
