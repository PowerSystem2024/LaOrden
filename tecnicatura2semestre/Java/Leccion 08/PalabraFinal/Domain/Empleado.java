package Leccion8.PalabraFinal.Domain;

public class Empleado extends Persona{
    @Override
    public void imprimir(){
        System.out.println("Metodo imprimir desde la clase hija");
    }
}
