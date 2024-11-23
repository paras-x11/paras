// 6. Write a program in C to count the total number of alphabets, digits and special characters in a string.

#include <stdio.h>
#include<ctype.h>
#include <string.h>

void main(){
    int i, alpha=0, digits=0 , special_char=0;
    char str[100];
    
    printf("\nEnter string: ");
    gets(str);
    
    printf("\n");
    for(i=0; str[i]!='\0'; i++){
        if(isalpha(str[i])){
            printf("%c ", str[i]);
            alpha++;
        }
    }
    printf("\nTotal alphabet: %d\n\n", alpha);
    
    for(i=0; str[i]!='\0'; i++){
        if(isdigit(str[i])){
            printf("%c ", str[i]);
            digits++;
        }
    }
    printf("\nTotal digits: %d\n\n", digits);
    
    for(i=0; str[i]!='\0'; i++){
        if(ispunct(str[i])){
            printf("%c ", str[i]);
            special_char++;
        }
    }
    printf("\nTotal special_char: %d\n\n", special_char);
    
}