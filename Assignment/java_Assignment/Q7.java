// • Write a program in Java to make such a pattern like right angle triangle with number increased by 1 The pattern like: 
 
// 1 
// 2 3 
// 4 5 6 
// 7 8 9 10 


public class Q7 {
    public static void main(String[] args) {
        int n = 1;

        for (int r = 0; r < 4; r++) {
            for (int c = 0; c <= r; c++) {
                System.out.print(n + " ");
                n++;
            }
            System.out.println(" ");
        }
    }
}
