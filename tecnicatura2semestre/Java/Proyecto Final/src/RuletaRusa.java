import java.util.ArrayList;
import java.util.Random;
import java.util.Scanner;

public class RuletaRusa {

    private ArrayList<String> listaParticipantes;
    private int dardo; // Posición del disparo letal
    private int np; // Número de participantes

    public void jugar() {
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();

        System.out.println("=========================");
        System.out.println("|       Ruleta Rusa     |");
        System.out.println("=========================");
        System.out.println();

        // Leer número de participantes
        System.out.print("¿Cuántos participantes hay? ");
        np = scanner.nextInt();
        scanner.nextLine(); // Limpiar el buffer

        // Leer nombres de los participantes
        listaParticipantes = new ArrayList<>();
        for (int i = 1; i <= np; i++) {
            System.out.print("Ingrese el nombre del participante " + i + ": ");
            String nombre = scanner.nextLine();
            listaParticipantes.add(nombre);
        }

        // Preparar la ruleta
        System.out.println("Cargar dardo...");
        esperarTecla(scanner);
        dardo = random.nextInt(6) + 1; // Posición del dardo (bala)
        System.out.println("Listo.");
        esperarTecla(scanner);

        boolean perdio = false;
        int i = 0;

        // Juego de ruleta rusa
        while (!perdio) {
            if (i == np) {
                i = 0; // Reiniciar índice si alcanza el número de participantes
            }
            System.out.println();
            System.out.println("=========================");
            System.out.println("    Turno de: " + listaParticipantes.get(i));
            System.out.println("=========================");
            System.out.println();

            System.out.println("Girar cañon...");
            esperarTecla(scanner);
            int gatillo = random.nextInt(6) + 1; // Posición aleatoria del gatillo
            System.out.println("Listo.");
            System.out.println();

            System.out.println("Disparar.");
            esperarTecla(scanner);

            if (gatillo == dardo) {
                perdio = true;
            } else {
                i++; // Pasar al siguiente participante
            }
        }

        // Fin del juego
        System.out.println();
        System.out.println("Juego finalizado");
        System.out.println("=========================");
        System.out.println("El perdedor es: " + listaParticipantes.get(i));
        System.out.println("=========================");
    }

    // Método auxiliar para esperar una tecla
    private void esperarTecla(Scanner scanner) {
        System.out.print("Presiona ENTER para continuar...");
        scanner.nextLine();
    }
}
