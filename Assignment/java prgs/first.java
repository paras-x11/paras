import java.util.Scanner;

public class first {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.err.print("enter a: ");
        int a = sc.nextInt();

        System.err.print("enter b: ");
        int b = sc.nextInt();
        
        int sum = a  + b;

        System.out.println(a+" + " +b+ " is " +sum);
        
        System.out.print("enter value to check it is integer or not: ");
        boolean b1 = sc.hasNextInt();
        System.out.println(b1);

        String str = sc.nextLine();
        System.out.println(str);

        sc.close();
    }
}