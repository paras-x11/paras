//2. Write a program in C to separate individual characters from a string.

#include<stdio.h>
void main(){
    char str[50];

    printf("\nEnter string 1: ");
    gets(str);

    printf("\nSeprated character: \n");
    for(int i=0; str[i] != '\0'; i++){          //for seprate each characters
        printf("character %d: %c\n", i+1, str[i]);
    }


    printf("\nSeprated word: \n");
    for(int i=0; str[i] != '\0'; i++){          //for seprate word;

        if(str[i] != 32){
            printf("%c",str[i]);
        }
        else {
            printf("\n");
        }
    }
}