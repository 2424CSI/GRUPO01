package com.mycompany.algoritmopermutacion;

import java.util.Arrays;
import java.util.Scanner;
 
public class Permutaciones {
 
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String palabra;
        do{
            System.out.print("Ingresa una palabra: ");
            palabra = scanner.nextLine(); //Leemos la palabra ingresada por la consola
        }
        while(palabra.isEmpty());
        
        char[] caracteres = palabra.toCharArray(); // Convertimos la palabra en un arreglo de caracteres
        Arrays.sort(caracteres); // Ordenamos los caracteres alfabéticamente
        int totalPermutaciones = 0; // Contador para el número total de permutaciones
 
        // Mostrar las primeras 10 permutaciones ordenadas alfabéticamente
        do {
            totalPermutaciones++; // Incrementar el contador de permutaciones
            if (totalPermutaciones <= 10) {
                System.out.println(Arrays.toString(caracteres)); // Mostrar la permutación actual
            }
        } while (siguientePermutacion(caracteres)); // Generar la siguiente permutación
 
        // Mostrar el número total de permutaciones
        System.out.println("Número total de permutaciones: " + totalPermutaciones);
    }
 
    // Método para generar la siguiente permutación
    private static boolean siguientePermutacion(char[] array) {
        int i = array.length - 2;
        while (i >= 0 && array[i] >= array[i + 1]) {     
            i--;
        }
        if (i < 0) {
            return false;
        }
        int j = array.length - 1;
        while (array[j] <= array[i]) {
            j--;
        }
        intercambio(array, i, j);
        revertir(array, i + 1, array.length - 1);
        return true;
    }
 
    // Método para intercambiar dos elementos en un arreglo
    private static void intercambio(char[] array, int i, int j) {
        char temp = array[i];
        array[i] = array[j];
        array[j] = temp;
    }
 
    // Método para revertir un arreglo desde la posición start hasta la posición end
    private static void revertir(char[] array, int inicio, int fin) {
        while (inicio < fin) {
            intercambio(array, inicio, fin);
            inicio++;
            fin--;
        }
    }
}
