import java.util.Scanner;

public class method_practice_set {

    static void multiplication(int n){

        for (int i = 1; i <= 10; i++) {

            System.out.printf("%d x %d = %d\n", n, i, n*i);            
        }
    }

    static void pattern1(int n){

        // int r, c;

        // for (r = 0; r < n; r++) {

        //     for (c = 0; c <= r; c++) {

        //         System.out.print("* ");                
        //     }   
        //     System.out.println();         
        // }

        if(n > 0){
            pattern1(n-1);

            for (int i = 0; i < n; i++) {
                System.out.print("* ");
            }
        }
    }

    static void pattern1_recursion(int n){

        if(n > 0){
            pattern1_recursion(n-1);

            for (int i = 0; i < n; i++) {
                System.out.print("* ");
            }
            System.out.println();
        }
    }

    static int sum_recursion(int n){
        if(n > 0){
            return n + sum_recursion(n-1);
        }
        else{
            return 0;
        }
    }

    static void pattern2(int n){

        int r, c;

        for(r=n-1; r>=0; r--){

            for(c=0; c<=r; c++){

                System.out.print("* ");
            }
            System.out.println();
        }
    }

    static void pattern2_recursion(int n){
        
        if(n > 0){

            for (int i = n; i > 0; i--) {
                System.out.print("* ");
            }
            System.out.println();
            pattern2_recursion(n-1);
        }
    }


    public static void main(String[] args) {
    
        Scanner sc = new Scanner(System.in);

        // --- 1. multiplication table of n:
        // System.out.print("Enter number: ");
        // int n1 = sc.nextInt();

        // multiplication(n1);

        // --- 2. pattern:
        // System.out.print("Enter number: ");
        // int n2 = sc.nextInt();

        // pattern1(n2);

        // --- 3. sum of n natural numbers usimg recursion:
        // System.out.print("Enter number: ");
        // int n3 = sc.nextInt();

        // System.out.println(sum_recursion(n3));

        // --- 4. pattern 2:
        // System.out.print("Enter number: ");
        // int n4 = sc.nextInt();

        // pattern2(n4);

        // --- 5. pattern1 using recursion:
        // System.out.print("Enter number: ");
        // int n5 = sc.nextInt();

        // pattern1_recursion(n5);

        // --- 6. pattern2 using recursion:
        // System.out.print("Enter number: ");
        // int n6 = sc.nextInt();

        // pattern2_recursion(n6);



        sc.close();

    }



}






// public class method_practice_set {
//     static void multiplication(int n) {
//         for (int i = 1; i <= 10; i++) {
//             System.out.format("%d X %d = %d\n", n, i, n * i);
//         }
//     }

//     static void pattern1(int n) {
//         for (int i = 0; i < n; i++) {
//             for (int j = 0; j < i + 1; j++) {
//                 System.out.print("*");
//             }
//             System.out.println();
//         }
//     }

//     static void pattern1_rec(int n) {
//         if (n > 0) {
//             pattern1_rec(n - 1);
//             for (int i = 0; i < n; i++) {
//                 System.out.print("*");
//             }
//             System.out.println();
//         }
//     }
//     // pattern1_rec(3)
//     // pattern1_rec(2) + 3 times star and new line
//     // pattern1_rec(1) + 2 times star and new line + 3 times star and new line
//     // pattern1_rec(0) + 1 times star and new line + 2 times star and new line + 3 times star and new line


//     // sum(n) = 1 + 2 + 3... + n
//     // sum(n) = 1 + 2 + 3... + n-1 + n
//     // sum(n) = sum(n-1) + n
//     // sum(3) = 3 + sum(2)
//     // sum(3) = 3 + 2 + sum(1)
//     // sum(3) = 3 + 2 + 1
//     static int sumRec(int n) {
//         // Base condition
//         if (n == 1) {
//             return 1;
//         }
//         return n + sumRec(n - 1);
//     }

//     static int fib(int n) {
//         /* if(n==1){
//             return 0;
//         }
//         else if(n==2){
//             return 1;
//         } */
//         if (n == 1 || n == 2) {
//             return n - 1;
//         } else {
//             return fib(n - 1) + fib(n - 2);
//         }
//     }

//     public static void main(String[] args) {
//         // Problem 1
//         // multiplication(7);

//         // Problem 2
//         // pattern1(9);

//         // Problem 3
//         // int c = sumRec(4);
//         // System.out.println(c);

//         // Problem 4
//         // fibonacci series - 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
//         // int result = fib(7);
//         // System.out.println(result);

//         // Problem 8
//         pattern1(9);

//     }

    
// }
