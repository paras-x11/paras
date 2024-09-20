// • Write a Java program to print numbers between 1 to 100 which are divisible by 3, 5 and by both. 


public class Q9 {
    public static void main(String[] args) {
        int n = 1;

        while(n <= 100){
            if((n%3 == 0 || n%5 == 0)){                              // || (n%3 == 0 && n%5 == 0)){
                System.out.println(n);
            }
            n++;
        }
    }
}
