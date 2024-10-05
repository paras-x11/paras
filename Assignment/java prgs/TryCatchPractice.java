import java.util.Scanner;

class MaxRetryException extends Exception{
    @Override
    public String toString() {
        return "No more retry";
    }
}


public class TryCatchPractice {

    // public static String maxRetry() throws MaxRetryException{
        
    //     // block of code...
    //     return "max retries";
    // }

    @SuppressWarnings("resource")
    public static void main(String[] args){
        int[] a = new int[3];
        a[0] = 7;
        a[1] = 56;
        a[2] = 27;

        int index, i = 0;

        Scanner sc = new Scanner(System.in);      
        
        boolean flag = true;

        while (flag && i<5) {
            try {
                System.out.println("Enter index: ");
                index = sc.nextInt();
                System.out.println("Value at index " + index + ": " + a[index]);
            } 
            catch (Exception e) {
                System.out.println("Invalid Index");
                i++;
            }
        }

        if(i>=5){
            try {                               // normally throw is used in try block..
                throw new MaxRetryException();
            } 
            catch (MaxRetryException e) {
                System.out.println(e.toString());
            }
        }

        sc.close();
    }
}
