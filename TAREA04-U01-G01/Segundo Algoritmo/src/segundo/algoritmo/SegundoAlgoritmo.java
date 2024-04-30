import java.util.Scanner;

public class SegundoAlgoritmo {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Ingrese el mensaje: ");
        String mensaje = scanner.nextLine().replaceAll("\\s+", ""); // Eliminar espacios del mensaje
        System.out.print("Ingrese el numero de filas (n): ");
        int n = scanner.nextInt();
        
        int caracteresMensaje = mensaje.length();
        int caracteresMatriz = n * n;
        
        if (caracteresMensaje > caracteresMatriz) {
            System.out.println("El mensaje no cabe en la matriz de cifrado. Finalizando programa.");
            return;
        }
        
        char[][] matrizCifrado = new char[n][n];
        int indiceMensaje = 0;
        
        // Llenar la matriz de cifrado con el mensaje
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (indiceMensaje < caracteresMensaje) {
                    matrizCifrado[i][j] = mensaje.charAt(indiceMensaje);
                    indiceMensaje++;
                } else {
                    matrizCifrado[i][j] = '*'; // Llenar con "*" si sobran espacios en la matriz
                }
            }
        }
        
        // Mostrar la matriz de cifrado
        System.out.println("Matriz de cifrado:");
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                System.out.print(matrizCifrado[i][j] + " ");
            }
            System.out.println();
        }
        
        // Mostrar el mensaje original
        System.out.println("Mensaje original: " + mensaje);
        
        // Mostrar el mensaje cifrado
        StringBuilder mensajeCifrado = new StringBuilder();
        for (int j = 0; j < n; j++) {
            for (int i = 0; i < n; i++) {
                mensajeCifrado.append(matrizCifrado[i][j]);
            }
        }
        System.out.println("Mensaje cifrado: " + mensajeCifrado.toString());
    }
}
