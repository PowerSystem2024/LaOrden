import java.util.Scanner;

public class MenuJuegos {

    public static void main(String[] args) {
        mostrarMenu();
    }

    public static void mostrarMenu() {
        Scanner scanner = new Scanner(System.in);
        int opcion;
        System.out.println("------------------------------");
        System.out.println("¡Bienvenido al menú de juegos!");
        System.out.println("Seleccione un juego:");
        System.out.println("1. Dados");
        System.out.println("2. Acercarse al número");
        System.out.println("3. Bingo");
        System.out.println("4. Ruleta rusa");
        System.out.println("5. Salir");

        System.out.print("Ingrese su opción: ");
        opcion = scanner.nextInt();

        switch (opcion) {
            case 1:
                new Dados().jugar();
                break;
            case 2:
                new AcercarseAlNumero().jugar();
                break;
            case 3:
                new Bingo().jugar();
                break;
            case 4:
                new RuletaRusa().jugar();
                break;
            case 5:
                System.out.println("¡Hasta luego!");
                break;
            default:
                System.out.println("Opción inválida. Intente de nuevo.");
                mostrarMenu(); // Recursión para volver al menú en caso de opción inválida
                break;
        }
        scanner.close();
    }
}