import java.util.Scanner;

class MyException extends Exception{

    // this toString(), getMessage(), e.printStackTrace() is a inbuilt method that we can override from Exception class by inheritance.
    // there are many more methods to override but this is basic and necessary to print message.

    @Override                                       
    public String toString() {
        return "I am toString()";               // we can customize this messages
    }

    @Override
    public String getMessage() {
        return "I am getMessage()";
    }
}


public class CustomException {
    @SuppressWarnings("resource")
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        
        System.out.print("\nEnter 2 digit value: ");
        int n = sc.nextInt();

        if(n < 10 || n > 99){

            try {
                throw new MyException(); 
                // throw new ArithmeticException();        
            } 
            catch (Exception e) {
                System.out.println(e);                           // it directly call toString() method if we print only e
                System.out.println( "\n" + e.getMessage() );
                System.out.println( "\n" + e.toString() + "\n");
                e.printStackTrace();                      // this also by default calls toString() its show line number where axception occured
            }

            System.out.println("\nIt's not a 2 digit number: " + n);
        }

        System.out.println("\nEnd of program.");
        
        sc.close();
    }
}
