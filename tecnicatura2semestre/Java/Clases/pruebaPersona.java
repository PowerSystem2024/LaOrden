package Clases;

public class pruebaPersona {
    public static void main(String[] args){
        Persona persona1;
        persona1 new Persona(); //llamamos al constructor
        persona1.nombre = "Ariel";
        persona1.apellido = "Bentancud";
        persona1.obtenerInformacion();

        Persona persona2 =new Persona();
        System.out.println("persona2 = " + persona2);
        System.out.println("persona1 = " + persona1);
        persona2.obtenerInformacion();
        persona2.nombre= "Osvaldo";
        persona2.apellido = "Giordanini"
        persona2.obtenerInformacion();
    }
}