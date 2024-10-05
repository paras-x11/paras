import java.util.Scanner;

public class try1 {
    public static void main(String[] args) {
        int a, b, c;

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter a: ");
        a = sc.nextInt();

        System.out.print("Enter b: ");
        b = sc.nextInt();

        try {
            c = a/b;
            System.out.println(a + " / " + b + " = " + c);
        } 
        catch (Exception e) {
            System.out.println("Failed to divide.");
            System.out.print("Reason: " + e);
        }
        
        sc.close();        
    }
}
