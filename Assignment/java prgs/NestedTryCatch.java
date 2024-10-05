import java.util.Scanner;

public class NestedTryCatch {
    public static void main(String[] args) {
        int[] a = new int[3];
    
        a[0] = 25;   a[1] = 56;    a[2] = 10;
    
        Scanner sc = new Scanner(System.in);
        
        while(true){
            System.out.print("\nEnter the index of array: ");
            int index = sc.nextInt();
        
            try {
                System.out.println("\nThanks for running my program.");
                try {
                    System.out.printf("\nValue at " + index + " index in array is: " + a[index]);
                    break;
                }
                catch(ArrayIndexOutOfBoundsException e) {
                    System.out.println("\nException at level 2.");
                    System.out.println("\nThis index is not available. Try Again! :( ");
                    continue;
                }
            }
            catch (Exception e) {
                System.out.println("\nSome Exception Occured.\n" + e);
            }
        }

        System.out.println("\n\nprogram ended.");
        sc.close();        
    }
}    

