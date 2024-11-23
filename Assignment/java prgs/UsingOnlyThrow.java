import java.util.Scanner;

public class UsingOnlyThrow {
    @SuppressWarnings("resource")
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter Number 1: ");
        int a = sc.nextInt();
        
        System.out.print("Enter Number 2: ");
        int b = sc.nextInt();

        if(a <= 0 || b <= 0){               // normally throw is used in try block..
            throw new ArithmeticException("Can't divide by 0");
        }
        else{
            int c = a / b;
            System.out.println(c);
        }
        System.out.println("\n\nEnd Of Program");
        sc.close();
    }    
}
