import java.util.Scanner;

public class SpecificException {
    public static void main(String[] args) {
        int[] a = new int[3];

        a[0] = 25;   a[1] = 56;    a[2] = 10;

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter the index of array: ");
        int index = sc.nextInt();

        System.out.print("Enter the number: ");
        int number = sc.nextInt();

        try {
            System.out.printf("\nValue at " + index + " index in array is: " + a[index]);
            System.out.printf("\nResult is: " + a[index] + " / " + number + " = " + a[index] / number );
        }
        catch (ArithmeticException e) {
            System.out.println("\nArithmetic Exception Occured.\n       " + e);
        }
        catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("\nArray Index Out Of Bounds Exception Occured.\n" + e);
        }
        catch (Exception e) {
            System.out.println("\nSome Other Exception Occured.\n" + e);
        }
        sc.close();
    }
}
