// Write a program in Java to display the pattern like right angle triangle with a number. 
// 1 
// 12 
// 123 
// 1234 
// 12345 

public class Q6 {
    public static void main(String[] args) {
        int n = 1;

        for (int r = 0; r < 5; r++) {
            for (int c = 0; c <= r; c++) {
                System.out.print(n + " ");
                n++;
            }
            System.out.println(" ");
            n = 1;
        }
    }
}
