import java.util.Random;
import java.util.Scanner;

public class PiedraPapelTijera {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();

        String[] opciones = {"Piedra", "Papel", "Tijera"};
        boolean seguirJugando = true;

        while (seguirJugando) {
            System.out.println("Elegi una opcion: \n 1. Piedra \n 2. Papel \n 3. Tijera");

            int miOpcion = scanner.nextInt() - 1;

            if (miOpcion < 0 || miOpcion > 2) {
                System.out.println("Opción inválida");
                continue;
            }

            int opcionPc = random.nextInt(3);
            System.out.println("Elegiste: " + opciones[miOpcion]);
            System.out.println("La computadora eligió: " + opciones[opcionPc]);

            if (miOpcion == opcionPc) {
                System.out.println("Es un empate!");
            }
            else if ((miOpcion == 0 && opcionPc == 2) ||
                    (miOpcion == 1 && opcionPc == 0) ||
                    (miOpcion == 2 && opcionPc == 1)) {
                System.out.println("Ganaste!!");
            }
            else {
                System.out.println("Perdiste :( intentalo de nuevo");
            }
            System.out.println("Queres jugar otra vez? S/N");
            char respuesta = scanner.next().toUpperCase().charAt(0);
            if (respuesta == 'N')
                seguirJugando = false;
        }
    }
}
