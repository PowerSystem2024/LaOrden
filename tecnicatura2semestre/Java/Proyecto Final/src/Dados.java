import java.util.Random;

public class Dados {
    private int dadoMaquina;
    private int dadoJugador;

    // Método para simular el juego
    public void jugar() {
        Random random = new Random();
        // Genera un número entre 1 y 6
        dadoMaquina = random.nextInt(6) + 1;
        dadoJugador = random.nextInt(6) + 1;

        System.out.println("El dado de la máquina indicó: " + dadoMaquina);
        System.out.println("Tu dado indicó: " + dadoJugador);

        if (dadoMaquina < dadoJugador) {
            System.out.println("¡HAS GANADO! :D");
        } else if (dadoMaquina > dadoJugador) {
            System.out.println("HAS PERDIDO :(");
        } else {
            System.out.println("ES UN EMPATE");
        }
    }
}
