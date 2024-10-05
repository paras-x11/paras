import java.util.Scanner;

class MyAgeException extends Exception{
    @Override
    public String toString() {
        return "\nAge can not be greater than 125.";
    }

    @Override
    public String getMessage() {
        return "\nMake sure that you have entereed correct age.";
    }
}


public class CustomAgeException {
    @SuppressWarnings("resource")
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        System.out.print("\nEnter Your Age: ");
        int age = sc.nextInt();

        if(age < 1 || age > 125){

            try {
                throw new MyAgeException(); 
            } 
            catch (Exception e) {
                System.out.println(e);                           // it directly call toString() method if we print only e
                System.out.println( "\n" + e.getMessage() );
                System.out.println( "\n" + e.toString() + "\n");
                e.printStackTrace();                                // this also by default calls toString()
            }

            System.out.println("\nIt's not a valid age: " + age);
        }

        System.out.println("\nEnd of program.");
        
        sc.close();
    }
}
