// 13. Write a program in C to remove characters from a string except alphabets. 

#include <stdio.h>
#include <ctype.h>
#include <string.h>

void main(){
    int i, len;
    char str[100];

    printf("Enter string: ");
    gets(str);

    len = strlen(str);

    for ( i = 0; i < len; i++){
        
        if( isalpha(str[i]) ){

            printf("%c", str[i]);
        }
    }
    
}