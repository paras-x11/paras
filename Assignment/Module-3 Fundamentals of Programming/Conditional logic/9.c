//9 C Program to Check Uppercase or Lowercase or Digit or Special Character.

#include<stdio.h>
#include<stdlib.h>

void main(){
    char ch;

    start:
    printf("\n ------------------------");
    printf("\n ------------------------");
    printf("\n Enter Any Character: ");
    scanf("%c",&ch);

    if((ch >= 48) && (ch <= 57)){
        printf("\n You entered a digit: %c",ch);
        goto start;
    }

    else if ((ch >= 65) && (ch <= 90))
    {
        printf("\n You entered a upper-case letter: %c",ch);
        goto start;
    }

    else if ((ch >= 97) && (ch <= 122))
    {
        printf("\n You entered a lower-case letter: %c",ch);
        goto start;
    }
    else if (ch == '.')
    {
        printf("\n You entered a Symbol: %c",ch);
        printf("\n Exited.");
        exit(0);
    }
    
    else{
        printf("\n You entered a Symbol: %c",ch);
        goto start;
    }
    
}