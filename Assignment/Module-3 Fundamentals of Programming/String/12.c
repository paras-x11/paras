// 12. Write a program in C to find the number of times a given word 'is' appears in the given string. 

#include <stdio.h>
#include <ctype.h>
#include <string.h>

void main(){
    int i, len, word_len = 2, count = 0;
    char str[100];
    char word[] = "is";

    printf("\nEnter string: ");
    gets(str);

    len = strlen(str);

    for(i=0; i<len; i++){

        if(str[i] == 'i' && str[i+1] == 's' ){

            if( (i == 0 || !isalpha(str[i - 1]))  && !isalpha(str[i + word_len]) ){
                count++;
            }
        } 
    }

    printf("\n-> The word '%s' appears %d times in the string.\n", word, count);   
   
}