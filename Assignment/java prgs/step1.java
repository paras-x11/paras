import java.util.Scanner;

public class step1{

    public static void main(String[] args) {
        
        System.out.println("Hello World!");

        int count[] = new int[3];

        Scanner input = new Scanner(System.in);

        System.out.println("Enter Your String : ");
        String S = input.nextLine();

        String[] str= S.split(" ");
        System.out.println("\nEnter Not Allowed Words : ");

        String[] s1 = new String[3];

        for (int i = 0; i < 3; i++) {
            s1[i] = input.next();
        }

        for (int i = 0; i < 3; i++) {
            for (String str1 : str) {
                if (s1[i].equals(str1)) {
                    count[i]++;
                }
            }
        }

        System.out.println("\nWord Count : ");
        for (int i = 0; i < 3; i++) {
            System.out.println(s1[i] + " : " + count[i]);
        }

        input.close();
    
        }
}

