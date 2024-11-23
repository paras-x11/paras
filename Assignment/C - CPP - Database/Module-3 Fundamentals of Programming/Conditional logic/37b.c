// WAP to show 
// b. Vowel or Consonant using switch case.

#include<stdio.h>
#include<stdlib.h>
void main(){
    
    char ch;
    while(1){
                printf("\n-------------------------------------");
                printf("\nEnter any character (or '.' to exit): ");
                scanf(" %c", &ch);

            
                switch (ch) {
                    case 'a':       case 'A':
                    case 'e':       case 'E':
                    case 'i':       case 'I':
                    case 'o':       case 'O':
                    case 'u':       case 'U':

                        printf("%c is a vowel\n", ch);
                    break;

                    case '.' :
                        printf("\nExited.");
                        exit(0);

                    default:
                            printf("%c is a consonant\n", ch);
                    break;
                }
    }
}