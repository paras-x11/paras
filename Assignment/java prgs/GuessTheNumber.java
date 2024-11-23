import java.util.Random;
import java.util.Scanner;

class Game{
    public
    int computer_choice, user_choice, guess = 0;

    public Game(){
        Random r = new Random();

        computer_choice = r.nextInt(101);
    }

    public boolean isCorrectNumber(int n){
        user_choice = n;

        if (computer_choice == user_choice) {
            return true;
        } else {
            return false;
        }
    }   
    
    public void checkNumber(int n){
        user_choice = n;
        
        if(user_choice > computer_choice){
            System.out.println("-> You guessed greater number");
            System.out.println();
            guess ++;
        }

        else if(user_choice < computer_choice){
            System.out.println("-> You guessed lesser number");
            System.out.println();
            guess ++;
        }

        else{
            System.out.println("-> Congrats!, You Guessed right number in " + guess + " attempts. " + computer_choice);
            System.out.println();
        }
    }
}

public class GuessTheNumber {
    public static void main(String[] args) {

        int n;

        Scanner sc = new Scanner(System.in);

        System.out.println();
        System.out.println("=================== Guess The Number ===================");
        System.out.println();
        Game g = new Game();

        // System.out.println(g.computer_choice);

        System.out.print("Enter your number: ");
        n = sc.nextInt();

        if(g.isCorrectNumber(n)){
            System.out.println("-> Congrats!, You Guessed right number in 1 attempt. " + g.computer_choice);
        }

        else{
            g.checkNumber(n);
            do{
                System.out.print("Enter your number: ");
                n = sc.nextInt();

                g.checkNumber(n);
            } while( !g.isCorrectNumber(n) );
        }

        sc.close();
    }
}
