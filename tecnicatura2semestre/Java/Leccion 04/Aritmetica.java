package Leccion4;

public class Aritmetica {
    //atributos de la clase
    int a;
    int b;

    //el constructor es un metodo especial
    public Aritmetica(){ //constructor 1
        System.out.println("Se esta ejecutando este constructor numero uno");
    }
    //Estamos viendo lo que se llama sobrecarga de constructores
    public Aritmetica(int a, int b){ //constructor 2
        this.a = a;
        this.b = b;
        System.out.println("Se esta ejecutando este constructor numero dos");
    }
    //metodo
    public void sumarNumeros(){
        int resultado = a + b;
        System.out.println("resultado = "+resultado); 
    }

    public int sumarConRetorno() {
        //int resultado = a + b;
        return this.a + this.b;
    }

    public int sumarConArgumentos(int a, int b){
        this.a = a; //el argumento a se asigna al atributo this.a
        this.b = b;
        //return a + b;
        return this.sumarConRetorno();
    }


    

}
