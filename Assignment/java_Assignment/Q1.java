// Write a Java program to Take three numbers from the user and print the greatest number.

import java.util.Scanner;

public class Q1 {
    public static void main(String[] args) {
        int a, b, c;

        Scanner sc =new Scanner(System.in);

        System.out.print("Enter A: ");
        a = sc.nextInt();

        System.out.print("Enter B: ");
        b = sc.nextInt();

        System.out.print("Enter C: ");
        c = sc.nextInt();

        int max = (a > b) ? ((a > c) ? a : c) : ((b > c) ? b : c);

        System.out.println("The Greatest Number Is: " + max);

        sc.close();
    }
}

