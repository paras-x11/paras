import java.util.Scanner;

// packages works only on class files. if in calc folder(package) .java file is not available it will still work with class files
import calc.*;

public class UsingPackage {
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);

        Sum s = new Sum();
        Substraction s2 = new Substraction();
        Multiplication m = new Multiplication();
        Division d = new Division();

        int a, b, ch, e = 1;

        System.out.print("Enter Value 1: ");
        a = sc.nextInt();

        System.out.print("Enter Value 2: ");
        b = sc.nextInt();

        while (e != 0) {

            System.out.printf("\nEnter 1 for sum \t Enter 2 for substraction \t Enter 3 for multiplication \t Enter 4 for division");
            System.out.print("\nEnter your choice: ");
            ch = sc.nextInt();
                
            switch (ch) {
                case 1: s.sum(a, b);
                    break;

                case 2: s2.substraction(a, b);
                    break;

                case 3: m.multiply(a, b);
                    break;

                case 4: d.division(a, b);
                    break;

                case 0 : e = 0;
                    System.out.println("-> Exited.");
                    break;
            
                default: System.out.println("-> Enter valid choice.");
                    break;
            }
        }
        
        sc.close();
        
        
    }
}
