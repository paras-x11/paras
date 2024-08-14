import java.util.Scanner;

public class PracticeSet5 {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        // Que. 1:
        // * * * * *
        // * * * *
        // * * * 
        // * * 
        // *
        // int r, c;
        // for (r=5; r>0; r--) {
        //     for(c=0; c<r; c++){
        //         System.out.print("* ");
        //     }
        //     System.out.println();
        // }



        // que 2: sum of first n numbers
        // System.out.print("Enter number: ");
        // int n = sc.nextInt();
        // int temp = n;
        // int sum = 0;
         
        // while (n > 0) {
        //     sum = sum + n;
        //     n--;
        // }

        // System.out.println("Sum of first " + temp + " numbers is: " + sum);

        // que 2: sum of first n even/odd numbers
        // System.out.print("Enter number for even addition: ");
        // int n = sc.nextInt();
        // int even_temp = 0, odd_temp = 0;
        // int even_sum = 0, odd_sum = 0;
         
        // while (n > 0) {
        //     if(n%2 == 0){
        //         even_sum = even_sum + n;
        //         even_temp++;
        //         System.out.println(n);
        //     }
        //     n--;
        // }
        // System.out.println("Sum of first " + even_temp + " even numbers is: " + even_sum);

        // System.out.print("\nEnter number for odd addition: ");
        // n = sc.nextInt();

        // while (n > 0) {
        //     if(n%2 != 0){
        //         odd_sum = odd_sum + n;
        //         odd_temp++;
        //         System.out.println(n);
        //     }
        //     n--;
        // }
        // System.out.println("Sum of first " + odd_temp + " even numbers is: " + odd_sum);

        // que 3: multiplication table
        // System.out.print("Enter number: ");
        // int n = sc.nextInt();

        // for (int i = 1; i <= 10; i++) {
        //     System.out.println(n+ " * " +i+ " = " +n*i);
        // }

        // que 4: reverse multiplication table
        // System.out.print("Enter number: ");
        // int n = sc.nextInt();

        // for (int i = 10; i > 0; i--) {
        //     System.out.println(n+ " * " +i+ " = " +n*i);
        // }

        // que 5: find factorial
        // System.out.print("Enter number: ");
        // int n = sc.nextInt();
        // int fact = 1;

        // for (int i = 1; i <= n ; i++) {
        //     fact = fact * i; 
        // }
        // System.out.println("factorial of "+n+ " is: "+fact);


        // que 5: sum of numbers occuring in multiplication table of 8
        System.out.print("Enter number: ");
        int n = sc.nextInt();
        int sum = 0;

        for (int i = 0; i <= n*10; i++) {
            if(i%n == 0){
                sum = sum + i;
            }
        }

        System.out.println("sum of numbers occuring in multiplication table of " +n+ " is: " +sum);



        sc.close();   
    }
}
