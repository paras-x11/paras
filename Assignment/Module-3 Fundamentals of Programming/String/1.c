// 1. Write a program in C to find the length of a string without using library functions.

#include <stdio.h>
void main(){
    int i, length=0;
    char str[100];
    
    printf("\nEnter string: ");
    gets(str);
    
    for(i=0; str[i] != '\0'; i++){
        length++;
    }
    
    printf("\nLength is: %d",length);
}