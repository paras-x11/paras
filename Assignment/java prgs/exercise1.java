import java.util.Scanner;

public class exercise1 {
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        
        System.out.println("Enter 5 marks: ");
        int s1 = sc.nextInt();
        int s2 = sc.nextInt();
        int s3 = sc.nextInt();
        int s4 = sc.nextInt();
        int s5 = sc.nextInt();

        float sum = s1 + s2 + s3 + s4 + s5;
        float percentage = (sum*100) / 500;

        System.out.println("percentage is: " +percentage+ "%");

        sc.close();
    }
}