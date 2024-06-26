// 7. Write a program in C to copy one string to another string

#include <stdio.h>
#include <string.h>

void main(){
    int i;
    char str1[100], str2[100];
    
    printf("\nEnter string 1: ");
    gets(str1);
    
    // strcpy(str2, str1);
    
    for(i=0; str1[i]!='\0'; i++){
        str2[i] = str1[i];
    }
    
    printf("\nstring 2 is: %s", str2);
}