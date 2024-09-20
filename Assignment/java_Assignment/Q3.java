// Write a Java program that takes a year from user and print whether that year is a leap year or not.


import java.util.Scanner;

public class Q3 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter Year: ");
        int year = sc.nextInt();

        if ((year % 4 == 0 && year % 100 != 0) || year % 400 == 0) {
            System.out.println(year + " is leap year.");
        }

        else{
            System.out.println(year + " is not a leap year.");
        }

        sc.close();
    }
}
