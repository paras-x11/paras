//9 C Program to Check Uppercase or Lowercase or Digit or Special Character.

#include<stdio.h>
#include<stdlib.h>

void main(){
    char ch;
    int i = 1;

    printf("\nEnter dot(.) for exit. \n");
    printf("\n------------------------");

    while(1){
    printf("\n");
    printf("\n%d. Enter Any Character: ",i);
    scanf("%c",&ch);
    while((getchar()) != '\n');

    if((ch >= 48) && (ch <= 57)){
        printf("\n-> You entered a digit: %c",ch);
    }

    else if ((ch >= 65) && (ch <= 90))
    {
        printf("\n-> You entered a upper-case letter: %c",ch);
    }

    else if ((ch >= 97) && (ch <= 122))
    {
        printf("\n-> You entered a lower-case letter: %c",ch);
    }
    else if (ch == '.')
    {
        printf("\n-> You entered a Symbol: %c",ch);
        printf("\n Exited.");
        exit(0);
    }
    
    else{
        printf("\n-> You entered a Symbol: %c",ch);
    }
    i++;
    }    
}