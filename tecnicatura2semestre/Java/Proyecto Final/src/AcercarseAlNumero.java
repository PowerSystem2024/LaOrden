import java.util.Random;
import java.util.Scanner;

public class AcercarseAlNumero {
    // Método para ejecutar el juego
    public void jugar() {
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();

        int puntajeTotal = 0;
        int rondas = 5;

        System.out.println("¡Bienvenido al juego Acercarse al Número!");
        
        for (int i = 1; i <= rondas; i++) {
            // Generar número secreto para la ronda
            int numeroSecreto = random.nextInt(100) + 1; // Número entre 1 y 100
            
            System.out.print("Introduce un número entre 1 y 100: ");
            int numeroJugador = scanner.nextInt();

            // Calcular la distancia entre el número del jugador y el número secreto
            int distancia = Math.abs(numeroSecreto - numeroJugador);
            int puntosRonda;

            // Asignar puntos según la distancia
            if (distancia == 0) {
                puntosRonda = 30;  // 10 puntos básicos + 20 de bonus por acertar
                System.out.println("¡Has acertado el número secreto! Obtuviste un bonus de 20 puntos.");
            } else if (distancia <= 5) {
                puntosRonda = 10;
            } else if (distancia <= 10) {
                puntosRonda = 5;
            } else if (distancia <= 20) {
                puntosRonda = 2;
            } else {
                puntosRonda = 1;
            }

            // Mostrar resultados de la ronda
            System.out.println("Tu número fue " + numeroJugador + ". Estabas a " + distancia + " unidades del número secreto (" + numeroSecreto + ").");
            System.out.println("Obtienes " + puntosRonda + " puntos en esta ronda.");

            // Acumular puntos en el puntaje total
            puntajeTotal += puntosRonda;
        }

        // Mostrar el puntaje total al finalizar el juego
        System.out.println("Tu puntaje total es: " + puntajeTotal + ". ¡Felicidades!");
    }
}

