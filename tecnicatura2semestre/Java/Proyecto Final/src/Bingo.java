import java.util.Random;
import java.util.Scanner;

public class Bingo {
    private int[][] tablero;
    private int numeroJugadores;

    public void jugar() {
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();

        System.out.print("¿Cuántos jugadores hay? ");
        numeroJugadores = scanner.nextInt();
        System.out.println();

        for (int jugador = 1; jugador <= numeroJugadores; jugador++) {
            System.out.println("Tablero: " + jugador);
            tablero = new int[3][3];
            // Llenar el tablero con números aleatorios
            for (int i = 0; i < 3; i++) {
                for (int j = 0; j < 3; j++) {
                    int numAzar = random.nextInt(98) + 1; // Número entre 1 y 98
                    tablero[i][j] = numAzar;
                }
            }
            // Imprimir el tablero
            for (int i = 0; i < 3; i++) {
                for (int j = 0; j < 3; j++) {
                    System.out.print(tablero[i][j] + " ");
                }
                System.out.println();
            }
            System.out.println();
        }

        // Comienza el juego
        System.out.println("----------------------------");
        System.out.println("Para tirar un número presiona ENTER, para salir escribe 'BINGO'.");

        String seguir;
        do {
            System.out.println();
            System.out.print("Tirar número: ");
            seguir = scanner.nextLine().toLowerCase(); // Leer entrada y convertir a minúsculas

            if (seguir.equals("")) { // Si se presiona solo ENTER
                int numAzar = random.nextInt(98) + 1; // Generar un número aleatorio entre 1 y 98
                System.out.println("Número tirado: " + numAzar);
            }

        } while (!seguir.equals("bingo"));

        System.out.println("El juego ha finalizado, ¡felicitaciones al ganador!");

        scanner.close();
    }
}
