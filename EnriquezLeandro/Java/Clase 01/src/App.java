public class App {
    public static void main(String[] args) throws Exception {
        var conteo = 0;
        // Ciclo while
        while (conteo < 3) {
            System.out.println("conteo = " + conteo);
            conteo++;
        }
        // Ciclo do while
        var contador = 0;
        do {
            System.out.println("conteo = " + contador);
            contador++;
        } while (contador < 7);
        // ciclo for
        for (var cont = 0; cont < 7; cont++) {
            System.out.println("Contador = " + cont);
        }
        // Break and continue
        for (var cont = 0; cont < 7; cont++) {
            if (cont % 2 == 0) {
                System.out.println("Contador = " + cont);
                break;
            }
        }
        for (var cont = 0; cont < 7; cont++) {
            if (cont % 2 == 0) {
                continue;
            }
            System.out.println("Contador = " + cont);
        }
        // labels
        //Solo funciona con las palabras break and continue
        inicio: for (var cont = 0; cont < 7; cont++) {
            if (cont % 2 == 0) {
                continue inicio;
            }
            System.out.println("Contador = " + cont);
        }
    }
}
