package operaciones;

public class PruebaAritmetica {
    public static void main(String[] args) {
        var a = 10; // variables locales
        int b = 7; // memoria stack
        miMetodo(); // Llamamos al métdo nuevo
        Aritmetica aritmetica1 = new Aritmetica();
        aritmetica1.a = 3;
        aritmetica1.b = 7;
        // aritmetica1 = null;
        aritmetica1.sumarNumeros();

        // Para almacenra un objeto o los atributos se utiliza la memoria heap
        int resultado = aritmetica1.sumarConRetorno();
        System.out.println("resultado = " + resultado);

        resultado = aritmetica1.sumarConArgumentos(12, 26);
        System.out.println("Resultado usando argumentos = " + resultado);
        
        System.out.println("aritmetica1 a: " + aritmetica1.a);
        System.out.println("aritmetica1 b: " + aritmetica1.b);

        Aritmetica aritmetica2 = new Aritmetica(5, 8);        
        System.out.println("aritmetica2 a: " + aritmetica1.a);
        System.out.println("aritmetica3 b: " + aritmetica1.b);
        // aritmetica1 = null; // nunca utilizar esto, no se debe hacer
        // System.gc(); método para limpiar los residuos, es pesado, no utilizar
    }

    public static void miMetodo(){
        // a = 10; // una variable esta limitada
        System.out.println("Aqui hay otro metodo");
    }

}