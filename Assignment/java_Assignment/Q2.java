// Write a Java program that takes the user to provide a single character from the alphabet. Print Vowel or Consonant, depending on the user input.
// If the user input is not a letter (between a and z or A and Z), or is a string of length > 1, print an error message. 


import java.util.Scanner;

public class Q2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        System.out.print("Enter single character from the alphabet: ");
        String input = sc.nextLine();

        if(input.length() != 1){
            System.out.println("Error: Input should be a single character.");
        }
        else{
            char ch = input.charAt(0);

            if(!Character.isLetter(ch)){
                System.out.println("Error: Input is not a letter.");
            }
            else{
                ch = Character.toLowerCase(ch);

                if(ch == 'a' || ch == 'e' ||ch == 'i' || ch == 'o' || ch == 'u'){
                    System.out.println("Inputted Character is Vowel.");
                }
                else{
                    System.out.println("Inputted Character is COnsonant.");
                }
            }
        }
        sc.close();
    }
}
