// Write a program in Java to input 5 numbers from keyboard and find their sum and average using for loop. 


import java.util.Scanner;

public class Q5 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int sum = 0;
        int[] arr = new int[5];

        System.out.println("Input 5 numbers: ");
        for (int i = 0; i < arr.length; i++) {
            arr[i] = sc.nextInt();
        }

        for (int i = 0; i < arr.length; i++) {
            sum = arr[i] + sum;
        }

        System.out.println("Average is: " + sum/5);
        System.out.println("Sum is: " + sum);

        sc.close();
    }
}
