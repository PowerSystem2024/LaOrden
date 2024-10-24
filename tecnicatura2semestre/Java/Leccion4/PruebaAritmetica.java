package Leccion4;

public class PruebaAritmetica {
    public static void main(String[] args) {
        @SuppressWarnings("unused")
        var a = 10; //variables locales
        @SuppressWarnings("unused")
        int b = 7; //memoria stack
        miMetodo();
        Aritmetica aritmetica1 = new Aritmetica();
        aritmetica1.a = 3;
        aritmetica1.b = 7;
        
        aritmetica1.sumarNumeros();
        //para almacenar un objeto o los atributos se utiliza la memoria heap
        int resultado = aritmetica1.sumarConRetorno();
        System.out.println("resultado = " + resultado);

        resultado = aritmetica1.sumarConArgumentos(12, 26);
        System.out.println("Resultado usando argumentos = " +resultado);

        System.out.println("aritmetica a: "+aritmetica1.a);
        System.out.println("aritmetica b: "+aritmetica1.b);

        Aritmetica aritmetica2 = new Aritmetica(5, 8);
        System.out.println("aritmetica2= "+aritmetica2.a);
        System.out.println("aritmetica2= "+aritmetica2.b);
        //aritmetica1 = null; nunca utilizar esto, no se debe hacer
        //System.gc(); metodo para limpiar residuos, es pesado, no utilizar
        Persona persona = new Persona("Ariel", "Betancud");
        System.out.println("persona =" +persona);
        System.out.println("Persona nombre: "+persona.nombre);
        System.out.println("Persona apellido: "+persona.apellido);
    }
    // modularidad creamos un nuevo metodo
    public static void miMetodo(){
        // a = 10;
        System.out.println("Aqui hay otro metodo");
    }
}
//creamos una nueva clase

class Persona{
    String nombre;
    String apellido;

    Persona(String nombre, String apellido){ //constructor
        super(); //lamada al constructor de la clase padre onject
        //imprimir imprimir = new Imprimir();
        new Imprimir().imprimir(this);
        this.nombre = nombre;
        this.apellido = apellido;
        System.out.println("Objeto persona usando this: "+this);
    }
}
class Imprimir{
    public Imprimir(){
        super(); //el constructor de la clase padre, para reservar memoria
    }
    public void imprimir(Persona persona){
        System.out.println("Persona desde la clase imprimir: "+persona);
        System.out.println("Impresion del objeto actual (this)"+this);
    }
}