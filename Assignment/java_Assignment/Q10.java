// • Write a java program to find out the max number from given array using function 

import java.util.Scanner;

public class Q10 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int[] arr = new int[5];
        int max = Integer.MIN_VALUE, min = Integer.MAX_VALUE;

        System.out.println("Input 5 numbers: ");
        for (int i = 0; i < arr.length; i++) {
            arr[i] = sc.nextInt();
        }

        for (int i = 0; i < arr.length; i++) {
            if(arr[i] > max){
                max = arr[i];
            }
        }

        for (int i = 0; i < arr.length; i++) {
            if(arr[i] < min){
                min = arr[i];
            }
        }

        System.out.println("Minimum number is: " + min);
        System.out.println("Maximum number is: " + max);
        sc.close();
    }    
}

