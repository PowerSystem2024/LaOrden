
public class clase1 {
    public static void  main(String[] args){
        var conteo = 0;
        while (conteo<3){
            System.out.println("conteo = " + conteo);
            conteo++;
        }
        var contador = 0;
        do {
                System.out.println("contador = " + contador);
                contador++;

        }while (contador <= 7)
            for (var contando = 0; contando <7; contando++) {
                if (contando % 2 == 0) {
                    System.out.println("contando = " + contando);
                    break;
                }
                inicio:
                for (var contando = 0; contando <7; contando++) {
                    if (contando % 2 != 0) {
                        continue inicio;
            }
                    System.out.println("contando = " + contando);
    }
}