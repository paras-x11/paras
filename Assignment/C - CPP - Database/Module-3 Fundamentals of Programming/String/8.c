// 8. Write a program in C to count the total number of vowels or consonants in a string.

#include <stdio.h>
#include<ctype.h>
#include <string.h>

void main(){
    int i, consonants=0, vowels=0;
    char str[100];
    
    printf("\nEnter string: ");
    gets(str);
    
    printf("\n");
    for(i=0; str[i]!='\0'; i++){
        if(str[i] == 'a' || str[i] == 'e' || str[i] == 'i' || str[i] == 'o' || str[i] == 'u'){
            printf("%c ", str[i]);
            vowels++;
        }
    }
    printf("\nTotal vowels: %d\n\n", vowels);
    
    for(i=0; str[i]!='\0'; i++){
        if(!isspace(str[i])){
            printf("%c ", str[i]);
            consonants++;
        }
    }
    printf("\nTotal consonants: %d", consonants);
    
}