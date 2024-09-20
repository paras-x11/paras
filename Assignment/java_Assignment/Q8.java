// • Write a Java program that reads a positive integer and count the number of digits the number. 
// Input an integer number less than ten billion: 125463 
// Number of digits in the number: 6 

import java.util.Scanner;

public class Q8 {
    public static void main(String[] args) {
        int n, len = 0;

        Scanner sc = new Scanner(System.in);

        System.out.print("Input an integer number less than ten billion: ");
        n = sc.nextInt();

        if(n<=0){
            System.out.println("Enter the positive integer number.");
        }
        else{
            while (n > 0) {
                n = n / 10;
                len ++;
            }
            System.out.println(len);
        }
        sc.close();
    }
}
