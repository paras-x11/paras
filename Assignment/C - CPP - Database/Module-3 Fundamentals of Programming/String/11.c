// 11. Write a program in C to read a sentence and replace lowercase characters with uppercase and vice versa.

#include <stdio.h>
#include <ctype.h>
#include <string.h>

#include<stdio.h>
void main(){
    int i, len=0;
    char str[100];

    printf("Enter String: ");
    gets(str);

    len = strlen(str);

    for(i=0; i<len; i++){

        if( isupper(str[i]) ){
            printf("%c", tolower(str[i]));
        }   
        
        else{
            printf("%c", toupper(str[i]) );
        }
        
    }
   
}
