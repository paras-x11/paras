import java.util.Scanner;
import java.util.Random;

public class RockPaperScissor{
    public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);
		Random rand = new Random();

        String[] choices = {"rock", "paper", "scissors"};
		int user=0, comp=0;

		for (int i = 0; i < 5; i++) {

			int n2 = rand.nextInt(3);

			System.out.print("\n0 for rock \t 1 for paper \t 2 for scissors: ");
			int n1 = sc.nextInt();

			if (n1 < 0 || n1 > 2) {
                System.out.println("Invalid input. Please enter 0, 1, or 2.");
                i--; // Repeat the current iteration to prompt again
                continue;
            }

			System.out.println("\nYour choice: " + choices[n1] + "\t Computer's choice: " + choices[n2]);

			if( (n1==1 && n2==0) || (n1==2 && n2==1) || (n1==0 && n2==2) ){
				user++;
				System.out.println("\n-> You Win. Your score: " + user);
			}
			else if(n1==n2){
				System.out.println("\n-> Draw.");
				// i--;
			}
			else{
				comp++;
				System.out.println("\n-> Computer Wins. Computer's score: " + comp);
			}						
		}

		System.out.println("\nYour total score is: " +user);
		System.out.println("Computer's total score is: " +comp);

		if (user > comp) {
            System.out.println("\nCongratulations! You are the overall winner!");
        } else if (user < comp) {
            System.out.println("\nThe computer is the overall winner. Better luck next time!");
        } else {
            System.out.println("\nIt's a draw overall!");				// if draw counted as a round and we dont apply i-- for draw.
        }

		sc.close();
	}
}