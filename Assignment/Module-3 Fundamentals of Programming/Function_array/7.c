// 7. WAP Find out length of string without using inbuilt function 

#include<stdio.h>
int length(char str[]){
    int len=0;

    for(int i=0; str[i] != '\0'; i++){
        len++;
    }

    return len;
}

void main(){

    char str1[50];

    printf("\nEnter string 1: ");
    gets(str1);

    printf("\nLength of string 1 is: %d", length(str1));

    // char str[20] = "Hello World";
    // printf("\nLength of str is: %d", length(str));
   
}